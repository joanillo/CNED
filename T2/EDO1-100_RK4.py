# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-100: comparem la solució numèrica (~exacta), amb Eules i RK-4, i mirem la convergència
y' = ty
y(0) = 1

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 EDO1-100_RK4.py 
'''

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

t   = sp.symbols('t')
y   = sp.Function('y')

ode = sp.Eq(sp.Derivative(y(t),t),t*y(t))
sol = sp.dsolve(ode,y(t))
print("Solució exacta:")
print(sol) # Eq(y(t), C1*exp(t**2/2))
# solució amb PVI:
print('\nCI: y(0)=1')
sol = sp.dsolve(ode,y(t),ics={y(0):1})
print(sol) # Eq(y(t), exp(t**2/2))

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
        print("Pas ",i," (t=",np.round_(t0+h,2),"): ", y)
  
        # Update next value of x 
        t0 = t0 + h 
    return y 
  
# Driver method 
t0 = 0
y = 1
t = 1
h = 0.2
print("\nh = ",h)
print("Pas inicial (t=",np.round_(t0,2),"): ", y)
valor_final_N5 = rungeKutta(t0, y, t, h)
print("Valor final (N=5): ", valor_final_N5 )
error_final_N5 = np.abs(valor_final_N5 - np.exp(1**2/2))
print("Error final (N=5): ", error_final_N5)

h = 0.1
print("\nh = ",h)
print("Pas inicial (t=",np.round_(t0,2),"): ", y)
valor_final_N10 = rungeKutta(t0, y, t, h)
print("Valor final (N=10):", valor_final_N10 )
error_final_N10 = np.abs(valor_final_N10 - np.exp(1**2/2))
print("Error final (N=10): ", error_final_N10)

print("\nQuocient errors N=5/N=10: ", error_final_N5/error_final_N10)
print("L'error ha quedat dividit aproximadament per 16, que demostra que RK-4 és d'ordre 4.")
