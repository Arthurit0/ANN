
def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        x0 += h
        y0 += h * f(x0, y0)
        print(f'x_{k+1} = {x0} e y_{k+1} = {y0}')
        vals.append([x0, y0])
    return vals

def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += m2
        x0 += h
        vals.append([x0, y0])
    return vals

if __name__ == '__main__':
    def f(x, y):
        return y / 2 + 1

    x0 , y0 = 0, 1
    h = 0.5
    n = 10
    euler(f, x0, y0, h, n)


