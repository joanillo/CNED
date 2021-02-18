# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
https://stackoverflow.com/questions/52334558/runge-kutta-4th-order-method-to-solve-second-order-odes
y'' + y = 0
y(0) = 0 and y'(0) = 1/pi
solució analítica: sin(x)/pi

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 RK4_v2.py
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

# y' = u
# u' = -y

def F(y, u, x):
    return -y

a = 0
b = 6.0
N =1000
h = (b-a)/N

xpoints = np.arange(a,b,h)
ypoints = []
upoints = []

y = 0.0
u = 1./np.pi 

for x in xpoints:
    ypoints.append(y)
    upoints.append(u)

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


y_ana = np.sin(xpoints)/np.pi

plt.plot(xpoints, ypoints,'r-',linewidth=1,label='k=RK4')
plt.plot(xpoints, y_ana,'b-',linewidth=1,label='k=analytical')
plt.title('sin(x). RK4 coincideix perfectament')
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/RK4.png")

# la solució numèrica i l'analítica coincideixen molt bé:
print(ypoints[200],y_ana[200]) 