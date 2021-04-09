# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Integració numèrica, Problema 3
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T3_3.py
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

def trapz(f,a,b,N=50):
    x = np.linspace(a,b,N+1) # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T


# exemple sin(x)^2
f = lambda x : np.sin(x)**2
a = 0; b = np.pi/2; N = 4

# Regla del trapezi
T = trapz(f,a,b,N)
print("sin(x)^2")
print("Valor: " + str(T))

I = integrate.quad(lambda x: np.sin(x)**2, 0, np.pi/2 ) #càlcul del valor exacte
print("Valor exacte: " + str(I[0]) + " (pi/4)")
#I = 5 - np.cos(4) (analíticament)
print("Trapezoid Rule Error:",np.abs(I[0] - T)) # Trapezoid Rule Error: 
print("l'error és 0: simetria")

# x and y values for the trapezoid rule
x = np.linspace(a,b,N+1)
y = f(x)

# X and Y values for plotting y=f(x)
X = np.linspace(a,b,100)
Y = f(X)
fig = plt.gcf()
plt.plot(X,Y)

for i in range(N):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)

plt.title('sin(x)^2. Trapezoid Rule, N = {}'.format(N))
fig = plt.gcf()
plt.show()
fig.savefig("../img/T1/Prob_T3_3.png")
