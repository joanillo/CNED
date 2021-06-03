# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Exemple SF-47
https://stackoverflow.com/questions/4258106/how-to-calculate-a-fourier-series-in-numpy

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 exemple_SF-47_v2.py
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

N = 29

time = np.linspace(-np.pi, 3*np.pi, 500)

def an(n):
	return (1/(2*n-1))

def bn(n):
	return (-1)**n/(2*n)

def g(t, Nh):
	g = np.array([an(i)*np.cos(i*t) + bn(i)*np.sin(i*t) for i in range(1,Nh+1)])
	return g.sum()

f = np.pi/2 + np.array([g(t,N).real for t in time])

fig, ax = plt.subplots()
plt.plot(time, f)
ax.set(xlabel='Fourier fins a N='+str(N), ylabel='', title='Exemple SF-47')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-47_v2.png")
