import numpy as np
import math

def best_line(x, y, grau=1):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    A = [[n, sum_x], [sum_x, sum_x2]]
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

def poly(x, a, b):
    return (a*x**2)/(b+x**2)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [1.832, 2.1616, 3.487, 3.9339, 5.0189, 6.1236, 6.8241, 7.7963, 8.973, 9.2862, 10.5441, 11.7625]
    y = [1.1353, 1.3695, 2.4064, 2.7133, 3.1577, 3.4442, 3.5345, 3.7166, 3.7476, 3.8589, 3.856, 3.9722]
    values = [4.2918, 5.8162, 6.3942]

    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0
    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]
    y_ = (np.divide(1,y))

    xt = [xi + k2 for xi in x]
    x_ = np.divide(1,(np.power(x,2)))

    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = 1/a0
    b = a1*a

    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px = }')
