import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y = [0.109, 0.192, 0.282, 0.398, 0.516, 0.744, 0.988, 1.209, 1.414, 1.602, 1.714]
x = [10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90]


plt.plot(x, y, 'rx', label='Messdaten')
plt.xlim(5,100)
plt.ylim(0, 1.80)
plt.xlabel(r'$U \: / \: \mathrm{V}$')
plt.ylabel(r'$\mathrm{I} \,\,/\,\, \mathrm{A}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("K5.png")