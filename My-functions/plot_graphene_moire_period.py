# plot the relation of twisted angle and moire pattern length in graphene
# The relation is given by lambda = a/(2*sin(theta/2)), where a is the lattice constant of graphene
# The plot is in log scale, and the horizontal line is lambda = 2 nm

import numpy as np
import matplotlib.pyplot as plt

a = 0.246e-9 #unit: m

# define the theta angle from 2 to 60 degree
theta_angle = np.linspace(2,60,600)

def lambda_length(theta_angle):
    theta_radius = theta_angle/180*3.14159
    return a/(2*np.sin(theta_radius/2))

print(lambda_length(1.1))
# plot the relation of theta and lambda
fig, ax = plt.subplots()
fig.set_size_inches(4, 3)
# plot lambda_length in log scale
plt.plot(theta_angle, lambda_length(theta_angle), 'r')
# set x label as theta, Set y label as lambda
plt.xlabel(r'$\theta$ (degree)')
plt.ylabel(r'$\lambda$ (m)')
plt.yscale('log')
plt.tight_layout()
# show  only the vertical grid background
plt.grid(axis='x')
# show the horizontal line of lambda = 2 nm
plt.axhline(y=2e-9, color='grey', linestyle='--')
plt.show()