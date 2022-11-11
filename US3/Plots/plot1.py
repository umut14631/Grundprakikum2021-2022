import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

A = [0.49, 0.41, 0.73, 0.46, 1.05]
B = [1100.70, 932.70, 1627.88, 1407.74, 2340.44]
C = [0.81, 0.81, 1.21, 1.21, 1.71]
D = [1814.21, 1820.21, 2692.83, 2710.82, 3808.34]
E = [0.31, 0.39, 0.48, 0.60, 0.66]
F = [687.20, 873.85, 1073.23, 1338.35, 1480.46] 

plt.plot(B, A, 'rx--', label=r'Messdaten $15°$')
plt.plot(D, C, 'bx--', label=r'Messdaten $30°$')
plt.plot(F, E, 'gx--', label=r'Messdaten $45°$')

plt.grid()
plt.ylabel(r'$v \,\, / \,\, \frac{m}{s} $')
plt.xlabel(r'$ \frac{\nabla \nu}{\cos \alpha} $')
plt.legend(loc='best')
plt.savefig("Plot1.png")