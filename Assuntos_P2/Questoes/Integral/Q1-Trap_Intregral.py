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

a = -1.963
b = 1.838

n = [2, 17, 30, 50, 84, 113, 248, 389, 632, 868, 3371, 6838]

for i in range(len(n)):
    r = trapz(f, a, b, n[i])
    print(f'Ponto {n[i]} = {r}')