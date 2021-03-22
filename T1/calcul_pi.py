# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
IN-24: Suma de Riemann compost. La integral entre 0 i 1 de 4/(1+x^2) = PI
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

f = lambda x : 4/(1+x**2)
a = 0; b = 1; N = 10
n = 10 # Use n*N+1 points to plot the function smoothly

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
plt.title('Left Riemann Sum, N = {}'.format(N))

plt.subplot(1,3,2)
plt.plot(X,Y,'b')
x_mid = (x[:-1] + x[1:])/2 # Midpoints
y_mid = f(x_mid)
plt.plot(x_mid,y_mid,'b.',markersize=10)
plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
plt.title('Midpoint Riemann Sum, N = {}'.format(N))

plt.subplot(1,3,3)
plt.plot(X,Y,'b')
x_right = x[1:] # Left endpoints
y_right = y[1:]
plt.plot(x_right,y_right,'b.',markersize=10)
plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('Right Riemann Sum, N = {}'.format(N))
fig.savefig("../img/T1/IN-24_calcul_pi.png")
plt.show()

#Let's compute the value of each of the Riemann sums:

dx = (b-a)/N
x_left = np.linspace(a,b-dx,N)
x_midpoint = np.linspace(dx/2,b - dx/2,N)
x_right = np.linspace(dx,b,N)

print("Partition with",N,"subintervals.")
left_riemann_sum = np.sum(f(x_left) * dx)
print("Left Riemann Sum:",left_riemann_sum)

midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
print("Midpoint Riemann Sum:",midpoint_riemann_sum)

right_riemann_sum = np.sum(f(x_right) * dx)
print("Right Riemann Sum:",right_riemann_sum)
'''
Partition with 10 subintervals.
Left Riemann Sum: 3.2399259889071588
Midpoint Riemann Sum: 3.142425985001098
Right Riemann Sum: 3.0399259889071595
'''

'''
la integral entre 0 i 1 de 4/(1+x**2) és 4*arctan(1) = 3.141592653589793 (PI)
'''
I = 4*np.arctan(1) # PI
print("PI = " + str(I)) #3.141592653589793
#print(np.pi) #3.141592653589793
print("Left Riemann Sum Error:",np.abs(left_riemann_sum - I))
print("Midpoint Riemann Sum Error:",np.abs(midpoint_riemann_sum - I))
print("Right Riemann Sum Error:",np.abs(right_riemann_sum - I))
'''
Left Riemann Sum Error: 0.09833333531736566
Midpoint Riemann Sum Error: 0.0008333314113047052
Right Riemann Sum Error: 0.10166666468263363
'''