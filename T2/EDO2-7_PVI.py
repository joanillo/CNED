# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Resolució d'una EDO de 2n ordre (3 casos: disc>0, disc=0, disc<0). Molla esmorteïda
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
x = sp.symbols('y', cls=sp.Function)
'''
m = 1  # kg
k = 1  # N/m
b = 4 (overdamped); 2 (critically damped); 0.5 (underdamped)
'''
print("\nCas 1. Discriminant > 0")
# y'' + 4y' + y = 0
print('Exemple: y\'\' + 4y\' + y = 0')
y1 = sp.dsolve(y(t).diff(t,t) + 4*y(t).diff(t) + y(t), y(t))
print(y1) # Eq(y(t), C1*exp(t*(-2 - sqrt(3))) + C2*exp(t*(-2 + sqrt(3))))
print(y1.rhs)
print("PVI: y(0)=2, y'(0) = 0")
C = sp.solve([y1.rhs.subs(t,0)-2, y1.rhs.diff(t).subs(t,0)-0])
print(C) # {C2: 1 + 2*sqrt(3)/3, C1: 1 - 2*sqrt(3)/3}

print("\nCas 2. Discriminant = 0")
# y'' + 2y' + y = 0
print('Exemple: y\'\' + 2y\' + y = 0')
y1 = sp.dsolve(y(t).diff(t,t) + 2*y(t).diff(t) + y(t), y(t))
print(y1) # Eq(y(t), (C1 + C2*t)*exp(-t))
print(y1.rhs)
print("PVI: y(0)=2, y'(0) = 0")
C = sp.solve([y1.rhs.subs(t,0)-2, y1.rhs.diff(t).subs(t,0)-0])
print(C) # {C1: 2, C2: 2}

print("\nCas 3. Discriminant < 0")
# y'' + 0.5y' + y = 0
print('Exemple: y\'\' + 0.5y\' + y = 0')
y1 = sp.dsolve(y(t).diff(t,t) + 0.5*y(t).diff(t) + y(t), y(t))
print(y1) # Eq(y(t), (C1*sin(0.968245836551854*t) + C2*cos(0.968245836551854*t))*exp(-0.25*t))
print(y1.rhs) # (C1*sin(0.968245836551854*t) + C2*cos(0.968245836551854*t))*exp(-0.25*t))
print("PVI: y(0)=2, y'(0) = 0")
C = sp.solve([y1.rhs.subs(t,0)-2, y1.rhs.diff(t).subs(t,0)-0])
print(C) #{C1: 0.5164, C2: 2}
