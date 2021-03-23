# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Mirem la convergència de l'aproximació rectangular composta (en funció de h),
i veure que la convergència és lineal.
integral de 1/(1+x^2) entre 0 i 5 ( = arctan(5))

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 convergencia_trapezi.py
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

#--------------------------
def trapz(f,a,b,N=50):
    x = np.linspace(a,b,N+1) # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T
#--------------------------

I_exacta = np.arctan(5) 

f = lambda x : 1/(1+x**2)
a = 0; b = 5

error_list = []
h_list = []

for N in range(1,30):
    dx = (b-a)/N
    T = trapz(f,a,b,N)
    error = np.abs(I_exacta - T)
    error_list.append(error)
    h_list.append(dx)

# gràfica
fig, ax = plt.subplots()
plt.plot(h_list, error_list,'-b',label='Trapezi')
plt.plot(h_list, error_list,'bo')
plt.legend(loc="best")
plt.xlabel("h = (b-a)/n")
plt.ylabel("error trapezi")
ax.set(title='1/(1+x^2). Convergencia mètode trapezi')
ax.grid()
fig.savefig("../img/T1/convergencia_trapezi.png")
plt.show()