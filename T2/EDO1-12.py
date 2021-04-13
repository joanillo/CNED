# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-15

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-12.py
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

x   = sp.symbols('x')
y   = sp.Function('y')

print('\ny\'\' = -y')
ode = sp.Eq(sp.Derivative(y(x),x,x),-y(x))
sol = sp.dsolve(ode,y(x))
print(sol) # Eq(y(x), C1*sin(x) + C2*cos(x))
sp.checkodesol(ode,sol)
#    (True, 0)
if sp.checkodesol(ode,sol)[0]==True:
   print ('verified solution OK')


# solució amb PVI:
print('\nCI: y(0)=3; y\'(0)=2')
sol = sp.dsolve(ode,y(x),ics={y(0):3, y(x).diff(x,1).subs(x, 0): 2})
print(sol) # Eq(y(x), 2*sin(x) + 3*cos(x))

print('\nCI: y(0)=2; y\'(0)=3')
sol = sp.dsolve(ode,y(x),ics={y(0):2, y(x).diff(x,1).subs(x, 0): 3})
print(sol) # Eq(y(x), 3*sin(x) + 2*cos(x))

# plot
x = np.linspace(0,10,200)
y1 = 2*np.sin(x) + 3*np.cos(x)
y2 = 3*np.sin(x) + 2*np.cos(x)

plt.plot(x,y1,'r',linewidth=2,label='y(0)=3, y\'(0)=2')
plt.plot(x,y2,'b',linewidth=2,label='y(0)=2, y\'(0)=3')

plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.suptitle('EDO, y\'\' = -y. Sol: y(t) = C1*sin(x) + C2*cos(x)', fontsize=12)
plt.title('CI: y(0)=3; y\'(0)=2 : y = 2*sin(x) + 3*cos(x)', fontsize=10)

plt.show()
fig.savefig("../img/T2/EDO1-12.png")