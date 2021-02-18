# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
polinomis de Lagrange. Exemple
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 lagrange1.py 
'''

import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

from scipy.interpolate import lagrange
import numpy as np
x = np.array([0, 1, 2])
y=x**3
poly = lagrange(x, y)
print(poly)
'''
   2
3 x - 2 x
'''
