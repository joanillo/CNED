# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
polinomis de Lagrange. Visualitzar els 4 polinomis

Exemple AF-45: f(-2)=3, f(-1)=1, f(2)=-1 i f(4)=3
Visualitzar els 4 polinomis de Lagrange: L0, L1, L2 i L3

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 lagrange3.py
'''

# Lagrange Interpolation

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

#f(-2)=3, f(-1)=1, f(2)=-1 i f(4)=3 
x = np.array([-2, -1, 2, 4])
y = np.array([3, 1, -1, 3])

from scipy.interpolate import lagrange
poly = lagrange(x, y)
print(poly) # 0.03333 x^3 + 0.3667 x^2 - 1.133 x - 0.4667

def L0(x):
    return -(1/24) * (x+1) * (x-2) * (x-4)

def L1(x):
    return (1/15) * (x+2) * (x-2) * (x-4)

def L2(x):
    return -(1/24) * (x+2) * (x+1) * (x-4)

def L3(x):
    return (1/60) * (x+2) * (x+1) * (x-2)

x_ = np.arange(-5.0, 5.0, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x_, poly(x_), x, y, 'bo')
ax.set(title='Interpolació de Lagrange')
ax.grid()

x_ = np.arange(-2.5, 5.0, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.plot(x_, L0(x_), 'red', x_, L1(x_), 'green', x_, L2(x_), 'blue', x_, L3(x_), 'cyan')
plt.plot(x[0], L0(x[0]), 'ro', x[1], L1(x[1]), 'go', x[2], L2(x[2]), 'bo', x[3], L3(x[3]), 'co')

import matplotlib.patches as mpatches
pop_L0 = mpatches.Patch(color='red', label='L0(x)')
pop_L1 = mpatches.Patch(color='green', label='L1(x)')
pop_L2 = mpatches.Patch(color='blue', label='L2(x)')
pop_L3 = mpatches.Patch(color='cyan', label='L3(x)')

plt.legend(handles=[pop_L0, pop_L1, pop_L2, pop_L3])

ax.set(title='Polinomis de Lagrange')
ax.grid()

fig.savefig("../img/T1/lagrange3.png")
plt.show()
