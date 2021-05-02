# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-85
y' = ty, y(0) = 1

http://geofhagopian.net/m2c/M2C-S18/euler_method.pdf
cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-100_euler.py
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
n = 6 # 5 passos
deltat = (tf-t0) / (n-1)

t = np.linspace(t0,tf,n)
y = np.zeros([n])
y[0] = y0

y_sol_exacta = np.exp(t**2/2)

for i in range (1,n):
	y[i] = deltat * (t[i-1]*y[i-1]) + y[i-1]
	y_sol_exacta[i] = np.exp(t[i]**2/2)

for i in range (n):
	print ("t = ",np.round_(t[i],2)," ==> ", "y = ",np.round_(y[i],5))
	#print ("y_exacta = ",np.round_(y_sol_exacta[i],5))
	error = np.round_(np.abs(y[i]-y_sol_exacta[i]),5)
	#print ("error = ", error)
	#print()

error_final_N5 = error
print("Error N=5: ",error_final_N5)

# ==============
print()

t0 = 0
y0 = 1
tf = 1
n = 21 # 20 passos
deltat = (tf-t0) / (n-1)

t = np.linspace(t0,tf,n)
y = np.zeros([n])
y[0] = y0

y_sol_exacta = np.exp(t**2/2)

for i in range (1,n):
	y[i] = deltat * (t[i-1]*y[i-1]) + y[i-1]
	y_sol_exacta[i] = np.exp(t[i]**2/2)

for i in range (n):
	print ("t = ",np.round_(t[i],2)," ==> ", "y = ",np.round_(y[i],5))
	#print ("y_exacta = ",np.round_(y_sol_exacta[i],5))
	error = np.round_(np.abs(y[i]-y_sol_exacta[i]),5)
	#print ("error = ", error)
	#print()

error_final_N20 = error
print("Error N=20: ",error_final_N20)

print("\nQuocient errors N=5/N=20: ", error_final_N5/error_final_N20)
print("L'error ha quedat dividit aproximadament per 4, que demostra que Euler és d'ordre 1.")

