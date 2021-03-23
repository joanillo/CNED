# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
IN-7, IN-24: Suma de Riemann simple i compost
https://www.math.ubc.ca/~pwalls/math-python/integration/riemann-sums/
Integral amb el mètode d'aproximacions rectangulars simple (N=2) o compost (N>2, parell)
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 suma_riemann.py
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

f = lambda x : 1/(1+x**2)
a = 0; b = 5; N = 1


#Let's compute the value of each of the Riemann sums:

dx = (b-a)/N
x_left = np.linspace(a,b-dx,N)
x_midpoint = np.linspace(dx/2,b - dx/2,N)
x_right = np.linspace(dx,b,N)

print("Partition with",N,"subintervals.")
left_riemann_sum = np.sum(f(x_left) * dx)
print("\nLeft Riemann Sum:",left_riemann_sum)

midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
print("Midpoint Riemann Sum:",midpoint_riemann_sum)

right_riemann_sum = np.sum(f(x_right) * dx)
print("Right Riemann Sum:",right_riemann_sum)

'''
la integral entre 0 i 5 de 1/(1+x**2) és l'arctan(5) = 1.373400766945016
'''
I = np.arctan(5)
print("\nValor exacte (arctan(5))= " + str(I)) #1.373400766945016
print("\nLeft Riemann Sum Error:",np.abs(left_riemann_sum - I))
print("Midpoint Riemann Sum Error:",np.abs(midpoint_riemann_sum - I))
print("Right Riemann Sum Error:",np.abs(right_riemann_sum - I))

# gràfica
n = 50 # Use n*N+1 points to plot the function smoothly
x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b,n*N+1)
Y = f(X)

fig, ax = plt.subplots(figsize=(15,5))
plt.subplot(1,3,1)
plt.plot(X,Y,'b')
x_left = x[:-1] # Left endpoints
y_left = y[:-1]
plt.plot(x_left,y_left,'b.',markersize=10)
plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('1/(1+x^2). Left Riemann Sum, N = {}'.format(N))

plt.subplot(1,3,2)
plt.plot(X,Y,'b')
x_mid = (x[:-1] + x[1:])/2 # Midpoints
y_mid = f(x_mid)
plt.plot(x_mid,y_mid,'b.',markersize=10)
plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
plt.title('1/(1+x^2). Midpoint Riemann Sum, N = {}'.format(N))

plt.subplot(1,3,3)
plt.plot(X,Y,'b')
x_right = x[1:] # Left endpoints
y_right = y[1:]
plt.plot(x_right,y_right,'b.',markersize=10)
plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('1/(1+x^2). Right Riemann Sum, N = {}'.format(N))
if N==1:
	fig.savefig("../img/T1/IN-7_aproximacio_rectangular_simple.png")
elif N==2:
	fig.savefig("../img/T1/IN-7_suma_riemann_simple.png")
else:
	fig.savefig("../img/T1/IN-24_suma_riemann_compost.png")
plt.show()