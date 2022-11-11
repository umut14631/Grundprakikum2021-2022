
import numpy as np 
import matplotlib.pyplot as plt 

theta, N = np.genfromtxt('Messdaten/EmissionCu.dat', unpack = True, delimiter= ",")

plt.plot(theta, N, '.', markersize = 0.5, label = r'Messwerte')
plt.vlines(x = 20.2,ymin = 0, ymax = 1599, linewidth = 0.3, label = r'$K_{\beta}$ Linie' , color = 'tab:red')
plt.vlines(x = 22.5,ymin = 0, ymax = 5050, linewidth = 0.3, label = r'$K_{\alpha}$ Linie', color = 'tab:green')


plt.xlabel(r'$\theta$ / $\degree$')
plt.ylabel(r' $N$ ')
plt.legend()

plt.savefig('Kupfer.png')


def energie(theta):
    return 6.626e-34 * 299792458 / (2 * 201.4e-12 * np.sin(theta) * 1.602e-19) 

def radians(theta):
    return theta/180 * np.pi

Ebeta  = energie(radians(20.2)) 
Ealpha = energie(radians(22.5)) 

print(f'Die Energie der beta Linie beträgt:  {Ebeta}')
print(f'Die Energie der alpha Linie beträgt: {Ealpha}')