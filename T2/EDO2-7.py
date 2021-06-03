# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Resolució d'una EDO de 2n ordre (3 casos: disc>0, disc=0, disc<0)
https://mungoengineering.files.wordpress.com/2018/03/sympy_ode_example_12.pdf

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO2-7.py
'''

import numpy as np
import sympy as sp
from sympy.abc import t
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

x = sp.symbols('x')
y = sp.Function('y')

print("\nCas 1. Discriminant > 0")
# y'' + 3y' - 10y = 0
print('Exemple: y\'\' + 3y\' - 10y = 0')
y1 = sp.dsolve(y(t).diff(t,t) + 3*y(t).diff(t) - 10*y(t), y(t))
print(y1) # Eq(y(t), C1*exp(-5*t) + C2*exp(2*t))
print("que és la solució que hem trobat a EDO2-7")

print("\nCas 2. Discriminant = 0")
# y'' - 10y' + 25y = 0
print('Exemple: y\'\' - 10y\' + 25y = 0')
y1 = sp.dsolve(y(t).diff(t,t) - 10*y(t).diff(t) + 25*y(t), y(t))
print(y1) # Eq(y(t), (C1 + C2*t)*exp(5*t))
print("que és la solució que hem trobat a EDO2-12")

print("\nCas 3. Discriminant < 0")
# y'' - 6y' + 34y = 0
print('Exemple: y\'\' - 6y\' + 34y = 0')
y1 = sp.dsolve(y(t).diff(t,t) - 6*y(t).diff(t) + 34*y(t), y(t))
print(y1) # Eq(y(t), (C1*sin(5*t) + C2*cos(5*t))*exp(3*t))
print("que és la solució que hem trobat a EDO2-17")
