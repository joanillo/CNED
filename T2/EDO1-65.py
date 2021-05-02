# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-65: Resolució d'una eq dif lineal de 1r ordre

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-65.py
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

print('\nExemple: x^2 y\' + xy = 1')
ode = sp.Eq((x**2) * sp.Derivative(y(x),x) + x*y(x), 1)
sol = sp.dsolve(ode,y(x)) # Eq(y(x), (C1 + log(x))/x)
print(sol)
print("que és la solució que hem trobat a EDO1-66")
