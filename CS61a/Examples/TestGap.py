
# plot the function of semiconducting gap

import numpy as np
import matplotlib.pyplot as plt


def activation(temp):
    return r0 * np.exp(Eg / temp)


temp = np.linspace(40, 300, 299)
r0 = 1
Eg = 100
print(activation(40) / activation(100))
print(activation(50) / activation(110))

plt.plot(temp, activation(temp))
plt.show()
