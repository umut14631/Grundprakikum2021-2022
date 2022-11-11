import matplotlib.pyplot as plt
import numpy as np

A = [5, 10, 15, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
B = [0.1083, 0.116, 0.141, 0.273, 0.307, 0.380, 0.45, 0.404, 0.309, 0.238, 0.190, 0.145, 0.120, 0.119]

plt.plot(A, B, 'x', label=r'Messdaten')

plt.xlabel(r'$f / kHz$')
plt.ylabel(r'$\frac{U_C}{U_0}$')
plt.legend()
plt.savefig("plot1.png")