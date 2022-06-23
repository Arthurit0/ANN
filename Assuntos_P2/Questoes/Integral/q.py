pontos = [-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244, 0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717]
pesos = [0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204, 0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814]
pontos_e_pesos = zip(pontos, pesos)     
a,b = [-1.18525,1.91663]

def f(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2 + 1) + 2) + 3) + 4)

def quadratura(f,pontos_e_pesos):
    soma = 0
    for x_k,c_k in pontos_e_pesos:
        soma += c_k * f(x_k)
    return soma

def change(f,a,b,u):
    print(u)
    return f( (b+a)/2 + (b-a)*u/2) * (b-a) / 2

def g(u):
    print(u)
    return change(f,a,b,u)

r = quadratura(g,pontos_e_pesos)
print(g(u))
print(r)