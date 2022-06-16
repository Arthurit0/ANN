import numpy as np
import math

def best_line(x, y, grau):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    A = [[n, sum_x], [sum_x, sum_x2]]
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a*x*np.e**(b*x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.6124, 1.3868, 2.3009, 3.1336, 4.1709, 4.6711, 5.508, 5.921, 6.9998, 7.8026, 8.6391, 9.1876]
    y = [2.665, 5.0767, 6.904, 7.8889, 8.3979, 8.3985, 8.3346, 8.124, 7.6592, 7.1853, 6.6327, 6.2607]
    values = [5.8416, 6.9767, 8.1349]


    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0
    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]
    y_ = np.log(np.divide(y,x))

    xt = [xi + k2 for xi in x]
    x_ = x

    grau = 1

    a0, a1 = best_line(x_, y_, grau)
    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px = }')

    # visualização

    # import matplotlib.pyplot as plt

    # plt.scatter(x, y)

    # t = np.linspace(min(x), max(x), 200)
    # qt = [q(ti) for ti in t]

    # plt.plot(t, qt)

    # plt.savefig('best_poly_regressao_potencia.png')
