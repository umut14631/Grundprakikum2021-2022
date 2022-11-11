import matplotlib.pyplot as plt
import numpy as np

x = np.genfromtxt('Messdaten/2.txt', unpack=True)
Us = [0.32, 0.28, 0.198, 0.110, 0.044, 0.02, 0.01, 0.0017, 0.0085, 0.017, 0.034, 0.048, 0.115, 0.16, 0.23, 0.26, 0.31, 0.32, 0.305, 0.28, 0.23 ]  


x1 = np.linspace(0.1,100,6000)

y2 = np.sqrt((1/9)*(x1**2-1)**2/((1-x1**2)**2+9*x1**2))

plt.plot(x, Us,  '--x', color= "black" ,label=r'Messdaten', linewidth=0.5)
plt.plot(x1, y2, label='Theoriekurve')
plt.xlabel(r'$\Omega = \frac{v}{v_0}$')
plt.xscale('log')
plt.xlim(10**(-1), 10**(2.15))
plt.ylabel(r'$\frac{U_{Br}}{U_s}$')
plt.grid()
plt.legend(loc='best')
plt.savefig("plot2.pdf")