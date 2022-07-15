import numpy as np
import math

q_a = 1
q_b = 2
q_n = 250

def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma

def build_func(s, var: str='x'):
    scope = {}
    scope['math'] = math
    func = f'def func({var}): return {s}'
    exec(func, scope)
    return scope['func']

def coeffs(func, funcs):
    n = len(funcs)
    A = np.zeros([n, n], dtype=float)
    B = np.zeros(n, dtype=float)
    for i in range(n):
        for j in range(n):
            def f_ji(x):
                return funcs[j](x) * funcs[i](x) 
            # Produto de f_j e f_i e vive na posição cuja integral vive na posição i, j

            # Resolver as integrais, adaptável (método dos trapézios, romberg ou quadratura gaussiana)
            A[i][j] = trapz(f_ji, q_a, q_b, q_n)
            if i != j:
                A[j][i] = A[i][j]
        def ffi(x):
            return func(x) * funcs[i](x)
        
        B[i] = trapz(ffi, q_a, q_b, q_n)
    return np.linalg.solve(A, B)

if __name__ == "__main__":


    def func(x):
        return np.exp(-x ** 2) * np.cos(np.sqrt(x))
    
    funcs_str = ['x', 'math.cos(x)', 'math.exp(x)', 'math.log(x)']
    funcs = []
    # funcs = [lambda x: eval(s) for s in funcs_str]
    for funcs_str in funcs_str:
        f = build_func(funcs_str)
        funcs.append(f)
    print([f(2) for f in funcs])
    c = coeffs(func, funcs)