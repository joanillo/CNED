# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)
'''
Laplace Transform amb Sympy
*https://dynamics-and-control.readthedocs.io/en/latest/1_Dynamics/3_Linear_systems/Laplace%20transforms.html

cd /home/joan/UPC_2021/CNED/apunts/python/T3/
PS1="$ "
python3 laplace_transform_sympy.py
'''

import sympy
from matplotlib import pyplot as plt
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

sympy.init_printing()

#Letss define some symbols to work with.
t, s = sympy.symbols('t, s')
a = sympy.symbols('a', real=True, positive=True)

#20.1. Direct evaluation
#We start with a simple function
f = sympy.exp(-a*t)
print(f) # e−at

#We can evaluate the integral directly using integrate:
res = sympy.integrate(f*sympy.exp(-s*t), (t, 0, sympy.oo))
print(res)

#20.2. Library function
#This works, but it is a bit cumbersome to have all the extra stuff in there.

#Sympy provides a function called laplace_transform which does this more efficiently. By default it will return conditions of convergence as well (recall this is an improper integral, with an infinite bound, so it will not always converge).
res = sympy.laplace_transform(f, t, s)
print(res) #(1a+s, 0, True)
#If we want just the function, we can specify noconds=True.
F = sympy.laplace_transform(f, t, s, noconds=True)
print(F) #1a+s

# We will find it useful to define a quicker version of this:
def L(f):
    return sympy.laplace_transform(f, t, s, noconds=True)
res = L(f)
print(res)

#Inverses are simple as well,
def invL(F):
    return sympy.inverse_laplace_transform(F, s, t)

res = invL(F)
print(res) #e−atθ(t)


#20.3. What is that θ?
#The unit step function is also known as the Heaviside step function. We will see this function often in inverse laplace transforms. It is typeset as θ(t) by sympy.

print(sympy.Heaviside(t)) # θ(t)

sympy.plot(sympy.Heaviside(t));

#Look at the difference between f and the inverse laplace transform we obtained, which contains the unit step to force it to zero before t=0.
res = invL(F).subs({a: 2})
print(res) # e−2tθ(t)


p = sympy.plot(f.subs({a: 2}), invL(F).subs({a: 2}), xlim=(-1, 4), ylim=(0, 3), show=False)
p[1].line_color = 'red'
p.show()

# 20.4. Reproducing standard transform table
# Let's see if we can match the functions in the table

omega = sympy.Symbol('omega', real=True)
exp = sympy.exp
sin = sympy.sin
cos = sympy.cos
functions = [1,
         t,
         exp(-a*t),
         t*exp(-a*t),
         t**2*exp(-a*t),
         sin(omega*t),
         cos(omega*t),
         1 - exp(-a*t),
         exp(-a*t)*sin(omega*t),
         exp(-a*t)*cos(omega*t),
         ]
print (functions)
'''
[1, t, e−at, te−at, t2e−at, sin(ωt), cos(ωt), 1−e−at, e−atsin(ωt), e−atcos(ωt)]
Fs = [L(f) for f in functions]
Fs
[1s, 1s2, 1a+s, 1(a+s)2, 2(a+s)3, ωω2+s2, sω2+s2, as(a+s), ωω2+(a+s)2, a+sω2+(a+s)2]
'''

# 20.5. More complicated inverses
# Why doesn’t the table feature more complicated functions? Because higher-order rational functions can be written as sums of simpler ones through application of partial fractions expansion.

F = ((s + 1)*(s + 2)* (s + 3))/((s + 4)*(s + 5)*(s + 6))
print(F) # (s+1)(s+2)(s+3)(s+4)(s+5)(s+6)
res = F.apart(s) # descomposició en fraccions parcials 1 − 30/(s+6) + 24/(s+5) − 3/(s+4)
print(res)

#Even sympy can benefit from a little help sometimes. When we try to calculate the inverse of F we get a bit of a nasty answer:

res = invL(F)
print(res) # 3(e2t−2et+1)e−6tθ(t)−11(2e2t−5et+3)e−6tθ(t)+6(8e2t−25et+18)e−6tθ(t)+L−1s[s3s3+15s2+74s+120](t)

#Perhaps it looks better if we simplify?

res = invL(F).simplify()
print(res) # L−1s[s3s3+15s2+74s+120](t)+29e−4tθ(t)−101e−5tθ(t)+78e−6tθ(t)

#No, it still features an "unknown" laplace transform. If we do the partial fractions expansion first, we get a clean answer:

res = invL(F.apart(s))
print(res) # δ(t)−3e−4tθ(t)+24e−5tθ(t)−30e−6tθ(t)
