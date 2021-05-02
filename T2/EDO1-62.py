# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-62: Resolució d'una eq dif lineal de 1r ordre

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-62.py
'''

import sympy as sp
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

print('\nExemple: (1/x^2) y\' + 3y = 1')
ode = sp.Eq((1/x**2) * sp.Derivative(y(x),x) + 3*y(x), 1)
sol = sp.dsolve(ode,y(x)) # Eq(y(x), C1*exp(-x**3)/3 + 1/3)
print(sol)
print("que és la solució que hem trobat a EDO1-64")
