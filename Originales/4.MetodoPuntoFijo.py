import math

def  g(x):
    return 1 + math.sin(pn)**2

pn = 1.5
g_pn = None
error = None

# 10^-9
epsilon = math.pow(10, -9)

itr_n = 0
while True:
    g_pn = g(pn)
    error = math.fabs(g_pn - pn)
    # n | p_n | p_{n+1} | error
    print("{} | {: .10f} | {: .10f} | {: e}".format(itr_n, pn, g_pn, error))
    if error < epsilon or itr_n == 1000:
        break
    pn = g_pn
    itr_n = itr_n + 1
