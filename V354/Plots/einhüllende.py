import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import chirp

t = np.array([   0,    10,   20,  29.5, 38.5,  48.5, 58.5,  67.9, 77.0,  86.0, 97  ])
A = np.array([0.80, -0.60, 0.58, -0.44, 0.43, -0.32, 0.32, -0.22, 0.24, -0.18, 0.17])

A1 = A[A>0]
A2 = A[A<0]

def Fit(t,a,b):
    return a*np.exp(-b*t)

params1, covariance_matrix1 = curve_fit (Fit,t[A>0],A1, p0=(100,0))
params2, covariance_matrix2 = curve_fit (Fit,t[A<0],A2, p0=(100,0))

uncertainties1= np.sqrt(np.diag(covariance_matrix1))
uncertainties2= np.sqrt(np.diag(covariance_matrix2))


for name, value, uncertainty in zip('ab', params1, uncertainties1):

    print(f'{name}={value: 4f} +\- {uncertainty: 4f}')


for name, value, uncertainty in zip('ab', params2, uncertainties2):

    print(f'{name}={value: 4f} +\- {uncertainty: 4f}')


x_plot=np.linspace (0,1000,2000)

plt.plot(x_plot, Fit(x_plot, *params1),'r-' , label='A>0')
plt.plot(x_plot, Fit(x_plot, *params2),'r-' , label='A<0')
plt.plot(t,A, "-x", color="black", label="Messdaten")

plt.legend(loc='best')
plt.xlim(0,500)
plt.xlabel(r'$t\,/\,\mu s$')
plt.ylabel(r'$A\,/\,V$')
plt.axis([0, 100, -0.8, 0.8])
plt.grid()
plt.savefig('Einhüllende.png')