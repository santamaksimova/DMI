# -*- coding: utf-8 -*-
import numpy as np #1
import matplotlib.pyplot as plt #2

def mans_sinuss(x): #6b
   k = 0
   a = (-1)**0*x**1/(1)
   S = a
   while k < 500: #0<=3 (1), 1<=3 (2), 2<=3 (3), 3<=3 (4)
     k = k + 1
     R = (-1) * x**2/((2*k)*(2*k+1))
     a = a * R
     S = S + a
   return S

a = 1.57 #3
b = 4.71 #4
# funkcijas zīmēšana
x = np.arange(a, b, 0.01) #5
y = mans_sinuss(x) #6a
plt.plot(x,y) #7
plt.grid() #8
plt.show() #9


# funkcijas saknes meklēšana
delta_x = 1.e-3 #0.001
funa = mans_sinuss(a)
funb = mans sinuss(b)
if funa * funb > 0:
    print "Intervālā [%.2f,%.2f] funkcijai nav saknes"%(a,b),
    print "Vai funkcijai šajā itervālā ir pāru sakņu skaits"
    exit()

print "Uz robežām f(%.2f)=%2f f(%.2f)=%.2f"%(a,funa,b,funb)
k = 0
while b-a > delta_x:
    k = k + 1
    x = (a + b)/2
    funx = mans_sinuss(x)
    print "%3d. a=%.9f f(%.9f)=%7%.4f b=%.4f"%(a,funa, b, funab)
    if funa * funx > 0:
        a = x
    else:
            b = x
print "a=%.f(%.4f)=%.4f f(%.4f)=%.4f f(%.4f)=%.4f"%(a,funa,b,funb)
print "Interāciju skaits: %d"%(k)
