# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-23: solució amb sympy d'una Eq diferencial, i un cas particular de CI
https://12000.org/my_notes/faq/sympy_python/index.htm

cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 odeint_pvi.py
'''

import sympy as sp
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

x   = sp.symbols('x')
y   = sp.Function('y')

print('\nExemple 1: y\'=1+2x')
ode = sp.Eq(sp.Derivative(y(x),x),1+2*x)
sol = sp.dsolve(ode,y(x))
print(sol) # Eq(y(x), C1 + x**2 + x)
sp.checkodesol(ode,sol)
#    (True, 0)
if sp.checkodesol(ode,sol)[0]==True:
   print ('verified solution OK')

# solució amb PVI:
print('CI: y(0)=3')
sol = sp.dsolve(ode,y(x),ics={y(0):3})
print(sol) # Eq(y(x), x**2 + x + 3)
#print(sp.latex(sol)) # printem en format LaTeX
print(sp.checkodesol(ode,sol)) #(True, 0)


print('\nExemple 2: y\'= y')
ode = sp.Eq(sp.Derivative(y(x),x),y(x))
sol = sp.dsolve(ode,y(x))
print(sol) # Eq(y(x), C1 + x**2 + x)
print(sp.checkodesol(ode,sol)) #(True, 0)

# solució amb PVI:
print('CI: y(0)=1')
sol = sp.dsolve(ode,y(x),ics={y(0):1})
print(sol) # Eq(y(x), x**2 + x + 3)
#print(sp.latex(sol)) # printem en format LaTeX
print(sp.checkodesol(ode,sol)) #(True, 0)
