import math
import numpy as np


def richardson(col_1):
    n = len(col_1) - 1
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = 2 ** (i + 1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i + 1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]


if __name__ == '__main__':
    approximations = [-4.5041115928877105, -4.584891462030413, -4.618803610363244, -4.634224646910582, -4.641562507757044, -4.645139685871754]

    new_value = richardson(approximations.copy())
    aprox = richardson(approximations + [new_value])
    print(aprox)
