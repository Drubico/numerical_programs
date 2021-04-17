from math import *


def f(z):
    return z**3 -2*z + 2
    
def df(z):
    return 3*z**2 - 2  
    

def newton(p0, TOL, Nmax):
    
    for i in range(0, Nmax):
        p = p0 - f(p0)/df(p0)
        
        print(str(i) + " \n " + str(p0) + " \n " + str(p) + " \n " + str(abs(p-p0))) 
        
        if (abs(p-p0) < TOL):
            break
        else:
            p0 = p
            
newton(1+1j, 10**-10, 20)