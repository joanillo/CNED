# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 EX_1920_Q2_Par1_P2.py
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

x = np.array([0.0, 0.2, 0.4])
y = np.array([1.0000, 1.2214, 1.4918])


#interpolació quadràtica
poly = lagrange(x, y)
print("y(x) =  \n" + str(poly)) # 0.6125 x^2 + 0.9845 x + 1

print("y(0.25) = " + str(poly(0.25))) # e^(1/4) = 1.28440625
print()

x_ = np.arange(0.0, 0.4, 0.005)
fig, ax = plt.subplots()
plt.plot(x_, poly(x_), x, y, 'bo')
ax.set(title='Funció exp(x). Interpolació de Lagrange')
ax.grid()
fig.savefig("../img/T1/EX_1920_Q2_Par1_P2.png")
plt.show()
