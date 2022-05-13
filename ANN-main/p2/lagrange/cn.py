from math import*

class Cn:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = [self.denom(i) for i in range(len(x))]
    
    def denom(self, xn):#indice do x e não o proprio x
        mult = 1
        for i in range(len(x)):
            if i != xn:
                mult *= (x[xn] - x[i])
        return mult
    
    def constN(self, y): #usar indice do y
        return self.y[y]/self.dx[y]

x = [1.592, 1.943, 2.272, 2.616, 2.89, 3.125, 3.501, 3.875, 4.097, 4.576, 4.832]

def f(x):
    e = 2.718281828459045235360287
    #return sin(x)**4 -4*sin(x)**2 + cos(x**2) + e**-(x**2) + 5
    #return cos(x)**3 + 2*cos(x)**2 + 1
    return cos(x + log(x**2)**(1/2))

y = [f(i) for i in x]

cn = Cn(x, y)
print(y)
for i in range(len(y)):
    print(f'C{i}: {cn.constN(i)}')