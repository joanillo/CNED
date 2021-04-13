# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-15

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-15.py
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

t   = sp.symbols('t')
y   = sp.Function('y')

print('\nExemple 1: y\'=3t^2-4t')
ode = sp.Eq(sp.Derivative(y(t),t),3*t**2-4*t)
sol = sp.dsolve(ode,y(t))
print(sol) # Eq(y(t), C1 + t**3 - 2*t**2)
sp.checkodesol(ode,sol)
#    (True, 0)
if sp.checkodesol(ode,sol)[0]==True:
   print ('verified solution OK')

# solució amb PVI:
print('\nCI: y(1)=4')
sol = sp.dsolve(ode,y(t),ics={y(1):4})
print(sol) # t**3 - 2*t**2 + 5
#print(sp.latex(sol)) # printem en format LaTeX

print('\nCI: y(0)=2')
sol = sp.dsolve(ode,y(t),ics={y(0):2})
print(sol) # t**3 - 2*t**2 + 2

print('\nCI: y(0)=-1')
sol = sp.dsolve(ode,y(t),ics={y(0):-1})
print(sol) # t**3 - 2*t**2 -1

print('\nCI: y(0)=-4')
sol = sp.dsolve(ode,y(t),ics={y(0):-4})
print(sol) # t**3 - 2*t**2 -4

# plot results
# time points
t = np.linspace(0,4,200)
y1 = t**3 - 2*t**2 + 5
y2 = t**3 - 2*t**2 + 2
y3 = t**3 - 2*t**2 - 1
y4 = t**3 - 2*t**2 - 4

plt.plot(t,y1,'r',linewidth=2,label='y(1)=4')
plt.plot(t,y2,'b',linewidth=2,label='y(0)=2')
plt.plot(t,y3,'g',linewidth=2,label='y(0)=-1')
plt.plot(t,y4,'c',linewidth=2,label='y(0)=-4')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.suptitle('EDO, y\'(t) = =3t^2-4t. Sol: y(t) = t^3 - 2t^2 + C', fontsize=12)
plt.title('diferents condicions inicials', fontsize=10)

plt.show()
fig.savefig("../img/T2/EDO1-15.png")

