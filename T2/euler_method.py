# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-86
y' = −y + sin(x), y(0) = 1

http://geofhagopian.net/m2c/M2C-S18/euler_method.pdf
cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 euler_method.py
'''

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

#y' = −y + sin(x), y(0) = 1
x0 = 0
y0 = 1
xf = 10
n = 101
deltax = (xf-x0) / (n-1)

x = np.linspace(x0,xf,n)
y = np.zeros([n])
y [ 0 ] = y0

for i in range (1,n):
	y[i] = deltax * (-y [i-1] + np.sin(x[i-1])) + y[i-1]

for i in range (n):
	print (x[i],y[i])

plt.plot(x,y,'o')
plt.xlabel ("Value of x")
plt.ylabel ("Value of y")
plt.title ("Approximate Solution with Forward Euler's Method")
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-88_Eulers_Method.png")
