from math import *

def f(x):
    return 0.5 + 0.5*e**(-x/(2*pi))*sin(x) - 0.75


def bisection1(f, a, b, TOL, Nmax):
    for i in range(0, Nmax):
        p = (a + b)/2
        
        
        print( str(i) + " \n " + str(a) + " \n " + str(b) + " \n " + str(p) + " \n " + str(f(p)) + " \n " + str(b-a/2) + " \n ")
        
        if ( f(p) == 0 or (b-a)/2 < TOL):
            break
        elif ( f(a)*f(p) < 0 ):
            b = p
        else:
            a = p
            
            
bisection1(f, 0, 2.1, 0.2, 100)