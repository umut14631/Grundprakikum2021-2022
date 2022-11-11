import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



U = Uc

def h (x,m,b):
    return b/np.sqrt(1+m**2*x**2)  


params, covariance_matrix = curve_fit(h, f, U)
x_plot = np.linspace(10**0.95, 10**4.5, 1000000)
plt.plot(x_plot, h(x_plot, params[0], params[1]), '-', label=r'Ausgleichskurve', linewidth=1, color= 'black')

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))



plt.plot(f, U, 'rx', label='Messdaten')
plt.xscale('log')
plt.xlabel(r'$f \: / \: \frac{1}{s}$')
plt.ylabel(r'$\frac{U_{C}}{U_0}$')
plt.xlim(10**0.95, 10**4.4)
plt.legend(loc='best')
plt.tight_layout()

plt.savefig("Amplituden.png")
