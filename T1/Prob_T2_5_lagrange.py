# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T2_5_lagrange.py
'''

import numpy as np
from scipy.interpolate import lagrange
from scipy.special import gamma
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

x = np.array([1.0, 1.1, 1.2, 1.3])
y = np.array([1.00000, 0.95135, 0.91817, 0.89747])

poly = lagrange(x, y)
print("P(x) = " + str(poly)) # -0.4983 x^3 + 2.418 x^2 - 3.915 x + 2.995
print("P(1.23) = " + str(poly(1.23)))

x_ = np.arange(0.5, 1.8, 0.005)
fig, ax = plt.subplots()
plt.plot(x_, gamma(x_), x_, poly(x_), x, y, 'bo')
ax.set(title='Funció gamma i la seva interpolació cúbica')
ax.grid()

fig.savefig("../img/T1/Prob_T2_5_lagrange.png")
plt.show()
