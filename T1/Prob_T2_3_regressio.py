# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T2_3_regressio.py
'''

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

x = np.array([2, 2.5, 3, 3.5, 4])
y = np.array([0.12, 0.11, 0.09, 0.09, 0.08])

model = LinearRegression().fit(x.reshape((-1, 1)), y)

r_sq = model.score(x.reshape((-1, 1)), y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print('recta de regressió: y = ' + str(model.coef_[0]) + '*x + ' + str(model.intercept_) )

def p(x):
    return model.coef_[0] * x + model.intercept_

y_pred = p(x) #valors predits pel model

# gràfica
x_ = np.arange(2.0, 4.0, 0.05)
fig, ax = plt.subplots()
plt.plot(x_, p(x_), x, y, 'bo')
plt.suptitle('Problema 3. Recta de regressió')
plt.title('y = ' + str(round(model.coef_[0],3)) + '*x + ' + str(round(model.intercept_,3)))
ax.grid()
fig.savefig("../img/T1/Prob_T2_3_regressio.png")
plt.show()
