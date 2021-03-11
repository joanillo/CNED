# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)

'''
exemple: x^3-x+1
Problema 4. Amb bisecció necessitem 17 iteracions; amb Newton no convergeix; combinant bisecció amb Newton aconseguim molt bon resultat
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T1_4.py
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
            if rk < tol and np.abs(f(a_n)) < tol:
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
    return m_n # he modificat aquesta línia per poder empalmar bé amb el mètode de Newton


# ==============================

def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if n > 0:
            rn = abs(xn-xnant)/abs(xn)
            print('r'+str(n-1),' = ',rn)
            if rn < epsilon and np.abs(f(xnant)) < epsilon:
                print("hem arribat al tol")
                return m_n
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

# ==============================

f = lambda x: x**3 - x + 1
Df = lambda x: 3*x**2 - 1

tol = 0.00005 #tolx = tolf

print('\n== Mètode de la bisecció ==')
print('(Necessitem 17 iteracions)')
approx = bisection(f,-2.0,0.0,1000,tol)
print('=====')

print('\n== Mètode de Newton ==')
print('(No convergeix, interpretar gràfica, mala elecció del punt)')
approx = newton(f,Df,1.0,tol,5) # provar també amb N=15. Veure la gràfica, x=1 és una mala elecció.

print('\n== Mètode combinat: comencem amb bisecció i després Newton ==')
print('(Bona combinació de bisecció i Newton)')
approx = newton(f,Df,bisection(f,-2.0,0.0,2,tol),tol,4)

# ==============================

x = np.arange(-2.0, 2.0, .005)
y = x**3 - x + 1

fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y', title='x^3 - x + 1')
ax.grid()

fig.savefig("../img/T1/Prob_T1_4.png")
plt.show()

