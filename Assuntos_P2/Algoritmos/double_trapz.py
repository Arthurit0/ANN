import math

def double_trapz(f, a: float, b: float, c: float, d: float, n1: int, n2: int) -> float:
    if n1 <= 0 or n2 <= 0:
        raise ValueError('Ops, isso nÃ£o pode')
    h1 = (b-a) / n1
    h2 = (d-c) / n2
    
    soma_interior = 0
    for i in range(1, n1):
        for j in range(1, n2):
            soma_interior += f(a + i * h1, c + j*h2)
    
    soma_arestas_horizontais = 0
    for i in range(1, n1):
        for j in [0, n2]:
            soma_arestas_horizontais += f(a + i * h1, c + j * h2)
    
    soma_arestas_verticais = 0
    for j in range(1, n2):
        for i in [0,n1]:
            soma_arestas_verticais += f(a + i *h1, c + j * h2)
    
    soma_vertices = 0
    for i in [0,n1]:
        for j in [0, n2]:
            soma_vertices += f(a + i * h1, c + j * h2)
    return (h1*h2/4) * (soma_vertices + 4 * soma_interior + 2 * (soma_arestas_verticais + soma_arestas_horizontais))

def f (x,y):
    return math.cos(x**2) * math.sin(y**2*x) * math.exp(-y**2) + 1

a,b =  [-1.249, 1.198]
c,d =   [-1.663, 1.39]
n1, n2 = 37, 16

r = double_trapz(f, a, b, c, d, n1, n2)
print(r)