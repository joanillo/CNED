# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Tema4.3 SolucionProblemasEDOsNum.pdf
P1: 
y' = 4x - 2y, y(0) = 2

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 ProblemesEDOsNum_P1.py
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

#y' = 4x - 2y, y(0) = 2
print('y\' = 4x - 2y, y(0) = 2\n')
x0 = 0
y0 = 2
xf = 0.5
n = 11
deltax = (xf-x0) / (n-1) # h=0.05

x = np.linspace(x0,xf,n)
y = np.zeros([n])
y [ 0 ] = y0

for i in range (1,n):
	y[i] = deltax * (4*x[i-1] - 2*y[i-1]) + y[i-1]

for i in range (n):
	print (round(x[i],2),"\t",round(y[i],5))

plt.plot(x,y,'o')
plt.xlabel ("Value of x")
plt.ylabel ("Value of y")
plt.title ("Problema 1. Euler amb h=0.05")
plt.suptitle ("y' = 4x − 2y")
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/python3ProblemesEDOsNum_P1.png")
