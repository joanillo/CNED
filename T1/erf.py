# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
IN-4: error de Gauss (distribució normal)
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 erf.py
'''

import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

from math import pi, exp
import numpy as np
from scipy import integrate

mean = 0
sd   = 1

#l'àrea sota la distribució normal val 1 (entre -inf i +inf)
#cercar a google images: integral distribucion normal
print(integrate.quad(lambda x: 1 / ( sd * ( 2 * pi ) ** 0.5 ) * exp( x ** 2 / (-2 * sd ** 2) ), 0, np.inf ))

# la integral entre -inf i inf de e^(-(x^2)) = sqrt(pi)
print(integrate.quad(lambda x: np.exp(- x** 2), -np.inf, np.inf )) # sqrt(pi) = 1.772
