from math import*

def simps(f, a, b, n):
    if( n % 2) != 0 or n < 1:
        raise ValueError("n deve ser par e maior que 1")
    h = (b-a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1, n, 2):
        soma_odd += f(a+k *h)
    for k in range(2, n, 2):
        soma_even +=f(a+k*h)
    return (h / 3) * (f(a) + 4 * soma_odd + 2 *soma_even +f(b))


def f(x):
    e = 2.718281828459045235360287
    #return e**(-x**2)
    

intervalo = [0.905,4.55]
subintervalos = [0.905, 1.051, 1.197, 2.8735, 4.55]
for i in subintervalos:
    r = simps(f, intervalo[0], intervalo[1], i)
    print(f'n {i}: {r}')