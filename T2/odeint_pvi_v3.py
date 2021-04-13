# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-23 - EDO1-26: Discussió sobre el Teorema de Picard

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 odeint_pvi_v3.py
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

print('\nExemple: y\'= t/y')
ode = sp.Eq(sp.Derivative(y(t),t),t/y(t))
sol = sp.dsolve(ode,y(t))
print(sol) # [Eq(y(t), -sqrt(C1 + t**2)), Eq(y(t), sqrt(C1 + t**2))]
print('(hem obtingut dues solucions)')


# CI1
print('\nCI1: y(0)=0')
sol = sp.dsolve(ode,y(t),ics={y(0):0})
print(sol) # 1*exp(t)
print('(hem obtingut dues solucions: y1=-t i y2=+t)')
print('La solució existeix però no és única.')
print('I el teorema de Picard ens ho diu.')
print('En aquest cas no es compleix les condicions del teorema')
print('i no es pot assegurar la unicitat de la solució.')

# CI2
print('\nCI2: y(0)=2')
sol = sp.dsolve(ode,y(t),ics={y(0):2})
print(sol) # sqrt(t**2 + 4)
print('Hem obtingut una sola solució: y1=sqrt(t^2+4)')
print('En aquest cas sí que podem aplicar Picard')

# CI3
print('\nCI2: y(0)=3')
sol = sp.dsolve(ode,y(t),ics={y(0):3})
print(sol) # sqrt(t**2 + 9)
print('Hem obtingut una sola solució: y1=sqrt(t^2+9)')
print('En aquest cas sí que podem aplicar Picard')


# plot results
# time points
t = np.linspace(-4,4,200)
y2 = np.sqrt(t**2 + 4)
y3 = np.sqrt(t**2 + 9)

plt.plot(t,y2,'r',linewidth=2,label='y(0)=2')
plt.plot(t,y3,'b',linewidth=2,label='y(0)=3')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.suptitle('EDO, y\'(t) = t/y. Sol: y(t) = sqrt(t**2 + C)', fontsize=18)
plt.title('diferents condicions inicials', fontsize=10)

plt.show()
fig.savefig("../img/T2/odeint_pvi_v3.png")
