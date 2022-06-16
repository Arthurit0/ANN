import numpy as np


def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi**p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi*xi**i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a*x**b


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':
    x = [0.6203, 0.8268, 1.0384, 1.3271, 1.5179, 1.7275, 1.8413, 2.0314, 2.2664, 2.4494, 2.6962, 2.9289]
    y = [0.2229, 0.2458, 1.4194, 3.6961, 7.2255, 11.589, 15.2704, 22.2796, 33.183, 44.7936, 65.7907, 90.337]
    values = [1.3899, 1.8217, 1.9783]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(yt)

    xt = [xi + k2 for xi in x]

    x_ = np.log(xt)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    a = np.exp(a0)

    b = a1

    print('Coeficientes da reta')
    print(f'{a0 = } e {a1 = }')

    print('Coeficientes da potencia')
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    for value in values:
        print(q(value))

    # visualização

    # import matplotlib.pyplot as plt

    # plt.scatter(x, y)

    # t = np.linspace(min(x), max(x), 200)
    # qt = [q(ti) for ti in t]

    # plt.plot(t, qt)

    # plt.savefig('best_poly_regressao_potencia.png')
