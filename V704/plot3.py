import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import elementary_charge, m_e, epsilon_0

x1 = np.array([0.27, 0.33, 0.41, 0.43, 0.54])
y1 = np.array([38.5, 9.58, 9.26, 5.95, 2.50])
y11= np.array([0.26, 0.06, 0.05, 0.03, 0.03])
x2 = np.array([0.68, 0.81, 0.91, 1.08, 1.19])
y2 = np.array([0.95, 0.73, 0.72, 0.64, 0.59])
y22= np.array([0.02, 0.02, 0.02, 0.01, 0.01])


def f(x1, a, b):
    return a*x1+b

def g(x2, c, d):
    return c*x2+d


params1, covariance_matrix = curve_fit(f,x1,y1)
errors1 = np.sqrt(np.diag(covariance_matrix))
params2, covariance_matrix = curve_fit (g,x2,y2)
errors2 = np.sqrt(np.diag(covariance_matrix))


print('a = {:.6f} ± {:.6f}'.format(params1[0], errors1[0]))
print('b = {:.4f} ± {:.5f}'.format(params1[1], errors1[1]))
print('c = {:.6f} ± {:.6f}'.format(params2[0], errors2[0]))
print('d = {:.4f} ± {:.5f}'.format(params2[1], errors2[1]))

w = np.linspace(0.2, 0.60)
z = np.linspace(0.60, 1.25)


plt.errorbar(x1, y1, yerr=y11, fmt='x', label='Messdaten1', ecolor='blue', color='red')
plt.plot(w, f(w, *params1), '-', label='Theoriekurve1', c = 'lightblue')
plt.errorbar(x2, y2, yerr=y22, fmt='x', label='Messdaten2', ecolor='purple', color='green')
plt.plot(z, g(z, *params2), '-', label='Theoriekurve2', c = 'black')
plt.ylabel(r'$ Aktivität ln(A - A_0)\,\,/\,\,\frac{1}{s}$')
plt.xlabel(r'$ R\,\,/\,\,kg/m^2  $')
plt.legend(loc='best')
plt.savefig("3.png")