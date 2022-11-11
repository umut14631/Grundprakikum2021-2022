import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, y, z = np.loadtxt("Messdaten/messdaten.txt", unpack=True, delimiter = '&')

a, b = np.loadtxt("Messdaten/errors.txt", unpack=True, delimiter = '&')

x1 = x * 10**-19
z1 = z * 10**-19
a1 = a * 10**-19
b1 = b * 10**-19

plt.errorbar(y, z1, yerr=b1, fmt='x', label='Korrigiert', ecolor='blue', color='green')

plt.xlabel(r'Nummer der benachbarten Tropfes')
plt.ylabel(r'$ q \,\,/\,\, C $')
plt.legend(loc='best')
plt.savefig("korrigiert.png")