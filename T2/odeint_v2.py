# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-12: Llei de Hooke amb K=-1: y''(t) = -y(t)
https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html
cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 odeint_v2.py
'''

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

#The second order differential equation for the angle theta of a pendulum acted on by gravity with friction can be written:
#theta''(t) + b*theta'(t) + c*sin(theta(t)) = 0


def hooke(arr, t):
    y,v = arr
    darrdt = [v, -y]
    return darrdt


#For initial conditions, we assume the pendulum is nearly vertical with theta(0) = pi - 0.1, and is initially at rest, so omega(0) = 0. Then the vector of initial conditions is
arr0 = [3.0, 2.0]

#We will generate a solution at 101 evenly spaced samples in the interval 0 <= t <= 10. So our array of times is:
t = np.linspace(0, 10, 101)

#Call odeint to generate the solution.
sol = odeint(hooke, arr0, t)

#The solution is an array with shape (101, 2). The first column is theta(t), and the second is omega(t). The following code plots both components.
plt.plot(t, sol[:, 0], 'b', label='y(t)')
plt.plot(t, sol[:, 1], 'g', label='v(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.title('Llei de Hooke y\'\'(t) = -y(t)')
plt.grid()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-12_llei_hooke.png")
