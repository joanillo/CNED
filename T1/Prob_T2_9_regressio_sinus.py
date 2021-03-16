# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
AF-80: Exercici proposat. Aproximació per mínims quadrats (regressió quadratica)
Les fórmules per plantejar el sistema d'equacions les he tret de martin_milton.pdf (https://recursos.salonesvirtuales.com/assets/bloques/martin_milton.pdf)

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T2_9_regressio_sinus.py
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

x = np.array([-3, -1.5, 0, 1.5, 3])
y = np.array([0, 2, -1, 3, 4])

def u0(x):
    return np.sin(2*x)

def u1(x):
    return np.cos(2*x)

a0 = np.sum(u0(x)**2)
a1 = np.sum(u0(x)*u1(x))
a2 = np.sum(u1(x)**2)

b0 = np.sum(u0(x).dot(y))
b1 = np.sum(u1(x).dot(y))

A = np.array([[a0, a1],
	[a1, a2]])

B = np.array([b0, b1])
print(A)
print(B)

sol = np.linalg.solve(A,B) # dues formes
#sol = np.linalg.inv(A).dot(B)

print(sol)
print ("\np(x) = " + str(round(sol[1],3)) + "*cos(2x) + " + str(round(sol[0],3)) + "*sin(2x)")

def p(x):
    return sol[1]*u1(x) + sol[0]*u0(x)

# gràfica
x_ = np.arange(-3.0, 3.0, 0.05)
fig, ax = plt.subplots()
plt.plot(x_, p(x_), x, y, 'bo')

plt.suptitle('Prob 9. a*sin(2x) + b*cos(2x)')
#plt.title("\np(x) = " + str(np.around(sol[2],3)) + "*x^2 + " + str(np.around(sol[1],3)) + "*x + " + str(np.around(sol[0],3)))
plt.title("p(x) = " + str(round(sol[0],3)) + "*sin(2x) + " + str(round(sol[1],3)) + "*cos(2x)")
ax.set(xlabel='x', ylabel='y')
ax.grid()
fig.savefig("../img/T1/Prob_T2_9_regressio_sinus.png")
plt.show()
