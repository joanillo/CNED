# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Sistema trigonomètric ortogonal (SF-14)

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 sistema_trigonometric_ortogonal.py
'''

import numpy as np
from matplotlib import pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

time_vec = np.linspace(-np.pi, np.pi, 100)

y1 = np.sin(time_vec) # sin(x)
y2 = np.sin(2*time_vec) # sin(2x)

fig, ax = plt.subplots()
plt.plot(time_vec, y1, time_vec, y2)

ax.set(xlabel='alpha', ylabel='', title='sin(x) i sin(2x) són ortogonals respecte el producte escalar integral')
ax.grid()

fig.savefig("../img/T3/SF-14_sistema_trigonometric_ortogonal.png")
plt.show()
