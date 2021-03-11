# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
polinomis de Lagrange. Exemple: donats 3 punts, trobem el polinomi de grau 2 (paràbola), pel mètode de Lagrange
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 lagrange1.py 
'''

from scipy.interpolate import lagrange
import numpy as np
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


x_or = np.array([0, 1, 2])
#y_or=x**3 
y_or = np.array([0, 1, 8])
poly = lagrange(x_or, y_or)
print("punts: (" + str(x_or[0]) + "," + str(y_or[0]) + "), (" + str(x_or[1]) + "," + str(y_or[1]) + "), (" + str(x_or[2]) + "," + str(y_or[2]) + ")")
print('solució')
print(poly)
'''
   2
3 x - 2 x
'''

x = np.arange(-3.0, 3.0, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x, poly(x), x_or, y_or, 'bo')
#plt.plot(x, f(x), punts[:3], punts[3:6], 'bo')

ax.set(title='Paràbola a partir de 3 punts (Lagrange)')
ax.grid()

fig.savefig("../img/T1/lagrange1.png")
plt.show()
