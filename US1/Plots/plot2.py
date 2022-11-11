import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = [40.0175, 61.25, 80.25, 120.25]
y = [0.157, -0.5798184953, 0.07696104114, -1.714798428]


params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.10f} ± {:.10f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

def f (x, a, b):
    return a*x+b


z = np.linspace(37, 125)

plt.plot(x, y, 'rx', label='Messdaten')
plt.plot(z, f (z, *params), '--', label='Theoriekurve', c = 'black')
plt.ylabel(r'$ ln(U) \,\,/\,\, V $')
plt.xlabel(r'$ Länge \,\, Zylinder \,\,\,\, l\,\,/\,\, mm  $')
plt.legend(loc='best')
plt.savefig("2.png")