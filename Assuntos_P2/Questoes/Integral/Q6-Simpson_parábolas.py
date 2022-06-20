# from math import sqrt, cos

# def simps(a, b, n):
#     if n%2 != 0 or n < 1:
#         raise ValueError("n deve ser par e maior que 1")
#     h = (b - a)/n
#     soma_odd, soma_even = 0, 0
#     for k in range(1, n, 2):
#         soma_odd += f(a + k * h)
#     for k in range(2, n, 2):
#         soma_even += f(a + k * h)
#     return (f(a) + 4 * soma_odd + 2 * soma_even + f(b)) * (h/3)


if __name__ == '__main__':
    # def f(x):
    #     return sqrt(1 + cos(x) ** 2)

    # a, b = -1.375, 1.973
    # n = [4, 16, 42, 72, 84, 118, 144, 160, 184, 226, 498]

    # for ni in n:
    #     print(f'n = {ni} => {simps(a, b, ni)}')

    x = [0.972, 1.712, 2.452, 2.7025, 2.953]
    y = [2.871, 2.083, 2.203, 2.474, 2.788]

    def somaparab(x, y):
        soma = 0
        for k in range(0, len(x) - 2, 2):
            soma += ((x[k + 1] - x[k])/3) * (y[k] + 4 * y[k + 1] + y[k + 2])
        return soma


    print(f'aprox = {somaparab(x, y)}')