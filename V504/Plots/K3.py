import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y = [0.084, 0.150, 0.232, 0.310, 0.385, 0.525, 0.628, 0.727, 0.731, 0.738]
x = [10, 15, 20, 25, 30, 40, 50, 60, 70, 80]


plt.plot(x, y, 'rx', label='Messdaten')
plt.xlim(5,85)
plt.ylim(0, 0.78)
plt.xlabel(r'$U \: / \: \mathrm{V}$')
plt.ylabel(r'$I \,\,/\,\, \mathrm{A}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("K3.png")