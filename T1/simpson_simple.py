# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
exemple x^2+2x-1 (grau 2), x^3+2x-1 (grau 3), x^3-0.5x^2-3x+2 (grau 3), x^4-x^3-0.5x^2-3x+2 (grau 4)

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 simpson_simple.py
'''

# Lagrange Interpolation

import numpy as np
from scipy.interpolate import lagrange
from scipy import integrate
import matplotlib
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============
print("x^2 + 2*x + 1")
def f1(x):
    return x**2+2*x+1

a=0.0
b=3.0
xm=(a+b)/2 # 1.5
h=b-a

x = np.array([a,b,xm])
y = f1(x)
poly1 = lagrange(x, y) # evidentment el polinomi de Lagrange coincideix amb el nostre polinomi
print(poly1) # x^2 + 2x + 1 

# en aquest cas l'error és 0 perquè Lagrange integra perfectament el nostre polinomi de grau 2
A = h/6*(poly1(a)+4*poly1(xm)+poly1(b))
print("Area (simpson) = " + str(A))
A_analitic = integrate.quad(lambda x: f1(x), 0, 3 ) # integral de x^2+2x+1 entre 0 i 3
print("Area (analític) = " + str(A_analitic[0]))

x_ = np.arange(0, 3.0, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x_, f1(x_),'r',label='x^2+2x+1')
plt.plot(x_, poly1(x_),'g',label='Lagrange')
plt.plot(x, y, 'bo')
ax.legend();
ax.set(title='x^2+2x+1 (grau 2)')
ax.grid()
fig.savefig("../img/T1/simpson_simple_1.png")
plt.show()

print("===============")
print("x^3 + 2*x + 1")
def f2(x):
    return x**3+2*x+1

a=0.0
b=3.0
xm=(a+b)/2 # 1.5
h=b-a

x = np.array([a,b,xm])
y = f2(x)
poly2 = lagrange(x, y) # 4.5 x^2 - 2.5 x + 1
print(poly2) # 4.5 x^2 - 2.5 x + 1

# i en aquest cas també donarà 0, encara que el polinomi de Lagrange és d'ordre 2 i el meu polinomi és d'ordre 3
A = h/6*(poly2(a)+4*poly2(xm)+poly2(b))
print("Area (simpson) = " + str(A))
A_analitic = integrate.quad(lambda x: f2(x), 0, 3 ) # integral de x^3+2x+1 entre 0 i 3
print("Area (analític) = " + str(A_analitic[0]))
print("També dóna un error 0! (superconvergència)")

x_ = np.arange(0, 3.0, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x_, f2(x_),'r',label='x^3+2x+1')
plt.plot(x_, poly2(x_),'g',label='Lagrange')
plt.plot(x, y, 'bo')
ax.legend();
ax.set(title='x^3+2x+1 (grau 3)')
ax.grid()
fig.savefig("../img/T1/simpson_simple_2.png")
plt.show()

print("===============")
print("x^3 - 0.5x^2 - 3x + 2")
def f3(x):
    return x**3 - 0.5*x**2 - 3*x + 2

a=-1.0
b=1.0
xm=(a+b)/2 # 0
h=b-a

x = np.array([a,b,xm])
y = f3(x)
poly3 = lagrange(x, y)
print(poly3) # -0.5 x^2 - 2 x + 2

# i en aquest cas també donarà 0, encara que el polinomi de Lagrange és d'ordre 2 i el meu polinomi és d'ordre 3
A = h/6*(poly3(a)+4*poly3(xm)+poly3(b))
print("Area (simpson) = " + str(A))
A_analitic = integrate.quad(lambda x: f3(x), -1, 1 ) # integral de x^3-1 entre -1 i 1
print("Area (analític) = " + str(A_analitic[0]))
print("També dóna un error 0! (superconvergència)")

x_ = np.arange(-1.0, 1.0, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
#plt.plot(x_, f3(x_),'r',x_, poly3(x_),'g', x, y, 'bo')
plt.plot(x_, f3(x_),'r', label='x^3-0.5x^2-3x+2')
plt.plot(x_, poly3(x_),'g', label='Lagrange')
plt.plot(x, y, 'bo')
ax.legend();
ax.set(title='x^3 - 0.5x^2 - 3x + 2 (grau 3)')
ax.grid()
fig.savefig("../img/T1/simpson_simple_3.png")
plt.show()

print("===============")
print("x^4 - x^3 - 0.5x^2 - 3x + 2 (grau 4)")
def f4(x):
    return x**4 - x**3 - 0.5*x**2 - 3*x + 2

a=-1.0
b=1.0
xm=(a+b)/2 # 0
h=b-a

x = np.array([a,b,xm])
y = f4(x)
poly4 = lagrange(x, y)
print(poly4) # 0.5 x^2 - 4 x + 2

# i en aquest cas també donarà 0, encara que el polinomi de Lagrange és d'ordre 2 i el meu polinomi és d'ordre 3
A = h/6*(poly4(a)+4*poly4(xm)+poly4(b))
print("Area (simpson) = " + str(A))
A_analitic = integrate.quad(lambda x: f4(x), -1, 1 ) # integral de x^3-1 entre -1 i 1
print("Area (analític) = " + str(A_analitic[0]))
print("Polinomi de grau 4. Ara l'error és > 0")

x_ = np.arange(-1.0, 1.0, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x_, f4(x_),'r', label='x^4-x^3-0.5x^2-3x+2')
plt.plot(x_, poly4(x_),'g', label='Lagrange')
plt.plot(x, y, 'bo')
ax.legend();
ax.set(title='x^4-x^3-0.5x^2-3x+2 (grau 4)')
ax.grid()
fig.savefig("../img/T1/simpson_simple_4.png")
plt.show()
