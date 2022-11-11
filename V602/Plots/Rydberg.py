import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y = [30, 31, 35, 38, 40]
x = [3.89* 10**-8, 4.03* 10**-8, 4.59* 10**-8, 4.97* 10**-8, 5.30* 10**-8]


params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def f (x, m, b):
    return m*x+b


#z = np.linspace(29, 41)
z = np.linspace(3.89* 10**-8, 5.30* 10**-8)

plt.plot(x, y, 'rx', label='Messdaten', )
plt.plot(z, f (z, *params), '-', label='Theoriekurve', c = 'black')
plt.xlabel(r'$ \sqrt{E_K}$')
plt.ylabel(r'$ Z $')
plt.legend(loc='best')
plt.savefig("Rydberg.png")