# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Mirem la convergència de l'aproximació rectangular composta (en funció de h),
i veure que la convergència és lineal.
integral de 1/(1+x^2) entre 0 i 5 ( = arctan(5))

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 convergencia_rectangle.py
'''

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

I_exacta = np.arctan(5) 

f = lambda x : 1/(1+x**2)
a = 0; b = 5

error_list_leftpoint = []
error_list_midpoint = []
h_list = []

for N in range(1,30):
    dx = (b-a)/N
    x_left = np.linspace(a,b-dx,N)
    x_midpoint = np.linspace(dx/2,b - dx/2,N)
    x_right = np.linspace(dx,b,N)

    I_leftpoint = np.sum(f(x_left) * dx)
    I_midpoint = np.sum(f(x_midpoint) * dx)

    error_leftpoint = np.abs(I_exacta - I_leftpoint)
    error_midpoint = np.abs(I_exacta - I_midpoint)
    error_list_leftpoint.append(error_leftpoint)
    error_list_midpoint.append(error_midpoint)
    h_list.append(dx)

# gràfica
fig, ax = plt.subplots()
plt.plot(h_list, error_list_leftpoint,'-b',label='left point')
plt.plot(h_list, error_list_leftpoint,'bo')
plt.plot(h_list, error_list_midpoint,'-r',label='mid point')
plt.plot(h_list, error_list_midpoint, 'ro')
plt.legend(loc="best")
plt.xlabel("h = (b-a)/n")
plt.ylabel("error rectangular")
ax.set(title='1/(1+x^2). Convergencia aproximació rectangular')
ax.grid()
fig.savefig("../img/T1/convergencia_rectangle.png")
plt.show()