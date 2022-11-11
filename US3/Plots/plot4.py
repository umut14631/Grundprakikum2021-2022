import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

A = [12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5]
B = [61, 87, 102, 131, 140, 161, 177, 190, 145, 130, 115, 98, 92]
C = [53, 79, 91, 122, 115, 170, 120, 114, 71, 73, 65, 92, 112]

plt.plot(A, B, 'rx--', label=r'$70\%$ Pumpleistung')
plt.plot(A, C, 'bx--', label=r'$45\%$ Pumpleistung')

plt.grid()
plt.ylabel(r'$ I \,\, / \,\, \frac{kv^2}{s} $')
plt.xlabel(r'$ Messtiefe \,\, / \,\, \mu m  $')
plt.legend(loc='best')
plt.savefig("Plot4.png")