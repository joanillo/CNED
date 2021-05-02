# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Propagació rumors (P1, P2, pàg 128)

cd /home/joan/UPC_2021/CNED/apunts/python/proves/
PS1="$ "
python3 rumors.py
'''

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

T = 10000 # població total

t = sp.symbols('t')
r   = sp.Function('r')

print('\nExemple: r\'= r(T-r)')
ode = sp.Eq(sp.Derivative(r(t),t),r(t)*(T-r(t)))
sol = sp.dsolve(ode,r(t))
print(sol) # 10000/(C1*exp(-10000*t) + 1))

# CI1
print('\nCI1: r(0)=T/10')
sol = sp.dsolve(ode,r(t),ics={r(0):T/10})
print(sol) # 10000/(1 + 9.0*exp(-10000*t)))

# CI2
print('\nCI2: r(0)=T/50')
sol = sp.dsolve(ode,r(t),ics={r(0):T/50})
print(sol) # 10000/(1 + 49.0*exp(-10000*t)))


t = np.linspace(0,.001,1000)
r1 = 10000/(1 + 9.0*np.exp(-10000*t))
r2 = 10000/(1 + 49.0*np.exp(-10000*t))

plt.plot(t,r1,'r',linewidth=2,label='y(0)=T/10')
plt.plot(t,r2,'b',linewidth=2,label='y(0)=T/50')
plt.xlabel('time')
plt.ylabel('r(t)')
plt.legend()
fig = plt.gcf()
plt.suptitle('EDO, r\'(t) = r(T-r). Sol: r(t) = 10000/(C*exp(-10000*t) + 1))', fontsize=10)
plt.title('Propagació de rumors', fontsize=10)

plt.show()
fig.savefig("../img/T2/propagacio_rumors.png")
