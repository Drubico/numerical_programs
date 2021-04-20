from math import *
    
def f1(x):
    D=0.75
    if(x<=2.1 or x>0):
        expo= -(x/(2 *pi))
        euler_elevado=pow((e),expo)
        return (0.5 + (0.5*euler_elevado* sin(x)) - D)
    else:
        print("r se sale de rango")


def bisection1(f, a, b, TOL, Nmax):
    for i in range(0, Nmax):
        p = (a + b)/2
        
        print( "{:<5}".format(str(i)) + " | " + "{:<25}".format(str(a))+ " | " + "{:<25}".format(str(b))+ " | " + "{:<25}".format(str(p)) + " | " + "{:<25}".format(str(f(p))) + " | " + "{:<25}".format(str((a + b)/2)) )
        # print( str(i) + " | " + str(a)+" | " + str(b)+ " | " + str(p) + " | " + str(f(p)) + " | " + str((a + b)/2) ) 

        if ( f(p) == 0 or (b-a)/2 < TOL):
            print("\n" +"Los datos llegaron a: ")
            print("P = "+ str(f(p)))
            print("(b-a)/2 : " +str((b-a)/2))
            print("Tolerancia : "+ str(TOL))
            break
        elif ( f(a)*f(p) < 0 ):
            b = p
        else:
            a = p
            
bisection1(f1, 0, 2.1, 0.2, 100000)
