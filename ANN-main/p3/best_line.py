import random
import numpy as np
#gerar linha de pontos
'''def model(x):
    a, b = -1, 1
    erro = a + (b - a) * random.random()
    return 2+0.5*x+erro

p ,q = 0, 10
n = 5 #numero de pontos no eixo x
x = [p + i * (q - p) / (n-1) for i in range(n)]
y = [model(xi) for xi in x]

print(x)
print(y)'''

x = [0.3025, 0.459, 0.8557, 1.0355, 1.4377, 1.8159, 2.2573, 2.658, 2.7051, 3.0922, 3.4242, 3.9074, 4.0496, 4.5443, 4.7745, 5.0835, 5.5081, 5.9575, 6.3056, 6.5909, 6.7871, 7.0226, 7.5722, 7.9054, 8.0877, 8.6527, 8.7861, 9.1275, 9.5619, 9.824]
y = [5.9775, 5.8232, 5.5763, 5.0696, 4.7935, 4.5351, 4.1458, 4.3229, 4.3082, 3.7456, 3.3346, 3.4487, 3.774, 3.7358, 3.3474, 3.084, 3.2529, 3.194, 4.1304, 3.3927, 3.0568, 3.1958, 3.7355, 3.8224, 2.5577, 3.9752, 3.703, 4.8265, 4.573, 4.7103]


def best_line(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    A = [[n, sum_x], [sum_x, sum_x2]]
    B = [sum_y, sum_xy]
    a0, a1 = np.linalg.solve(A, B)
    return a0, a1 #a0 + a1 * x

a0, a1 = best_line(x, y)
    
print(f'a0: {a0}\na1: {a1}')
    
    