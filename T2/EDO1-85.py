# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-85
y' = ty, y(0) = 1

http://geofhagopian.net/m2c/M2C-S18/euler_method.pdf
cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-85.py
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

#y' = ty, y(0) = 1
t0 = 0
y0 = 1
tf = 1
#n = 21
n = 6
deltat = (tf-t0) / (n-1)

t = np.linspace(t0,tf,n)
y = np.zeros([n])
y[0] = y0

y_sol_exacta = np.exp(t**2/2)

for i in range (1,n):
	y[i] = deltat * (t[i-1]*y[i-1]) + y[i-1]
	y_sol_exacta[i] = np.exp(t[i]**2/2)

for i in range (n):
	print ("t = ",t[i])
	print ("y = ",np.round_(y[i],5))
	print ("y_exacta = ",np.round_(y_sol_exacta[i],5))
	print ("error = ",np.round_(np.abs(y[i]-y_sol_exacta[i]),5))
	print()

plt.plot(t,y,'ro',label='Euler')
plt.plot(t,y_sol_exacta,'bo',label='e^(x^2/2)')
plt.xlabel ("t")
plt.ylabel ("y")
plt.title ("EDO1-85. Mètode d'Euler")
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-85.png")
