# Joan Quintana Compte-joanillo. Assignatura CNED (UPC-EEBE)

'''
Treballar amb una precisió arbitrària, amb la llibreria decimal
https://stackoverflow.com/questions/20314324/precision-in-python-upto-50-decimal-places

cd /home/joan/UPC_2021/CNED/apunts/python/T1/
PS1="$ "
python3 precisio_50_decimals.py
'''

from decimal import *
import math
import os

# ==============
os.system("clear")
titol = 'script ' + os.path.basename(__file__) + '\n'
for i in range(0,len(titol)-1):
    titol = titol + '='
print(titol)
# ==============

context = Context(prec=50)
setcontext(context)

# agafem 3 valors i fem una sèrie de càlculs
print("introdueix 3 valors:")
r1 = Decimal(int(input()))
r2 = Decimal(int(input()))
r3 = Decimal(int(input()))
k1=Decimal(1.0)/Decimal(r1)
k2=Decimal(1.0)/Decimal(r1)
k3=Decimal(1.0)/Decimal(r1)

k4=k1+k2+k3+2*(k1*k2+k2*k3+k3*k1).sqrt()
r4=Decimal(1.0)/Decimal(k4)
print (r4)
