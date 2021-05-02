# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
y' = ty
y(0) = 1

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-99.py 
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

def dydt(t, y): 
    return t*y
  
# Finds value of y for a given x using step size h 
# and initial value y0 at x0. 
def rungeKutta(t0, y0, t, h): 
    # Count number of iterations using step size or 
    # step height h 
    n = (int)((t - t0)/h)  
    # Iterate for number of iterations 
    y = y0 
    for i in range(1, n + 1): 
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydt(t0, y) 
        k2 = h * dydt(t0 + 0.5 * h, y + 0.5 * k1) 
        k3 = h * dydt(t0 + 0.5 * h, y + 0.5 * k2) 
        k4 = h * dydt(t0 + h, y + k3) 
  
        # Update next value of y 
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
        print("Pas ",i," (t=",t0+h,"): ", y)
  
        # Update next value of x 
        t0 = t0 + h 
    return y 
  
# Driver method 
t0 = 0
y = 1
t = 1
h = 0.2
print("h = ",h)
print("\nPas inicial (t=",t0,"): ", y)
print("Valor final:", rungeKutta(t0, y, t, h) )

h = 0.1
print("h = ",h)
print("\nPas inicial (t=",t0,"): ", y)
print("Valor final:", rungeKutta(t0, y, t, h) )
