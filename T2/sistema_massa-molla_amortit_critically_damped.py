# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO2-25: critycally damped
============================================
Damped spring-mass oscillator
equació característica: s^2 + (b/m)s + (k/m) = 0. Tenim la solució analítica: transparència EDO(2)-25
Cas 1: sistema amb amortiment crític (critically damped)
∆ = b^2 − 4mk = 0
============================================

cd /home/joan/UPC_2021/CNED/apunts/python/
PS1="$ "
python3 sistema_massa-molla_amortit_critically_damped.py
'''

import numpy as np
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
b = 2  # N s/m

f1 = b/(2*m)
f2 = k/m
s1 = -f1

#CI y(0)=2, y'(0) = 0
C1 = 2
C2 = 2 

#y = np.empty(len(b), dtype=object)

time_vec = np.linspace(0, 25, 100)
#print (type(time_vec))

fig, ax = plt.subplots()

y = (C1 + C2*time_vec)*np.exp(s1*time_vec)
plt.plot(time_vec, y, label='b=' + str(b))

plt.legend(loc='best')

ax.set(xlabel='temps (s)', ylabel='y (m)', title='sistema massa-molla amb amortiment crític')
ax.grid()
fig.savefig("../img/T2/EDO2-25_sistema_massa-molla_amortit_critically_damped_v1.png")
plt.show()

v = C2*np.exp(s1*time_vec) - (C1 + C2*time_vec)*np.exp(s1*time_vec)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.plot(time_vec, y, label='y (b=' + str(b) + ')')
plt.plot(time_vec, v, label='v (b=' + str(b) + ')')
plt.legend(loc='best')
ax1.set(xlabel='temps (s)', ylabel='y (m)', title='sistema massa-molla amb amortiment crític')
ax2.set(ylabel='v (m/s)')
ax1.grid()
fig.savefig("../img/T2/EDO2-25_sistema_massa-molla_amortit_critically_damped_v2.png")
plt.show()
