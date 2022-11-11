import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import elementary_charge, m_e, epsilon_0, Boltzmann

x = np.array([350, 380, 410, 450, 500, 550, 600, 630, 680])
y = np.array([1.80, 2.47, 2.35, 3.56, 4.20, 4.66, 4.62, 5.74, 6.78])



def f (x, m, b):
    return m*x+b

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.6f} ± {:.6f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

z = np.linspace(340,690)

plt.plot(x, y, 'r*', label='Messdaten')
plt.plot(z, f (z, *params), '-', label='Theoriekurve', c = 'black')
plt.xlabel(r'$U \,\, / \,\, \mathrm{V}$')
plt.ylabel(r'$ Q \,\, / \,\, 10**-9 \mathrm{C} $')
plt.xlim(340, 690)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("2.png")