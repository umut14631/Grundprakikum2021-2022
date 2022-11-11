import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



x, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt("Messdaten/1StatischeMethode.txt", unpack=True)


x = 5*x
y = T5
#plt.errorbar (x,y,yerr=0.01, fmt="b.", label="T5")
plt.plot(x,y, "r-", label="Aluminium")

y = T8
#plt.errorbar (x,y,yerr=0.01, fmt="g.", label="T8")
plt.plot(x,y, "b-", label="Edelstahl")

plt.grid()
plt.xlabel(r'$t \,\, / \,\, s $')
plt.ylabel(r'$T \,\, / \,\, °C $')
plt.legend(loc='best')
plt.savefig("TemprVerlStT5T8.png")
