
from math import sin, cos, e

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
        return (sin(x) ** 4) - (4 * (sin(x) ** 2)) + cos(x ** 2) + (e ** (-x ** 2)) + 5

    x0 = -0.86634
    # h = 0.44232
    err_order = 6

    def F1(h):
        return (f(x0+h) - f(x0)) / h

    col_F1 = [4.77795469135776, 4.800692793394013, 4.803949919627456, 4.803454364559059, 4.802653211030645, 4.80211094006188]

    aprox = richardson(col_F1)
    print(f'O(h^{err_order}) = {aprox}')
