# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
polinomis de Lagrange.
Problemes 1 i 2 d'AF (Aproximació de funcions)
Prob1: (0.146447, cos(0.146447)) i (0.853553, cos(0.853553)) -> per dos punts passa una recta
Prob2: (0, cos(0)), (0.5, cos(0.5), (1, cos(1)) -> per tres punts passa una paràbola

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 P-AF-1_2.py
'''

# Lagrange Interpolation

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
from scipy.interpolate import lagrange
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

# P-AF-1 ======================
#f(0.146447)=cos(0.146447), f(0.853553)=cos(0.853553)
x = np.array([0.146447, 0.853553])
y = np.array([np.cos(0.146447), np.cos(0.853553)])

poly = lagrange(x, y)
print(poly) # -0.4695 x + 1.058

x_ = np.arange(0.0, np.pi/2, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x_, poly(x_), x_, np.cos(x_), x, y, 'bo')
ax.set(title='P-AF-1. cos(x). Interpolació de Lagrange')
ax.grid()
fig.savefig("../img/T1/P-AF-1.png")
plt.show()

# P-AF-2 ======================
#f(0)=cos(0), f(0.5)=cos(0.5), f(1)=cos(1)
x = np.array([0.0, 0.5, 1.0])
y = np.array([np.cos(0.0), np.cos(0.5), np.cos(1.0)])

poly = lagrange(x, y)
print(poly) # -0.4297 x^2 - 0.02997 x + 1

x_ = np.arange(0.0, np.pi/2, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x_, poly(x_), x_, np.cos(x_), x, y, 'bo')
ax.set(title='P-AF-2. cos(x). Interpolació de Lagrange')
ax.grid()
fig.savefig("../img/T1/P-AF-2.png")
plt.show()
