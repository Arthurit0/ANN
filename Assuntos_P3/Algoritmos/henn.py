
def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        x0 += h
        y0 += h * f(x0, y0)
        print(f'x_{k+1} = {x0} e y_{k+1} = {y0}')
        vals.append([x0, y0])
    return vals

def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += m2
        x0 += h
        vals.append([x0, y0])
    return vals

"""
import math
def heun(f, x0:float, y0:float, h:float, n:int):
    r = []
    for _ in range (n):
        #realizar as iterações
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y1 = y0 + h * (m1+m2)/2
        #atualizando os valores 
        x0 += h
        y0 = y1
        #colocando valores na lista
        r.append((x0, y0))
    return r

if __name__ == "__main__":
    #exemplo
    #y'= 1+xy, y(1)=2
    # 
    # x0 = 1
    # y0 = 2
    #  
    def f(x, y):
        return y*(2 - x) + x + 1
    
    x0 = 0.28985
    y0 = 0.49871
    r = heun(f, x0, y0, h=0.11166, n=10)
    for i in range(len(r)):
        print(r[i])
"""


def henn(f, vA, vB, h, n):
    vals = []
    for _ in range(n):
        m1 = f(vA, vB)
        m2 = f(vA + h, vB + h*m1)
        y1 = vB + h * (m1+m2)/2
        vA += h
        vB = y1
        vals.append((vA, vB));
    return vals;

if __name__ == '__main__':
    def f(x):
        return x / 2 + 1
    x0 , y0 = 0, 1
    h = 0.5
    n = 10
    euler(f, x0, y0, h, n)


