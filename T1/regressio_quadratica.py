# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
AF-73: Regressió quadràtic. Simulació del tir parabòlic

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 regressio_quadratica.py
'''

import numpy as np
import pylab as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

# tir parabòlic: y = vy*t - .5gt^2
vy = 10 # 10m/s
g = 9.81 # m/s^2
t_max = 2*vy/g

t = np.linspace(0, t_max, 10)
y_or = vy*t - .5*g*t**2
noise = np.random.normal(0, .3, 10) # simulem dades experimentals
y = y_or + noise

# ajustament a una paràbola
z = np.polyfit(t, y, 2)
print(z)
print("Equació del moviment:")
print("y = " + str(round(z[0],3)) + "t^2 + " + str(round(z[1],3)) + "t + " + str(round(z[2],3)))
g_exp = 2.0*z[0]
print("g experimental = " + str(round(g_exp,3)) + " m/s^2")

t_ = np.linspace(0, t_max, 100)
y_ = z[0]*t_**2 + z[1]*t_ + z[2]

fig, ax = plt.subplots()
plt.plot(t_, y_, t, y, 'bo')
plt.suptitle("Tir parabòlic. Regressió quadràtica")
plt.title("y = " + str(round(z[0],3)) + "t^2 + " + str(round(z[1],3)) + "t + " + str(round(z[2],3)) + " -> g exp = " + str(round(g_exp,3)) + " m/s^2")
ax.set(xlabel='temps (s)', ylabel='y (m)')
ax.grid()

fig.savefig("../img/T1/regressio_quadratica.png")
plt.show()
