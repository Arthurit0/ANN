from re import A
import numpy as np

#BEST_EXP

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p=i+j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    # LN da função
    return a*x*np.exp(b*x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':


    x = [1.3149, 2.1686, 3.1273, 3.9632, 4.0575, 4.7747, 5.7361, 6.4903, 7.2742, 8.3587, 8.6312, 9.792]
    y = [2.9799, 3.945, 4.7442, 5.218, 5.1999, 5.5863, 5.9065, 6.1739, 6.3911, 6.5113, 6.7366, 6.9022]
    values = [2.1627, 7.8164, 7.9121]

    #transladar os pontos para cima, já que log pode ser negativo
    k = abs(min(y)) + 1
    yt = [yi + k for yi in y]

    # LN de X
    x_ = np.log(x)

    y_ = y

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = a1
    b = a0

    print(f'{a = } e {b = }')

    n = len(values)
    somas = []
    for xi in range(n):
        print(f'y(x{xi+1}) = {a0+a1*np.log(values[xi])}')

    p = build_func(a, b)

    def q(x):
        return p(x) - k