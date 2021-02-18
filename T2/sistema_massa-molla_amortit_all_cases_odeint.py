# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO2-21: Damped spring-mass oscillator
============================================
odeint: simulació . Transparència: EDO2(21)
mx'' + bx' + kx = 0
x'' + (b/m)x' + (k/m)x = 0
x'' = (-b/m)x' - (k/m)x

cd /home/joan/UPC_2021/CNED/apunts/python/
PS1="$ "
python3 sistema_massa-molla_amortit_v5_odeint.py
'''

import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

m = 1  # kg
k = 1  # N/m
b = np.array([8, 4, 2, .5, .1, 0])  # N s/m

mass = 1  # kg
kspring = 1  # N/m
cviscous = 4  # N s/m

def calc_deri(yvec, time, m,k,b):
    return (yvec[1], -(b/m)* yvec[1] - (k/m) * yvec[0])

yarr = np.empty(len(b), dtype=object)
time_vec = np.linspace(0, 25, 100)
yinit = (2, 0)

fig, ax = plt.subplots()

for i in range(0, len(b)):
	yarr[i] = odeint(calc_deri, yinit, time_vec, args=(m,k,b[i]))
	plt.plot(time_vec, yarr[i][:, 0], label='b=' + str(b[i]))


plt.legend(loc='best')
ax.set(xlabel='temps (s)', ylabel='y (m)', title='sistema massa-molla amb amortidor (odeint)')
ax.grid()
fig.savefig("../img/T2/EDO2-21_sistema_massa-molla_amortit_all_cases_odeint.png")
plt.show()

