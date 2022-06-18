import numpy as np
import math

# x0 = ponto onde a função será derivada
# x = lista de coordenadas na proximidade de x0
# y = cálculo da função em todos os pontos x
# k = ordem da derivada

def fin_dif(x0, x, k):
    n = len(x)
    A, B = [[1]* n], [0]
    for i in range(1, n):
        # construção da matriz A
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        # construção da matriz B
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i - k)
            el = (numer / denom) * x0 ** (i - k)
            B.append(el)
    return np.linalg.solve(A, B)
        
def prod(coeffs, y):
    return sum(ci * yi for ci, yi in zip(coeffs, y))
        

if __name__ == '__main__':
    def f(x):
        return math.log(2 + math.cos(math.exp(-x)))
    def p(xp):
        x0 = -0.3565
        x = [-0.5871, -0.5356, -0.4269, -0.3666, -0.3306, -0.2772, -0.1825, -0.1411]
        y = [f(xi) for xi in x]
        
        coeffs = fin_dif(x0, x, 1)
        f_1 = prod(coeffs, y)
        
        coeffs = fin_dif(x0, x, 2)
        f_2 = prod(coeffs, y)
        
        coeffs = fin_dif(x0, x, 3)
        f_3 = prod(coeffs, y)

        coeffs = fin_dif(x0, x, 4)
        f_4 = prod(coeffs,y)

        return f(x0) + f_1*(xp - x0) + (f_2/2)*((xp - x0)**2) + (f_3/6)*((xp - x0)**3) + (f_4/24)*((xp - x0)**4)
    
    
    values =  [-0.5412, -0.4069, -0.385, -0.3782]
    px = [p(vi) for vi in values]
    print(f'{px = }')

    fx_menos_px = [np.abs(f(vi) - p(vi)) for vi in values]
    print(f'{fx_menos_px = }')