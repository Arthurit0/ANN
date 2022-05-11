import numpy as np

def best_poly(x,y,grau):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)] # np.zeros(k,k)
    B = []
    n = len(x);
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p]= sum([xi**p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x,y)]))
    return np.linalg.solve(A,B)

def poly(x, coefs):
    s = coefs[0]
    for i, ci in enumerate(coefs[1:],1):
        s += ci * x ** i
    return s

def build_func(coefs):
    def temp(x):
        return poly(x,coefs)
    return temp

if __name__ == "__main__":

    x = [-2,-1,0,1,3] 
    y = [2,0,1,2,1.5]
    grau = 2

    coefs = best_poly(x,y,grau)

    print(f'{coefs = }')

    p = build_func(coefs)
    plt.scatter(x,y)

    import matplotlib.pyplot as plt
    t = np.linspace(min(x),max(x),200)
    pt = [p(ti) for ti in t]

    plt.plot(t,pt)
    plt.savefig(best_poly)