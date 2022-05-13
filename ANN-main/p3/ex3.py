import math
def f(x):
    return math.cos(pow(x,2)) + pow(x,2) + math.e**(pow(-x, 4))

x = [ 0.41265339,  4.30825904,  0.70512843,  8.47597657,  1.17506551, 16.65921052]
maxi = []
for i in x:
    maxi.append(f(i) - )