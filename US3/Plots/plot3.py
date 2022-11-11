import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

A = [12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5]
B = [1.24, 1.51, 1.62, 1.72, 1.77, 1.75, 1.62, 1.42, 1.25, 1.21, 1.45, 1.48, 1.56]
C = [0.63, 0.73, 0.77, 0.83, 0.82, 0.79, 0.74, 0.64, 0.58, 0.61, 0.65, 0.69, 0.67]

plt.plot(A, B, 'rx--', label=r'$70\%$ Pumpleistung')
plt.plot(A, C, 'bx--', label=r'$45\%$ Pumpleistung')

plt.grid()
plt.ylabel(r'$ v \,\, / \,\, \frac{m}{s} $')
plt.xlabel(r'$ Messtiefe \,\, / \,\, \mu m  $')
plt.legend(loc='best')
plt.savefig("Plot3.png")