# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
# https://wwwstaff.ari.uni-heidelberg.de/mitarbeiter/rschmidt/pycourse/html/15.html

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 splines7.py
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
#kinds = ('nearest', 'zero', 'linear', 'slinear', 'quadratic', 'cubic')
kinds = ('linear', 'quadratic', 'cubic')

N = 10
x = np.linspace(0, 1, N)
y = np.random.randint(10, size=(N,))

new_x = np.linspace(0, 1, 58)

new_y_lin = interpolate.interp1d(x, y, kind=1)(new_x)
new_y_quad = interpolate.interp1d(x, y, kind=2)(new_x)
new_y_cub = interpolate.interp1d(x, y, kind=3)(new_x)

fig, ax = plt.subplots()
plt.plot(x, y, 'bo',new_x, new_y_lin, 'r',new_x, new_y_quad, 'g',new_x, new_y_cub, 'y')
plt.legend(['raw','linear','quadratic spline','cubic spline'])

#plt.plot(x, y, 'bo',new_x,new_y_quad, 'g',new_x, new_y_cub, 'y')
#plt.legend(['raw','quadratic spline','cubic spline'])

fig.savefig("../img/T1/splines7.png")
plt.show()