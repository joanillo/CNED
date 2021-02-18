# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-6
Sistema de dues masses i dues molles acoplades que es deixen moure lliurement, sense fregament,
a partir d'una posició de no-repòs:
https://scipy-cookbook.readthedocs.io/items/CoupledSpringMassSystem.html
============================================
odeint: simulació . Exemple de resolució de EDO (transparència??)

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 sistema_masses-molles_acoblades.py
'''

import numpy as np
from scipy.integrate import odeint # Use ODEINT to solve the differential equations defined by the vector field
from matplotlib import pyplot as plt
import os
import sys

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

def vectorfield(w, t, p):
    """
    Defines the differential equations for the coupled spring-mass system.

    Arguments:
        w :  vector of the state variables:
                  w = [x1,y1,x2,y2]
        t :  time
        p :  vector of the parameters:
                  p = [m1,m2,k1,k2,L1,L2,b1,b2]
    """
    x1, y1, x2, y2 = w
    m1, m2, k1, k2, L1, L2, b1, b2 = p

    # Create f = (x1',y1',x2',y2'):
    f = [y1,
         (-b1 * y1 - k1 * (x1 - L1) + k2 * (x2 - x1 - L2)) / m1,
         y2,
         (-b2 * y2 - k2 * (x2 - x1 - L2)) / m2]
    return f


# ------------------------------------------------------------------

# Parameter values
# Masses:
m1 = 1.0
m2 = 1.5
# Spring constants
k1 = 8.0
k2 = 40.0
# Natural lengths
L1 = 0.5
L2 = 1.0
# Friction coefficients
b1 = 0.8
b2 = 0.5

# Initial conditions
# x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
x1 = 0.5
y1 = 0.0
x2 = 2.25
y2 = 0.0

# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10.0
numpoints = 250

# Create the time samples for the output of the ODE solver.
# I use a large number of points, only because I want to make
# a plot of the solution that looks nice.
t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

# Pack up the parameters and initial conditions:
p = [m1, m2, k1, k2, L1, L2, b1, b2]
w0 = [x1, y1, x2, y2]

# Call the ODE solver.
wsol = odeint(vectorfield, w0, t, args=(p,),
              atol=abserr, rtol=relerr)

original_stdout = sys.stdout
with open('two_springs.dat', 'w') as f:
    # Print & save the solution.
    for t1, w1 in zip(t, wsol):
        #print(<message>, file=<output_stream>)
        #print >> f, t1, w1[0], w1[1], w1[2], w1[3]
        #print (t1, w1[0], w1[1], w1[2], w1[3], f)
        sys.stdout = f # Change the standard output to the file we created.
        print(t1, w1[0], w1[1], w1[2], w1[3])
        sys.stdout = original_stdout # Reset the standard output to its original value


t, x1, xy, x2, y2 = np.loadtxt('two_springs.dat', unpack=True)

fig, ax = plt.subplots()
lw = 1
plt.plot(t, x1, 'b', linewidth=lw, label=r'$x_1$')
plt.plot(t, x2, 'g', linewidth=lw, label=r'$x_2$')


plt.legend(loc='best')
ax.set(xlabel='t', ylabel='x', title='sistema 2 masses-2 molles acoblades')
ax.grid()
fig.savefig("../img/T2/EDO1-6_sistema_masses-molles_acoblades.png")
plt.show()
