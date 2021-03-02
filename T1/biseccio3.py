# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)

'''
exemple: sin(sqrt(x))-x
modificació per tal d'introduir el concepte de tolerància, tol
rk = abs(xk+1 - xk)/abs(xk+1) < tol ; f(xk)<tol
sin(sqrt(x))-x, trobar el 0 pel mètode de la bisecció
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 biseccio3.py
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

def bisection(f,a,b,N, tol):
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
    for n in range(0,N):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if (n>0):
            rk = np.abs((m_n-a_n)/m_n)
            print('rk =',rk)
            if rk < tol and np.abs(f_m_n) < tol:
            #if rk < tol: #només considerem el tolx
                print("hem arribat al tol")
                return m_n
        print ('-----')
        print ('it',n)
        print ('a =',m_n)
        print('fxk =',np.abs(f_m_n))
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

f = lambda x: np.sin(np.sqrt(x))-x
#tol = 0.05
tol = 0.001 #línia 55, només hem de considerar tolx. Dóna 7 iteracions (1->7), però també ho podem pensar com a (0->6)
approx_phi = bisection(f,.75,.8,1000,tol)
print('=====')
print('resultat:',approx_phi)

# ==============================
# gràfica:
x = np.arange(.5, .9, .005)
y = np.sin(np.sqrt(x))-x

fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y', title='sin(sqrt(x)) - x')
ax.grid()

fig.savefig("../img/T1/biseccio3.png")
plt.show()

