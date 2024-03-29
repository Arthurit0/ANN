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
        return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)

    x0 = 4.4927
    xs = [4.2579, 4.3489, 4.4019, 4.4592, 4.5336, 4.6132, 4.6757, 4.7014]
    ordem = 4

    '''# pontos para construir a fórmula (usa numeros aleatorios para construir a lista de pontos, será usado caso não seja dada a lista de pontos)
    num_pontos = 7 #sempre maior que a ordem
    a = x0 - 0.25
    b = x0 + 0.25
    xs = [a + (b-a) * random.random() for _ in range(num_pontos)]
    xs.sort()'''

    r = finite_diffs(xs, ordem, x0, f)

    # print(xs)
    print(
        f'aproximação para a derivada de ordem {ordem} de f no ponto {x0} = ', r)
