from math import *

b = -1.16583607818894
c = 0.0542253936905836
d = -1.25100322759761*10**-4
t = 273.15
r = 0.08205

def f(v):
    return -200 + r*t/v + b/v**2 + c/v**3 + d/v**4
    
def df(v):
    return - r*t/v**2 - 2*b/v**3 - 3*c/v**4 - 4*d/v**5 
    

def newton(p0, TOL, Nmax):
    
    for i in range(0, Nmax):
        p = p0 - f(p0)/df(p0)
        
        print(str(i) + " \t " + str(p0) + " \t " + str(p) + " \t " + str(fabs(p-p0))) 
        
        if (fabs(p-p0) < TOL):
            break
        else:
            p0 = p
            
newton(r*t/200, 10**-9, 20)