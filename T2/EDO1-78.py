# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-78: y' = y + e^2t + 1 − 3t

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-78.py
'''

import sympy as sp
from sympy import exp
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

t   = sp.symbols('t')
y   = sp.Function('y')

print('\nExemple 1: y\' = y + e^2t + 1 − 3t')
ode = sp.Eq(sp.Derivative(y(t),t),y(t)+exp(2*t)+1-3*t)
sol = sp.dsolve(ode,y(t))
print(sol) # Eq(y(t), (C1 + (3*t + 2)*exp(-t) + exp(t))*exp(t))
sp.checkodesol(ode,sol)
#    (True, 0)
if sp.checkodesol(ode,sol)[0]==True:
   print ('verified solution OK')

# solució amb PVI:
print('\nCI: y(0)=1')
sol = sp.dsolve(ode,y(t),ics={y(0):1})
print(sol) # Eq(y(t), ((3*t + 2)*exp(-t) + exp(t) - 2)*exp(t))

print('\nCI: y(0)=2')
sol = sp.dsolve(ode,y(t),ics={y(0):2})
print(sol) # Eq(y(t), ((3*t + 2)*exp(-t) + exp(t) - 1)*exp(t))

print('\nCI: y(0)=3')
sol = sp.dsolve(ode,y(t),ics={y(0):3})
print(sol) # Eq(y(t), ((3*t + 2)*exp(-t) + exp(t))*exp(t))

print('\nCI: y(0)=4')
sol = sp.dsolve(ode,y(t),ics={y(0):4})
print(sol) # Eq(y(t), ((3*t + 2)*exp(-t) + exp(t) + 1)*exp(t))

# plot results
# time points
t = np.linspace(0,2,200)
y1 = ((3*t + 2)*np.exp(-t) + np.exp(t) - 2)*np.exp(t)
y2 = ((3*t + 2)*np.exp(-t) + np.exp(t) - 1)*np.exp(t)
y3 = ((3*t + 2)*np.exp(-t) + np.exp(t))*np.exp(t)
y4 = ((3*t + 2)*np.exp(-t) + np.exp(t) + 1)*np.exp(t)

plt.plot(t,y1,'r',linewidth=2,label='y(0)=1')
plt.plot(t,y2,'b',linewidth=2,label='y(0)=2')
plt.plot(t,y3,'g',linewidth=2,label='y(0)=3')
plt.plot(t,y4,'c',linewidth=2,label='y(0)=4')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.suptitle('EDO, y\'(t) = y + e^2t + 1 − 3t. Sol: y(t) = ((3*t + 2)*exp(-t) + exp(t) + C)*exp(t)', fontsize=12)
plt.title('diferents condicions inicials', fontsize=10)

plt.show()
fig.savefig("../img/T2/EDO1-78.png")

t_, y = np.meshgrid(np.linspace(0,2,25), np.linspace(0, 70, 25))
alfa = np.arctan(y + np.exp(2*t_) + 1 - 3*t_)

U=np.cos(alfa)*1
V=np.sin(alfa)/35 # és un factor d'escala dels eixos, crec (70/2)

plt.figure()
plt.title('Arrows scale with plot width, not view')
Q = plt.quiver(t_,y,U,V, units='width')
plt.plot(t,y1,'r',linewidth=2,label='y(0)=1')
plt.plot(t,y2,'b',linewidth=2,label='y(0)=2')
plt.plot(t,y3,'g',linewidth=2,label='y(0)=3')
plt.plot(t,y4,'c',linewidth=2,label='y(0)=4')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.suptitle('EDO, y\'(t) = y + e^2t + 1 − 3t', fontsize=12)
plt.title('diferents condicions inicials', fontsize=10)

plt.show()
fig.savefig("../img/T2/EDO1-78_v2.png")
