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


def poly(x, coefs):
    s = coefs[0]
    for i, ci in enumerate(coefs[1:], 1):
        s += ci * x ** i
    return s

def build_func(coefs):
    def temp(x):
        return poly(x, coefs)
    return temp

def modelo(x):
    a, b = -10, 10
    erro = 1 + (b-a) * np.random.random()
    return 2 + 2.34 * x - 1.86 *x ** 2 - 3.21


if __name__ == '__main__':

    x = [-4.1676, -4.1299, -4.0701, -3.9352, -3.8392, -3.7303, -3.6983, -3.5483, -3.5244, -3.3767, -3.2947, -3.2249, -3.1774, -3.0455, -2.9535, -2.9053, -2.747, -2.7043, -2.6134, -2.5153, -2.4293, -2.337, -2.2526, -2.1941, -2.0867, -1.9672, -1.8602, -1.8439, -1.7463, -1.6242, -1.5254, -1.4315, -1.3771, -1.2912, -1.2277, -1.1484, -1.0299, -0.9102, -0.8479, -0.7181, -0.6631, -0.6111, -0.4503, -0.3905, -0.347, -0.2469, -0.136, -0.0219, 0.0575, 0.1741, 0.2266, 0.3408, 0.4271, 0.4677, 0.534, 0.6974, 0.779, 0.8471, 0.9603, 1.0401, 1.1199, 1.2333, 1.3027, 1.4066, 1.4585, 1.5376, 1.6272, 1.6831, 1.816, 1.8634, 1.9986, 2.1031, 2.2003, 2.2993, 2.3396, 2.4264, 2.5618, 2.6504, 2.7171, 2.7594, 2.8651, 2.9302, 3.0863, 3.1191, 3.222, 3.3326, 3.4086, 3.5334, 3.5523, 3.7013, 3.7789, 3.8759, 3.913, 3.9958, 4.1578, 4.2149]
    y = [3.6622, 4.1789, 4.3573, 5.2851, 5.7633, 6.0978, 6.4216, 6.4507, 6.5043, 6.7439, 6.7454, 6.5971, 6.7019, 6.8342, 6.5228, 6.6126, 5.6271, 6.0761, 6.5038, 6.3825, 4.8604, 5.6389, 3.9595, 5.523, 4.8975, 4.853, 4.8123, 5.2434, 4.9091, 4.6088, 3.2986, 4.3852, 5.3403, 4.2192, 4.5516, 4.5208, 4.1142, 3.709, 4.2042, 4.5139, 4.6143, 4.3241, 4.7564, 4.8287, 3.7093, 4.7666, 6.6216, 5.1457, 6.2631, 4.9335, 5.2347, 5.2605, 5.2757, 5.6494, 5.5832, 5.3348, 4.3645, 5.9695, 6.2611, 5.5269, 5.646, 5.1939, 5.8229, 5.6352, 5.6638, 5.6802, 5.5115, 5.3359, 5.2197, 6.2511, 4.9372, 4.0576, 4.5603, 4.5806, 4.3738, 4.1261, 2.6978, 3.6997, 3.5861, 3.5336, 3.3832, 3.2689, 3.3892, 2.2208, 3.3388, 3.1269, 3.4887, 3.1419, 3.3064, 3.812, 3.8782, 4.1773, 4.4648, 5.0334, 5.9764, 6.4111]
    grau = 5

    coefs = best_poly(x, y, grau)
    p = build_func(coefs)
    #print(f'{coefs = }')

    for i in coefs:
        print(round(i,7))

