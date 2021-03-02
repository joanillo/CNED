# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Mètode de la secant
https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/secant/
ZF-84: x^3 - 6*x^2 + 9x - 6

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 secant2.py
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

def secant(f,a,b,N):
    '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

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
    m_N : number
        The x intercept of the secant line on the the Nth interval
            m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
        for some intercept m_n then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iterations, the secant method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secant(f,1,2,5)
    1.6180257510729614
    '''
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(0,N):

        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)

        if n > 0:
            r_n = abs(m_n-m_nant)/abs(m_n)
            print('r_'+str(n-1),' = ',r_n)

        print('---')
        print('it',n)
        print('m_'+str(n),' = ', m_n)
        print('f_m_'+str(n),' = ',f_m_n)

        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
            m_nant = b_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
            m_nant = a_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None

    print('---')
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
# ======================================================
p = lambda x: x**3 - 6*x**2 + 9*x - 6

approx = secant(p,2,3,20) #Secant method fails. (a la segona iteració la recta secant és horitzontal)
#approx = secant(p,2,5,20) 
print(approx)

# ==============================

x = np.arange(2.0, 5.0, .005)
y = x**3 - 6*x**2 + 9*x - 6

fig, ax = plt.subplots()
plt.axhline(0, color='black')
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y', title='x^3 - 6x^2 + 9x - 6')
ax.grid()

fig.savefig("../img/T1/ZF-84_secant2.png")
plt.show()
