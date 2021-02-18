# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
https://www.math.ubc.ca/~pwalls/math-python/integration/trapezoid-rule/
Integral amb el mètode del trapezoid simple (N=1) o compost (N>1)
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 erf.py
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

# exemple sin(x)+1
f = lambda x : np.sin(x) + 1
a = 0; b = 4; N = 1

# x and y values for the trapezoid rule
x = np.linspace(a,b,N+1)
y = f(x)

# X and Y values for plotting y=f(x)
X = np.linspace(a,b,100)
Y = f(X)
plt.plot(X,Y)
#fig, ax = plt.subplots()
#ax.plot(x, y)

for i in range(N):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='b',alpha=0.2)

plt.title('sin(x) + 1. Trapezoid Rule, N = {}'.format(N))
fig = plt.gcf()
plt.show()

if N==1:
    fig.savefig("../img/T1/IN-11_trapezoid2_simple.png")
else:
    fig.savefig("../img/T1/IN-37_trapezoid2_compost.png")

# Let's compute the sum of areas of the trapezoids:
T = trapz(f,a,b,N)
print(T) # 5.513487172039481
# We know the exact value and we can compare the trapezoid rule to the value
I = 5 - np.cos(4)
print(I) # 5.653643620863612
print("Trapezoid Rule Error:",np.abs(I - T)) # Trapezoid Rule Error: 0.14015644882413092

