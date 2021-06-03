# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
SF-76
sistema_massa-molla_excitat. Excitació amb una funció senoidal. Diferents casos

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 sistema_massa-molla_excitat.py
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

def MassSpringDamper(state, t, g, k, m, c, A, omega, phi):
    '''
    k=spring constant, Newtons per metre
    m=mass, Kilograms
    c=dampign coefficient, Newton*second / meter    
    
    for a mass,spring
        xdd = ((-k*x)/m) + g
    for a mass, spring, damper 
        xdd = -k*x/m -c*xd-g
    for a mass, spring, dmaper with forcing function
        xdd = -k*x/m -c*xd-g + cos(4*t-pi/4)
    '''
  
    # unpack the state vector
    x,xd = state # displacement,x and velocity x'

    # compute acceleration xdd = x''
    xdd = -k*x/m -c*xd-g + A*np.cos(omega*t - phi)
    return [xd, xdd]

# CAS 1: sense excitació externa ===========================================

# CONSTANTS
g = 9.8 # metres per second**2
# la freqüència pròpia ve donada per
# fo = (1/(2*pi)) * sqrt(k/m)
# wo = 2*pi*fo = sqrt(k/m)
# To = 1/fo = 2*pi/wo = 2*pi*sqrt(m/k)
k=124e3  # spring constant, kN/m
m=64.2 # mass, Kg
#m=k/(4*np.pi**2) # condició de ressonància
#c=3.0  # damping coefficient
c=0.0 # sense esmorteïment
freq = 1.0 # freqüència d'excitació
omega = 2*np.pi*freq
phi = 0 # phase shift
A=0 # amplitud. No tenim excitació externa

state0 = [0.0, 1.2]  #initial conditions [x0 , v0]  [m, m/sec] 
ti = 0.0  # initial time
tf = 4.0  # final time
step = 0.001  # step
t = np.arange(ti, tf, step)

state = odeint(MassSpringDamper, state0, t, args=(g, k, m, c, A, omega, phi))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

# Plotting displacement and velocity
plt.rcParams['figure.figsize'] = (15, 12)
plt.rcParams['font.size'] = 18

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(t,x*1e3,'b',label = r'$x (mm)$', linewidth=2.0)
ax1.set_xlabel('time , sec')
ax1.set_ylabel('disp (mm)',color='b')
plt.title('Sistema massa-molla sense excitació amb $V_0=1.2 \frac{m}{s}$')
plt.grid()
plt.show()
fig.savefig("../img/T3/SF-76_sistema_massa-molla_excitat_v1.png")

# CAS 2: amb excitació externa ===========================================

# CONSTANTS
g = 9.8 # metres per second**2
# la freqüència pròpia ve donada per
# fo = (1/(2*pi)) * sqrt(k/m)
# wo = 2*pi*fo = sqrt(k/m)
# To = 1/fo = 2*pi/wo = 2*pi*sqrt(m/k)
k=124e3  # spring constant, kN/m
m=64.2 # mass, Kg
#m=k/(4*np.pi**2) # condició de ressonància
#c=3.0  # damping coefficient
c=0.0 # sense esmorteïment
freq = 1.0 # freqüència d'excitació
omega = 2*np.pi*freq
phi = 0 # phase shift
A=15 # amplitud. Tenim excitació externa

state0 = [0.0, 1.2]  #initial conditions [x0 , v0]  [m, m/sec] 
ti = 0.0  # initial time
tf = 4.0  # final time
step = 0.001  # step
t = np.arange(ti, tf, step)

state = odeint(MassSpringDamper, state0, t, args=(g, k, m, c, A, omega, phi))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

# Plotting displacement and velocity
plt.rcParams['figure.figsize'] = (15, 12)
plt.rcParams['font.size'] = 18

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(t,x*1e3,'b',label = r'$x (mm)$', linewidth=2.0)
ax1.set_xlabel('time , sec')
ax1.set_ylabel('disp (mm)',color='b')
plt.title('Sistema massa-molla amb excitació i amb $V_0=1.2 \frac{m}{s}$')
plt.grid()
plt.show()
fig.savefig("../img/T3/SF-76_sistema_massa-molla_excitat_v2.png")

# CAS 3: amb excitació externa  i velocitat inicial = 0 ===========================================

# CONSTANTS
g = 9.8 # metres per second**2
# la freqüència pròpia ve donada per
# fo = (1/(2*pi)) * sqrt(k/m)
# wo = 2*pi*fo = sqrt(k/m)
# To = 1/fo = 2*pi/wo = 2*pi*sqrt(m/k)
k=124e3  # spring constant, kN/m
m=64.2 # mass, Kg
#m=k/(4*np.pi**2) # condició de ressonància
#c=3.0  # damping coefficient
c=0.0 # sense esmorteïment
freq = 1.0 # freqüència d'excitació
omega = 2*np.pi*freq
phi = 0 # phase shift
A=15 # amplitud. Tenim excitació externa

state0 = [0.0, 0.0]  #initial conditions [x0 , v0]  [m, m/sec] 
ti = 0.0  # initial time
tf = 4.0  # final time
step = 0.001  # step
t = np.arange(ti, tf, step)

state = odeint(MassSpringDamper, state0, t, args=(g, k, m, c, A, omega, phi))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

# Plotting displacement and velocity
plt.rcParams['figure.figsize'] = (15, 12)
plt.rcParams['font.size'] = 18

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(t,x*1e3,'b',label = r'$x (mm)$', linewidth=2.0)
ax1.set_xlabel('time , sec')
ax1.set_ylabel('disp (mm)',color='b')
plt.title('Sistema massa-molla amb excitació i amb $V_0=0 \frac{m}{s}$')
plt.grid()
plt.show()
fig.savefig("../img/T3/SF-76_sistema_massa-molla_excitat_v3.png")

# CAS 4: amb excitació externa  i velocitat inicial = 0. Afegim esmorteïment ===========================================

# CONSTANTS
g = 9.8 # metres per second**2
# la freqüència pròpia ve donada per
# fo = (1/(2*pi)) * sqrt(k/m)
# wo = 2*pi*fo = sqrt(k/m)
# To = 1/fo = 2*pi/wo = 2*pi*sqrt(m/k)
k=124e3  # spring constant, kN/m
m=64.2 # mass, Kg
#m=k/(4*np.pi**2) # condició de ressonància
c=3.0  # damping coefficient
freq = 1.0 # freqüència d'excitació
omega = 2*np.pi*freq
phi = 0 # phase shift
A=15 # amplitud. Tenim excitació externa

state0 = [0.0, 0.0]  #initial conditions [x0 , v0]  [m, m/sec] 
ti = 0.0  # initial time
tf = 4.0  # final time
step = 0.001  # step
t = np.arange(ti, tf, step)

state = odeint(MassSpringDamper, state0, t, args=(g, k, m, c, A, omega, phi))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

# Plotting displacement and velocity
plt.rcParams['figure.figsize'] = (15, 12)
plt.rcParams['font.size'] = 18

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(t,x*1e3,'b',label = r'$x (mm)$', linewidth=2.0)
ax1.set_xlabel('time , sec')
ax1.set_ylabel('disp (mm)',color='b')
plt.title('Sistema massa-molla amb excitació i amb $V_0=0 \frac{m}{s}$ i esmorteït')
plt.grid()
plt.show()
fig.savefig("../img/T3/SF-76_sistema_massa-molla_excitat_v4.png")

# CAS 5: amb excitació externa  i velocitat inicial = 0. Condició de ressonància =======================

# CONSTANTS
g = 9.8 # metres per second**2
# la freqüència pròpia ve donada per
# fo = (1/(2*pi)) * sqrt(k/m)
# wo = 2*pi*fo = sqrt(k/m)
# To = 1/fo = 2*pi/wo = 2*pi*sqrt(m/k)
k=124e3  # spring constant, kN/m
#m=64.2 # mass, Kg
m=k/(4*np.pi**2) # condició de ressonància
#c=3.0  # damping coefficient
c=0
freq = 1.0 # freqüència d'excitació
omega = 2*np.pi*freq
phi = 0 # phase shift
A=15 # amplitud. Tenim excitació externa

state0 = [0.0, 0.0]  #initial conditions [x0 , v0]  [m, m/sec] 
ti = 0.0  # initial time
tf = 4.0  # final time
step = 0.001  # step
t = np.arange(ti, tf, step)

state = odeint(MassSpringDamper, state0, t, args=(g, k, m, c, A, omega, phi))
x = np.array(state[:,[0]])
xd = np.array(state[:,[1]])

# Plotting displacement and velocity
plt.rcParams['figure.figsize'] = (15, 12)
plt.rcParams['font.size'] = 18

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(t,x*1e3,'b',label = r'$x (mm)$', linewidth=2.0)
ax1.set_xlabel('time , sec')
ax1.set_ylabel('disp (mm)',color='b')
plt.title('Sistema massa-molla amb excitació i amb $V_0=0 \frac{m}{s}$ i ressonància')
plt.grid()
plt.show()
fig.savefig("../img/T3/SF-76_sistema_massa-molla_excitat_v5.png")

'''
CÀLCULS ===================

Cas 1. Tenim un moviment harmònic simple.
Sobre la gràfica es veu que són 28 cicles en 4 segons: T = 4/28 = 0.142
Es correspon amb la fórmula T = 2pi*sqrt(m/k) = 2*pi*sqrt(64.2/124000) = 0.142

Cas 2
Exictem amb una ona de f=1Hz. w=2*pi*f = 6.28
Sobre la gràfica veiem un rissat de 4 cicles en 4 segons. T = 4/4 = 1s. 
w = 2*pi/T = 6.28 
'''
