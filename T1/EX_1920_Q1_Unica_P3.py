# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
AF-80: Exercici proposat. Aproximació per mínims quadrats (regressió quadratica)
Les fórmules per plantejar el sistema d'equacions les he tret de martin_milton.pdf (https://recursos.salonesvirtuales.com/assets/bloques/martin_milton.pdf)

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 EX_1920_Q1_Unica_P3.py
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

x = np.array([0, 1, 2, 3])
y = np.array([1.1, 2.8, 8, 20])

a0 = len(x)
a1 = np.sum(np.exp(x))
a2 = np.sum(np.exp(2*x))

b0 = np.sum(y)
b1 = np.sum(np.exp(x).dot(y))

A = np.array([[a0, a1],
	[a1, a2]])

B = np.array([b0, b1])
print(A)
print(B)

sol = np.linalg.solve(A,B) # dues formes
#sol = np.linalg.inv(A).dot(B)

print(sol)
print ("\np(x) = " + str(round(sol[0],3)) + " + " + str(round(sol[1],3)) + "*exp(x)")

def p(x):
    return sol[0] + sol[1]*np.exp(x)

print("p(3) = a + b*e^3 = " + str(p(3)))

# gràfica
x_ = np.arange(0.0, 3.0, 0.05)
fig, ax = plt.subplots()
plt.plot(x_, p(x_), x, y, 'bo')

plt.suptitle('a + b*exp(x)')
plt.title("p(x) = " + str(round(sol[0],3)) + " + " + str(round(sol[1],3)) + "*e^x")
ax.set(xlabel='x', ylabel='y')
ax.grid()
fig.savefig("../img/T1/EX_1920_Q1_Unica_P3.png")
plt.show()
