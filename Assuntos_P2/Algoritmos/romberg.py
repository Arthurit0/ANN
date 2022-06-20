import math

def romberg(col_1):
    n = len(col_1)
    for i in range(n-1):
        for j in range(n-1-i):
            numer = 4 ** (i+1) * col_1[j + 1] - col_1[j]
            denom = 4 ** (i+1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]


def trapz(f, a, b, h):
    n = int((b-a) / h)
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    return (h/2) * (f(a) + 2* soma + f(b))


def f(x):
    return math.exp(-x**2)


if __name__ == '__main__':
    a = 0
    b = 1

    h = 0.5
    k = 5
    hs = [h/2 ** i for i in range(k)]
    
    col1 = [trapz(f, a, b, hi) for hi in hs]

    r = romberg(col1)

    print(f'approx = {r}')