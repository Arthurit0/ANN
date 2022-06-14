from math import*

def double_trapz(f, a:float, b:float, c:float, d:float, n1:int, n2: int) -> float:
    if n1 <=0 or n2<=0:
        raise ValueError("Ops, isso não pode")

    h1 = (b-a) / n1
    h2 = (d-c)/n2
    soma_interior = 0
    for i in range(1, n1):
        for j in range(1, n2):
            soma_interior += f(a + i * h1, c+j *h2)
    
    soma_arestas_horizontais = 0
    for i in range (1, n1):
        for j in [0, n2]:
            soma_arestas_horizontais += f(a+i*h1, c+j*h2)
    
    soma_arestas_verticais = 0
    for j in range (1, n2):
        for i in [0, n1]:
            soma_arestas_verticais += f(a+i*h1, c+j*h2)
    soma_vertices = 0
    for i in [0,n1]:
        for j in [0, n2]:
            soma_vertices += f(a + i*h1, c+j*h2)
    return (h1 * h2/4) * (soma_vertices + 4 * soma_interior + 2 * soma_arestas_horizontais + 2*soma_arestas_verticais)


def f(x, y):
    e = 2.718281828459045235360287
    return cos(x**2)*sin(x*y**2)*e**(-y**2) + 1




intervalo1 = [-1.646, 1.193]
intervalo2 = [-1.291, 1.108]
n1 = 37
n2 = 16
r = double_trapz(f, intervalo1[0], intervalo1[1], intervalo2[0], intervalo2[1], n1, n2)
print(r)