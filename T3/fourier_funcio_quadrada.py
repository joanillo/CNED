# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Fourier funció quadrada (SF-29)

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 fourier_funcio_quadrada.py
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

time_vec = np.linspace(-np.pi, np.pi, 100)

y1 = (4/np.pi)*np.sin(time_vec)

fig, ax = plt.subplots()
plt.plot(time_vec, y1)
ax.set(xlabel='alpha', ylabel='', title='sèrie de Fourier de la funció quadrada')
ax.grid()
plt.show()

y2 = (4/np.pi)*np.sin(time_vec) + (4/(3*np.pi))*np.sin(3*time_vec) + (4/(5*np.pi))*np.sin(5*time_vec) 

fig, ax = plt.subplots()
plt.plot(time_vec, y2)
ax.set(xlabel='alpha', ylabel='', title='sèrie de Fourier de la funció quadrada')
ax.grid()
plt.show()

y3 = (4/np.pi)*np.sin(time_vec) + (4/(3*np.pi))*np.sin(3*time_vec) + (4/(5*np.pi))*np.sin(5*time_vec) + (4/(7*np.pi))*np.sin(7*time_vec) + (4/(9*np.pi))*np.sin(9*time_vec) + (4/(11*np.pi))*np.sin(11*time_vec) + (4/(13*np.pi))*np.sin(13*time_vec)    

fig, ax = plt.subplots()
plt.plot(time_vec, y3)
ax.set(xlabel='alpha', ylabel='', title='sèrie de Fourier de la funció quadrada')
ax.grid()
plt.show()

fig, ax = plt.subplots()
plt.plot(time_vec, y1,time_vec, y2,time_vec, y3)
ax.set(xlabel='alpha', ylabel='', title='sèrie de Fourier de la funció quadrada')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-29_fourier_funcio_quadrada.png")

