# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Integració numèrica, Problema 1
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T3_1.py
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

f = lambda x : x**3 - 6*x**2 + 12*x + 2 #x^3-6x^2+12x+2
a = 0; b = 3

'''
la integral entre 0 i 3 de x^3-6x^2+12x+2 és 6720/256 = 26,25
'''
I = 26.25
print("\nValor exacte = 26.25")

#Let's compute the value of each of the Riemann sums:
N = 6
dx = (b-a)/N
x_left = np.linspace(a,b-dx,N)
x_right = np.linspace(dx,b,N)

print("\nPartition with",N,"subintervals.")
left_riemann_sum = np.sum(f(x_left) * dx)
print("Left Riemann Sum:",left_riemann_sum)

right_riemann_sum = np.sum(f(x_right) * dx)
print("Right Riemann Sum:",right_riemann_sum)

print("Error Left Riemann Sum:",np.abs(left_riemann_sum - I))
print("Error Right Riemann Sum:",np.abs(right_riemann_sum - I))

# ---
N=12
dx = (b-a)/N
x_left = np.linspace(a,b-dx,N)
x_right = np.linspace(dx,b,N)

print("\nPartition with",N,"subintervals.")
left_riemann_sum = np.sum(f(x_left) * dx)
print("Left Riemann Sum:",left_riemann_sum)

right_riemann_sum = np.sum(f(x_right) * dx)
print("Right Riemann Sum:",right_riemann_sum)

print("Error Left Riemann Sum:",np.abs(left_riemann_sum - I))
print("Error Right Riemann Sum:",np.abs(right_riemann_sum - I))

n = 50 # Use n*N+1 points to plot the function smoothly
x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b,n*N+1)
Y = f(X)

fig, ax = plt.subplots(figsize=(15,5))

plt.subplot(1,2,1)
plt.plot(X,Y,'b')
x_left = x[:-1] # Left endpoints
y_left = y[:-1]
plt.plot(x_left,y_left,'b.',markersize=10)
plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('x^3-6x^2+12x+2. Aprox rectangular, N = {}'.format(N))

plt.subplot(1,2,2)
plt.plot(X,Y,'b')
x_right = x[1:] # Right endpoints
y_right = y[1:]
plt.plot(x_right,y_right,'b.',markersize=10)
plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
plt.title('x^3-6x^2+12x+2. Aprox rectangular, N = {}'.format(N))

fig.savefig("../img/T1/Prob_T3_1.png")
plt.show()