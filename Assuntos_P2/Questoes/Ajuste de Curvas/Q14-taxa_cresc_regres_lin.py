import numpy as np
import math

def best_line(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    A = [[n, sum_x], [sum_x, sum_x2]]
    B = [sum_y, sum_xy]
    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a * (x/(x+b))

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [2.3943, 3.4746, 4.3397, 6.5013, 8.0169, 9.0656, 10.6874, 13.3254, 14.6812, 15.9011, 17.0895, 18.8973]
    y = [0.7129, 0.9699, 1.1337, 1.2902, 1.4136, 1.491, 1.4998, 1.6786, 1.7245, 1.7455, 1.808, 1.7968]
    values = [2.8091, 5.7804, 9.9388]

    # Melhorando aproximações
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
    x_ = np.divide(1,x)

    grau = 1

    a0, a1 = best_line(x_, y_, grau)
    a = 1/a0
    b = a1/a0

    print(f'{a0 = } e {a1 = }')
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px = }')
