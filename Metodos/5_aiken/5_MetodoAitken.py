import math

p0 = 1.5
p1 = None
p2 = None
pg = None
pg_anterior = None
error = None
epsilon = math.pow(10, -9)
itr_n = 0

def g_x(x):
    return 1 + math.sin(x)**2

# Calcular el pgorro inicial
p1 = g_x(p0)
p2 = g_x(p1)
pg = p0 - ((p1 - p0)**2) / (p2 - 1 * p1 + p0)

# Ya que es el primero, no se puede calcular el error
print("{} & {: .10f} & {: .10f} & {: .10f} & {: .10f} & - \\\\".format(itr_n, p0, p1, p2, pg))
while True:
    itr_n = itr_n + 1
    pg_anterior = pg

    p0 = p1
    p1 = p2
    p2 = g_x(p1)

    # Formula de Aitken
    pg = p0 - ((p1 - p0)**2) / (p2 - 2 * p1 + p0)

    # Error entre aproximaciones de pgorro
    error = math.fabs(pg - pg_anterior)

    print("{} | {: .10f} | {: .10f} | {: .10f} | {: .10f} | {: e} ".format(itr_n, p0, p1, p2, pg, error))
    if(error < epsilon):
        break
