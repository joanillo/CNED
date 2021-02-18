# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
variables separables
EDO1-44: y' = (2sqrt(y) - 2y)/t
cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 odeint_v5.py
'''

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

# function that returns dy/dt
def model(y,t):
	#y' = (2sqrt(y) - 2y)/t
    dydt = (2*np.sqrt(y) -2*y)/t
    return dydt

# ===========
# initial condition
y0 = 0.5

# time points
t = np.linspace(1,5)

# solve ODEs
y1 = odeint(model,y0,t)

plt.plot(t,y1,'g-',linewidth=2,label='y(1)=0.5')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-44_cas_1.png")

# ===========
# initial condition
y0 = 2

# time points
t = np.linspace(1,5)

# solve ODEs
y1 = odeint(model,y0,t)

plt.plot(t,y1,'g-',linewidth=2,label='y(1)=2')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-44_cas_2.png")

# ===========
# initial condition
y0 = 0.8

# time points
t = np.linspace(-0.2,-5)

# solve ODEs
y1 = odeint(model,y0,t)

plt.plot(t,y1,'g-',linewidth=2,label='y(-0.2)=0.8')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-44_cas_3.png")

# ===========
# initial condition
y0 = 1.5

# time points
t = np.linspace(-1.5,-5)

# solve ODEs
y1 = odeint(model,y0,t)

plt.plot(t,y1,'g-',linewidth=2,label='y(-1.5)=1.5')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-44_cas_4.png")