# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-67: Resolució d'una eq dif lineal de 1r ordre

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-67.py
'''

import sympy as sp
from sympy import cos
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

t = sp.symbols('t')
y = sp.Function('y')

print('\nExemple: t y\' + y = t cos(t)')
ode = sp.Eq(t * sp.Derivative(y(t),t) + y(t), t*cos(t))
sol = sp.dsolve(ode,y(t)) # Eq(y(t), C1/t + sin(t) + cos(t)/t)
print(sol)
print("que és la solució que hem trobat a EDO1-69")
