# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 splines5.py
'''
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

x = np.arange(0, 10)
y = np.exp(-x/3.0)
f = interpolate.interp1d(x, y, kind=3)

xnew = np.arange(0, 9)
ynew = f(xnew)   # use interpolation function returned by `interp1d`

fig, ax = plt.subplots()
plt.plot(x, y, 'o', xnew, ynew, '-')
fig.savefig("../img/T1/splines5.png")
plt.show()
