# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Mètode de la secant
https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/secant/

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 secant3.py
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
    for n in range(1,N+1):

        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)

        print('m_n=',m_n)
        print('f_m_n=',f_m_n)
        if n!=1:
            rn = abs(m_n-m_nant)/abs(m_n)
            print('rn=',rn)
        print('---')
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
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
# ======================================================
p = lambda x: np.cos(x)

approx = secant(p,1,2,0) # 0 iteracions és de fet 1 iteració: deixo entrar en el bucle per calcular la primera iteració
print(approx)


'''
solució:
x0=1; x1=2; hem de calcular x2
x2 = x1 - f(x1)/s1
on
s1 = (f(x1)-f(x0))/(x1-x0)
'''
print('solució=',(2 - np.cos(2)/(np.cos(2)-np.cos(1))))
'''
m_n= 1.5649043758915777 -> solució
f_m_n= 0.005891916813448233
'''
# ==============================

x = np.arange(1.0, 2.0, .005)
y = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y', title='cos(x)')
ax.grid()

fig.savefig("../img/T1/secant3.png")
plt.show()
