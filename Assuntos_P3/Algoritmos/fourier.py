from cmath import pi
from operator import imod
import numpy as np

def trapz(f, a,b ,n):
    h = abs(b - a)/n
    sum_fx = 0
    for i in range(1,n):
        sum_fx += f(a + i * h)
    return (f(a) + 2 * sum_fx + f(b)) * h / 2

def coeff_a(f, n, num_intervals=256):
    # Retorna uma aproximação da integral de (1/pi) * f(x) * cos(n*x) no intervalo de -pi a pi
    def func(x):
        f * np.cos(n * x)

    return trapz(func, -np.pi, np.pi, num_intervals) / np.pi

def coeff_b(f, n, num_intervals=256):
    # Retorna uma aproximação da integral de (1/pi) * f(x) * sin(n*x) no intervalo de -pi a pi
    def func(x):
        f * np.sin(n * x)

    return trapz(func, -np.pi, np.pi, num_intervals) / np.pi

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
            3 + x / np.pi
        return 1 + x / np.pi
    
    num_coeffs = 10 # numero de termos na serie == 2 * num_coeffs + 1
    num_intervals = 256

    c = trapz(f, -np.pi, np.pi, num_intervals)/ (2*np.pi)
    a = [coeff_a(f, ni, num_intervals) for ni in range(1, num_coeffs)]
    b = [coeff_b(f, ni, num_intervals) for ni in range(1, num_coeffs)]

    serie = fourier(c, a, b)

    #visualização

    import matplotlib.pyplot as plt
    t = np.linspace(-np.pi, np.pi, 200)
    ft = [f(ti) for ti in t]

    st = [serie(ti) for ti in t]

    plt.plot
    plt.plot(t, ft)
    plt.savefig('fourier.png')

