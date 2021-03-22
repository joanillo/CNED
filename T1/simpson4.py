# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Simpson simple

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 simpson4.py
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

x = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
y = f(x)

poly1 = lagrange(x[0:3], y[0:3])
print(poly1)
poly2 = lagrange(x[2:5], y[2:5])
print(poly2)

# per comparar:
x_simple = np.array([0, np.pi/2, np.pi])
y_simple = f(x_simple)
poly_simple = lagrange(x_simple, y_simple)

x_ = np.arange(0.0, np.pi, 0.005)
if (len(x_) % 2 == 0):
	meitat=int(len(x_)/2)
else:
	meitat=int((len(x_)+1)/2)

fig, ax = plt.subplots()
plt.plot(x_, f(x_), x_, poly_simple(x_), x_[0:meitat], poly1(x_[0:meitat]), x_[meitat:len(x_)], poly2(x_[meitat:len(x_)]), x, y, 'bo')
plt.legend(['sin(x)+1','Lagrange simple', 'Lagrange1','Lagrange2'])
ax.set(title='sin(x) + 1. Simpson compost vs Simpson simple')
ax.grid()

fig.savefig("../img/T1/simpson4.png")
plt.show()

result1 = integrate.quad(lambda x: f(x), 0, np.pi) #valor real: 2+pi
print(result1[0])
result2 = integrate.quad(lambda x: poly_simple(x), 0, np.pi) # simpson simple
print(result2[0])
print("ERROR simpson simple: " + str(result1[0]-result2[0]))
result3 = integrate.quad(lambda x: poly1(x), 0, np.pi/2) # simpson compost, meitat 1
result4 = integrate.quad(lambda x: poly2(x), np.pi/2, np.pi) # simpson compost, meitat 2
print("ERROR simpson compost: " + str(result1[0]-(result3[0]+result4[0])))