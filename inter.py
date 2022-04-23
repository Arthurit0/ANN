import numpy as np

    #Exemplos
    x = [1, 2, 3]
    y = [1, 4, 1]


    coeffs = poly(x,y)
    print(coeffs)

    def p(x):
        return func_poly(x, coeffs)

    #Vsualização

    import matplotlib.pylab as plt
    plt.scatter(x,y)

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti)]


    def poly(x, y):
        n = len(x) - 1
        A = []
        B = y
        for xi in x:
            row = [1]
            for j in range(1, n + 1):
                row.append(xi ** j)
            A.append(row)
        return np.linalg.solve(A,y)

    if __name__ == '__main__':
        coeffs = poly(x,y)
        print(coeffs)

    def func_poly(x, coeffs):
        first = coeffs[0]
        return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:],1)])