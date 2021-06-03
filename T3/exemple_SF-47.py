# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Exemple SF-47

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 exemple_SF-47.py
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

time_vec = np.linspace(-np.pi, 3*np.pi, 500)

y1 = np.pi/2
y1 = y1 + (1*np.cos(time_vec) - (1/2)*np.cos(time_vec))
y1 = y1 + ((1/3)*np.cos(2*time_vec) + (1/4)*np.cos(2*time_vec))
y1 = y1 + ((1/5)*np.cos(3*time_vec) - (1/6)*np.cos(3*time_vec))
y1 = y1 + ((1/7)*np.cos(4*time_vec) + (1/8)*np.cos(4*time_vec))
y1 = y1 + ((1/9)*np.cos(5*time_vec) - (1/10)*np.cos(5*time_vec))
y1 = y1 + ((1/11)*np.cos(6*time_vec) + (1/12)*np.cos(6*time_vec))
y1 = y1 + ((1/13)*np.cos(7*time_vec) - (1/14)*np.cos(7*time_vec))

fig, ax = plt.subplots()
plt.plot(time_vec, y1)
ax.set(xlabel='Fourier fins a N=7', ylabel='', title='Exemple SF-47')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-47_exemple.png")

# --------------------------
# Cn = 4/(n*pi)
# phi = pi/2 (senar), -pi/2 (parell)
freq = ['wo', '2wo', '3wo', '4wo', '5wo', '6wo', '7wo']
coef = [4/(np.pi), 4/(2*np.pi), 4/(3*np.pi), 4/(4*np.pi), 4/(5*np.pi), 4/(6*np.pi), 4/(7*np.pi)]

fig, ax = plt.subplots()
plt.bar(freq, coef, width= 0.9, align='center',color='cyan', edgecolor = 'red')

# This is the location for the annotated text
i = 1.0
j = 2000
# Annotating the bar plot with the values (total death count)
for i in range(len(freq)):
    plt.annotate(coef[i], (-0.1 + i, coef[i] + j))
plt.title("Coeficients Cn de la forma harmònica")
plt.xlabel('freqüència')
plt.ylabel('Cn')
plt.show()
fig.savefig("../img/T3/SF-47_exemple_coef.png")

freq = ['wo', '2wo', '3wo', '4wo', '5wo', '6wo', '7wo']
fase = [np.pi/2, -np.pi/2, np.pi/2, -np.pi/2, np.pi/2, -np.pi/2, np.pi/2]

fig, ax = plt.subplots()
plt.bar(freq, fase, width= 0.9, align='center',color='cyan', edgecolor = 'red')

# This is the location for the annotated text
i = 1.0
j = 2000
# Annotating the bar plot with the values (total death count)
for i in range(len(freq)):
    plt.annotate(coef[i], (-0.1 + i, coef[i] + j))
plt.title("Fases de la forma harmònica")
plt.xlabel('fases')
plt.ylabel('Phi_n')
plt.show()
fig.savefig("../img/T3/SF-47_exemple_fases.png")
