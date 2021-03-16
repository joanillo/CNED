# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
AF-80: Exercici proposat. Aproximació per mínims quadrats (regressió quadratica)
Les fórmules per plantejar el sistema d'equacions les he tret de martin_milton.pdf (https://recursos.salonesvirtuales.com/assets/bloques/martin_milton.pdf)

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T2_8_regressio.py
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

x = np.array([80, 40, -40, -120, -200, -280, -340])
y = np.array([6.47e-6, 6.24e-6, 5.72e-6, 5.09e-6, 4.30e-6, 3.33e-6, 2.45e-6])

print (y)
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

print(sol)
print ("\np(x) = " + str(round(sol[2],3)) + "*x^2 + " + str(round(sol[1],3)) + "*x + " + str(round(sol[0],3)))

def p(x):
    return sol[2]*x**2 + sol[1]*x + sol[0]

# https://stackoverflow.com/questions/18915378/rounding-to-significant-figures-in-numpy/63272943
def round_sig(f, p):
    return float(('%.' + str(p) + 'e') % f)

# gràfica
x_ = np.arange(-340.0, 80.0, 0.05)
fig, ax = plt.subplots()
plt.plot(x_, p(x_), x, y, 'bo')
plt.suptitle('Prob 8. Cilindre d\'acer. Regressió quadràtica')
#plt.title("\np(x) = " + str(np.around(sol[2],3)) + "*x^2 + " + str(np.around(sol[1],3)) + "*x + " + str(np.around(sol[0],3)))
plt.title("\np(x) = " + str(round_sig(sol[2],3)) + "*x^2 + " + str(round_sig(sol[1],3)) + "*x + " + str(round_sig(sol[0],3)))
ax.ticklabel_format(axis='y', style='sci', scilimits=(-3, 3))
ax.set(xlabel='Temp (F)', ylabel='Coef')

ax.grid()
fig.savefig("../img/T1/Prob_T2_8_regressio.png")
plt.show()
