import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



x, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt("Messdaten/2DynamischeMethode80s.txt", unpack=True)


x = 5*x
y = T5
#plt.errorbar (x,y,yerr=0.01, fmt="r.", label="T5")
plt.plot(x,y, "b-", label="T5")

y = T6
#plt.errorbar (x,y,yerr=0.01, fmt="k.", label="T6")
plt.plot(x,y, "r-", label="T6")

plt.grid()
plt.xlabel(r'$t \,\, / \,\, s $')
plt.ylabel(r'$T \,\, / \,\, °C $')
plt.legend(loc='best')
plt.savefig("TemprVerlDyT5T6.png")
