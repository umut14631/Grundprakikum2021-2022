import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Uc, phi1 = np.loadtxt('Messdaten/Frequenzabhaengigkeit2.txt', unpack=True, delimiter=',')

#U0 = 1.5
#U = Uc/U0

#T = 1/f
#y1 = y
#phi = (y1/T)*2*np.pi

plt.polar(phi1, Uc,'xr', label=r'$\text{Messwerte} \; \phi $')

RC = 0.003
x = np.linspace(0, 50000, 10000000)
phi = np.arcsin(((x*RC)/(np.sqrt(1+x**2*(RC)**2))))
y = 1/(np.sqrt(1+x**2*(RC)**2))

plt.polar(phi,y,'-', label=r'$\text{Messwerte}  \; U_C \ /\  U_0$')
plt.xticks([0, np.pi/4, np.pi/2,  3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4],[r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$",  r"$\frac{3\pi}{4}$", r"$\pi$", r"$\frac{5\pi}{4}$", r"$\frac{3\pi}{2}$", r"$\frac{7\pi}{4}$"])
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("Polarplot1.png")
