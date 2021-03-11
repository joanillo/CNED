# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Interpolació pura. Matriu de Vandermonde
https://www.unioviedo.es/compnum/laboratorios_py/new/05_Interpol_polinomica.html

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 runge.py 
'''

import numpy as np
from scipy.interpolate import lagrange
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

# =============================================================
# 1. Funció cos(x). Interpolació pura de Lagrange amb 5 punts 
# Fixar-se amb els termes senars que són 0. És el desenvolupament de Taylor
x = np.linspace(-np.pi/2, np.pi/2, 5)
y = np.cos(x)
poly = lagrange(x, y)
print(poly) # polinomi de Lagrange

xp = np.linspace(-np.pi/2, np.pi/2, 100)
yp = np.cos(xp)

fig, ax = plt.subplots()
plt.plot(xp, yp)
plt.plot(xp, poly(xp), x, y, 'bo')
plt.suptitle("cos(x). Fenòmen de Runge")
plt.title("Interpolació pura Lagrange. 5 punts sense soroll")
ax.grid()

fig.savefig("../img/T1/runge0.png")
plt.show()

# =============================================================
# 2. Afegim soroll. Interpolació pura de Lagrange amb 5 punts 
x = np.linspace(-np.pi/2, np.pi/2, 5)
y_or = np.cos(x)
noise = np.random.normal(0, .05, 5)
print(noise)
y = y_or + noise
poly = lagrange(x, y)
print(poly) # polinomi de Lagrange

xp = np.linspace(-np.pi/2, np.pi/2, 100)
yp = np.cos(xp)

fig, ax = plt.subplots()
plt.plot(xp, yp)
plt.plot(xp, poly(xp), x, y, 'bo')
plt.suptitle("cos(x). Fenòmen de Runge")
plt.title("Interpolació pura Lagrange. 5 punts amb soroll")
ax.grid()

fig.savefig("../img/T1/runge1.png")
plt.show()

# =============================================================
# 3. Afegim soroll. Interpolació pura de Lagrange amb 10 punts 
x = np.linspace(-np.pi/2, np.pi/2, 10)
y_or = np.cos(x)
noise = np.random.normal(0, .05, 10)
print(noise)
y = y_or + noise
poly = lagrange(x, y)
print(poly) # polinomi de Lagrange

xp = np.linspace(-np.pi/2, np.pi/2, 100)
yp = np.cos(xp)

fig, ax = plt.subplots()
plt.plot(xp, yp)
plt.plot(xp, poly(xp), x, y, 'bo')
plt.suptitle("cos(x). Fenòmen de Runge")
plt.title("Interpolació pura Lagrange. 10 punts amb soroll")
ax.grid()

fig.savefig("../img/T1/runge2.png")
plt.show()

# =============================================================
# 4. Afegim soroll. Interpolació pura de Lagrange amb 15 punts 
x = np.linspace(-np.pi/2, np.pi/2, 15)
y_or = np.cos(x)
noise = np.random.normal(0, .05, 15)
print(noise)
y = y_or + noise
poly = lagrange(x, y)
print(poly) # polinomi de Lagrange

xp = np.linspace(-np.pi/2, np.pi/2, 100)
yp = np.cos(xp)

fig, ax = plt.subplots()
plt.plot(xp, yp)
plt.plot(xp, poly(xp), x, y, 'bo')
plt.suptitle("cos(x). Fenòmen de Runge")
plt.title("Interpolació pura Lagrange. 15 punts amb soroll")
ax.grid()

fig.savefig("../img/T1/runge3.png")
plt.show()
