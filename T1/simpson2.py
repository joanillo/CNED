# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
IN-15
https://www.math.ubc.ca/~pwalls/math-python/integration/simpsons-rule/
Integral amb el mètode de Simpson simple (N=2) o compost (N>2, parell)
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 simpson2.py
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

def simps(f,a,b,N=50):
    '''Approximate the integral of f(x) from a to b by Simpson's rule.

    Simpson's rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/3) \sum_{k=1}^{N/2} (f(x_{2i-2} + 4f(x_{2i-1}) + f(x_{2i}))
    where x_i = a + i*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : (even) integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using
        Simpson's rule with N subintervals of equal length.

    Examples
    --------
    >>> simps(lambda x : 3*x**2,0,1,10)
    1.0
    '''
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


print ('\nexemple sin(x)+1 a l\'intèrval [0,4] amb el mètode compost de Simpson amb 4 intèrvals:')
res = simps(lambda x : np.sin(x) + 1,0,4,4)
print(res) # 5.664052109938163


# ==============

import scipy.integrate as spi


N = 4; a = 0; b = 4;
x = np.linspace(a,b,N+1)
y = np.sin(x)+1
approximation = spi.simps(y,x) # amb scipy
print(approximation) # 5.664052109938163

#valor exacte:
I = 5 - np.cos(4)
print(I) # 5.653643620863612
print("Simpson Rule Error:",np.abs(I - res)) # Simpson Rule Error: 0.010408489074551497

