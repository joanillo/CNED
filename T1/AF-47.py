# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
polinomis de Lagrange. Visualitzar els 4 polinomis

Exemple proposat AF-47, sin(x): f(0)=sin(0), f(.5)=sin(.5), f(1)=sin(1) i f(1.5)=sin(1.5)
Visualitzar els 4 polinomis de Lagrange: L0, L1, L2 i L3

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 AF-47.py
'''

# Lagrange Interpolation

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

#f(0)=sin(0), f(.5)=sin(.5), f(1)=sin(1) i f(1.5)=sin(1.5)
x = np.array([0, .5, 1., 1.5])
y = np.array([np.sin(0), np.sin(.5), np.sin(1.), np.sin(1.5)])

from scipy.interpolate import lagrange
poly = lagrange(x, y)
print(poly) # -0.1182 x^3 - 0.05748 x^2 + 1.017 x

def L0(x):
    return 0*x

def L1(x):
    return (4) * x * (x-1) * (x-1.5)

def L2(x):
    return -4 * x * (x-0.5) * (x-1.5)

def L3(x):
    return (4/3) * x * (x-0.5) * (x-1)

# aproximació molt bona
x_ = np.arange(0.0, 1.5, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x_, poly(x_), x_, np.sin(x_), x, y, 'bo')
pop_px = mpatches.Patch(color='red', label='p(x)')
pop_sinx = mpatches.Patch(color='green', label='sin(x)')
plt.legend(handles=[pop_px, pop_sinx])
ax.set(title='AF-47. sin(x). Interpolació de Lagrange')
ax.grid()
fig.savefig("../img/T1/AF-47a.png")

# quan sortim de l'intèrval, l'aproximació deixa de ser bona
x_ = np.arange(-1.5, 3.0, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x_, poly(x_), x_, np.sin(x_), x, y, 'bo')
pop_px = mpatches.Patch(color='red', label='p(x)')
pop_sinx = mpatches.Patch(color='green', label='sin(x)')
plt.legend(handles=[pop_px, pop_sinx])
ax.set(title='AF-47. sin(x). Interpolació de Lagrange')
ax.grid()
fig.savefig("../img/T1/AF-47b.png")

# visualització dels polinomis de Lagrange
x_ = np.arange(0.0, 1.5, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.plot(x_, L0(x_), 'red', x_, L1(x_), 'green', x_, L2(x_), 'blue', x_, L3(x_), 'cyan')
plt.plot(x[0], L0(x[0]), 'ro', x[1], L1(x[1]), 'go', x[2], L2(x[2]), 'bo', x[3], L3(x[3]), 'co')

pop_L0 = mpatches.Patch(color='red', label='L0(x)')
pop_L1 = mpatches.Patch(color='green', label='L1(x)')
pop_L2 = mpatches.Patch(color='blue', label='L2(x)')
pop_L3 = mpatches.Patch(color='cyan', label='L3(x)')

plt.legend(handles=[pop_L0, pop_L1, pop_L2, pop_L3])

ax.set(title='AF-47. sin(x). Polinomis de Lagrange')
ax.grid()
fig.savefig("../img/T1/AF-47c.png")
plt.show()
