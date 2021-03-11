# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Mètode de Newton
https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 newton2.py
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

def newton(f,Df,x0,epsilon,max_iter):
    '''Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/Df(xn)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> Df = lambda x: 2*x - 1
    >>> newton(f,Df,1,1e-8,10)
    Found solution after 5 iterations.
    1.618033988749989
    '''
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if n > 0:
            rn = abs(xn-xnant)/abs(xn)
            print('r'+str(n-1),' = ',rn)
            rn_ant = rn

        print('---')
        print('it',n)
        print('x'+str(n),' = ', xn)
        print('fx'+str(n),' = ',fxn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xnant = xn
        xn = xn - fxn/Dfxn
    print('---')
    print('Després de',max_iter,'iteracions hem obtingut:')
    print('(',xn,',',fxn,')')
    return None
# ==============

p = lambda x: x**3 - 6*x**2 + 9*x - 6
Dp = lambda x: 3*x**2 - 12*x + 9
approx = newton(p,Dp,5.0,1e-18,5)
#approx = newton(p,Dp,3,1e-16,5) # Zero derivative. No solution found.
#approx = newton(p,Dp,3.01,1e-16,20)
#approx = newton(p,Dp,2.0,1e-16,20) # amb 20 iteracions no trobem la solució, amb 50 iteracions sí que la trobem
print(approx)

# ==============

x = np.arange(2.0, 5.0, .005)
y = x**3 - 6*x**2 + 9*x - 6

fig, ax = plt.subplots()
plt.axhline(0, color='black')
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y', title='x^3 - 6x^2 + 9x - 6')
ax.grid()

fig.savefig("../img/T1/ZF-68_newton2.png")
plt.show()
