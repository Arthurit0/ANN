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
    return a * 2 ** (b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.0383, 0.0817, 0.1391, 0.1886, 0.2518, 0.322, 0.3467, 0.3928, 0.4695, 0.5015, 0.5891, 0.6603, 0.6916, 0.7293, 0.7908, 0.8845, 0.9229, 0.9831, 1.0408, 1.0888, 1.1643, 1.1987, 1.2539, 1.2969, 1.3473, 1.3909, 1.4546, 1.5384, 1.5581, 1.6586, 1.7138, 1.743, 1.8291, 1.8544, 1.9384, 1.9502]
    y = [4.6677, 4.0793, 5.6333, 5.1066, 5.4838, 6.8801, 6.3883, 6.6764, 4.5581, 7.9766, 8.5901, 9.753, 11.995, 10.7806, 9.0111, 11.7891, 12.5319, 13.7759, 16.4074, 17.7335, 16.0996, 17.2562, 17.8658, 18.9146, 20.8029, 21.0379, 21.4097, 25.5719, 26.8262, 28.9725, 31.0095, 31.4989, 35.4666, 35.808, 39.645, 40.5572]
    y_ = np.log(y)
 
    grau = 1

    a0, a1 =  best_poly(x, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1/np.log(2)

    print(f'{a = } e {b = }')

    p = build_func(a, b)

    x_values =  [0.1335, 0.4959, 0.4996, 1.7226, 1.9309]
    
    for xi_v in x_values:
        print(p(xi_v))
