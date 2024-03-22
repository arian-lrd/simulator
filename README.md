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


