import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy

P, T=np.genfromtxt('Messdaten/1bis15bar.text', unpack=True, delimiter='&' )

T+=273.15  #auskommentieren falls die schon in °C umgerechnet sind
P*=1e5     #auskommentieren falls du die in bar haben möchtest

params2, _f = np.polyfit(T,P, deg=3, cov=True)
err = np.sqrt(np.diag(_f))
uparam=unp.uarray(params2,err)
print("\nPolynomwerte /T^3, /T^2, /T und :\n", uparam,'\n')


plt.figure()
plt.plot(T,P,'.',label="Messwerte")
plt.plot(T, params2[0]*T**3 + params2[1]*T**2+params2[2]*T+params2[3], label="Ausgleichskurve")
plt.xlabel("T / [K]")
plt.ylabel("P / [Pa] $\cdot 10^5$")
plt.tight_layout()
plt.legend()
plt.savefig('plot2.png')

R=8.31446261815324
#R=const.gas_constant
A=0.9
def L(x,a,b,c,d):
    return (((R*x)/2)+np.sqrt(((R*x)/2)**2-A*(a*x**3+b*x**2+c*x+d)))*((3*a*x**3+2*b*x**2+c*x)/(a*x**3+b*x**2+c*x+d))

x= np.linspace(T[-1],T[0],30)

plt.figure()
plt.plot(x, L(x, *params2),'x', label='Genäherte Funktion für L', color='blue')
plt.xlabel("T [K]")
plt.ylabel("L [J/mol]")
plt.savefig('plot3.png')

R=8.31446261815324
#R=const.gas_constant
A=0.9
def K(x,a,b,c,d):
    return (((R*x)/2)-np.sqrt(((R*x)/2)**2-A*(a*x**3+b*x**2+c*x+d)))*((3*a*x**3+2*b*x**2+c*x)/(a*x**3+b*x**2+c*x+d))

x= np.linspace(T[-1],T[0],30)


plt.figure()
plt.plot(x, K(x, *params2),'x', label='Genäherte Funktion für L', color='blue')
plt.xlabel("T [K]")
plt.ylabel("L [J/mol]")
plt.savefig('plot4.png')