import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = [0.05324, 0.04606, 0.03818, 0.03016, 0.022152, 0.01418, 0.00696]
y = [20, 17.3, 14.6, 11.7, 8.85, 5.95, 5.10]


params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def f (x, m, b):
    return m*x+b


z = np.linspace(0.001, 0.06)

plt.plot(x, y, 'rx', label='Messdaten', )
plt.plot(z, f (z, *params), '-', label='Theoriekurve', c = 'black')
plt.ylabel(r'$ t_{oben}$')
plt.xlabel(r'$ l $')
plt.legend(loc='best')
plt.savefig("schall.png")