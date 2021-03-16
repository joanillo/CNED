# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 Prob_T2_7_regressio.py
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

x = np.array([-4.0, -2.0, 0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([0.0, 0.7, 0.7, 1.9, 2.5, 2.8, 6.3])

model = LinearRegression().fit(x.reshape((-1, 1)), y)

r_sq = model.score(x.reshape((-1, 1)), y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print('recta de regressió: y = ' + str(model.coef_[0]) + '*x + ' + str(model.intercept_) )

def p(x):
    return model.coef_[0] * x + model.intercept_

y_pred = p(x) #valors predits pel model
error_quadratic = np.sum(np.square(y - y_pred))
print("error quadràtic = " + str(error_quadratic)) # aquest és el valor que és mínim

# gràfica
x_ = np.arange(-4.0, 4.0, 0.05)
fig, ax = plt.subplots()
plt.plot(x_, p(x_), x, y, 'bo')
plt.suptitle('Problema 7. Recta de regressió')
plt.title('y = ' + str(round(model.coef_[0],3)) + '*x + ' + str(round(model.intercept_,3)))
ax.grid()
fig.savefig("../img/T1/Prob_T2_7_regressio.png")
plt.show()
