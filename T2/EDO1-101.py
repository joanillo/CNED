# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
https://stackoverflow.com/questions/52334558/runge-kutta-4th-order-method-to-solve-second-order-odes
y'' + y = 0 (és l'equació de la molla)
y(0) = 0 and y'(0) = 1/pi
solució analítica: sin(x)/pi

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-101.py
'''

import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

# per resoldre una eq diferencial de segon ordre, fem un sistema de dos equacions
# amb dos incògnites, de primer ordre:
# y' = u #u és la velocitat
# u' = -y

def F(y, u, x):
    return -y

a = 0
b = 6.0
N =100 # prova 1000, 100, 10, 5
h = (b-a)/N

xpoints = np.arange(a,b,h)

# RK-4
ypoints_RK4 = []
upoints_RK4 = []

y = 0.0
u = 1./np.pi 

for x in xpoints:
    ypoints_RK4.append(y)
    upoints_RK4.append(u)

    m1 = h*u
    k1 = h*F(y, u, x)  #(x, v, t)

    m2 = h*(u + 0.5*k1)
    k2 = h*F(y+0.5*m1, u+0.5*k1, x+0.5*h)

    m3 = h*(u + 0.5*k2)
    k3 = h*F(y+0.5*m2, u+0.5*k2, x+0.5*h)

    m4 = h*(u + k3)
    k4 = h*F(y+m3, u+k3, x+h)

    y += (m1 + 2*m2 + 2*m3 + m4)/6
    u += (k1 + 2*k2 + 2*k3 + k4)/6

# Euler
ypoints_Euler = []
upoints_Euler = []

y = 0.0
u = 1./np.pi 

for x in xpoints:
    ypoints_Euler.append(y)
    upoints_Euler.append(u)

    #y[i] = deltat * (t[i-1]*y[i-1]) + y[i-1]
    m1 = h*u
    k1 = h*F(y, u, x)  #(x, v, t)
    y += m1
    u += k1

y_ana = np.sin(xpoints)/np.pi

plt.plot(xpoints, ypoints_RK4,'r-',linewidth=1,label='k=RK4')
plt.plot(xpoints, ypoints_Euler,'y-',linewidth=1,label='k=Euler')
plt.plot(xpoints, y_ana,'b-',linewidth=1,label='k=analytical')
plt.title('Molla. sin(x). N=' + str(N))
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-101.png")

print("Provar N=1000, N=100, N=10, N=5")
print("Amb N=1000, hi ha coincidència exacta dels 3 mètodes")
print("Amb N=100, hi ha coincidència exacta de RK-4, i ja podem veure l'error d'Euler")
print("Amb N=10, hi ha coincidència exacta de RK-4, i ja podem veure l'error d'Euler")
print("No és fins a N=5, que podem diferenciar RK-4. RK-4 és un mètode molt bo.")

print("\nValor final: ")
print("Solució analítica: ",y_ana[N-1])
print("Solució RK-4: ",ypoints_RK4[N-1]) 
print("Solució Euler: ",ypoints_Euler[N-1]) 
