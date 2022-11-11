import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



x, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt("Messdaten/2DynamischeMethode80s.txt", unpack=True)

#x = np.linspace(0, 800, 801)
x = 5*x
y = T1
#plt.errorbar (x,y,yerr=0.01, fmt="r.", label="T1")
plt.plot(x,y, "-", label="T1")

y = T2
#plt.errorbar (x,y,yerr=0.01, fmt="k.", label="T2")
plt.plot(x,y, "-", label="T2")

plt.grid()
plt.xlabel(r'$t \,\, / \,\, s $')
plt.ylabel(r'$T \,\, / \,\, °C $')
plt.legend(loc='best')
plt.savefig("TemprVerlDyT1T2.png")



