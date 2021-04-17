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

# Solo muestra la primera parte de la tabla
first_table=True
first_table_print= "| {:>15} | {:>25} | {:>25} |".format("Iteracion","Valor de p","funcion en p")
format_row="{:>25}"
format_row_2="{:>15}"

def bisection1(f, a, b, TOL, Nmax):
    global first_table
    for i in range(0, Nmax):
        p = (a + b)/2
        if( first_table): 
            print(first_table_print) 
            first_table=False
        
        print("| " +format_row_2.format(str(i)) + " | " + format_row.format(str(p)) + " | " + format_row.format(str(f(p)))+" |"  )
        
        if ( f(p) == 0 or (b-a)/2 < TOL):
            break
        elif ( f(a)*f(p) < 0 ):
            b = p
        else:
            a = p
            

bisection1(f1, 0, 1, 10**-6, 100000)

