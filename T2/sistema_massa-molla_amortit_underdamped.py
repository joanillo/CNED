# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO2-28: underdamped
============================================
Damped spring-mass oscillator
equació característica: s^2 + (b/m)s + (k/m) = 0. Tenim la solució analítica: transparència EDO(2)-28
Cas 1: sistema subamortiguat (underdamped)
∆ = b^2 − 4mk < 0
============================================

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 sistema_massa-molla_amortit_underdamped.py
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
b = np.array([.5, .2, .1, 0])  # N s/m

#omega = np.sqrt(kspring / mass)
f1 = b/(2*m)
f2 = k/m
s= -f1
w = np.sqrt(f2 - f1**2)

#CI y(0)=2, y'(0) = 0
C1 = np.array([2,2,2,2]) 
C2 = -2*s/w

y = np.empty(len(b), dtype=object)

time_vec = np.linspace(0, 25, 100)

fig, ax = plt.subplots()

for i in range(0, len(b)):
	y[i] = np.exp(s[i]*time_vec)*(C1[i]*np.cos(w[i]*time_vec) + C2[i]*np.sin(w[i]*time_vec))
	plt.plot(time_vec, y[i], label='b=' + str(b[i]))

plt.legend(loc='best')

ax.set(xlabel='temps (s)', ylabel='y (m)', title='sistema massa-molla amb amortidor subamortiguat')
ax.grid()
fig.savefig("../img/T2/EDO2-28_sistema_massa-molla_amortit_underdamped_v1.png")
plt.show()


v = np.empty(len(b), dtype=object)
y[1] = np.exp(s[1]*time_vec)*(C1[1]*np.cos(w[1]*time_vec) + C2[1]*np.sin(w[1]*time_vec))
v[1] = np.exp(s[1]*time_vec)*((s[1]*C1[1]+w[1]*C2[1])*np.cos(w[1]*time_vec) + (s[1]*C2[1]-w[1]*C1[1])*np.sin(w[1]*time_vec))

fig, ax1 = plt.subplots()
#ax2 = ax1.twinx()
plt.plot(time_vec, y[1], label='y (b=' + str(b[1]) + ')')
plt.plot(time_vec, v[1], label='v (b=' + str(b[1]) + ')')
plt.legend(loc='best')
ax1.set(xlabel='temps (s)', ylabel='y (m)', title='sistema massa-molla amb amortidor subamortiguat')
#ax2.set(ylabel='v (m/s)')
ax1.grid()
fig.savefig("../img/T2/EDO2-28_sistema_massa-molla_amortit_underdamped_v2.png")
plt.show()
