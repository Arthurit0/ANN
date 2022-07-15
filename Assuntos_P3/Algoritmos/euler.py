
def euler(f, x0, y0, h, n):
    for k in range(n):
        x0 += h
        y0 += h * f(x0, y0)
        print(f'x_{k+1} = {x0} e y_{k+1} = {y0}')
    



if __name__ == '__main__':
    def f(x, y):
        return y / 2 + 1

    x0 , y0 = 0, 1
    h = 0.5
    n = 10
    euler(f, x0, y0, h, n)


