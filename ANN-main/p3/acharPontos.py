import math
def f(x):
    return math.cos(pow(x,2)) + pow(x,2) + math.e**(pow(-x, 4))

y = []
x = [-1.39017,1.41543]

for i in x:
    y.append(f(i))

print(x)
print(y)


