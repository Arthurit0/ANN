import numpy as np


def best_poly(x, y, grau=1):

    k = grau + 1
    ## A = np.zeros((k, k))
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
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a * np.exp(b*x)


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

# def modelo(x):
#     a, b = -10, 10
#     erro = 1 + (b-a) * np.random.random()
#     return 2.5 + np.e ** (1.47 + x) + erro


if __name__ == '__main__':

    x = [1, 2, 3]
    y = [3, 2, 1]
    y_ = np.log(y)

    grau = 1

    a0, a1 = best_poly(x, y_, grau)
    p = build_func(a0, a1)
    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1/np.log(2)

    print(f'{a = } e {b = }')

    p = build_func(a, b)    

    values = [0.332, 0.3806, 0.6234, 0.6389, 1.8221]

    for xi in values:
        print(p(xi))    
