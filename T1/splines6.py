# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
# https://wwwstaff.ari.uni-heidelberg.de/mitarbeiter/rschmidt/pycourse/html/15.html

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 splines6.py
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

np.random.seed(6)
kinds = ('nearest', 'zero', 'linear', 'slinear', 'quadratic', 'cubic')

N = 10
x = np.linspace(0, 1, N)
y = np.random.randint(10, size=(N,))

new_x = np.linspace(0, 1, 28)
fig, axs = plt.subplots(nrows=len(kinds)+1, sharex=True)
axs[0].plot(x, y, 'bo-')
axs[0].set_title('raw')
for ax, kind in zip(axs[1:], kinds):
    new_y = interpolate.interp1d(x, y, kind=kind)(new_x)
    ax.plot(new_x, new_y, 'ro-')
    ax.set_title(kind)

fig.savefig("../img/T1/splines6.png")
plt.show()

