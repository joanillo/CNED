# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-15: Predator-prey equation
https://sam-dolan.staff.shef.ac.uk/mas212/notebooks/ODE_Example.html
cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 odeint_v4.py
'''

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============


def dP_dt(P, t):
    return [P[0]*(a - b*P[1]), -P[1]*(c - d*P[0])]

a,b,c,d = 1,1,1,1

ts = np.linspace(0, 12, 100)
P0 = [1.5, 1.0]
Ps = odeint(dP_dt, P0, ts)
prey = Ps[:,0]
predators = Ps[:,1]

plt.plot(ts, prey, "+", label="Rabbits")
plt.plot(ts, predators, "x", label="Foxes")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend();
plt.title('dinàmica de poblacions (conills vs guineus)')
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/predator_prey1.png")

ic = np.linspace(1.0, 3.0, 21)
for r in ic:
    P0 = [r, 1.0]
    Ps = odeint(dP_dt, P0, ts)
    plt.plot(Ps[:,0], Ps[:,1], "-")
plt.xlabel("Rabbits")
plt.ylabel("Foxes")
plt.title("Rabbits vs Foxes");
fig = plt.gcf()
plt.show()
fig.savefig("../img/T2/EDO1-15_predator_prey2.png")

