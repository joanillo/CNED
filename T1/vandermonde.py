# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Interpolació pura. Matriu de Vandermonde
https://www.unioviedo.es/compnum/laboratorios_py/new/05_Interpol_polinomica.html

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 vandermonde.py 
'''

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

def Vandermonde(x):
	print('Matriu de Vandermonde V:')
	V = np.array([
		[1, x[0], x[0]**2, x[0]**3, x[0]**4],
		[1, x[1], x[1]**2, x[1]**3, x[1]**4],
		[1, x[2], x[2]**2, x[2]**3, x[2]**4],
		[1, x[3], x[3]**2, x[3]**3, x[3]**4],
		[1, x[4], x[4]**2, x[4]**3, x[4]**4]
		])
	print (V)
	return V

def polVandermonde(x,y):
	V = Vandermonde(x)
	# Anem a calcular els coeficients del polinomi resolent el sistema lineal Vp = y, on V serà la matriu de Vandermonde.
	p = np.linalg.solve(V,y)
	p = p[::-1] # li donc la volta, de manera que comença pel terme de grau 4
	return p

x = np.array([-1, 0, 2, 3, 5])
y = np.array([ 1, 3, 4, 3, 1])

# opcions del print
np.set_printoptions(precision = 2)   # només dos decimals
np.set_printoptions(suppress = True) # no utilitzar notació exponencial

print("5 punts, polinomi de grau 4")
print("(-1,1) (0,3) (2,4) (3,3) (5,1)")
print()

p = polVandermonde(x,y)
print('\nCoeficients del polinomi:')
print(p)


#numpy té una funció per calcular la matriu de Vandermonde
print('\nMatriu de Vandermonde amb la funció np.vander():')
va = np.vander(x, len(x))
print(va)

cond = np.linalg.cond(va, p='fro')
print("Núm de condició MMC1: " + str(cond))
print("És un valor molt gran, vol dir que la matriu està mal condicionada")

# gràfica
xp = np.linspace(min(x),max(x)) # 50 punts
yp = np.polyval(p,xp)
fig, ax = plt.subplots()
plt.plot(xp, yp)
plt.plot(x, y,'bo')


ax.set(title='Interpolació pura (coef. del polinomi resolent el sistema d\'equacions)')
ax.grid()

fig.savefig("../img/T1/vandermonde.png")
plt.show()
