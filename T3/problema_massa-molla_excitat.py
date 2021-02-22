# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
SF-76
problema_massa-molla_excitat. Excitació amb una funció senoidal. Sense esmorteïment
sense ressonància i amb ressonància.
Solució analítica a problema_massa-molla_excitat.pdf, comparació solució analítica vs simulació

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 problema_massa-molla_excitat.py
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

'''
eq diferencial:
mx'' + kx = A sin(wt)
x'' + (k/m) = A/m sin(wt)
x'' + wo^2 = A/m sin(wt)
'''
# dades:
m=1 # Kg
k=1 # N/m
wo = np.sqrt(k/m) # wo=1
A = 1

# condicions inicials: x(0) = 3 ; x'(0) = 0

time = np.linspace(0,100, 1000)


# cas 1: w != wo =====================================================================
def solucio_sense_ressonancia(w):
	x = 3*np.cos(wo*time) - (w/(wo**2 - w**2))*np.sin(wo*time) + (1/(wo**2 - w**2))*np.sin(w*time)
	return x

# wo >> w
w = 0.1
x = solucio_sense_ressonancia(w)

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació')
plt.title('$\\omega_o$ >> $\\omega$. $\\omega_o$=1, $\\omega$=0.1. Rissat de freq 0.1')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_v1.png")

# wo > w
w = 0.4
x = solucio_sense_ressonancia(w)

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació')
plt.title('$\\omega_o$ > $\\omega$. $\\omega_o$=1, $\\omega$=0.4. Rissat de freq 0.4')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_v2.png")

# wo << w
w = 5
x = solucio_sense_ressonancia(w)

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació')
plt.title('$\\omega_o$ << $\\omega$. $\\omega_o$=1, $\\omega$=5. No hi ha rissat')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_v3.png")

# wo < w
w = 1.2
x = solucio_sense_ressonancia(w)

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació')
plt.title('$\\omega_o$ < $\\omega$. $\\omega_o$=1, $\\omega$=1.2. Rissat')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_v4.png")

# wo ~ w
w = 1.05
x = solucio_sense_ressonancia(w)

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació')
plt.title('$\\omega_o$ ~ $\\omega$. $\\omega_o$=1, $\\omega$=1.05.  Apareix la ressonància, i l\'amplitud puja')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_v5.png")

# cas 2: w = wo (ressonància) ========================================================
def solucio_amb_ressonancia():
	x = (3 - time/(2*wo))*np.cos(wo*time) + (1/(2*wo**2))*np.sin(wo*time)
	return x

# wo = w
x = solucio_amb_ressonancia()

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació')
plt.title('$\\omega_o$ = $\\omega$. $\\omega_o$=1.  Ressonància')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_v6.png")