import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



x, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt("Messdaten/3DynamischeMethode200s.txt", unpack=True)

#x = np.linspace(0, 10, 1000)
x = 5*x
y = T7
#plt.errorbar (x,y,yerr=0.01, fmt="r.", label="T7")
plt.plot(x,y, "b-", label="T7")

y = T8
#plt.errorbar (x,y,yerr=0.01, fmt="k.", label="T8")
plt.plot(x,y, "g-", label="T8")

plt.grid()
plt.plot(x,y,)
plt.xlabel(r'$t \,\, / \,\, s $')
plt.ylabel(r'$T \,\, / \,\, °C $')
plt.legend(loc='best')
plt.savefig("TemprVerlDyT7T8.png")