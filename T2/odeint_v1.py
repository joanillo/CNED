# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-6: exemple del pèndol
https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html
cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 odeint_v1.py
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

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

# We assume the constants are b = 0.25 and c = 5.0:
b = 0.25
c = 5.0

#For initial conditions, we assume the pendulum is nearly vertical with theta(0) = pi - 0.1, and is initially at rest, so omega(0) = 0. Then the vector of initial conditions is
y0 = [np.pi - 0.1, 0.0]

#We will generate a solution at 101 evenly spaced samples in the interval 0 <= t <= 10. So our array of times is:
t = np.linspace(0, 10, 101)

#Call odeint to generate the solution. To pass the parameters b and c to pend, we give them to odeint using the args argument.
sol = odeint(pend, y0, t, args=(b, c))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

#The solution is an array with shape (101, 2). The first column is theta(t), and the second is omega(t). The following code plots both components.
ax1.plot(t, sol[:, 0], 'b', label='theta(t)')
ax2.plot(t, sol[:, 1], 'g', label='omega(t)')

ax1.set_xlabel('time , sec')
ax1.set_ylabel('theta (rad)',color='b')
ax2.set_ylabel('w (rad/s)',color='g')
plt.title('Pèndol oscil·lant amb fregament')
plt.grid()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-6_pendol_oscillant.png")
