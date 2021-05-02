# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-67: Resolució d'una eq dif lineal de 1r ordre (però en aquest cas és homogènea, i per tant és separable)

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-71.py
'''

import sympy as sp
from sympy import exp
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

print('\nExemple: x^2 y\' + x(x+2)y = e^x')
ode = sp.Eq(x**2 * sp.Derivative(y(x),x) + x*(x+2)*y(x), exp(x))
sol = sp.dsolve(ode,y(x)) # Eq(y(x), (C1 + exp(2*x)/2)*exp(-x)/x**2)
print(sol) 
print("que és la solució que hem trobat a EDO1-72")
