import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y, x = np.genfromtxt('Messdaten/Entladevorgang.txt', unpack=True, delimiter=',')

x1 = x*1e-3
#y1 = np.log(y)

params, covariance_matrix = np.polyfit(x1, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def f (x, m, b):
    return m*x+b

z = np.linspace(0,0.0068)

plt.plot(x1, y, 'rx', label='Messdaten')
plt.plot(z, f (z, *params), '-', label='Theoriekurve', c = 'black')
plt.xlim(0,0.0068)
plt.ylim(-4.1, -0.18)
plt.xlabel(r'$t \: / \: \mathrm{s}$')
plt.ylabel(r'$\ln{\left(\frac{U_C}{1\,V}\right)}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("Entladevorgang.png")