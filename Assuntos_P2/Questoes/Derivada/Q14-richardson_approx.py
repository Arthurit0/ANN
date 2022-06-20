
from math import pi, sin, tan


def richardson(col_1):
    n = len(col_1)
    for i in range(n-1):
        for j in range(n-1-i):
            numer = 2 ** (i+1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i+1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]


if __name__ == '__main__':
    # exemplo 1
    def f(x):
        return x ** (x ** -x)

    x0 = 1.49693
    # h = 0.44232
    err_order = 3

    def F1(h):
        return (f(x0+h) - f(x0)) / h

    col_F1 = [-0.19283908639579295, -0.6151830674679317, -0.8234196366750695]

    aprox = richardson(col_F1)
    print(f'O(h^{err_order}) = {aprox}')
