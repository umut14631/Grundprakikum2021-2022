import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, y = np.genfromtxt("Messdaten/Emission.txt", unpack=True, delimiter = ',')

x = x
y = y


plt.plot(x, y, 'b-', label='Messdaten', )

plt.ylabel(r'$ Imp \,\,/\,\, \sec$')
plt.xlabel(r'$ \alpha_{Gm} \,\,/\,\, \degree$')
plt.legend(loc='best')
plt.savefig("Emission.png")