# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Mirem la convergència de l'aproximació rectangular composta (en funció de h),
i veure que la convergència és lineal.
integral de 1/(1+x^2) entre 0 i 5 ( = arctan(5))

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 convergencia_simpson.py
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
def simps(f,a,b,N=50):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S
#--------------------------

I_exacta = np.arctan(5) 

f = lambda x : 1/(1+x**2)
a = 0; b = 5

error_list = []
h_list = []

for N in range(1,30):
    if (N%2==0):
        dx = (b-a)/N
        S = simps(f,a,b,N)
        error = np.abs(I_exacta - S)
        error_list.append(error)
        h_list.append(dx)

# gràfica
fig, ax = plt.subplots()
plt.plot(h_list, error_list,'-b',label='Simpson')
plt.plot(h_list, error_list,'bo')
plt.legend(loc="best")
plt.xlabel("h = (b-a)/n")
plt.ylabel("error simpson")
ax.set(title='1/(1+x^2). Convergencia mètode Simpson')
ax.grid()
fig.savefig("../img/T1/convergencia_simpson.png")
plt.show()