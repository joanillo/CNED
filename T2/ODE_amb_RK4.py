# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-100: Problema del pèndol amb fregament:
https://perso.crans.org/besson/publis/notebooks/Runge-Kutta_methods_for_ODE_integration_in_Python.html

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 ODE_amb_RK4.py
'''

import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from scipy.integrate import odeint  # for comparison
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

# primer de tot farem la solució amb odeint, que és la millor manera de resoldre EDOs amb Python
def pend(y, t, b, c):
    return np.array([y[1], -b*y[1] - c*np.sin(y[0])])

b = 0.25
c = 5.0
y0 = np.array([np.pi - 0.1, 0.0])

t = np.linspace(0, 10, 101)

sol = odeint(pend, y0, t, args=(b, c))
plt.plot(t, sol[:, 0], 'b', label=r'$\theta(t)$')
plt.plot(t, sol[:, 1], 'g', label=r'$\omega(t)$')
plt.legend(loc='best')
plt.xlabel('t')
plt.suptitle('Pèndol amb fregament')
plt.title('solució amb odeint')
plt.grid()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-100_ODE_amb_odeint.png")

# Runge-Kutta method of order 1, or the Euler method
# El mètode d'Euler seria el mètode de Runge-Kutta d'ordre 1

def rungekutta1(f, y0, t, args=()):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n - 1):
        y[i+1] = y[i] + (t[i+1] - t[i]) * f(y[i], t[i], *args)
    return y

sol = rungekutta1(pend, y0, t, args=(b, c))

plt.plot(t, sol[:, 0], 'b', label=r'$\theta(t)$')
plt.plot(t, sol[:, 1], 'g', label=r'$\omega(t)$')
plt.legend(loc='best')
plt.xlabel('t')
plt.suptitle('Pèndol amb fregament')
plt.title('solució amb Euler (RK1) (100 punts)')
plt.grid()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-100_ODE_amb_Euler.png")

# com més punts tinguem, millorem el resultat
t2 = np.linspace(0, 10, 1001)
sol2 = rungekutta1(pend, y0, t2, args=(b, c))
t3 = np.linspace(0, 10, 10001)
sol3 = rungekutta1(pend, y0, t3, args=(b, c))

plt.plot(t, sol[:, 0], label=r'$\theta(t)$ with 101 points')
plt.plot(t2, sol2[:, 0], label=r'$\theta(t)$ with 1001 points')
plt.plot(t3, sol3[:, 0], label=r'$\theta(t)$ with 10001 points')
plt.legend(loc='best')
plt.xlabel('t')
plt.suptitle('Pèndol amb fregament')
plt.title('solució amb Euler (RK1) (més punts)')
plt.grid()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-100_ODE_amb_Euler_v2.png")

# Runge-Kutta method of order 2
def rungekutta2(f, y0, t, args=()):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n - 1):
        h = t[i+1] - t[i]
        y[i+1] = y[i] + h * f(y[i] + f(y[i], t[i], *args) * h / 2., t[i] + h / 2., *args)
    return y

t4 = np.linspace(0, 10, 21)
sol4 = rungekutta2(pend, y0, t4, args=(b, c))

t = np.linspace(0, 10, 101)
sol = rungekutta2(pend, y0, t, args=(b, c))

t2 = np.linspace(0, 10, 1001)
sol2 = rungekutta2(pend, y0, t2, args=(b, c))

t3 = np.linspace(0, 10, 10001)
sol3 = rungekutta2(pend, y0, t3, args=(b, c))

plt.plot(t4, sol4[:, 0], label='with 11 points')
plt.plot(t, sol[:, 0], label='with 101 points')
plt.plot(t2, sol2[:, 0], label='with 1001 points')
plt.plot(t3, sol3[:, 0], label='with 10001 points')
plt.legend(loc='best')
plt.xlabel('t')
plt.suptitle('Pèndol amb fregament')
plt.title('solució amb RK2')
plt.grid()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-100_ODE_amb_RK2.png")

# Runge-Kutta method of order 4, RK4

def rungekutta4(f, y0, t, args=()):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n - 1):
        h = t[i+1] - t[i]
        k1 = f(y[i], t[i], *args)
        k2 = f(y[i] + k1 * h / 2., t[i] + h / 2., *args)
        k3 = f(y[i] + k2 * h / 2., t[i] + h / 2., *args)
        k4 = f(y[i] + k3 * h, t[i] + h, *args)
        y[i+1] = y[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
    return y

t4 = np.linspace(0, 10, 21)
sol4 = rungekutta4(pend, y0, t4, args=(b, c))

t = np.linspace(0, 10, 101)
sol = rungekutta4(pend, y0, t, args=(b, c))

t2 = np.linspace(0, 10, 1001)
sol2 = rungekutta4(pend, y0, t2, args=(b, c))

plt.plot(t4, sol4[:, 0], label='with 21 points')
plt.plot(t, sol[:, 0], label='with 101 points')
plt.plot(t2, sol2[:, 0], label='with 1001 points')
plt.legend(loc='best')
plt.xlabel('t')
plt.suptitle('Pèndol amb fregament')
plt.title('solució amb RK4')
plt.grid()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-100_ODE_amb_RK4.png")