# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Fourier funció quadrada (SF-37)

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 fourier_funcio_triangle.py
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

y1 = np.pi/2 + (4*np.pi)*np.cos(time_vec)

fig, ax = plt.subplots()
plt.plot(time_vec, y1)
ax.set(xlabel='alpha', ylabel='', title='sèrie de Fourier de la funció triangle')
ax.grid()
plt.show()

y2 = np.pi/2 + (4*np.pi)*np.cos(time_vec) + (4*np.pi/9)*np.cos(3*time_vec)

fig, ax = plt.subplots()
plt.plot(time_vec, y2)
ax.set(xlabel='alpha', title='sèrie de Fourier de la funció triangle')
ax.grid()
plt.show()

y3 = np.pi/2 + (4*np.pi)*np.cos(time_vec) + (4*np.pi/9)*np.cos(3*time_vec) + (4*np.pi/25)*np.cos(5*time_vec)

fig, ax = plt.subplots()
plt.plot(time_vec, y3)
ax.set(xlabel='alpha', ylabel='', title='sèrie de Fourier de la funció triangle')
ax.grid()
plt.show()

fig, ax = plt.subplots()
plt.plot(time_vec, y1,time_vec, y2,time_vec, y3)
ax.set(xlabel='alpha', ylabel='', title='sèrie de Fourier de la funció quadrada')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-37_fourier_funcio_triangle.png")

