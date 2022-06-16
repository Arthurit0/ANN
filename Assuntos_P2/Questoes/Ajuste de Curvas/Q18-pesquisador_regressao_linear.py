import numpy as np

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


def poly(x, coefs):
    s = coefs[0]
    for i, ci in enumerate(coefs[1:], 1):
        s += ci * x ** i
    return s

def build_func(coefs):
    def temp(x):
        return poly(x, coefs)
    return temp

if __name__ == '__main__':

    x = [0.6749, 2.0822, 2.5733, 3.5434, 3.6825, 4.7012, 5.5837, 6.786, 7.4124, 8.0704, 9.2043, 9.5578]
    y = [9.9981, 4.0549, 3.4838, 2.6482, 2.6735, 2.2458, 1.9893, 1.8556, 1.7757, 1.607, 1.4703, 1.4909]
    values = [0.8946, 4.701, 8.7648]

    
    # sqrt( y ) = 1/b + a/b * 1/sqrt( x )

    y_ = np.sqrt(y)
    x_ = 1/np.sqrt(x)

    grau = 1

    coefs = best_poly(x_, y_, grau)
    a0, a1 = best_poly(x_, y_, grau)

    b = 1/a0
    a = a1 * b

    p = build_func(coefs)
    n = len(coefs)

    for xi in range(n):
        print(f'a{xi} = [{coefs[xi]}]')

    print(f'a = {a} b = {b}')

    n = len(values)
    for xi in range(n):
        print(f'y(x{xi+1}) = {(a0 + a1 * 1/np.sqrt(values[xi]))**2}')