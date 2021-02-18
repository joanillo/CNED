# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)

'''
ZF-5: trobar el zero de e^x - 5sin(x)
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 fsolve.py
'''

import numpy as np
from scipy.optimize import fsolve
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

def f(x):
    return np.exp(x) - 5*np.sin(x)

# podem trobar la solució (les solucions) amb scipy
x = np.array([0.0, 2.0])
sol = fsolve(f, x)
#trobem les dues solucions
print(sol, f(sol))

# podem trobar la solució aproximada fent la representació gràfica
# representació gràfica
x = np.arange(0.0, 2.0, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
ax.plot(x, f(x))

ax.set(xlabel='x', ylabel='y', title='e^x - 5sin(x)')
ax.grid()

fig.savefig("../img/T1/ZF-5_fsolve.png")
plt.show()

# podem cercar una aproximació de la solució fent una taula de valors
for valor in x:
	print(valor, f(valor))
