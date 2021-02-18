# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
# https://www.geeksforgeeks.org/runge-kutta-4th-order-method-solve-differential-equation/
# Python program to implement Runge Kutta method 
# A sample differential equation "dy / dx = (x - y)/2" 

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 RK4_v1.py
'''

import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============


def dydx(x, y): 
    return ((x - y)/2) 
  
# Finds value of y for a given x using step size h 
# and initial value y0 at x0. 
def rungeKutta(x0, y0, x, h): 
    # Count number of iterations using step size or 
    # step height h 
    n = (int)((x - x0)/h)  
    # Iterate for number of iterations 
    y = y0 
    for i in range(1, n + 1): 
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y) 
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1) 
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2) 
        k4 = h * dydx(x0 + h, y + k3) 
  
        # Update next value of y 
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
  
        # Update next value of x 
        x0 = x0 + h 
    return y 
  
# Driver method 
x0 = 0
y = 1
x = 2
h = 0.2
print('The value of y at x is:', rungeKutta(x0, y, x, h) )
