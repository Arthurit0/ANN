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
        return math.exp(-x**2)+math.cos(x)+3

    def p(xp):
        x0 = 8.7126
        n = 10  # numero de pontos igualmente espaçados
        # queremos pontos no intervalo [x0-e, x0+e]
        # ao diminuir o epsilon (e) os pontos são cada vez mais próximos
        e = 0.001
        x = [8.5214, 8.5769, 8.6941, 8.7444, 8.8139, 8.8882]
        y = [f(xi) for xi in x]

        coeffs = coeffs_dif_fin(x0, x, 1)
        f_1 = dif_fin(coeffs, y)

        coeffs = coeffs_dif_fin(x0, x, 2)
        f_2 = dif_fin(coeffs, y)

        coeffs = coeffs_dif_fin(x0, x, 3)
        f_3 = dif_fin(coeffs, y)
        return f(x0) + f_1*(xp - x0) + (f_2/2)*((xp - x0)**2) + (f_3/6)*((xp - x0)**3)

    values = [8.5352, 8.6901, 8.7175]
    px = [p(vi) for vi in values]
    print(f'{px = }')

    fx_menos_px = [np.abs(f(vi) - p(vi)) for vi in values]
    print(f'{fx_menos_px = }')

    x0 = 3.7409
    xs = [3.4942, 3.5255, 3.5601, 3.6163, 3.6575, 3.6751, 3.7031,
          3.7366, 3.7674, 3.7949, 3.8524, 3.859, 3.897, 3.947, 3.9697]
    ordem = 5

    '''# pontos para construir a fórmula (usa numeros aleatorios para construir a lista de pontos, será usado caso não seja dada a lista de pontos)
    num_pontos = 7 #sempre maior que a ordem
    a = x0 - 0.25
    b = x0 + 0.25
    xs = [a + (b-a) * random.random() for _ in range(num_pontos)]
    xs.sort()'''

    # r = finite_diffs(xs, ordem, x0, f)

    # print(xs)
    # print(
    #     f'aproximação para a derivada de ordem {ordem} de f no ponto {x0} = ', r)
