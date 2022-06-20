import math

# def trapz(f, a, b, n):
#     h = (b-a) / n
#     soma = 0
#     for k in range(1, n):
#         soma += f(a + k*h)
#     soma *= 2
#     soma += (f(a) + f(b))
#     return (h/2) * soma


def trapz_intervalos(x, y):
    soma = 0
    for i in range(len(x)-1):
        altura = y[i] + y[i+1]
        base = x[i+1] - x[i]
        soma += (base * altura) / 2
    return soma


if __name__ == '__main__':

    x = [0.397, 1.537, 1.999, 2.77, 3.604, 3.654, 4.138]
    y = [2.541, 2.213, 2.0, 2.559, 2.539, 2.395, 1.01]

    aprox = trapz_intervalos(x,y)

    print(f'{aprox = }')

    # n = 5

    # for i in range(n):
    #     r = trapz(f, a[n], b[n], 2)
    #     print(f'Ponto {a[n]} = {r}')

