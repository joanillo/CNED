# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
AF-78: Exercici proposat. Aproximació per mínims quadrats (regressió lineal)
$ pip3 install scikit-learn

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 AF-78-regressio_lineal.py
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

x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0])
y = np.array([0.36, 0.25, 0.59, 1.07, 0.90, 1.37])

model = LinearRegression().fit(x.reshape((-1, 1)), y)

r_sq = model.score(x.reshape((-1, 1)), y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print('recta de regressió: y = ' + str(model.coef_[0]) + '*x + ' + str(model.intercept_) )

def p(x):
    return model.coef_[0] * x + model.intercept_

# error quadràtic i error quadràtic mig (MSE, mean square error)
#https://www.iartificial.net/error-cuadratico-medio-para-regresion/
y_pred = p(x) #valors predits pel model

'''
error_quadratic = np.sum(np.square(y - y_pred))
error_quadratic_mitja = error_quadratic / len(x)
print(error_quadratic)
print(error_quadratic_mitja)
'''
mse = (np.square(y - y_pred)).mean() #error quadràtic mitjà, mean square error
print("MSE = " + str(mse))
rmse = np.sqrt(mse) # root mean square error
print("RMSE = " + str(rmse))

# gràfica
x_ = np.arange(0.0, 1.2, 0.05)
fig, ax = plt.subplots()
plt.plot(x_, p(x_), x, y, 'bo')
plt.suptitle('AF-78. Recta de regressió')
plt.title('y = ' + str(round(model.coef_[0],3)) + '*x + ' + str(round(model.intercept_,3)))
ax.grid()
fig.savefig("../img/T1/AF-78-recta_regressio.png")
plt.show()
