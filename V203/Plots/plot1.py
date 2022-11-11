import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

P, T, ln1, k = np.loadtxt('Messdaten/bis1bar.text', unpack=True, delimiter=',')

 

params, covariance_matrix = np.polyfit(k, ln1, deg=1, cov=True)

def gerade (k, m, b ):
   return m*k+b

z = np.linspace(np.min(k), np.max(k+0.05))

plt.plot(z, gerade (z, *params), '-', label='Theoriekurve', c = 'black')
plt.plot(k, ln1, 'x', label='Messdaten', color= 'red')
plt.xlim(2.6, 3.5 )
plt.ylabel(r'$ \ln(\frac{p}{p_{0}})$')
plt.xlabel(r'$\frac{1}{K}$')
plt.legend(loc='best')
plt.savefig("plot1.png")