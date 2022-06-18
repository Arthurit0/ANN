
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
    h = 0.44232
    err_order = [4, 5, 6, 7, 8]

    def F1(h):
        return (f(x0+h) - f(x0)) / h

    for order in err_order:
        col_F1 = [F1(h/2 ** i) for i in range(order)]
        aprox = richardson(col_F1)
        print(f'O(h^{order}) = {aprox}')
