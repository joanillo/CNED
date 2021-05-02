# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-48: Resolució d'una eq dif de variables separables: y lnx x' = (y+1)^2/x^2

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-48.py
'''

import sympy as sp
from sympy import log
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

x = sp.Function('x')
y = sp.symbols('y')

print('\nExemple: y lnx x\' = (y+1)^2/x^2')
print('Exemple: x\' = (y+1)^2 / (x^2 * lnx *y)')
ode = sp.Eq(sp.Derivative(x(y),y),((y+1)**2 / (x(y)**2 * log(x(y)) * y)))
sol = sp.dsolve(ode,x(y)) # Eq(x(y), exp(LambertW(C1 + 9*y**2*exp(-1)/2 + 18*y*exp(-1) + 9*exp(-1)*log(y))/3 + 1/3))
print(sol) # 
print("ha sabut trobar la forma explícita de la solució, però és molt complicada")

print("====")
print("Com que són variables separables, podem trobar les integrals per separat:")

x = sp.symbols('x')
solx = sp.integrate(x**2 * log(x), x)
print(solx)

y = sp.symbols('y')
soly = sp.integrate((y+1)**2 / y, y)
print(soly)
print("Hem d'igualar les dues integrals, i afegir-hi una constant.")