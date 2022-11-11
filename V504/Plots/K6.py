import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import elementary_charge, m_e, epsilon_0

x = np.array([10, 15, 20, 25, 30, 40, 50, 60, 70, 80])
y = np.array([0.121, 0.208, 0.300, 0.402, 0.516, 0.750, 1.007, 1.200, 1.604, 1.953])


def f (x, c, b):
    return c * 4/9 * epsilon_0 * np.sqrt(2* elementary_charge/m_e) * x**b

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))


print('c = {:.6f} ± {:.6f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

z = np.linspace(10, 80)

plt.plot(x, y, 'rx', label='Messdaten')
plt.plot(z, f (z, *params), '-', label='Theoriekurve', c = 'black')
plt.xlabel(r'$U \: / \: \mathrm{V}$')
plt.ylabel(r'$I \,\,/\,\, \mathrm{A}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("K6.png")