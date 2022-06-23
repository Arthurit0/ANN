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
    return (h/2) * (f(a) + 2*soma + f(b))


def f1(x):
    return math.exp(x)*math.sin(x)/(1+x**2)

def f2(x):
    return math.sqrt(1+x**2)

def f3(x):
    return math.exp(-x**2)

def f4(x):
    return (x+1/x)**2

def f5(x):
    return math.cos(-x**2/3)


if __name__ == '__main__':
    func = [f1,f2,f3,f4,f5]

    a = [0.76, 0.63, -0.83, 0.5, 0.68]
    b = [1.76, 1.63, 0.17, 1.5, 1.68]
    k = [6, 10, 10, 4, 10]
    h = [0.25, 0.1, 0.5, 0.2, 0.125]

    for i in range(5):
        hs = [h[i]/2 ** j for j in range(k[i])]
        col1 = [trapz(func[i], a[i], b[i], hi) for hi in hs]
        r = romberg(col1)
        print(f'approx = {r}')