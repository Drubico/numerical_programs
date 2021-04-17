from math import cos, ceil, log, sqrt

def f1(x):
    return cos(x) - x
    
print(f1(0))
print(f1(1))

'''
f: función para el método de bisección
a: extremo izquierdo del intervalo
b: extremo derecho del intervalo
TOL: tolerancia o precisión deseada
Nmax: número máximo de iteraciones
'''
def bisection1(f, a, b, TOL, Nmax):
    for i in range(0, Nmax):
        p = (a + b)/2
        
        print( str(i) + " \t " + str(p) + " \t " + str(f(p))  )
        
        if ( f(p) == 0 or (b-a)/2 < TOL):
            break
        elif ( f(a)*f(p) < 0 ):
            b = p
        else:
            a = p
            
bisection1(f1, 0, 1, 10**-6, 100000)

'''
f: función para el método de bisección
a: extremo izquierdo
b: extremo derecho
TOL: tolerancia
'''
def bisection2(f, a, b, TOL):
    n = ceil( log( (b-a)/TOL , 2 ) ) #Aquí calculo las iteraciones requeridas
    for i in range(0, n):
        p = (a + b)/2
        print( str(i) + " \t " + str(p) + " \t " + str(f(p))  )
        if( f(a)*f(p) < 0 ):
            b = p
        else:
            a = p
            
bisection2(f1, 0, 1, 10**-6)

Re = 10**4

def f2(x):
    return -0.4 + 1.74*log(Re*sqrt(x)) - sqrt(1/x)
    
bisection2(f2, 0.005, 0.01, 10**-20)

