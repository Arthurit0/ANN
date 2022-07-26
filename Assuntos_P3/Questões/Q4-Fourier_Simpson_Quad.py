import math
import numpy as np

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

def quadratura(f,x,c):
    return sum([ci * f(xi) for ci, xi in zip(c,x)]) 

def change(f,a,b):
    def g(u):
        return f(a + (b - a) * (u + 1) / 2) * (b - a) / 2
    return g

# def trapz(f, a,b ,n):
#     h = abs(b - a)/n
#     sum_fx = 0
#     for i in range(1,n):
#         sum_fx += f(a + i * h)
#     return (f(a) + 2 * sum_fx + f(b)) * h / 2

def simps(f, a, b, n):
    if n%2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior que 1")
    h = (b - a)/n
    soma_odd, soma_even = 0, 0
    for k in range(1, n+2, 2):
        # print(f'soma_odd está em {soma_odd}\nsoma_odd += f({a} + {k} * {h}) = f({a+k*h}) = {f(a+k*h)}')
        soma_odd += f(a + k * h)
    for k in range(2, n, 2):
        # print(f'soma_even está em {soma_even}\nsoma_even += f({a} + {k} * {h}) = f({a+k*h}) = {f(a+k*h)}')
        soma_even += f(a + k * h)
    return (f(a) + 4 * soma_odd + 2 * soma_even + f(b)) * (h/3)

def coeff_a(f, n, num_intervals):
    # Retorna uma aproximação da integral de (1/pi) * f(x) * cos(n*x) no intervalo de -pi a pi
    def func(x):
        return f(x) * np.cos(n * x)
    # Métodos de aproximação: trapz, simpson, quad...
    # return trapz(func, -np.pi, np.pi, num_intervals) / np.pi
    return simps(func, -np.pi, np.pi, num_intervals)

def coeff_b(f, n, num_intervals):
    # Retorna uma aproximação da integral de (1/pi) * f(x) * sin(n*x) no intervalo de -pi a pi
    def func(x):
        return f(x) * np.sin(n * x)
    # Métodos de aproximação: trapz, simpson, quad...
    # return trapz(func, -np.pi, np.pi, num_intervals) / np.pi
    return simps(func, -np.pi, np.pi, num_intervals)

def fourier(c, a, b):
    def func(x):
        soma = c
        for n, coeffs in enumerate(zip(a,b)):
            ai, bi = coeffs
            soma += (ai * np.cos(n * x) + bi * np.sin(n * x))
        return soma
    return func

if __name__ == '__main__':
    def f(x):
        return x * np.sin(6* math.e ** (-x ** 2))

    values = [-1.967, 0.302, 2.651]
    num_coeffs = 6 # numero de termos na serie == 2 * num_coeffs + 1
    num_intervals = 128

    c = simps(f, -np.pi, np.pi, num_intervals)/ (2*np.pi)
    a = [coeff_a(f, ni, num_intervals) for ni in range(1, num_coeffs)]
    b = [coeff_b(f, ni, num_intervals) for ni in range(1, num_coeffs)]

    serie = fourier(c, a, b)

    print(c)
    for i in range(len(a)):
        print(f'c{i+1} = {a[i]}')
    for i in range(len(b)):
        print(f'c{i+1} = {b[i]}')

    def g(x):
        return c + sum(a[n-1] * np.cos(n*x) + b[n-1] * np.sin(n * x) for n in range(1, 6))  

    for value in values:
        print(f'g({value}) = {g(value)}')

    def h(x):
        return (f(x)-g(x))**2

    j = change(h, a, b)
    err = quadratura(j, nós[10], pesos[10])

    print(f'\nQ(10) = {err}')