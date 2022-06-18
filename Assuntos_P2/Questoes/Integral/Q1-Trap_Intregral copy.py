import math

def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma


def f(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2+1)+2)+3)+4)

a = [0.397, 1.537, 1.999, 2.77, 3.604, 3.654, 4.138]
b = [2.541, 2.213, 2.0, 2.559, 2.539, 2.395, 1.01]

n = 5

for i in range(n):
    r = trapz(f, a[n], b[n], 2)
    print(f'Ponto {a[n]} = {r}')