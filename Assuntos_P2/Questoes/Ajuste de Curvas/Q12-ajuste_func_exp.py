import numpy as np


def best_poly(x, y, grau=1):

    k = grau + 1
    ## A = np.zeros((k, k))
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a * 2 ** (b*x)


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

# def modelo(x):
#     a, b = -10, 10
#     erro = 1 + (b-a) * np.random.random()
#     return 2.5 + np.e ** (1.47 + x) + erro


if __name__ == '__main__':

    x = [0.0025, 0.101, 0.1241, 0.2046, 0.2565, 0.3248, 0.3373, 0.4269, 0.4866, 0.5377, 0.5577, 0.6171, 0.7182, 0.7507, 0.8262, 0.8838, 0.9295, 0.9547, 1.0153, 1.0957, 1.125, 1.1718, 1.2597, 1.3155, 1.3365, 1.4434, 1.4584, 1.5016, 1.6078, 1.6406, 1.6782, 1.7573, 1.8283, 1.8887, 1.9195, 1.9558]
    y = [4.9449, 4.7369, 7.4815, 5.5763, 6.0694, 9.4285, 6.6273, 7.4329, 7.8598, 7.5307, 9.217, 9.0422, 12.4886, 10.6746, 11.9081, 13.365, 14.3212, 14.634, 15.1207, 16.6212, 16.1684, 17.2037, 21.7201, 22.8098, 23.1513, 26.8713, 25.9858, 28.654, 31.9409, 32.2315, 34.2788, 39.1154, 42.066, 45.9055, 47.3987, 49.6777]
    y_ = np.log(y)

    grau = 1

    a0, a1 = best_poly(x, y_, grau)
    
    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1/np.log(2)

    print(f'{a = } e {b = }')

    p = build_func(a, b)    

    values = [0.332, 0.3806, 0.6234, 0.6389, 1.8221]

    for xi in values:
        print(p(xi))    
