import numpy as np
import math

nós = {
    4: (-0.33998104358485626, 0.33998104358485626, -0.8611363115940526, 0.8611363115940526),
    6: (0.6612093864662645, -0.6612093864662645, -0.2386191860831969, 0.2386191860831969, -0.932469514203152, 0.932469514203152),
    8: (-0.1834346424956498, 0.1834346424956498, -0.525532409916329, 0.525532409916329, -0.7966664774136267, 0.7966664774136267, -0.9602898564975363, 0.9602898564975363),
    10: (-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717),
    12: (-0.1252334085114689, 0.1252334085114689, -0.3678314989981802, 0.3678314989981802, -0.5873179542866175, 0.5873179542866175, -0.7699026741943047, 0.7699026741943047, -0.9041172563704749, 0.9041172563704749, -0.9815606342467192, 0.9815606342467192)
}

pesos = {
    4: (0.6521451548625461, 0.6521451548625461, 0.34785484513745385, 0.34785484513745385),
    6: (0.3607615730481386, 0.3607615730481386, 0.46791393457269104, 0.46791393457269104, 0.17132449237917036, 0.17132449237917036),
    8: (0.362683783378362, 0.362683783378362, 0.31370664587788727, 0.31370664587788727, 0.22238103445337448, 0.22238103445337448, 0.10122853629037626, 0.10122853629037626),
    10: (0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204, 0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814),
    12: (0.24914704581340277, 0.24914704581340277, 0.2334925365383548, 0.2334925365383548, 0.20316742672306592, 0.20316742672306592, 0.16007832854334622, 0.16007832854334622, 0.10693932599531843, 0.10693932599531843, 0.04717533638651183, 0.04717533638651183)
}

q_a = -1.128
q_b = 2.393
q_n = 256


def quadratura(f,x,c):
    return sum([ci * f(xi) for ci, xi in zip(c,x)]) 

def change(f,a,b):
    def g(u):
        return f(a + (b - a) * (u + 1) / 2) * (b - a) / 2
    return g

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

    def f(x):
        return 2 * math.sin(x) + math.cos(-x**2)
    
    values = [-0.621, 0.419, 1.346]

    funcs_str =  ['1', 'x', 'x**2', 'x**3', 'x**4', 'x**5']
    funcs = []
    # funcs = [lambda x: eval(s) for s in funcs_str]
    for funcs_str in funcs_str:
        h = build_func(funcs_str)
        funcs.append(h)
    c = coeffs(f, funcs)

    for i, ci in enumerate(c):
        print(f'c{i} = {ci}')

    print();

    for value in values:
        g = 0
        print(f'g({value}) =',end=" ")
        for i in range(len(funcs)):
            g += c[i]*funcs[i](value)
        print(f'{g}') 

    def g(x):
        return sum(ci * fi(x) for ci, fi in zip(c, funcs))

    def h(x):
        return (f(x)-g(x))**2

    j = change(h, q_a, q_b)
    err = quadratura(j, nós[10], pesos[10])

    print(f'\nQ(10) = {err}')