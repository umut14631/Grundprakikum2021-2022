import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


a, b, c, d, e, f, g, h, i = np.genfromtxt("statisch.txt", unpack=True)

x=5*a


def fkt(x, j, k):
    return j*x + k

# hier Fit ergänzen

para, cov= curve_fit(fkt, x, b)


plt.errorbar(x, b, yerr=0.01, fmt="k.", label="Messwerte")

t = np.linspace(0, 20, 21)



plt.plot(t, g(t, *para),label="Regressionsgerade")

#plt.xlabel(r'$(3 L^2 x - 4 x^3)/10^4 \unit{\cubic\centi\meter}$')
#plt.ylabel(r'$D(X)$ / $\unit{\centi\meter}$')
#plt.legend(loc='best')
#plt.xlim(0,20)
#plt.savefig('build/bquader.pdf')
#print(cov)
plt.show()