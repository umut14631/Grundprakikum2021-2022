import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y = [0.055, 0.103, 0.154, 0.197, 0.227, 0.256, 0.268, 0.272, 0.275, 0.277 ]
x = [10, 15, 20, 25, 30, 40, 50, 60, 70, 80]


plt.plot(x, y, 'rx', label='Messdaten')
plt.xlim(5,85)
plt.ylim(0, 0.3)
plt.xlabel(r'$U \: / \: \mathrm{V}$')
plt.ylabel(r'$I \,\,/\,\, \mathrm{A}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("K2.png")