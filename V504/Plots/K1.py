import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y = [0.05, 0.104, 0.123, 0.129, 0.130, 0.131, 0.132, 0.133]
x = [10, 20, 30, 40, 50, 60, 70, 80,]


plt.plot(x, y, 'rx', label='Messdaten')
plt.xlim(5,85)
plt.ylim(0, 0.14)
plt.xlabel(r'$U \: / \: \mathrm{V}$')
plt.ylabel(r'$I \,\,/\,\, \mathrm{A}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("K1.png")