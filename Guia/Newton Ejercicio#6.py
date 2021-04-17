from math import *
from scipy.integrate import quad

def function(x,a):
    return cos((((3*pi)/2)*x))*((3*pi)/2)/(((3*pi)/2)*x)**a 
    
def derivate(x,a):
    return -((3*pi)/2)*(log((((3*pi)/2)*x))*(cos((((3*pi)/2)*x))) / (((3*pi)/2)*x)**a)
    

def f(a):
    return quad(function, 0,1, args=(a))[0]
    
def df(a):
    return quad(derivate, 0,1, args=(a))[0]
    

def newton(p0, TOL, Nmax):
    
    for i in range(0, Nmax):
        
        p = p0 - f(p0)/df(p0)
        
        print(str(i) + " \t " + str(p0) + " \t " + str(p) + " \t " + str(fabs(p-p0))) 
        
        if (fabs(p-p0) < TOL):
            break
        else:
            p0 = p
            
            
newton(0.5, 10**-15, 10000)