# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
caiguda exponencial (per ex, descàrrega del condensador): y'(t) = -ky(t)
https://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 odeint_v3.py
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
def model(y,t,k):
    dydt = -k * y
    return dydt

# initial condition
y0 = 5

# time points
t = np.linspace(0,20)

# solve ODEs
k = 0.1
y1 = odeint(model,y0,t,args=(k,))
k = 0.2
y2 = odeint(model,y0,t,args=(k,))
k = 0.5
y3 = odeint(model,y0,t,args=(k,))

# plot results
plt.plot(t,y1,'r-',linewidth=2,label='k=0.1')
plt.plot(t,y2,'b--',linewidth=2,label='k=0.2')
plt.plot(t,y3,'g:',linewidth=2,label='k=0.5')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
#plt.title('caiguda exponencial')
plt.suptitle('caiguda exponencial', fontsize=18)
plt.title('descàrrega del condensador, desintegració radioactiva', fontsize=10)

plt.show()
fig.savefig("../img/T2/EDO1-12_descarrega_condensador.png")


