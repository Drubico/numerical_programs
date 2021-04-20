import math

# Inicializando variables
p0 = 20
p1 = None
p2 = None
pg = None
pg_anterior = None
error = None
epsilon = 1e-6
itr_n = 0

def g_x(x):
    return 0.389045*pow((pow(x, 1.70922) + 124.667), 0.705)

p1 = g_x(p0)
p2 = g_x(p1)
pg = p0 - pow( p1-p0 , 2.0)/(p2 - 2.0*p1 + p0)

print("{} & {: .10f} & {: .10f} & {: .10f} & {: .10f} & - \\\\".format(itr_n, p0, p1, p2, pg))
while True:
    itr_n = itr_n + 1
    pg_anterior = pg
    p0 = p1
    p1 = p2
    p2 = g_x(p1)
    # Formula de Aitken
    pg = p0 - pow( p1-p0 , 2.0)/(p2 - 2.0*p1 + p0)
    error = math.fabs(pg - pg_anterior)
    print("{} | {: .15f} | {: .15f} | {: .15f} | {: .15f} | {: e} ".format(itr_n, p0, p1, p2, pg, error))
    if(error < epsilon):
        print("logrado con : "+str(itr_n+1)+" Iteraciones")
        break
