import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, y = np.genfromtxt("Messdaten/Sr.txt", unpack=True, delimiter = ',')

x = x
y = y


plt.plot(x, y, 'b-', label='Messdaten', )

plt.ylabel(r'$ Imp \,\,/\,\, \sec$')
plt.xlabel(r'$ \alpha_{Gm} \,\,/\,\, \degree$')
plt.legend(loc='best')
plt.savefig("Strontium.png")