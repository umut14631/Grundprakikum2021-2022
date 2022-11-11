import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y = [0.068, 0.134, 0.222, 0.309, 0.420, 0.602, 0.763, 0.874, 0.945, 0.995, 1.006, 1.012]
x = [10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]


plt.plot(x, y, 'rx', label='Messdaten')
plt.xlim(5,105)
plt.ylim(0, 1.20)
plt.xlabel(r'$U \: / \: \mathrm{V}$')
plt.ylabel(r'$I \,\,/\,\, \mathrm{A}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("K4.png")