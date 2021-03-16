# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T2_8_lagrange.py
'''

import numpy as np
from scipy.interpolate import lagrange
import matplotlib
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

t = np.array([3.0, 3.1, 3.2, 3.3])
p = np.array([24.0, 27.8, 32.0, 36.5])

#interpolació lineal, hem d'agafar els dos valors més propers a t=3.14
poly1 = lagrange(t[1:3], p[1:3])
print("P(t) = \n" + str(poly1)) # 42 x - 102.4
print("P(3.14) = " + str(round(poly1(3.14),3))) # 29.48
print()

#interpolació quadràtica, hem d'agafar els tres valors més propers a t=3.14
poly2 = lagrange(t[0:3], p[0:3])
print("P(t) =  \n" + str(poly2)) # 20 x^2 - 84 x + 96
print("P(3.14) = " + str(round(poly2(3.14),3))) # 29.432
print()

#interpolació quadràtica, hem d'agafar els tres valors més propers a t=3.14
poly3 = lagrange(t, p)
print("P(t) = \n" + str(poly3)) # -16.67 x^3 + 175 x^2 - 564.3 x + 592
print("P(3.14) = " + str(round(poly3(3.14),3))) # 29.438
print()

t_ = np.arange(2, 5, 0.005)
fig, ax = plt.subplots()
plt.plot(t_, poly1(t_), t_, poly2(t_), t_, poly3(t_), 3.14, 29.438, 'bo')
ax.set(title='Heli líquid. Predicció de P(3.14)')
ax.grid()
fig.savefig("../img/T1/Prob_T2_8_lagrange.png")
plt.show()
