# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-76: 

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-76.py
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

t = sp.symbols('t')
y = sp.Function('y')

print('\nExemple: y\' = t - y^2')
ode = sp.Eq(sp.Derivative(y(t),t), t - y(t)**2)
sol = sp.dsolve(ode,y(t))
print(sol) 
print("No acaba de trobar la solució i diu que hi ha un terme d'ordre O(t^6)")
