# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
EDO1-5
https://ca.wikipedia.org/wiki/Equaci%C3%B3_de_la_calor
https://ca.wikipedia.org/wiki/Llei_de_Fick
https://scicomp.stackexchange.com/questions/30839/python-finite-difference-schemes-for-1d-heat-equation-how-to-express-for-loop-u
Equació de la calor
cd /home/joan/UPC_2021/CNED/apunts/python/T2/
PS1="$ "
python3 equacio_calor_v2.py
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============


T0             = np.zeros(50, dtype=float)
T0[17:25]      = 1.

T1             = T0.copy()  # method 1  np.roll()
T2             = T0.copy()  # method 2  convolve()

do_me          = np.ones_like(T0, dtype=bool)
do_me[[0, -1]] = False    #  keep the boundaries of your bounding box fixed

a              = 0.01

hold_1         = [T0.copy()]
for i in range(10001):
    Ttemp      = T1 + a*(np.roll(T1, +1) + np.roll(T1, -1) - 2*T1)
    T1[do_me]  = Ttemp[do_me]
    if not i%1000:
        hold_1.append(T1.copy())

hold_2         = [T0.copy()]
kernel         = np.array([a, (1 - 2.*a), a])

for i in range(10001):
    Ttemp      = convolve(T2, kernel)
    T2[do_me]  = Ttemp[do_me]
    if not i%1000:
        hold_2.append(T2.copy())

if True:
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.title('equació de la calor (difusió)')
    for thing in hold_1:
        plt.plot(thing)

    plt.subplot(1, 2, 2)
    for thing in hold_2:
        plt.plot(thing)

    plt.title('2 mètodes')
    fig = plt.gcf()
    plt.show()
    fig.savefig("../img/T2/EDO1-5_equacio_calor2.png")