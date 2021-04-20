#OJO ESTE Y EL CPP SON LO MISMO SOLO ESTABA COMPROBANDO

from math import *
def f(x):
    return (pow(x,4) - 16* pow(x,3) + 78 * pow(x,2) - (412 * x) + (624));
    
def df(x):
    h=10**-4
    return (f(x+h)-f(x))/h

def newton(p0, TOL, Nmax):    
    for i in range(0, Nmax):
        p = p0 - f(p0)/df(p0)
        print(str(i) + " \t " + str(p0) + " \t " + str(p) + " \t " + str(abs(p-p0))) 
        if (abs(p-p0) < TOL):
            break
        else:
            p0 = p
            
newton(-6, 10**-4, 20)