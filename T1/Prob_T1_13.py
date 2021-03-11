# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)

'''
Comparació dels mètodes de la bisecció, Newton i secant
exemple: f(x) = 2 - x^3.

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T1_13.py num_iter
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

if len(sys.argv) != 2:
	print('ex: python3 Prob_T1_13.py 5')
	exit(0)
N = int(sys.argv[1])+1 # 5 iteracions vols dir que només calculo 4 valors de r_k. L'hi sumo 1 per tenir-ne una altra.

def bisection(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b

    for n in range(0,N):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        
        if (n>0):
            #per calcular rk necessitem el valor següent
            rk = np.abs((m_n-a_n)/m_n)
            print('rk =',rk)
            list_bisection.append(rk)

        print ('-----')
        print ('it',n)
        print ('a =',m_n)
        print('fxk =',f_m_n)

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

def newton(f,Df,x0,max_iter):
    xn = x0

    for n in range(0,max_iter):
        fxn = f(xn)
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn

        if (n>0):
            #per calcular rk necessitem el valor següent
            rk = np.abs((xn-xnant)/xn)
            print('rk =',rk)
            list_newton.append(rk)

        print ('-----')
        print ('it',n)
        print ('a =',xn)
        print('fxk =',fxn)
        xnant = xn

    return xn

# ==============================

def secant(f,a,b,N):

    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    m_nant = a

    for n in range(0,N):

        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if (n>1):
            #per calcular rk necessitem el valor següent
            rk = np.abs((m_n-m_nant)/m_n)
            print('rk =',rk)
            list_secant.append(rk)
            p = (np.log(rk) / np.log(rk_ant))
            rk_ant = rk
            print('p = ', p)
        elif (n>0):
            #per calcular rk necessitem el valor següent
            rk = np.abs((m_n-m_nant)/m_n)
            print('rk =',rk)
            list_secant.append(rk)
            rk_ant = rk

        print ('-----')
        print ('it',n)
        print ('a =',m_n)
        print('fxk =',f_m_n)
        
        # Nota: si vull veure el comportament superlinial, no he de fer la tria if f(a_n)*f_m_n < 0 per escollir un dels dos intèrvals
        a_n = a_n
        b_n = m_n
        m_nant = m_n

	
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

# ==============================
f = lambda x: 2 - x**3
Df = lambda x: -3*x**2
# ==============================
print('== Mètode de la bisecció ==')
list_bisection = []
approx = bisection(f,1.0,2.0,N)
print('=====')
print('Bisecció resultat:',approx)
print('=====')
# ==============================

print('== Mètode de Newton ==')
list_newton = []
approx = newton(f,Df,1,N)
print('=====')
print('Newton resultat:',approx)
print('=====')
# ==============================

print('== Mètode de la Secant ==')
list_secant = []
approx = secant(f,1,2,N)
print('=====')
print('Secant resultat:',approx)
print('=====')
# ==============================

#gràfica:
x = []
for n in range(0,N-1):
	x.append(n)

fig, ax = plt.subplots()
plt.yscale("log")
plt.plot(x, list_bisection, 'r-o', x, list_newton, 'b-o', x, list_secant, 'g-o')
plt.legend(['bisecció','newton', 'secant'])
ax.set(xlabel='passos', ylabel='log(r_k)', title='comparació tres mètodes')
ax.grid()

fig.savefig("../img/T1/Prob_T1_13.png")
plt.show()
