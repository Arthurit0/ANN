import numpy as np

def best_poly(x, y, grau = 1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if (p == 0):
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a * np.exp(b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':

    x = [0.1316, 0.2715, 0.4474, 0.5722, 0.6991, 0.8487, 1.0064, 1.2929, 1.3976, 1.6606, 1.7417, 1.9601]
    y = [5.194, 6.8801, 9.6246, 11.1588, 12.4384, 16.6468, 24.6409, 37.2644, 43.1973, 67.2803, 76.9931, 113.197]
    y_ = np.log(y)

    grau = 1

    a0, a1 = best_poly(x, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1

    print(f'{a = } e {b = }')

    p = build_func(a, b)
    
    x_values = [0.7121, 1.1225, 1.2412]
    
    for xi_v in x_values:
        print(p(xi_v))
