import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, y = np.genfromtxt("Messdaten/1.txt", unpack=True, delimiter = '&')


plt.plot(x, y, '-', label='Messdaten', color='black' )


plt.xlabel(r'$ Frequenz \,\,/\,\, KHz$')
plt.ylabel(r'$ U_{A} \,\,/\,\, V$')
plt.legend(loc='best')
plt.savefig("Gaußglocke.png")