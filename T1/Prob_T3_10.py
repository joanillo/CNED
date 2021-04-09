# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Integració numèrica, Problema 5
Integral amb el mètode del trapezoid simple (N=1) o compost (N>1)
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T3_10.py
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

# exemple 1/srqt(2pi) e^(-x^2/2)
f = lambda x : 1/((2*np.pi)**0.5)*np.exp(-x**2/2)
a = 0; b = 1

I = integrate.quad(lambda x: 1/((2*np.pi)**0.5)*np.exp(-x**2/2), 0, 1 ) #càlcul del valor exacte
print("1/srqt(2pi) e^(-x^2/2)")
print("Valor exacte: " + str(I[0]))

# Regla del trapezi
N = 21
T = trapz(f,a,b,N)
print ("\nNúm intèrvals: " + str(N))
print("Valor: " + str(T))
print("Trapezoid Rule Error:",np.abs(I[0] - T))

N = 22
T = trapz(f,a,b,N)
print ("\nNúm intèrvals: " + str(N))
print("Valor: " + str(T))
print("Trapezoid Rule Error:",np.abs(I[0] - T))

print("\nAmb 22 intèrvals tenim 4 xifres decimals correctes. En la solució això ho podem assegurar amb n>=26")

N = 5
T = trapz(f,a,b,N)
print ("\nNúm intèrvals: " + str(N))
print("Valor: " + str(T))
print("Trapezoid Rule Error:",np.abs(I[0] - T))

# x and y values for the trapezoid rule
x = np.linspace(a,b,N+1)
y = f(x)

# X and Y values for plotting y=f(x)
X = np.linspace(a,b,2000)
Y = f(X)
fig = plt.gcf()
plt.plot(X,Y)

for i in range(N):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)

plt.title('1/srqt(2pi) e^(-x^2/2). Trapezoid Rule, N = {}'.format(N))
fig = plt.gcf()
plt.show()
fig.savefig("../img/T1/Prob_T3_10.png")

'''
sortida del script:
script Prob_T3_10.py
====================
1/srqt(2pi) e^(-x^2/2)
Valor exacte: 0.341344746068543

Núm intèrvals: 21
Valor: 0.3412990187410618
Trapezoid Rule Error: 4.572732748120423e-05

Núm intèrvals: 22
Valor: 0.341303081572739
Trapezoid Rule Error: 4.1664495804005774e-05

Amb 22 intèrvals tenim 4 xifres decimals correctes. En la solució això ho podem assegurar amb n>=26

Núm intèrvals: 5
Valor: 0.3405370984784699
Trapezoid Rule Error: 0.0008076475900730684
'''