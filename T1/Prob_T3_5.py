# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Integració numèrica, Problema 5
Integral amb el mètode del trapezoid simple (N=1) o compost (N>1)
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T3_5.py
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

# exemple abs(sin(20x))
f = lambda x : np.abs(np.sin(20*x))
a = 0; b = np.pi; N = 20

# Regla del trapezi
T = trapz(f,a,b,N)
print("abs(sin(20x))")
print("Valor: " + str(T))

I = integrate.quad(lambda x: np.abs(np.sin(20*x)), 0, np.pi ) #càlcul del valor exacte
print("Valor exacte: " + str(I[0]))
print("Trapezoid Rule Error:",np.abs(I[0] - T)) # Trapezoid Rule Error: 
print('L\'error és molt gran, però té lògica perquè els punts on agafem les particions valen 0. Mirar la solució.')

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

plt.title('abs(sin(20x)). Trapezoid Rule, N = {}'.format(N))
fig = plt.gcf()
plt.show()
fig.savefig("../img/T1/Prob_T3_5.png")
