# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
IN-11, IN-31
https://www.math.ubc.ca/~pwalls/math-python/integration/trapezoid-rule/
Integral amb el mètode del trapezoid simple (N=1) o compost (N>1)
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 trapezoid.py
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

# primer exemple: e^(-x^2)
x = np.linspace(-0.5,1.5,100)
y = np.exp(-x**2)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y', title='exp(-x^2)')
ax.grid()

x0 = 0; x1 = 1;
y0 = np.exp(-x0**2); y1 = np.exp(-x1**2);
plt.fill_between([x0,x1],[y0,y1])

plt.xlim([-0.5,1.5]); plt.ylim([0,1.5]);
fig = plt.gcf()
plt.show()
fig.savefig("../img/T1/IN-11_trapezoid_ex2_simple.png")

#Approximate the integral by the area of the trapezoid:
A = 0.5*(y1 + y0)*(x1 - x0)
print("Trapezoid area:", A)

# més exemples:
print(trapz(np.sin,0,np.pi/2,1000)) # integral de sin(x) entre 0 i pi/2
print(trapz(lambda x : 3*x**2,0,1,10000)) # integral de 3x^2 entre 0 i 1
print(trapz(lambda x : x,0,1,1)) # integral de x entre 0 i 1

# exemple de l'arctan
f = lambda x : 1/(1 + x**2)
a = 0; b = 5; N = 10

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

plt.title('arctan. Trapezoid Rule, N = {}'.format(N))
fig = plt.gcf()
plt.show()
if N==1:
    fig.savefig("../img/T1/IN-11_trapezoid_arctan_simple.png")
else:
    fig.savefig("../img/T1/IN-31_trapezoid_arctan_compost.png")

# Let's compute the sum of areas of the trapezoids:
T = trapz(f,a,b,N)
print(T) # 1.3731040812301096
# We know the exact value and we can compare the trapezoid rule to the value
I = np.arctan(5)
print(I) # 1.373400766945016
print("Trapezoid Rule Error:",np.abs(I - T)) # Trapezoid Rule Error: 0.00029668571490626405

