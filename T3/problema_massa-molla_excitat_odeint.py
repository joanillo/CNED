# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
SF-76
problema_massa-molla_excitat. Excitació amb una funció senoidal. Sense esmorteïment
sense ressonància i amb ressonància.
Solució simulada amb odeint (per comparar amb la solució analítica)
Solució analítica a problema_massa-molla_excitat.pdf

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 problema_massa-molla_excitat_odeint.py
'''

import numpy as np
from scipy.integrate import odeint
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

def EqDif_MassaMolla(state, t, k, m, A, w):
    # unpack the state vector
    x,xd = state # displacement,x and velocity x'

    # compute acceleration xdd = x''
    #xdd = -k*x/m -c*xd-g + A*np.cos(omega*t - phi)
    xdd = -k*x/m + (A/m)*np.sin(w*t)
    return [xd, xdd]

time = np.linspace(0,100, 1000)

state0 = [3.0, 0.0]  #initial conditions [x0 , v0]  [m, m/sec] 

# wo >> w
w = 0.1
state = odeint(EqDif_MassaMolla, state0, time, args=(k, m, A, w))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació (simulació)')
plt.title('$\\omega_o$ >> $\\omega$. $\\omega_o$=1, $\\omega$=0.1. Rissat de freq 0.1')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_simulacio_v1.png")

# wo > w
w = 0.4
state = odeint(EqDif_MassaMolla, state0, time, args=(k, m, A, w))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació (simulació)')
plt.title('$\\omega_o$ > $\\omega$. $\\omega_o$=1, $\\omega$=0.4. Rissat de freq 0.4')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_simulacio_v2.png")

# wo << w
w = 5
state = odeint(EqDif_MassaMolla, state0, time, args=(k, m, A, w))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació (simulació)')
plt.title('$\\omega_o$ << $\\omega$. $\\omega_o$=1, $\\omega$=5. No hi ha rissat')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_simulacio_v3.png")

# wo < w
w = 1.2
state = odeint(EqDif_MassaMolla, state0, time, args=(k, m, A, w))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació (simulació)')
plt.title('$\\omega_o$ < $\\omega$. $\\omega_o$=1, $\\omega$=1.2. Rissat')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_simulacio_v4.png")

# wo ~ w
w = 1.05
state = odeint(EqDif_MassaMolla, state0, time, args=(k, m, A, w))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació (simulació)')
plt.title('$\\omega_o$ ~ $\\omega$. $\\omega_o$=1, $\\omega$=1.05.  Apareix la ressonància, i l\'amplitud puja')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_simulacio_v5.png")

# cas 2: w = wo (ressonància) ========================================================
# wo = w
w = wo
state = odeint(EqDif_MassaMolla, state0, time, args=(k, m, A, w))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

fig, ax = plt.subplots()
plt.plot(time, x)
plt.suptitle('Problema massa-molla amb excitació (simulació)')
plt.title('$\\omega_o$ = $\\omega$. $\\omega_o$=1.  Ressonància')
ax.set(xlabel='temps (s)', ylabel='x (m)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-76_problema_massa-molla_excitat_simulacio_v6.png")
