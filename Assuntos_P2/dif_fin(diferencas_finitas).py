import numpy as np
import math


def coeffs_dif_fin(x0, x, k):
    n = len(x)
    A, B = [[1] * n], [0]
    n = len(x)
    for i in range(1, n):
        # Construção da matriz A
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        # Construção da matriz B
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i-k)
            el = (numer/denom) * x0 ** (i-k)
            B.append(el)
    return np.linalg.solve(A, B)


def dif_fin(coeffs, y):
    return sum(ci * yi for ci, yi in zip(coeffs, y))


if __name__ == '__main__':
    # exemplo 1
    def f(x):
        return math.exp(x)
    x0 = 0
    k = 5
    n = 8  # número de pontos
    # Queremos pontos no intervalo [x0-e, x0+e]
    e = 0.1
    x = np.linspace(x0-e, x0+e, n)
    # Se não for dada a lista, é preciso calculá-la utilizando a função
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)

    print(f'{coeffs = }')
    print(f'{aprox = }')
