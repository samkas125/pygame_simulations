# Physics simulations using the pygame library in Python

## Bouncing ball simulation
This simulation uses the physics concept of coefficient of restitution to simulate a ball bouncing up and down off a horizontal surface. It makes use of simple algebra, and kinematics concepts. 

## Pendulum simulation
Takes length of the string, and initial angle of displacement as inputs, and simulates an oscillating pendulum. It makes use of basic algebra, trigonometry and kinematics. Also calculates the time period of the pendulum.

## Pipe flow velocity
Takes the radius of the pipe and viscosity of fluid as inputs. It uses constant values for the pressure difference between the two ends of the pipe, and the length of the pipe. It then uses the following formula to calculate the theoretical velocity of the fluid in the pipe:

ΔPr^2 / 8ηl 

(Where 'P' is the pressure difference, 'r' is the radius, 'η' is the viscosity, and 'l' is the length)

Finally, it plays a simulation, where a droplet is seen moving through a pipe at the calculated velocity.

## Spring - mass system
The spring-mass system is a form of simple harmonic motion, where a mass is attached to a spring. It is allowed to oscillate back and forth. For this simulation, the theoretical equations for displacement, velocity and acceleration are used:

x(t) = A * cos(ωt)

v(t) = -A * ω * sin(ωt)

a(t) = -A * ω * ω * cos(ωt)

The formula T = 2π √(m/k) is used to calculate the time period from mass. The spring constant, k is assumed constant. Mass and amplitude are taken from the user.
