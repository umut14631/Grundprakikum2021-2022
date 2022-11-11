import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = [0.001, 0.010, 0.012, 0.015, 0.017, 0.020, 0.022, 0.025, 0.030, 0.032, 0.035, 0.040]
y = [4.59935330067, 3.73193894357, 3.40784192438, 3.12807546054, 2.90416508003, 2.6553524121, 2.50634193051, 2.183801557, 1.84371920816, 1.49290409618, 1.35325450704, 1.20597080699 ]
y1= [1, 0.43, 0.33, 0.26, 0.22, 0.09, 0.08, 0.07, 0.04, 0.03, 0.03, 0.02]


def f (x, a, b):
    return a*x+b

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

z = np.linspace(0, 0.05)

plt.errorbar(x, y, yerr=y1, fmt='x', label='Messdaten', ecolor='blue', color='red')
plt.plot(z, f (z, *params), '-', label='Theoriekurve', c = 'black')
plt.ylabel(r'$ Aktivität ln(A - A_0)\,\,/\,\,\frac{1}{s}$')
plt.xlabel(r'$ Dichte\,\,/\,\, mm $')
plt.legend(loc='best')
plt.savefig("2.png")