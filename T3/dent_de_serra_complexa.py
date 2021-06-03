# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Exemple SF-47

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 dent_de_serra_complexa.py
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

N = 5 # paràmetre que podem canviar

time = np.linspace(-6, 6, 500)

def an(n):
	return 2*(-1)**n/(np.pi*n)

def g(t, Nh):
	g = np.array([an(i)*1j*np.exp(1j*np.pi*i*t/2) for i in range(1,Nh+1)])
	h = np.array([-an(i)*1j*np.exp(-1j*np.pi*i*t/2) for i in range(1,Nh+1)])
	return (g+h).sum()

f = np.array([g(t,N).real for t in time]) # hem d'agafar la part real

fig, ax = plt.subplots()
plt.plot(time, f)
ax.set(xlabel='Funció dent de serra. Fourier forma complexa fins a N='+str(N), ylabel='', title='Exemple SF-59')
ax.grid()
plt.show()
fig.savefig("../img/T3/dent_de_serra_complexa.png")
