Code for a simulator solving ODE (Ordinary Differential Equation) of a door in motion, using the Runge-Kutta 45 method. The door is equipped with a custom-built door damper developed by Seneca Polytechnic researchers in collaboration with SmartOnes Solutions.

Outputs:
Three graphs, predicting varying information of interest. These include:
- Graph of Theta vs. Time
- Graph of Angular Velocity vs. Time
- Graph of Voltage vs. Time

Inputs:
- J: Mass moment of Inertia
- Kem: Motor constant
- Ra: Armature resistance
- t: Normal distance between the motor's base and the hinge
- r1: Radius of pivot
- l: Distance between Fm (which is tangent to the motor pinion's pitch diameter)
- Ks: Spring stifness
- d: Normal distance between the spring and the hinge
- L: Door's length
- F: User's input force
- N: Number of motors


# Key notes from deployment:

## app.py code differences: 
-> The app.py code on the server is slightly different, it is as follows:
**1) app routes the beginning of the code:**
app = Flask(__name__)

@app.route('/smartone')
def smartone_index():
    return render_template('index.html')  # Render the form

\# Define other routes as needed
@app.route('/')
def default_index():
    return render_template('index.html')

@app.route('/smartone/solve', methods=['POST'])
def solve_ode():
    # Extract parameters from request


**2) at the end of the file:**
   if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


### To fix 502 Bad Gateway:
-> sudo chown www-data:www-data /home/smartone/simulator/app.sock
-> sudo chmod 660 /home/smartone/simulator/app.sock
-> may also be fixed with: sudo chmod 775 /home/smartone/simulator/app.sock

### Adjustment in /etc/systemd/system/app.service:
-> Group=sudo
-> Make sure to adjust Group the group of the user

### sudo privileges:
-> Remember to give the user sudo privileges to install packages, etc


### Guiding video for setup (Gunicorn, Flask, NGINX):
-> https://www.youtube.com/watch?v=KWIIPKbdxD0&list=LL&index=3&t=292s
-> used the phrase 'app' instead of 'peak'. (at all locations) 
-> The user on the server used is called 'smartone'
-> Make sure venv is set and required packages are installed 


### Frewall settings:
-> Ensuring the required ports are open.
-> Gave full NGINX access with: 'sudo ufw allow "Nginx Full"'

### Reseting the system:
-> Use propper commands after adjustments to make sure they work
-> sudo systemctl reload nginx
-> sudo systemctl restart nginx
-> sudo systemctl restart app (or 'peak' or whatever name we chose to use)



