# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-28: Discussió sobre el Teorema de Picard

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 odeint_pvi_v4.py
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

print('\nExemple: y\'= (t^2 * cos(t) + y) / t')
ode = sp.Eq(sp.Derivative(y(t),t),(t**2 * sp.cos(t) + y(t))/t)
sol = sp.dsolve(ode,y(t))
print(sol) # Eq(y(t), t*(C1 + sin(t)))
print('Hem obtingut una solució')
print('Però aquesta solució no funciona amb la CI to=0 (teorema de Picard)')

'''
# CI1
print('\nCI1: y(0)=0')
sol = sp.dsolve(ode,y(t),ics={y(0):0})
print('no es pot resoldre')
'''

# CI2
print('\nCI2: y(1)=0')
sol = sp.dsolve(ode,y(t),ics={y(1):0})
print(sol) # Eq(y(t), t*(sin(t) - sin(1)))
print('Hem obtingut una sola solució: y2=t*(sin(t)-sin(1))')
print('En aquest cas sí que podem aplicar Picard')

# CI3
print('\nCI2: y(1)=2')
sol = sp.dsolve(ode,y(t),ics={y(1):2})
print(sol) # Eq(y(t), t*(sin(t) - sin(1) + 2))
print('Hem obtingut una sola solució: y3=t*(sin(t)-sin(1)+2)')
print('En aquest cas sí que podem aplicar Picard')


# plot results
# time points
t = np.linspace(-4,4,200)
y2 = t*(np.sin(t)-np.sin(1))
y3 = t*(np.sin(t)-np.sin(1)+2)

plt.plot(t,y2,'r',linewidth=2,label='y(1)=0')
plt.plot(t,y3,'b',linewidth=2,label='y(1)=2')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
fig = plt.gcf()
plt.suptitle('EDO, y\'(t) = (t^2 * cos(t) + y) / t. Sol: y(t) = t*(C1 + sin(t))', fontsize=12)
plt.title('diferents condicions inicials', fontsize=10)

plt.show()
fig.savefig("../img/T2/odeint_pvi_v4.png")
