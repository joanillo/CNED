# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Circuit RLC (transparència L-44, Eq Dif amb Transformades de Laplace)

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 RLC.py
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

time_vec = np.linspace(0, 15, 100)

y=2.0/np.sqrt(3)*np.sin((np.sqrt(3)/2)*time_vec)*np.exp(-time_vec/2)

fig, ax = plt.subplots()
plt.plot(time_vec, y)

ax.set(xlabel='temps (s)', ylabel='intensitat', title='circuit RLC. Transparència L-44')
ax.grid()

fig.savefig("../img/T3/L-44_circuit_RLC.png")
plt.show()
