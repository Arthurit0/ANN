

def diff_a(f, x0, h):
    """
    Usada para aprixmar a primeira
    derivada de f no ponto x0
    """
    return (f(x0 + h) - f(x0))/h


def diff_b(f, x0, h):
    """
    Usada para aprixmar a primeira
    derivada de f no ponto x0
    """
    return (f(x0) - f(x0 - h))/h


def diff_c(f, x0, h):
    """
    Usada para aprixmar a primeira
    derivada de f no ponto x0
    """
    return (f(x0 + h) - f(x0 - h)) / (2 * h)


if __name__ == "__main__":
    def f(x):
        return x ** x

    x0 = 2
    hs = [10 ** (-i) for i in range(1, 20)]

    print(hs)

    for h in hs:
        #print(f'diff_a(f, x0={x0}, h={h}) = {diff_a(f, x0, h)}')
        # print(f'diff_b(f, x0={x0}, h={h}) = {diff_b(f, x0, h)}')
        print(f'diff_c(f, x0={x0}, h={h}) = {diff_c(f, x0, h)}')
