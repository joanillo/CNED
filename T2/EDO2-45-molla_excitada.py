# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Resolució d'una EDO de 2n ordre no homogènea

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO2-45-molla_excitada.py
'''

import numpy as np
import sympy as sp
from sympy.abc import t
from sympy import sin, cos
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
x = sp.Function('x')

# x'' + x = sin(t)
print('\nExemple: x\'\' + x = sin(t)')
x1 = sp.dsolve(x(t).diff(t,t) + x(t) - sin(t), x(t))
print(x1) # C2*sin(t) + (C1 - t/2)*cos(t)
print("PVI: x(0)=1, x'(0) = 0")
x1_pvi = sp.solve([x1.rhs.subs(t,0)-1, x1.rhs.diff(t).subs(t,0)-0])
print(x1_pvi) # {C1: 1, C2: 1/2}

# x'' + x = cos(t)
print('\nExemple: x\'\' + x = cos(t)')
x2 = sp.dsolve(x(t).diff(t,t) + x(t) - cos(t), x(t))
print(x2) # C2*cos(t) + (C1 + t/2)*sin(t)
print("PVI: x(0)=1, x'(0) = 0")
x2_pvi = sp.solve([x2.rhs.subs(t,0)-1, x2.rhs.diff(t).subs(t,0)-0])
print(x2_pvi) # {C1: 0, C2: 1}

# x'' + x = -sin(t)
print('\nExemple: x\'\' - x = -sin(t)')
x3 = sp.dsolve(x(t).diff(t,t) + x(t) + sin(t), x(t))
print(x3) # C2*sin(t) + (C1 + t/2)*cos(t)
print("PVI: x(0)=1, x'(0) = 0")
x3_pvi = sp.solve([x3.rhs.subs(t,0)-1, x3.rhs.diff(t).subs(t,0)-0])
print(x3_pvi) # {C1: 1, C2: -1/2}


t = np.linspace(0,20,2000)
x1_ = 0.5*np.sin(t) + (1 - t/2)*np.cos(t)
x2_ = np.cos(t) + t/2*np.sin(t)
x3_ = -0.5*np.sin(t) + (1+t/2)*np.cos(t)

plt.plot(t,x1_,'r',linewidth=2,label='f(t)=sin(t)')
plt.plot(t,x2_,'b',linewidth=2,label='f(t)=cox(t)')
plt.plot(t,x3_,'g',linewidth=2,label='f(t)=-sin(t)')
plt.xlabel('time')
plt.ylabel('x(t)')
plt.legend()
fig = plt.gcf()
plt.suptitle('EDO, x\'\'(t) + x(t) = f(t), x(0)=1, x\'(0)=0', fontsize=12)
plt.title('Molla amb excitació externa forta', fontsize=10)

plt.show()
fig.savefig("../img/T2/EDO2-45-molla_excitada.png")
