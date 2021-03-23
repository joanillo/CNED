# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Mirem la convergència de l'aproximació rectangular composta (en funció de h),
i veure que la convergència és lineal.
integral de 1/(1+x^2) entre 0 i 5 ( = arctan(5))

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 convergencia_comparacio.py
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

error_list_leftpoint = []
error_list_midpoint = []
error_list_trapezi = []
error_list_simpson = []
h_list = []
h_list_simpson = []

for N in range(1,30):
    dx = (b-a)/N
    # rectangle
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

    # trapezi
    dx = (b-a)/N
    T = trapz(f,a,b,N)
    error = np.abs(I_exacta - T)
    error_list_trapezi.append(error)

    # simpson
    if (N%2==0):
        S = simps(f,a,b,N)
        error = np.abs(I_exacta - S)
        error_list_simpson.append(error)
        h_list_simpson.append(dx)

# gràfica
fig, ax = plt.subplots()
plt.plot(h_list, error_list_leftpoint,'-c',label='Rect leftpoint')
plt.plot(h_list, error_list_leftpoint,'co')
plt.plot(h_list, error_list_midpoint,'-g',label='Rect midpoint')
plt.plot(h_list, error_list_midpoint,'go')
plt.plot(h_list, error_list_trapezi,'-r',label='Trapezi')
plt.plot(h_list, error_list_trapezi,'ro')
plt.plot(h_list_simpson, error_list_simpson,'-b',label='Simpson')
plt.plot(h_list_simpson, error_list_simpson,'bo')
plt.legend(loc="best")
plt.xlabel("h = (b-a)/n")
plt.ylabel("errors")
ax.set(title='1/(1+x^2). Comparació rect-trapezi-simpson')
ax.grid()
fig.savefig("../img/T1/convergencia_comparacio.png")
plt.show()

# gràfica
fig, ax = plt.subplots()
plt.plot(np.log(h_list), np.log(error_list_leftpoint),'-c',label='Rect leftpoint')
plt.plot(np.log(h_list), np.log(error_list_leftpoint),'co')
plt.plot(np.log(h_list), np.log(error_list_midpoint),'-g',label='Rect midpoint')
plt.plot(np.log(h_list), np.log(error_list_midpoint),'go')
plt.plot(np.log(h_list), np.log(error_list_trapezi),'-r',label='Trapezi')
plt.plot(np.log(h_list), np.log(error_list_trapezi),'ro')
plt.plot(np.log(h_list_simpson), np.log(error_list_simpson),'-b',label='Simpson')
plt.plot(np.log(h_list_simpson), np.log(error_list_simpson),'bo')
plt.legend(loc="best")
plt.xlabel("h = (b-a)/n (log)")
plt.ylabel("errors (log)")
ax.set(title='1/(1+x^2). Comparació rect-trapezi-simpson (log)')
ax.grid()
fig.savefig("../img/T1/convergencia_comparacio_log.png")
plt.show()
