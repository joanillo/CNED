# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
polinomis de Lagrange. Exemple
https://www.codesansar.com/numerical-methods/python-program-lagrange-interpolation-method.htm

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 lagrange2.py

Exemple AF-44: f(-2)=3, f(-1)=1, f(2)=-1 i f(4)=3 
Enter number of data points: 4
Enter data for x and y: 
x[0]=-2
y[0]=3
x[1]=-1
y[1]=1
x[2]=2
y[2]=-1
x[3]=4
y[3]=3
Enter interpolation point: 0
Interpolated value at 0.000 is -0.467.
'''

# Lagrange Interpolation

# Importing NumPy Library
import numpy as np
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

# Reading number of unknowns
n = int(input('Enter number of data points: (per ex: -2, 3, -1, 1, 2, -1, 4, 3)'))

# Making numpy array of n & n x n size and initializing 
# to zero for storing x and y value along with differences of y
x = np.zeros((n))
y = np.zeros((n))


# Reading data points
print('Enter data for x and y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))


# Reading interpolation point
xp = float(input('Enter interpolation point: '))

# Set interpolated value initially to zero
yp = 0

# Implementing Lagrange Interpolation
for i in range(n):
    
    p = 1
    
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    
    yp = yp + p * y[i]    

# Displaying output
print('Interpolated value at %.3f is %.3f.' % (xp, yp))

#f(-2)=3, f(-1)=1, f(2)=-1 i f(4)=3 
from scipy.interpolate import lagrange
x = np.array([-2, -1, 2, 4])
y = np.array([3, 1, -1, 3])
poly = lagrange(x, y)
print(poly) # 0.03333 x^3 + 0.3667 x^2 - 1.133 x - 0.4667
