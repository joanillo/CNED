# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Exemple SF-47

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 dent_de_serra_estandard.py
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

N = 30 # paràmetre que podem canviar

time = np.linspace(-6, 6, 500)

def bn(n):
	return -4*(-1)**n/(np.pi*n)

def g(t, Nh):
	g = np.array([bn(i)*np.sin(i*np.pi*t/2) for i in range(1,Nh+1)])
	return g.sum()

f = np.array([g(t,N) for t in time])

fig, ax = plt.subplots()
plt.plot(time, f)
ax.set(xlabel='Funció dent de serra. Fourier forma estàndard fins a N='+str(N), ylabel='', title='Exemple SF-59')
ax.grid()
plt.show()
fig.savefig("../img/T3/dent_de_serra_estandard.png")
