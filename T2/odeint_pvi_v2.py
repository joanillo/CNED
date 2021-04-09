# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-23: solució amb sympy d'una Eq diferencial, i un cas particular de CI
https://12000.org/my_notes/faq/sympy_python/index.htm

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 odeint_pvi_v2.py
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

t = sp.symbols('t')
y   = sp.Function('y')

print('\nExemple: y\'= y')
ode = sp.Eq(sp.Derivative(y(t),t),y(t))
sol = sp.dsolve(ode,y(t))
print(sol) # Eq(y(t), C1*exp(t))

# CI1
print('\nCI: y(0)=1')
sol = sp.dsolve(ode,y(t),ics={y(0):1})
print(sol) # 1*exp(t)


# CI2
print('\nCI: y(0)=1.5')
sol = sp.dsolve(ode,y(t),ics={y(0):1.5})
print(sol) # 1.5*exp(t)

# CI3
print('\nCI: y(0)=2')
sol = sp.dsolve(ode,y(t),ics={y(0):2})
print(sol) # 2*exp(t)

# CI4
print('\nCI: y(0)=2.5')
sol = sp.dsolve(ode,y(t),ics={y(0):2.5})
print(sol) # 2.5*exp(t)

# plot results
# time points
t = np.linspace(0,2,200)
y1 = np.exp(t)
y2 = 1.5*np.exp(t)
y3 = 2*np.exp(t)
y4 = 2.5*np.exp(t)

plt.plot(t,y1,'r',linewidth=2,label='y(0)=1.0')
plt.plot(t,y2,'b',linewidth=2,label='y(0)=1.5')
plt.plot(t,y3,'g',linewidth=2,label='y(0)=2.0')
plt.plot(t,y4,'c',linewidth=2,label='y(0)=2.5')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.suptitle('EDO, y\'(t) = y(t). Sol: y(t) = C*exp(t)', fontsize=18)
plt.title('diferents condicions inicials', fontsize=10)

plt.show()
fig.savefig("../img/T2/odeint_pvi_v2.png")
