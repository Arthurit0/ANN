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

    x = [0.117, 0.137, 0.144, 0.674, 0.751, 0.967, 1.106, 1.115, 1.138, 1.146, 1.295, 1.339, 1.385, 1.407, 1.617, 1.648, 1.768, 2.298, 2.43, 2.495, 2.513, 2.717, 2.733, 2.749, 2.882, 2.984, 2.991, 3.173, 3.194, 3.195, 3.238, 3.272, 3.299, 3.374, 3.463, 3.714, 3.795, 3.869, 3.908, 4.004, 4.083, 4.182, 4.196, 4.217, 4.475, 4.728, 4.743]
    y = [1.607, 1.677, 1.701, 2.982, 3.0, 2.876, 2.717, 2.706, 2.677, 2.666, 2.477, 2.423, 2.369, 2.344, 2.146, 2.124, 2.054, 2.089, 2.184, 2.243, 2.26, 2.492, 2.512, 2.532, 2.702, 2.824, 2.832, 2.981, 2.989, 2.99, 2.999, 2.999, 2.993, 2.95, 2.842, 2.202, 1.92, 1.656, 1.522, 1.233, 1.069, 1.001, 1.006, 1.02, 1.843, 2.916, 2.946]

    aprox = trapz_intervalos(x,y)

    print(f'{aprox = }')

    # n = 5

    # for i in range(n):
    #     r = trapz(f, a[n], b[n], 2)
    #     print(f'Ponto {a[n]} = {r}')
