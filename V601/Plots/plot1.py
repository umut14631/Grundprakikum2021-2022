import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



x, y = np.genfromtxt("Messdaten1.txt", unpack=True, delimiter='&')


plt.plot(x, y, "rx", label="Messdaten")
plt.xlabel(r'$ U_{1} \,\, / \,\, V $')
plt.ylabel(r'$ \Delta y \,\, / \,\, \Delta x_{1} $')
plt.legend(loc='best')
plt.savefig("1.png")
