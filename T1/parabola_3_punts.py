# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)

'''
Construcció d'una paràbola a partir de 3 punts (3 punts, polinomi de grau 2)

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 parabola_3_punts.py
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import random

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

punts=[]

while len(punts)<6:
	r=random.randint(1,10)-5
	if r not in punts: punts.append(r)

#print(punts)
print("punts: (" + str(punts[0]) + "," + str(punts[3]) + "), (" + str(punts[1]) + "," + str(punts[4]) + "), (" + str(punts[2]) + "," + str(punts[5]) + ")")

m_list = [[1, punts[0], punts[0]**2], [1, punts[1], punts[1]**2], [1, punts[2], punts[2]**2]]
A = np.array(m_list)
B = np.array([punts[3], punts[4], punts[5]])
X = np.linalg.inv(A).dot(B)
print("Solució: p(x) = " + str(X[2]) + "x^2 + " + str(X[1]) + "x + " + str(X[0]))

def f(x):
    return X[2]*x**2 + X[1]*x + X[0]

x = np.arange(-5.0, 5.0, 0.005)
fig, ax = plt.subplots()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.plot(x, f(x), punts[:3], punts[3:6], 'bo')

ax.set(title='Paràbola a partir de 3 punts')
ax.grid()

fig.savefig("../img/T1/parabola_3_punts.png")
plt.show()
