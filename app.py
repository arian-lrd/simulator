from flask import Flask, render_template, request, jsonify
import numpy as np
from scipy.integrate import solve_ivp
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the form

@app.route('/solve', methods=['POST'])
def solve_ode():
    # Extract parameters from request
    data = request.json
    j = float(data['j'])
    Kem = float(data['Kem'])
    Ra = float(data['Ra'])
    t = float(data['t'])
    r1 = float(data['r1'])
    l = float(data['l'])
    Ks = float(data['Ks'])
    d = float(data['d'])
    L = float(data['L'])
    F = float(data['F'])
    N = float(data['N'])
    maximumTime = float(data['maximumTime'])
    theta_0 = float(data['theta_0'])
    omega_0 = float(data['omega_0'])

    # Assign the coefficients 
    a = j
    b = 2*N*(Kem)**2*r1*(l+t)/Ra
    c = 2*Ks*r1*d
    d = F*L

    # Assign finishing time for the graph
    max_time = maximumTime


    # Define the system of ODEs
    def system_of_odes(t, y):
        theta, omega = y
        return [omega, (d - b*omega - c*theta) / a]

    # Initial conditions and time span
    initial_conditions = [theta_0, omega_0]
    t_span = [0, max_time]  # Modify as needed
    t_eval = np.linspace(t_span[0], t_span[1], 300)

    # Solve the ODE
    solution = solve_ivp(system_of_odes, t_span, initial_conditions, t_eval=t_eval)

    # Convert theta from radians to degrees
    theta_degrees = solution.y[0] * 180 / np.pi

    # Calculate angular velocity in rpm
    omega_rpm = solution.y[1] * 60 / (2 * np.pi)

    # Calculate voltage
    omega = 2 * solution.y[1]  # as omega = 2 * thetadot
    voltage = Kem * omega

    # Prepare the data for plotting
    data = {
        'time': solution.t.tolist(),
        'theta': theta_degrees.tolist(),
        'omega': omega_rpm.tolist(),
        'voltage': voltage.tolist(),
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

