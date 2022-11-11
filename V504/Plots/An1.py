import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import elementary_charge, m_e, epsilon_0, Boltzmann

x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
y = np.array([12, 6.5, 3.6, 2, 1.45, 0.8, 0.5, 0.38, 0.25, 0.21, 0.175])

def f (x, a, b):
    return a * np.exp((- elementary_charge * x)/(Boltzmann * b))

params, covariance_matrix = curve_fit(f, x, y, p0=[12, 1e4])
errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.6f} ± {:.6f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

z = np.linspace(0, 1.1)

plt.plot(x, y, 'rx', label='Messdaten')
plt.plot(z, f (z, *params), '-', label='Theoriekurve', c = 'black')
plt.xlabel(r'$U \: / \: \mathrm{V}$')
plt.ylabel(r'$I \,\,/\,\, \mathrm{A}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("An1.png")