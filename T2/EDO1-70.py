# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-67: Resolució d'una eq dif lineal de 1r ordre (però en aquest cas és homogènea, i per tant és separable)

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-70.py
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

print('\nExemple: y\' + exp(x)/(1+exp(x))*y = 0')
ode = sp.Eq(sp.Derivative(y(x),x) + exp(x)/(1+exp(x))*y(x), 0)
sol = sp.dsolve(ode,y(x)) # Eq(y(x), C1/(exp(x) + 1))
print(sol)
print("que és la solució que hem trobat a EDO1-70")
