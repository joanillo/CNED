# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Resolució d'una EDO de 2n ordre no homogènea

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO2-45.py
'''

import numpy as np
import sympy as sp
from sympy.abc import t
from sympy import exp
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

# y'' + 3y' - 10y = 5t^2
print('Exemple: y\'\' + 3y\' - 10y = 5t^2')
y1 = sp.dsolve(y(t).diff(t,t) + 3*y(t).diff(t) - 10*y(t) - 5*t**2, y(t))
print(y1) # Eq(y(t), C1*exp(-5*t) + C2*exp(2*t) - t**2/2 - 3*t/10 - 19/100)
print("que és la solució que hem trobat a EDO2-45")

# y'' - y' - 6y = 10exp(3t)
print('\nExemple: y\'\' - y\' - 6y = 10*exp(3t)')
y1 = sp.dsolve(y(t).diff(t,t) - y(t).diff(t) - 6*y(t) - 10*exp(3*t), y(t))
print(y1) # Eq(y(t), C2*exp(-2*t) + (C1 + 2*t)*exp(3*t))
print("que és la solució que hem trobat a EDO2-48")



