# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
AF-80: Exercici proposat. Aproximació per mínims quadrats (regressió quadratica)
Les fórmules per plantejar el sistema d'equacions les he tret de martin_milton.pdf (https://recursos.salonesvirtuales.com/assets/bloques/martin_milton.pdf)

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 EX_1920_Q1_Par1_P3.py
'''

import numpy as np
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

#np.set_printoptions(precision=2)

x = np.array([30, 62, 75, 105])
y = np.array([80, 120, 170, 250])

a0 = len(x)
a1 = np.sum(x)
a2 = np.sum(x**2)
a3 = np.sum(x**3)
a4 = np.sum(x**4)
b0 = np.sum(y)
b1 = np.sum(x.dot(y))
b2 = (x**2).dot(y.reshape((-1, 1)))[0]

A = np.array([[a0, a1, a2],
	[a1, a2, a3],
	[a2, a3, a4]])

B = np.array([b0, b1, b2])
print(A)
print(B)

sol = np.linalg.solve(A,B) # dues formes
#sol = np.linalg.inv(A).dot(B)

print(sol) # p(x) = 0.0165*x^2 + 0.0835*x + 61.0386
print ("\np(x) = " + str(round(sol[2],4)) + "*x^2 + " + str(round(sol[1],4)) + "*x + " + str(round(sol[0],4)))

def p(x):
    return sol[2]*x**2 + sol[1]*x + sol[0]

print("preu(100m^2) = " + str(p(100)))

# gràfica
x_ = np.arange(30.0, 105.0, 0.05)
fig, ax = plt.subplots()
plt.plot(x_, p(x_), x, y, 'bo')
plt.suptitle('Preu de l\'habitatge')
plt.title("\np(x) = " + str(round(sol[2],3)) + "*x^2 + " + str(round(sol[1],3)) + "*x + " + str(round(sol[0],3)))
ax.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3))
ax.set(xlabel='metres quadrats', ylabel='preu (euros)')

ax.grid()
fig.savefig("../img/T1/EX_1920_Q1_Par1_P3.png")
plt.show()
