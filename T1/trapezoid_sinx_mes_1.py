# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
IN-11, IN-31 (exemple arctan)
https://www.math.ubc.ca/~pwalls/math-python/integration/trapezoid-rule/
Integral amb el mètode del trapezoid simple (N=1) o compost (N>1)
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 trapezoid_exp_x2.py
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
    '''Approximate the integral of f(x) from a to b by the trapezoid rule.

    The trapezoid rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/2) \sum_{k=1}^N (f(x_k) + f(x_{k-1}))
    where x_k = a + k*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using the
        trapezoid rule with N subintervals of equal length.

    Examples
    --------
    >>> trapz(np.sin,0,np.pi/2,1000)
    0.9999997943832332
    '''
    x = np.linspace(a,b,N+1) # N+1 points make N subintervals
    y = f(x)
    y_right = y[1:] # right endpoints
    y_left = y[:-1] # left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T


# exemple sin(x) + 1
f = lambda x : np.sin(x)+1
a = 0; b = 4; N = 1

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

plt.title('sin(x)+1. Trapezoid Rule, N = {}'.format(N))
fig = plt.gcf()
plt.show()
if N==1:
    fig.savefig("../img/T1/IN-11_trapezoid_sinx_mes_1_N1.png")
elif N==2:
    fig.savefig("../img/T1/IN-11_trapezoid_sinx_mes_1_N1.png")
else:
    fig.savefig("../img/T1/IN-31_trapezoid_sinx_mes_1_compost.png")

# Regla del trapezi
T = trapz(f,a,b,N)
print("sin(x)+1")
print("Valor: " + str(T)) # 5.631536018149299 (N=10)

I = integrate.quad(lambda x: np.sin(x)+1, 0, 4 ) #càlcul del valor exacte
print("Valor exacte: " + str(I[0])) # 5.653643620863611
#I = 5 - np.cos(4) (analíticament)
print("Trapezoid Rule Error:",np.abs(I[0] - T)) # Trapezoid Rule Error: 0.022107602714312335 (N=10)