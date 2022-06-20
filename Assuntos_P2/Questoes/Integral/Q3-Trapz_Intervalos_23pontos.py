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

    x = [0.6, 0.898, 1.104, 1.154, 1.268, 1.495, 1.563, 1.884, 2.024, 2.247, 2.359, 2.463, 2.751, 3.067, 3.383, 3.553, 3.614, 3.982, 4.035, 4.585, 4.636, 4.827, 4.944]
    y = [2.925, 2.937, 2.719, 2.656, 2.511, 2.252, 2.19, 2.013, 2.001, 2.061, 2.129, 2.213, 2.535, 2.908, 2.942, 2.667, 2.511, 1.292, 1.159, 2.389, 2.617, 2.991, 2.687]

    aprox = trapz_intervalos(x,y)

    print(f'{aprox = }')

    # n = 5

    # for i in range(n):
    #     r = trapz(f, a[n], b[n], 2)
    #     print(f'Ponto {a[n]} = {r}')

