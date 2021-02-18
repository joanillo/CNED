# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Half Wave Rectifier (SF-44)

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 half_wave_rectifier.py
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

time_vec = np.linspace(-1, 1, 100)

y1 = 1/np.pi - .5*np.sin(np.pi*time_vec)

fig, ax = plt.subplots()
plt.plot(time_vec, y1)
ax.set(xlabel='-L a L', ylabel='', title='sèrie de Fourier del rectificador de mitja ona (diode)')
ax.grid()
plt.show()

y2 = 1/np.pi - .5*np.sin(np.pi*time_vec) - 2/(np.pi*3)*np.cos(2*np.pi*time_vec)

fig, ax = plt.subplots()
plt.plot(time_vec, y2)
ax.set(xlabel='-L a L', ylabel='', title='sèrie de Fourier del rectificador de mitja ona (diode)')
ax.grid()
plt.show()

y3 = 1/np.pi - .5*np.sin(np.pi*time_vec) - 2/(np.pi*3)*np.cos(2*np.pi*time_vec) - 2/(np.pi*15)*np.cos(4*np.pi*time_vec)

fig, ax = plt.subplots()
plt.plot(time_vec, y3)
ax.set(xlabel='-L a L', ylabel='', title='sèrie de Fourier del rectificador de mitja ona (diode)')
ax.grid()
plt.show()

y4 = 1/np.pi - .5*np.sin(np.pi*time_vec) - 2/(np.pi*3)*np.cos(2*np.pi*time_vec) - 2/(np.pi*15)*np.cos(4*np.pi*time_vec) - 2/(np.pi*35)*np.cos(6*np.pi*time_vec)

fig, ax = plt.subplots()
plt.plot(time_vec, y4)
ax.set(xlabel='-L a L', ylabel='', title='sèrie de Fourier del rectificador de mitja ona (diode)')
ax.grid()
plt.show()

fig, ax = plt.subplots()
plt.plot(time_vec, y1,time_vec, y2,time_vec, y3,time_vec, y4)
ax.set(xlabel='-L a L', ylabel='', title='sèrie de Fourier del rectificador de mitja ona (diode)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-44_half_wave_rectifier.png")

