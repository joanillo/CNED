# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO2-25: overdamped
============================================
Damped spring-mass oscillator
equació característica: s^2 + (b/m)s + (k/m) = 0. Tenim la solució analítica: transparència EDO(2)-22
Cas 1: sistema sobreamortiguat (overdamped)
∆ = b^2 − 4mk > 0
============================================

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 sistema_massa-molla_amortit_overdamped.py
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
b = np.array([4,8,12])  # N s/m (3 coeficients de fregament diferents)


f1 = b/(2*m)
f2 = k/m
s1 = -f1 + np.sqrt(f1**2 - f2)
s2 = -f1 - np.sqrt(f1**2 - f2)

#CI y(0)=2, y'(0) = 0
C1 = np.array([2.1547,2.033,2.014]) # aquests coeficients es calculen manualment o amb EDO2-7_PVI.py
C2 = np.array([-0.1547,-0.033,-0.014]) 

y = np.empty(len(b), dtype=object)

time_vec = np.linspace(0, 25, 100)
#print (type(time_vec))

fig, ax = plt.subplots()

for i in range(0, len(b)):
	#print(b[i])
	y[i] = C1[i]*np.exp(s1[i]*time_vec) + C2[i]*np.exp(s2[i]*time_vec)
	plt.plot(time_vec, y[i], label='b=' + str(b[i]))

plt.legend(loc='best')

ax.set(xlabel='temps (s)', ylabel='y (m)', title='sistema massa-molla amb amortidor sobreamortiguat')
ax.grid()
fig.savefig("../img/T2/EDO2-25_sistema_massa-molla_amortit_overdamped1.png")
plt.show()

v = np.empty(len(b), dtype=object)
y[0] = C1[0]*np.exp(s1[0]*time_vec) + C2[0]*np.exp(s2[0]*time_vec)
v[0] = s1[0]*C1[0]*np.exp(s1[0]*time_vec) +s2[0]*C2[0]*np.exp(s2[0]*time_vec)

fig, ax1 = plt.subplots()
#ax2 = ax1.twinx()
plt.plot(time_vec, y[0], label='y (b=' + str(b[0]) + ')')
plt.plot(time_vec, v[0], label='v (b=' + str(b[0]) + ')')
plt.legend(loc='best')
ax1.set(xlabel='temps (s)', ylabel='y (m)', title='sistema massa-molla amb amortidor sobreamortiguat')
#ax2.set(ylabel='v (m/s)')
ax1.grid()
fig.savefig("../img/T2/EDO2-25_sistema_massa-molla_amortit_overdamped2.png")
plt.show()
