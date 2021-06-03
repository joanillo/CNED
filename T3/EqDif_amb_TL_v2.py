# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Resolució d'una equació diferencials amb Transformades de Laplace
Exemple: y'' + 3y' + 2y = 0; CI: y(0)=2, y'(0)=-3
*https://notebook.community/relopezbriega/mi-python-blog/content/notebooks/ecuaciones-diferenciales-en
*https://github.com/sympy/sympy/issues/17094

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 EqDif_amb_TL_v2.py
'''

import sympy
import numpy as np
import matplotlib.pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

# la definció de laplace_transform_derivatives() l'agafem de https://github.com/sympy/sympy/issues/17094,
# que difereix en una línia de la versió que tenim en el notebook i que fa que no funcioni
def laplace_transform_derivatives(e):
    """
    Evaluate the unevaluted laplace transforms of derivatives
    of functions
    """
    if isinstance(e, sympy.LaplaceTransform):
        if isinstance(e.args[0], sympy.Derivative):
            d, t, s = e.args
            n = d.args[1][1]
            #n = len(d.args) - 1
            return ((s**n) * sympy.LaplaceTransform(d.args[0], t, s) -
                     sum([s**(n-i) * sympy.diff(d.args[0], t, i-1).subs(t, 0) for i in range(1, n+1)]))
    if isinstance(e, (sympy.Add, sympy.Mul)):
        t = type(e)
        return t(*[laplace_transform_derivatives(arg) for arg in e.args])
    return e

print("\ny\'\' + 3y\' + 2y = 0")
print("CI: y(0) = 2,  y\'(0) = -3")

# Definim les incògnites
t = sympy.symbols("t", positive=True)
y = sympy.Function("y")

# símbols addicionals
s, Y = sympy.symbols("s, Y", real=True)

# definim l'equació diferencial
edo = y(t).diff(t, t) + 3*y(t).diff(t) + 2*y(t)
print()
print(sympy.Eq(edo,0))

# Transformada de Laplace 
L_edo = sympy.laplace_transform(edo, t, s, noconds=True)
L_edo_2 = laplace_transform_derivatives(L_edo)

print(L_edo)
#print(L_edo_2)

# reemplacem la transfomada de Laplace de y(t) per la incògnita Y per facilitar la lectura de l'equació.
L_edo_3 = L_edo_2.subs(sympy.laplace_transform(y(t), t, s), Y)
print("\nJa tenim una equació algebraica:")
print(sympy.Eq(L_edo_3,0))

# Definim les condicions inicials
print("\nCondicions inicials:")
ics = {y(0): 2, y(t).diff(t).subs(t, 0): -3}
print(ics)

# Apliquem les condicions inicials
L_edo_4 = L_edo_3.subs(ics)

# Resolem l'equació algebraica en el domini de la freqüència
Y_sol = sympy.solve(L_edo_4, Y)
print("\nSolució Laplace:")
print(Y_sol)

# Calculem la TLI per tornar al domini del temps, i així obtenir la solució de l'Eq diferencial:
y_sol = sympy.inverse_laplace_transform(Y_sol[0], s, t)
print("\nSolució Eq Dif:")
print(y_sol) # (exp(t) + 1)*exp(-2*t)

print("\nComprovem la solució (substituïm les CI)")
print(y_sol.subs(t, 0), sympy.diff(y_sol).subs(t, 0))

# ==========================================================
# representació gràfica
tp = np.linspace(0, 4, 100)
#yp = (np.exp(tp) + 1)*np.exp(-2*tp)
# NOTA: aquesta és la manera de convertir la solució que he trobat a una funció executable
y_sol_f = sympy.lambdify(t, y_sol)
yp = y_sol_f(tp)


plt.plot(tp,yp,'b',linewidth=2)
plt.xlabel('time')
plt.ylabel('y(t)')
fig = plt.gcf()
plt.suptitle('y\'\' + 3y\' + 2y = 0; CI: y(0)=2, y\'(0)=-3', fontsize=12)
plt.title('SOL: (e^t + 1)*e^(-2*t)', fontsize=12)

plt.show()
fig.savefig("../img/T3/EqDif_amb_TL_v2.png")
