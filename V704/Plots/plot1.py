import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = [0.005, 0.005, 0.010, 0.010, 0.015, 0.015, 0.020, 0.020, 0.025, 0.030, 0.035, 0.040]
y = [4.50601261445, 4.48469603252, 4.3237352263, 4.27067599175, 4.13931792786, 4.05369616374, 3.89263629163, 3.8670256395, 3.70671937224, 3.51720105742, 3.24259235149, 3.03543364041]
y1= [0.92, 0.90, 0.77, 0.36, 0.64, 0.29, 0.25, 0.16, 0.21, 0.12, 0.09, 0.08]


params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def f (x, a, b):
    return a*x+b


z = np.linspace(0, 0.05)

plt.errorbar(x, y, yerr=y1, fmt='x', label='Messdaten', ecolor='blue', color='red')
plt.plot(z, f (z, *params), '-', label='Theoriekurve', c = 'black')
plt.ylabel(r'$ Aktivität ln(A - A_0)\,\,/\,\,\frac{1}{s}$')
plt.xlabel(r'$ Dichte\,\,/\,\, mm  $')
plt.legend(loc='best')
plt.savefig("1.png")