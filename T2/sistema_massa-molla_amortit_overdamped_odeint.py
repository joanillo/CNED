# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO2-25: overdamped
https://scipy-lectures.org/intro/scipy/auto_examples/plot_odeint_damped_spring_mass.html -> però la fórmula està malament
Damped spring-mass oscillator
============================================
odeint: simulació . Transparència: EDO2(21)
mx'' + bx' + kx = 0
x'' + (b/m)x' + (k/m)x = 0
x'' = (-b/m)x' - (k/m)x

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 sistema_massa-molla_amortit_overdamped_odeint.py
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
b = 4  # N s/m

def calc_deri(yvec, time, m,k,b):
    return (yvec[1], -(b/m)* yvec[1] - (k/m) * yvec[0])

time_vec = np.linspace(0, 25, 100)
yinit = (2, 0)
yarr = odeint(calc_deri, yinit, time_vec, args=(m,k,b))

fig, ax1 = plt.subplots()
#ax2 = ax1.twinx()
plt.plot(time_vec, yarr[:, 0], label='y')
plt.plot(time_vec, yarr[:, 1], label="y'")
plt.legend(loc='best')
ax1.set(xlabel='temps (s)', ylabel='y (m)', title='sistema massa-molla amb amortiment (odeint)')
#ax2.set(ylabel='v (m/s)')
ax1.grid()
fig.savefig("../img/T2/EDO2-25_sistema_massa-molla_amortit_overdamped_odeint.png")
plt.show()

