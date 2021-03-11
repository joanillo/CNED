# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Exercici d'autoavaluació 2 (ZF-98)
p(x) = -x^5 + 3x^4 - x^3 - 5x^2 + 6x - 2 = (x-1)^5*(x-sqrt(2))*(x+sqrt(2)) (x=1 és arrel d'ordre 3; sqrt(2) i sqrt(-2) són arrels simples)
convergència subòptima cercant el zero x=1 (arrel triple); convergència òptima cercant el zero x=sqrt(2) (arrel simple)
Mètode de Newton
https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/

cd /home/joan/UPC_2021/CNED/apunts/python/T1
PS1="$ "
python3 Exercici_Autoavaluacio_2.py
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
    #Approximate solution of f(x)=0 by Newton's method.
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if n > 1:
            rn = abs(xn-xnant)/abs(xn)
            pn = np.abs(np.log(rn)/np.log(rn_ant))
            lambdan = np.abs(rn/rn_ant)
            print('r'+str(n-1),' = ',rn)
            print('p'+str(n-1),' = ',pn)
            print('lambda'+str(n-1),' = ',lambdan)
            rn_ant = rn
        elif n > 0:
            rn = abs(xn-xnant)/abs(xn)
            print('r'+str(n-1),' = ',rn)
            rn_ant = rn

        print('---')
        print('it',n)
        print('x'+str(n),' = ', xn)
        print('fx'+str(n),' = ',fxn)

        if abs(fxn) < epsilon:
            print('---')
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xnant = xn
        xn = xn - fxn/Dfxn
    print('Després de',max_iter,'iteracions hem obtingut:')
    print('(',xn,',',fxn,')')
    return None
# ==============

p = lambda x: -x**5 + 3*x**4 - x**3 - 5*x**2 + 6*x - 2
Dp = lambda x: -5*x**4 + 12*x**3 - 3*x**2 - 10*x + 6

approx = newton(p,Dp,0.5,1e-4,20) # transparència ZF-99 convergència subòptima cercant el zero x=1 (arrel triple)
#approx = newton(p,Dp,2.0,1e-10,40) # transparència ZF-99 convergència òptima cercant el zero x=sqrt(2) (arrel simple)
print(approx)

# ==============

x = np.arange(-1.6, 1.6, .005)
y = -x**5 + 3*x**4 - x**3 - 5*x**2 + 6*x - 2

fig, ax = plt.subplots()
plt.axhline(0, color='black')
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y', title='-x^5 + 3x^4 - x^3 - 5x^2 + 6x - 2')
ax.grid()

fig.savefig("../img/T1/ZF-98_ex_autoav_2a.png")
plt.show()

# més detall entre 0.8 i 1.5, doncs x=1 és una arrel triple, i sqrt(2) és arrel simple
x = np.arange(0.8, 1.5, .005)
y = -x**5 + 3*x**4 - x**3 - 5*x**2 + 6*x - 2

fig, ax = plt.subplots()
plt.axhline(0, color='black')
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y', title='-x^5 + 3x^4 - x^3 - 5x^2 + 6x - 2')
ax.grid()

fig.savefig("../img/T1/ZF-98_ex_autoav_2b.png")
plt.show()
