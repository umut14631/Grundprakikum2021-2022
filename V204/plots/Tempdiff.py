import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



x, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt("Messdaten/1StatischeMethode.txt", unpack=True)


x = 5*x
y = T2 - T1
#plt.errorbar (x,y,yerr=0.01, fmt="r.", label="T1")
plt.plot (x, y, "-", label="Differenz des breiten Messingstabs (T2-T1)")

y = T7 - T8
#plt.errorbar (x,y,yerr=0.01, fmt="k.", label="T4")
plt.plot(x,y, "-", label="Differenz des Edelstahlstabs (T7-T8)")

plt.grid()
plt.xlabel(r'$t \,\, / \,\, s $')
plt.ylabel(r'$T \,\, / \,\, °C $')
plt.legend(loc='best')
plt.savefig("Tempdiff.png")