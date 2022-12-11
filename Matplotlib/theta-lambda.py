
# plot a rectangle to show the relation of theta and lambda

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.ticker import MultipleLocator
import numpy as np

# mpl.rcParams["font.serif"] = "Source Serif Pro"
mpl.rcParams["font.size"] = 10
mpl.rcParams["font.weight"] = 400
# mpl.rcParams["font.family"] = "serif"
mpl.rcParams["axes.labelweight"] = 400

theta_size = 600
theta = np.linspace(0.1,20,theta_size)/180*3.1415926
theta = theta.reshape(theta_size,1)
a = 0.246 #unit: nm
period_length = a/(2*np.sin(theta/2))
y_axis = np.linspace(0.99,1,theta_size)
y_axis = y_axis.reshape(1,theta_size)
z_axis = period_length + y_axis

# print(theta, y_axis, z_axis)
fig, ax = plt.subplots()
fig.set_size_inches(12, 1.2)

theta = np.linspace(0.1,20,theta_size)
y_axis = np.linspace(0.99,1,theta_size)
z_axis = z_axis.transpose()
cmap = ax.pcolormesh(theta, y_axis, z_axis, cmap='rainbow', shading='auto',
                    norm=colors.LogNorm())
plt.xscale('log')
## secondary x-axis
def theta_to_lambda(theta):
    return a/(2*np.sin(theta/180*3.1415926/2))

def lambda_to_theta(length):
    return 2*np.arcsin(a/(2*length))

print(theta_to_lambda(1.1))

secax_x = ax.secondary_xaxis('top', functions=(theta_to_lambda, lambda_to_theta))
secax_x.set_xticks(ticks=[1, 10, 100], labels=['1 nm', '10 nm', '100 nm'])
# secax_x.set_xlabel(r'$\lambda$', fontsize=18)
secax_x.tick_params(labelsize=16)



ax.set_xticks(ticks=[0.11, 1.1, 11], labels=[r'$0.11^{\circ}$', r'$1.1^{\circ}$', r'$11^{\circ}$'])
plt.tick_params(axis="x", which="major", labelsize=16)
plt.tight_layout()
plt.show()
