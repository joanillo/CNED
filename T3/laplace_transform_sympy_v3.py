# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Utilitzem la consola de ipython per tenir unes fórmules més boniques
$ pip3 install ipython

Laplace Transform amb Sympy
Exemple de com amb sympy puc calcular les principals transformades de Laplace
*https://dynamics-and-control.readthedocs.io/en/latest/1_Dynamics/3_Linear_systems/Laplace%20transforms.html

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
ipython3 laplace_transform_sympy_v3.py
'''

import sympy
from matplotlib import pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

sympy.init_printing()
sympy.init_session()

#Letss define some symbols to work with.
t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)

omega = sympy.Symbol('omega', real=True)
exp = sympy.exp
sin = sympy.sin
cos = sympy.cos
functions = [1,
         t,
         exp(-a*t),
         t*exp(-a*t),
         t**2*exp(-a*t),
         sin(omega*t),
         cos(omega*t),
         1 - exp(-a*t),
         exp(-a*t)*sin(omega*t),
         exp(-a*t)*cos(omega*t),
         ]
print (functions)
# [1, t, e−at, te−at, t2e−at, sin(ωt), cos(ωt), 1−e−at, e−atsin(ωt), e−atcos(ωt)]

# definim la transformada de Laplace:
def L(f):
    return sympy.laplace_transform(f, t, s, noconds=True)

# transformades de Laplace
Fs = [L(f) for f in functions]
print(Fs)
# [1s, 1s2, 1a+s, 1(a+s)2, 2(a+s)3, ωω2+s2, sω2+s2, as(a+s), ωω2+(a+s)2, a+sω2+(a+s)2]

print('NOTA: estudiar pprint, etc. En la consola (>>>), Fs printa correctament els denominadors...')
