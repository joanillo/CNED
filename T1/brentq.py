# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Mètode de Brent per trobar l'arrel de x^2 -1
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 brentq.py
'''

import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

import numpy as np
from scipy import optimize


def f(x):
    return (x**2 - 1)

root = optimize.brentq(f, -2, 0)
print(root) # -1.0
root = optimize.brentq(f, 0, 2)
print(root) # +1