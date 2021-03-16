# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
AF-80: Exercici proposat. Aproximació per mínims quadrats (regressió quadratica)
Les fórmules per plantejar el sistema d'equacions les he tret de martin_milton.pdf (https://recursos.salonesvirtuales.com/assets/bloques/martin_milton.pdf)

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 AF-80-regressio_quadratica.py
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

x = np.array([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5])
y = np.array([10.08, 12.03, 11.38, 18.81, 20.53, 28.5, 31.38, 38-4, 48.39, 60.6, 66.66, 82.61, 91.37, 105.44, 122.53, 137.77, 152.74, 172.65, 188.84, 207.77, 230.94, 251.35, 274.07, 295.95])

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

# gràfica
x_ = np.arange(0.0, 12.0, 0.05)
fig, ax = plt.subplots()
plt.plot(x_, p(x_), x, y, 'bo')
plt.suptitle('AF-80. Regressió quadratica')
plt.title("\np(x) = " + str(round(sol[2],3)) + "*x^2 + " + str(round(sol[1],3)) + "*x + " + str(round(sol[0],3)))
ax.grid()
fig.savefig("../img/T1/AF-80-regressio_quadratica.png")
plt.show()