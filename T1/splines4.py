# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
# https://wwwstaff.ari.uni-heidelberg.de/mitarbeiter/rschmidt/pycourse/html/15.html

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 splines4.py
'''

from scipy.interpolate import interp1d
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

x = np.array([0., 1., 3., 4.])
y = np.array([0., 4., 2.7, 2.08])

f = interp1d(x,y) #per defecte és interpolació lineal

# i ara ja podem interpolar
print(f(0.5))
print(f(3.3))
print(f(np.array([0.5, 1.5, 2.5, 3.5])))
#If the interpolating function is called outside the original range, an error is raised:
#f(-1.)

#By default, interp1d uses linear interpolation, but it is also possible to use e.g. cubic spline interpolation:
f = interp1d(x, y, kind='cubic') #cubic spline interpolation
print(f(0.5))


xp=np.arange(0,4,0.1)
print(xp)

f = interp1d(x,y)
g = interp1d(x,y,kind=2) # equivalent to 'quadratic'
h = interp1d(x,y,kind=3)  # equivalen to 'cubic'

fig, ax = plt.subplots()
plt.plot(x, y, 'bo', xp,f(xp),xp,g(xp),xp,h(xp))
plt.xlim(0,6)
plt.legend(['linear','quadratic spline','cubic spline'])
plt.show()
fig.savefig("../img/T1/splines4.png")
