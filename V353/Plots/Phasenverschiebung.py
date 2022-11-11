import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f, A, Uc, y = np.loadtxt('Messdaten/Frequenzabhaengigkeit.txt', unpack=True, delimiter=',')

T = 1/f 
y1 = y
v=f

def f (x, a, m, b):
    return a*np.arctan(m*x)+b

params, covariance_matrix = curve_fit(f, v, y)
x_plot = np.linspace(10, 30**4, 1000000)
plt.plot(x_plot, f(x_plot, params[0], params[1], params[2]), '-', label=r'Theoriekurve', linewidth=1, c = 'black')

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))
print('c = {:.4f} ± {:.5f}'.format(params[2], errors[2]))

plt.plot(v, y1, 'rx', label='Messdaten')
plt.xscale('log')
plt.xlabel(r'$f \: / \: \frac{1}{s}$')
plt.ylabel(r'$\varphi \: / \: rad$')
plt.legend(loc='best')
plt.xlim(10**1, 10**4.5)
plt.tight_layout()
plt.savefig("Phasenverschiebung.png")