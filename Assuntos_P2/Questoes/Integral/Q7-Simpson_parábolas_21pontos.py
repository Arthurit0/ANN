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

    x = [0.427, 0.6315, 0.836, 1.0075, 1.179, 1.3855, 1.592, 1.596, 1.6, 2.1135, 2.627, 2.901, 3.175, 3.3215, 3.468, 3.543, 3.618, 3.9535, 4.289, 4.4215, 4.554]
    y = [2.619, 2.955, 2.977, 2.833, 2.624, 2.369, 2.166, 2.162, 2.159, 2.013, 2.383, 2.726, 2.982, 2.985, 2.834, 2.689, 2.5, 1.375, 1.136, 1.593, 2.237]

    def somaparab(x, y):
        soma = 0
        for k in range(0, len(x) - 2, 2):
            soma += ((x[k + 1] - x[k])/3) * (y[k] + 4 * y[k + 1] + y[k + 2])
        return soma


    print(f'aprox = {somaparab(x, y)}')