# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)

'''
ZF-77: x^ - 2 = 0. Trobar p: p = log(r_k)/logr_(k-1) (quocient d'errors relatius entre iteracions)
treballar amb precisió de 50 decimals
*https://zetcode.com/python/decimal/

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 comparacio_biseccio_newton_secant.py biseccio
python3 comparacio_biseccio_newton_secant.py newton
python3 comparacio_biseccio_newton_secant.py secant
'''

import numpy as np
import os
import sys
import math
from decimal import Decimal, getcontext

getcontext().prec = 50

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============


if len(sys.argv) != 2:
    print('python3 comparacio_biseccio_newton_secant.py [biseccio | newton | secant]')
    exit(0)
tipus = sys.argv[1]

def bisection(f,a,b,N):
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

    '''
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b

    for n in range(1,N+1):
        m_n = (Decimal(a_n) + Decimal(b_n))/Decimal(2.0)
        f_m_n = Decimal(f(m_n))
        print ('-----')
        print ('it = ',n)
        print ('a = ',m_n)
        print('fxk =',f_m_n)

        #error relatiu:
        if n>2:
            r_n_1 = abs((Decimal(m_n) - Decimal(m_n_ant))/Decimal(m_n)) # el valor de r_n s'hauria de calcular a partir de m_n+1, com està en altres exemples
            p = Decimal(math.log(r_n_1) / math.log(r_n_ant))
            print('p = ',p)
            r_n_ant = r_n_1 # guardem el valor anterior
        elif n>1:
            r_n_1 = abs((Decimal(m_n) - Decimal(m_n_ant))/Decimal(m_n))
            print('err_rel = ',r_n_1)
            r_n_ant = r_n_1 # guardem el valor anterior
        m_n_ant = m_n # guardem el valor anterior


        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2


# ==============================

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

        print ('-----')
        print ('it = ',n)
        print ('a = ',xn)
        print('fxk =',fxn)

        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None

        #error relatiu:
        if n>2:
            r_n_1 = abs((Decimal(xn) - Decimal(xn_ant))/Decimal(xn))
            print('err_rel = ',r_n_1)
            p = Decimal(math.log(r_n_1) / math.log(r_n_ant))
            print('p = ',p)
            r_n_ant = r_n_1 # guardem el valor anterior
        elif n>1:
            r_n_1 = abs((Decimal(xn) - Decimal(xn_ant))/Decimal(n))
            print('err_rel = ',r_n_1)
            r_n_ant = r_n_1 # guardem el valor anterior
        xn_ant = xn # guardem el valor anterior

        xn = Decimal(xn) - Decimal(fxn)/Decimal(Dfxn)

    print('Exceeded maximum iterations. No solution found.')
    return None

# ======================================================
def secant(f,a,b,N):

    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    m_nant = b

    print ('-----')
    print ('it','0')
    print ('a =',a_n)
    print('fxk =',f(a_n))

    for n in range(1,N+1):

        m_n = Decimal(a_n) - Decimal(f(a_n))*(Decimal(b_n) - Decimal(a_n))/(Decimal(f(b_n)) - Decimal(f(a_n)))
        f_m_n = f(m_n)
        #per calcular rk necessitem el valor següent
        r_n_1 = np.abs((Decimal(m_n)-Decimal(m_nant))/Decimal(m_n))

        print('r_n_1 =',r_n_1)
        print('log(err_rel) =',Decimal(math.log(r_n_1)))
        if (n>1):
            p = Decimal((math.log(r_n_1) / math.log(r_n_ant)))
            print('p = ',p)
        print ('-----')
        print ('it',n)
        print ('a =',m_n)
        print('fxk =',f_m_n)
        
        # Nota: si vull veure el comportament superlinial, no he de fer la tria if f(a_n)*f_m_n < 0 per escollir un dels dos intèrvals
        a_n = a_n
        b_n = m_n
        m_nant = m_n
        r_n_ant =  r_n_1

    #per calcular rk necessitem el valor següent
    m_n = Decimal(a_n) - Decimal(f(a_n))*(Decimal(b_n) - Decimal(a_n))/(Decimal(f(b_n)) - Decimal(f(a_n)))
    f_m_n = f(m_n)
    r_n_1 = np.abs((m_n-m_nant)/m_n)
    print('r_n_1 =',r_n_1)
    print('log(err_rel) =',Decimal(math.log(r_n_1)))
    p = Decimal((math.log(r_n_1) / math.log(r_n_ant)))
    print('p = ',p)
    print('NOTA: p > 1 i p < 2, tot i que no arriba a valors de p ~ 1.5')
    
    return Decimal(a_n) - Decimal(f(a_n))*(Decimal(b_n) - Decimal(a_n))/(Decimal(f(b_n)) - Decimal(f(a_n)))

# ======================================================


if (tipus == 'biseccio'):
    print('== Mètode de la bisecció ==')
    f = lambda x: Decimal(x)**Decimal(2.0) - Decimal(2.0) # f(x) = x^2 - 2
    approx_phi = bisection(f,1.0,2.0,160)

elif (tipus == 'newton'):

    print('== Mètode de Newton ==')
    f = lambda x: Decimal(x)**Decimal(2.0) - Decimal(2.0) # f(x) = x^2 - 2
    Df = lambda x: 2*Decimal(x)
    approx = newton(f,Df,1.1,1e-30,8800)
    print (approx)

elif (tipus == 'secant'):
    print('== Mètode de la Secant ==')
    f = lambda x: Decimal(x)**Decimal(2.0) - Decimal(2.0) # f(x) = x^2 - 2
    approx = secant(f,1.0,2.0,15) 
    print(approx)
