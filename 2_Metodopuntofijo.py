from math import cos, log, exp
import matplotlib.pyplot as plt
import numpy as np

'''
g: función con un único punto fijo
p0: aproximación inicial del punto fijo
TOL: precisión deseada
Nmax: número máximo de iteraciones
'''
def fixedPoint(g, p0, TOL, Nmax):
    for i in range(0, Nmax):
        p = g(p0)
        print( "{0:d} \t {1:.15f} \t {2:.15f} \t {3:.5e} ".format(i, p0, p, abs(p0-p)) )
        if abs(p - p0) < TOL:
            break
        p0 = p
        
fixedPoint(lambda x: cos(x), 0.5, 10**-6, 1000)


def g1(x):
    return -5*log(exp(-0.75*x) + 1/4)

def g2(x):
    return (-4/3)*log(exp(-0.2*x) - 1/4)
    

print( 0 - g1(0) < 0 )
print( 2 - g1(2) > 0 )

print( 0 - g2(0) < 0 )
print( 2 - g2(2) > 0 )

x = np.linspace(-1, 3, 100)
y = (4/15)* ( np.exp(-0.2*x)/( np.exp(-0.2*x) - 1/4 ) )

plt.plot(x,y, 'r')

plt.show()

fixedPoint(g2, 1, 10**-15, 1000)
