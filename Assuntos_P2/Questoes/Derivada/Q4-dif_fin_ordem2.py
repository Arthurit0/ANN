import numpy as np
import math
import random


def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p


def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)
    for i in range(n):
        # para construir a matriz A
        A.append([0] * n)
        for j in range(n):
            A[i][j] = xs[j] ** i
        # para construir a matriz B
        potencias = [k+1 for k in range(i-ordem, i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i-ordem)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A, B)
    # construir a soma que dá a aproximação
    # f^k(x0) ~ c0 * f(x0) + c1 + f(x1) + ... + cn + f(xn)
    soma = 0
    for ck, xk in zip(cs, xs):
        soma += ck*f(xk)
    return soma


if __name__ == '__main__':
    def f(x):
        return math.sin(x)**3 - 3*math.sin(x)**2 + math.sin(x**2) + 4

    x0 = -0.1348
    xs = [-0.3756, -0.177, -0.1187, 0.0284]
    ordem = 2

    '''# pontos para construir a fórmula (usa numeros aleatorios para construir a lista de pontos, será usado caso não seja dada a lista de pontos)
    num_pontos = 7 #sempre maior que a ordem
    a = x0 - 0.25
    b = x0 + 0.25
    xs = [a + (b-a) * random.random() for _ in range(num_pontos)]
    xs.sort()'''

    r = finite_diffs(xs, ordem, x0, f)

    # print(xs)
    print(
        f'aproximação para a derivada de ordem {ordem} de f no ponto {x0} = ', round(r, 7))
