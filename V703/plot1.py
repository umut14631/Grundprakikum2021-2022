import numpy as np
from uncertainties import ufloat
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.constants import elementary_charge, m_e, epsilon_0, Boltzmann

x = np.array([320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700   ])
y = np.array([4643, 4772, 4898, 4976, 5070, 4975, 4839, 5062, 5110, 5105, 4827, 4943, 5098, 5049, 5116, 5096, 5020, 5011, 4995, 5092, 5181, 4998, 5180, 5147, 5086, 5171, 5155, 5005, 5193, 5119, 5097, 5222, 5245, 5206, 5216, 5263, 5303, 5390, 5302])

y1 = y/60

def f (x, m, b):
    return m*x+b

params, covariance_matrix = curve_fit(f, x, y1)
errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.6f} ± {:.6f}'.format(params[0], errors[0]))
print('b = {:.4f} ± {:.5f}'.format(params[1], errors[1]))

z = np.linspace(390,620)

plt.plot(x, y1, 'r*', label='Messdaten')
plt.plot(z, f (z, *params), '-', label='Theoriekurve', c = 'black')
plt.xlabel(r'$U \: / \: \mathrm{V}$')
plt.ylabel(r'$\frac{N}{t} \: / \: \frac{1}{\mathrm{s}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("1.png")