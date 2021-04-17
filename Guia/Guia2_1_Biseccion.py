from math import tan, ceil, log, sqrt

def f1(x):
    return x-tan(x)
    
print(f1(1))
print(f1(2))

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
        
        print( "{:<5}".format(str(i)) + " | " + "{:<5}".format(str(p)) + " | " + "{:<5}".format(str(f(p)))  )
        
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
            
bisection1(f1, 0, 1, 10**-15, 100000)

'''
f: función para el método de bisección
a: extremo izquierdo
b: extremo derecho
TOL: tolerancia
'''

# def bisection2(f, a, b, TOL):
#     n = ceil( log( (b-a)/TOL , 2 ) ) #Aquí calculo las iteraciones requeridas
#     print(n)
#     for i in range(0, n):
#         p = (a + b)/2
#         print( "{:<5}".format(str(i)) + " | " + "{:<30}".format(str(p)) + " | " + "{:<30}".format(str(f(p)))  )
#         if( f(a)*f(p) < 0 ):
#             b = p
#         else:
#             a = p
            
# bisection2(f1, 0, 1, 10**-15)

# Re = 10**4

# def f2(x):
#     return -0.4 + 1.74*log(Re*sqrt(x)) - sqrt(1/x)
    
# bisection2(f2, 0.005, 0.01, 10**-20)

'''
R/ FALLO YA QUE el valor de (b-a)/2 llego a un numero menor al de la tolerancia


'''