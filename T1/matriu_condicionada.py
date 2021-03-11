# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Matriu condicionada i no condicionada (intersecció de dues rectes)

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 matriu_condicionada.py
'''

# Lagrange Interpolation

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

# matriu mal condicionada
print("Matriu mal condicionada")
# x + 2y = 3
# 2x + 3.99y = 5
MMC1 = np.array([[1, 2],
               [2, 3.99]])

B = np.array([3, 5])

#número de condició
# cond = np.linalg.cond(MMC1)
# cond = np.linalg.norm(MMC1)*np.linalg.norm(np.linalg.inv(MMC1))
cond = np.linalg.cond(MMC1, p='fro')
print("Núm de condició MMC1: " + str(cond))

MMC2 = np.array([[1.001, 2.001],
               [2.001, 3.998]])

#número de condició
cond = np.linalg.cond(MMC2, p='fro')
print("Núm de condició MMC2: " + str(cond))

# matriu ben condicionada
print("\nMatriu ben condicionada")
# -x + y = 3
# 2x - y = 5
MBC1 = np.array([[-1, 1],
               [2, -1]])

#número de condició
cond = np.linalg.cond(MBC1, p='fro')
print("Núm de condició MBC1: " + str(cond))

MBC2 = np.array([[-1.001, 1.001],
               [2.001, -1.001]])

#número de condició
cond = np.linalg.cond(MBC2, p='fro')
print("Núm de condició MBC2: " + str(cond))

# solucions ====================
# MMC1
XMMC1 = np.linalg.inv(MMC1).dot(B)
print("\nSolució MMC1: (" + str(XMMC1[0]) + ", " + str(XMMC1[1]) + ")")

# MMC2
XMMC2 = np.linalg.inv(MMC2).dot(B)
print("Solució MMC2: (" + str(XMMC2[0]) + ", " + str(XMMC2[1]) + ")")

# MBC1
XMBC1 = np.linalg.inv(MBC1).dot(B)
print("\nSolució MBC1: (" + str(XMBC1[0]) + ", " + str(XMBC1[1]) + ")")
# MBC2
XMBC2 = np.linalg.inv(MBC2).dot(B)
print("Solució MBC2: (" + str(XMBC2[0]) + ", " + str(XMBC2[1]) + ")")

def f11(x):
    return (3+1.0*x)/1.0

def f12(x):
    return (2.0*x-5)/1.0

def f21(x):
    return (3+1.001*x)/1.001

def f22(x):
    return (2.001*x-5)/1.001

x = np.arange(7.99, 8.01, 0.005)
fig, ax = plt.subplots()
#plt.axhline(0, color='black')
#plt.axvline(0, color='black')
plt.plot(x, f11(x),x, f12(x), x, f21(x),x, f22(x))

ax.set(title='Matriu ben condicionada (intersecció de rectes)')
ax.grid()

fig.savefig("../img/T1/matriu_ben_condicionada.png")
plt.show()
