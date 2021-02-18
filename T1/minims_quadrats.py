# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
AF-73: Aproximació per mínims quadrats
*https://unipython.com/ajuste-minimos-cuadrados/
*https://www.iartificial.net/regresion-lineal-con-ejemplos-en-python/

$ pip3 install scikit-learn

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 minims_quadrats.py
'''

import numpy as np
import pylab as plt
from sklearn import linear_model
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

# este es nuestro conjunto de prueba, es solo una línea recta con algun ruido gaussiano
xmin, xmax = -5, 5
n_samples = 100
X = [[i] for i in np.linspace(xmin, xmax, n_samples)]
Y = 2 + 0.5 * np.linspace(xmin, xmax, n_samples) \
      + np.random.randn(n_samples, 1).ravel()
# ejecuta el clasificador
clf = linear_model.LinearRegression()
clf.fit(X, Y)
# plotea los resultados
plt.scatter(X, Y, color='black')
plt.plot(X, clf.predict(X), color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.title('recta de regressió linial (mínims quadrats)')
fig = plt.gcf()
plt.show()
fig.savefig("../img/T1/AF-73_minims_quadrats.png")

print('recta de regressió:')
print ('y = ' + str(clf.coef_) + ' *x + ' + str(clf.intercept_))

# vamos a predecir y = regresion_lineal(0)
nuevo_x = np.array([0]) 
prediccio = clf.predict(nuevo_x.reshape(-1,1))
print('\npredim el valor y(0) = ' + str(prediccio))
