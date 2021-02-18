# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
#https://hub.packtpub.com/how-to-compute-interpolation-in-scipy/
# interpolació amb spline de 10 punts que responen a un sinus. S'aconsegueix recostruir una funció en forma de sinus.

from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

# sampling
x = np.linspace(0, 10, 10)
y = np.sin(x)

# spline trough all the sampled points
tck = interpolate.splrep(x, y)
x2 = np.linspace(0, 10, 200)
y2 = interpolate.splev(x2, tck)

'''
# spline with all the middle points as knots (not working yet)
# knots = x[1:-1] # it should be something like this
knots = np.array([x[1]]) # not working with above line and just seeing what this line does
weights = np.concatenate(([1],np.ones(x.shape[0]-2)*.01,[1]))
tck = interpolate.splrep(x, y, t=knots, w=weights)
x3 = np.linspace(0, 10, 200)
y3 = interpolate.splev(x2, tck)
'''

fig, ax = plt.subplots()
#plt.plot(x, y, 'go', x2, y2, 'b', x3, y3,'r')
plt.plot(x, y, 'go', x2, y2)
fig.savefig("../img/T1/splines3.png")
plt.show()
