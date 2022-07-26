import numpy as np

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
        f(x) * np.cos(n * x)
    # Métodos de aproximação: trapz, simpson, quad...
    # return trapz(func, -np.pi, np.pi, num_intervals) / np.pi
    return simps(func, -np.pi, np.pi, num_intervals)

def coeff_b(f, n, num_intervals):
    # Retorna uma aproximação da integral de (1/pi) * f(x) * sin(n*x) no intervalo de -pi a pi
    def func(x):
        f(x) * np.sin(n * x)
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
        if x < 0:
            return 3 + x / np.pi
        return 1 + x / np.pi
    
    print(f'Valor Normal = {f(-3.0925052683774528)}')

    num_coeffs = 5 # numero de termos na serie == 2 * num_coeffs + 1
    num_intervals = 128

    c = simps(f, -np.pi, np.pi, num_intervals)/ (2*np.pi)
    a = [coeff_a(f, ni, num_intervals) for ni in range(1, num_coeffs)]
    b = [coeff_b(f, ni, num_intervals) for ni in range(1, num_coeffs)]

    serie = fourier(c, a, b)

    # for i, si in enumerate(serie):
    #     print(f'n{i+1} = {si}')
    # print();
