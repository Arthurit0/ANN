import numpy as np

# Define os coeficientes do polinômio
def poly(x,y):
    n = len(x) - 1
    A = []
    B = y
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi ** j)
        A.append(row)
    return np.linalg.solve(A,B)


def func_poly(x, coeffs):
    first = coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:],1)])    

if __name__ == '__main__':

    # Exemplo 1
    # x = [1, 2, 3]
    # y = [1, 4, 1]

    # Exemplo 2
    x = [0, np.pi / 2, np.pi]
    y = [0,1,0]

    coeffs = poly(x,y)
    print(coeffs)
    def p(x):
        return func_poly(x, coeffs)

    # Visualização
    import matplotlib.pylab as plt

    plt.scatter(x,y)

    t = np.linspace(min(x),max(x), 200)
    pt = p(t)

    # Função seno, Exemplo 2
    st = np.sin(t)

    plt.plot(t,pt)
    plt.plot(t, st)

    plt.savefig('interp.png')
