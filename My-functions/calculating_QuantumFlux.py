
#calculating the quantum flux of moire lattice 
import scipy.constants as cons
import numpy as np

a = 0.246e-9 #unit: m
theta = 1.44/180*3.14159
wavelength = a/(2*np.sin(theta/2))


S = 1.732/2*(a/theta)**2
quantum_flux = cons.h/cons.e/S  # unit in Tesla

print(a/theta, S, cons.h/cons.e, wavelength)
print('quantum flux (T) =', quantum_flux)