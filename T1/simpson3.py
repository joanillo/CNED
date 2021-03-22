# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Simpson simple

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 simpson3.py
'''

# Lagrange Interpolation

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import scipy.integrate as integrate
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

def f(x):
    return np.sin(x) + 1

x = np.array([0, np.pi/2, np.pi])
y = f(x)

poly = lagrange(x, y)
print(poly)
x_ = np.arange(0.0, np.pi, 0.005)
fig, ax = plt.subplots()
plt.plot(x_, f(x_), x_, poly(x_), x, y, 'bo')
plt.legend(['sin(x)+1','Lagrange'])
ax.set(title='sin(x) + 1. Simpson simple')
ax.grid()

fig.savefig("../img/T1/simpson3.png")
plt.show()

result1 = integrate.quad(lambda x: f(x), 0, np.pi) #valor real: 2+pi
print(result1[0])
result2 = integrate.quad(lambda x: poly(x), 0, np.pi)
print(result2[0])
print("ERROR: " + str(result1[0]-result2[0]))
