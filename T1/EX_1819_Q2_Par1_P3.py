# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
AF-80: Exercici proposat. Aproximació per mínims quadrats (regressió quadratica)
Les fórmules per plantejar el sistema d'equacions les he tret de martin_milton.pdf (https://recursos.salonesvirtuales.com/assets/bloques/martin_milton.pdf)

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 EX_1819_Q2_Par1_P3.py
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

t = np.array([-4, -2, 0, 2, 4])
p = np.array([252.7, 272.2, 292.8, 314.6, 337.7])

a0 = len(t)
a1 = np.sum(t**3)
a2 = np.sum(t**6)

b0 = np.sum(p)
b1 = np.sum((t**3).dot(p))

A = np.array([[a0, a1],
	[a1, a2]])

B = np.array([b0, b1])
print(A)
print(B)

sol = np.linalg.solve(A,B) # dues formes
#sol = np.linalg.inv(A).dot(B)

print(sol)

print ("\nP(T) = " + str(round(sol[0],3)) + " + " + str(round(sol[1],3)) + "*T^3")

def P(T):
    return sol[0] + sol[1]*T**3

print("P(0) = a + b*T^3 = " + str(P(0))) # P = 294

# gràfica
T_ = np.arange(-4.0, 4.0, 0.05)
fig, ax = plt.subplots()
plt.plot(T_, P(T_), t, p, 'bo')

plt.suptitle('a + b*T^3')
plt.title("P(T) = " + str(round(sol[0],3)) + " + " + str(round(sol[1],3)) + "*T^3")
ax.set(xlabel='x', ylabel='y')
ax.grid()
fig.savefig("../img/T1/EX_1819_Q2_Par1_P3.png")
plt.show()
