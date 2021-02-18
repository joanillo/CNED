# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Dent de serra (SF-59, SF-63)

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 dent_de_serra.py
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

time_vec = np.linspace(-6, 6, 100)

y1 = 4/np.pi*np.sin(np.pi*time_vec/2)

fig, ax = plt.subplots()
plt.plot(time_vec, y1)
ax.set(xlabel='-L a L', ylabel='', title='Dent de serra (SF-59)')
ax.grid()
plt.show()

y2 = 4/(np.pi)*np.sin(np.pi*time_vec/2) - 4/(2*np.pi)*np.sin(2*np.pi*time_vec/2)

fig, ax = plt.subplots()
plt.plot(time_vec, y2)
ax.set(xlabel='-L a L', ylabel='', title='Dent de serra (SF-59)')
ax.grid()
plt.show()

y3 = 4/(np.pi)*np.sin(np.pi*time_vec/2) - 4/(2*np.pi)*np.sin(2*np.pi*time_vec/2) + 4/(3*np.pi)*np.sin(3*np.pi*time_vec/2)

fig, ax = plt.subplots()
plt.plot(time_vec, y3)
ax.set(xlabel='-L a L', ylabel='', title='Dent de serra (SF-59)')
ax.grid()
plt.show()

y6 = 4/(np.pi)*np.sin(np.pi*time_vec/2) - 4/(2*np.pi)*np.sin(2*np.pi*time_vec/2) + 4/(3*np.pi)*np.sin(3*np.pi*time_vec/2) - 4/(4*np.pi)*np.sin(4*np.pi*time_vec/2) + 4/(5*np.pi)*np.sin(5*np.pi*time_vec/2) - 4/(6*np.pi)*np.sin(6*np.pi*time_vec/2) 

fig, ax = plt.subplots()
plt.plot(time_vec, y6)
ax.set(xlabel='-L a L', ylabel='', title='Dent de serra (SF-59)')
ax.grid()
plt.show()

y10 = 4/(np.pi)*np.sin(np.pi*time_vec/2) - 4/(2*np.pi)*np.sin(2*np.pi*time_vec/2) + 4/(3*np.pi)*np.sin(3*np.pi*time_vec/2) - 4/(4*np.pi)*np.sin(4*np.pi*time_vec/2) + 4/(5*np.pi)*np.sin(5*np.pi*time_vec/2) - 4/(6*np.pi)*np.sin(6*np.pi*time_vec/2) + 4/(7*np.pi)*np.sin(7*np.pi*time_vec/2) - 4/(8*np.pi)*np.sin(8*np.pi*time_vec/2) + 4/(9*np.pi)*np.sin(9*np.pi*time_vec/2) - 4/(10*np.pi)*np.sin(10*np.pi*time_vec/2) 

fig, ax = plt.subplots()
plt.plot(time_vec, y10)
ax.set(xlabel='-L a L', ylabel='', title='Dent de serra (SF-59)')
ax.grid()
plt.show()

fig, ax = plt.subplots()
plt.plot(time_vec, y1,time_vec, y2,time_vec, y3,time_vec, y6,time_vec, y10)
ax.set(xlabel='-L a L', ylabel='', title='Dent de serra (SF-59)')
ax.grid()
plt.show()
fig.savefig("../img/T3/SF-59_dent_de_serra.png")

