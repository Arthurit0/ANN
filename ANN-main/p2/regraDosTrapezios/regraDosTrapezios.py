from math import*


def f(x):
    e = 2.718281828459045235360287
    return e**(-x**2)

def trapz(f, a, b, n):
    h = (b - a)/n
    soma = 0
    for k in range(1, n):
        soma += (f(a + k * h))
    soma *= 2
    soma += (f(a) + f(b))
    return (h / 2) * soma


#n = 1_000_000 # numero de pontos na partição

intervalo = [1.107,4.829]
subintervalos = [10, 12, 37, 50, 94, 136, 194, 349, 511, 925, 1232]
for i in subintervalos:
    r = trapz(f, intervalo[0], intervalo[1], i)
    print(f'n {i}: {r}')

area = 0
for item in subintervalos:
    area = area + item

#r = trapz(f, intervalo[0], intervalo[1], n)
#print(r)
#print(area)