# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Més sobre la superconvergència

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 simpson_simple_superconvergencia.py
'''

import numpy as np
from scipy.interpolate import lagrange
from scipy import integrate
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============
print("Em mètode de Simpson simple integra perfectament polinomis de grau 2 i de grau 3.")

print("\nSi tinc un polinomi de grau 2 i faig el mètode simple de Simpson (3 punts), segur que funciona perquè la interpolació de Lagrange ens diu que el polinomi interpolador (de grau 2), segur que serà el mateix polinomi que l'original")
print("x**2+4*x-2, entre 0 i 4")

def f1(x):
	return x**2+4*x-2

x_or = np.array([0, 2, 4])
poly1 = lagrange(x_or, f1(x_or))
print("Lagrange: \n" + str(poly1)) #  x^2 + 4 x - 2 (coincideix, evidentment)

I1 = integrate.quad(lambda x: f1(x), 0, 4)
print("I1 = " + str(I1[0])) # 45.33
I2 = integrate.quad(lambda x: poly1(x), 0, 4)
print("I2 = " + str(I2[0])) # 45.33

print("\nEl tema és que si tinc un polinomi de grau 3 i també faig el mètode simple de Simpson (3 punts), el polinomi de Lagrange que obtenim (de grau 2) també integrarà amb exactitud el nostre polinomi (de grau 3) en aquest interval (superconvergència).")
print("-x^3 + 3x^2 -4x + 5, entre 0 i 6")

def f2(x):
	return -x**3+3*x**2-4*x+5

x_or = np.array([0, 3, 6])
poly2 = lagrange(x_or, f2(x_or))
print("Lagrange: \n" + str(poly2)) #  -6 x^2 + 14 x + 5

I1 = integrate.quad(lambda x: f2(x), 0, 6)
print("I1 = " + str(I1[0])) # -149.999
I2 = integrate.quad(lambda x: poly2(x), 0, 6)
print("I2 = " + str(I2[0])) # -149.999
