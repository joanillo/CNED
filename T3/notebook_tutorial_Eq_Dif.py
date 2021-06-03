# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
https://relopezbriega.github.io/blog/2016/01/10/ecuaciones-diferenciales-con-python/

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 notebook_tutorial_Eq_Dif.py
'''

import sympy
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

# Resolviendo ecuación diferencial
# defino las incognitas
x = sympy.Symbol('x')
y = sympy.Function('y')

# expreso la ecuacion
f = 6*x**2 - 3*x**2*(y(x))
print()
print(sympy.Eq(y(x).diff(x), f))

# Resolviendo la ecuación
sol = sympy.dsolve(y(x).diff(x) - f)
print()
print(sol)

# definiendo la ecuación
eq = 1.0/2 * (y(x)**2 - 1)

# Condición inicial
ics = {y(0): 2}

# Resolviendo la ecuación
edo_sol = sympy.dsolve(y(x).diff(x) - eq)
print()
print(edo_sol)

C_eq = sympy.Eq(edo_sol.lhs.subs(x, 0).subs(ics), edo_sol.rhs.subs(x, 0))
print()
print(C_eq)
sol = sympy.solve(C_eq)
print()
print(sol)

# Solución con serie de potencias
f = y(x)**2 + x**2 -1
sol = sympy.dsolve(y(x).diff(x) - f)
print()
print(sol)


# camps de direccions ==========================

def plot_direction_field(x, y_x, f_xy, x_lim=(-5, 5), y_lim=(-5, 5), ax=None):
    """Esta función dibuja el campo de dirección de una EDO"""
    
    f_np = sympy.lambdify((x, y_x), f_xy, modules='numpy')
    x_vec = np.linspace(x_lim[0], x_lim[1], 20)
    y_vec = np.linspace(y_lim[0], y_lim[1], 20)
    
    if ax is None:
        _, ax = plt.subplots(figsize=(4, 4))
    
    dx = x_vec[1] - x_vec[0]
    dy = y_vec[1] - y_vec[0]
    
    for m, xx in enumerate(x_vec):
        for n, yy in enumerate(y_vec):
            Dy = f_np(xx, yy) * dx
            Dx = 0.8 * dx**2 / np.sqrt(dx**2 + Dy**2)
            Dy = 0.8 * Dy*dy / np.sqrt(dx**2 + Dy**2)
            ax.plot([xx - Dx/2, xx + Dx/2],
                    [yy - Dy/2, yy + Dy/2], 'b', lw=0.5)
    
    ax.axis('tight')
    ax.set_title(r"$%s$" %
                 (sympy.latex(sympy.Eq(y(x).diff(x), f_xy))),
                 fontsize=18)
    
    return ax

# Defino incognitas
x = sympy.symbols('x')
y = sympy.Function('y')

# Defino la función
f = y(x)**2 + x**2 -1

# grafico de campo de dirección
fig, axes = plt.subplots(1, 1, figsize=(8, 6))
campo_dir = plot_direction_field(x, y(x), f, ax=axes)
plt.show()

# Condición inicial
ics = {y(0): 0}

# Resolviendo la ecuación diferencial
edo_sol = sympy.dsolve(y(x).diff(x) - f, ics=ics)
print()
print(edo_sol)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# panel izquierdo - solución aproximada por Serie de potencias
plot_direction_field(x, y(x), f, ax=axes[0])
x_vec = np.linspace(-3, 3, 100)
axes[0].plot(x_vec, sympy.lambdify(x, edo_sol.rhs.removeO())(x_vec),'b', lw=2)

# panel derecho - Solución por método iterativo
plot_direction_field(x, y(x), f, ax=axes[1])
x_vec = np.linspace(-1, 1, 100)
axes[1].plot(x_vec, sympy.lambdify(x, edo_sol.rhs.removeO())(x_vec),'b', lw=2)

# Resolviendo la EDO en forma iterativa 
edo_sol_m = edo_sol_p = edo_sol
dx = 0.125

# x positivos
for x0 in np.arange(1, 2., dx):
    x_vec = np.linspace(x0, x0 + dx, 100)
    ics = {y(x0): edo_sol_p.rhs.removeO().subs(x, x0)}
    edo_sol_p = sympy.dsolve(y(x).diff(x) - f, ics=ics, n=6)
    axes[1].plot(x_vec, sympy.lambdify(x, edo_sol_p.rhs.removeO())(x_vec),'r', lw=2)

# x negativos
for x0 in np.arange(1, 5, dx):
    x_vec = np.linspace(-x0-dx, -x0, 100)
    ics = {y(-x0): edo_sol_m.rhs.removeO().subs(x, -x0)}
    edo_sol_m = sympy.dsolve(y(x).diff(x) - f, ics=ics, n=6)
    axes[1].plot(x_vec, sympy.lambdify(x, edo_sol_m.rhs.removeO())(x_vec),'r', lw=2)

plt.show()