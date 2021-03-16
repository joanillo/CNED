# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
AF-73: Regressió exponencial. Simulació de la descàrrega del condensador
La regressió exponencial es fa treient logaritmes als dos costats, i aleshores és una regressió lineal
V = Vo * exp(-t/RC)

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 regressio_exponencial.py
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

# descàrrega del condensador
vo = 5 # volts
R = 10 # Kohm
C = 1 # mF

t = np.linspace(0, 50, 10)
v_or = vo * np.exp(-t/(R*C))
noise = np.random.normal(0, .05, 10) # simulem dades experimentals
v = v_or + noise
v_log = np.log(v) # treiem el logaritme de les dades

# ajustament a una recta
z = np.polyfit(t, v_log, 1)
print(z)
print("Equació de la descàrrega:")
print("log(V) = log(Vo) - (1/RC)*t")
print("log(V) = " +  str(round(z[1],3)) + " " + str(round(z[0],3)) + "*t")
print("V = Vo * exp (-t/RC)")
print("V = " + str(round(np.exp(z[1]),3)) + " * exp(" + str(round(z[0],3)) + "*t)")

t_ = np.linspace(0, 50, 500)
v_ = np.exp(z[1])*np.exp(z[0]*t_)

fig, ax = plt.subplots()
plt.plot(t_, v_, t, v, 'bo')
plt.suptitle("Descàrrega del condensador. Regressió exponencial")
plt.title("V = " + str(round(np.exp(z[1]),3)) + " * exp(" + str(round(z[0],3)) + "*t)")
ax.set(xlabel='temps (s)', ylabel='Volts (V)')
ax.grid()

fig.savefig("../img/T1/regressio_exponencial.png")
plt.show()
