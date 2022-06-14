import math

def euler_half(f, x0, y0, h, n):
    r = []
    for i in range(n):
        #realizar iterações do método
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        yk = y0 + h * m2
        #atualizando para a proxima iteração
        y0 = yk
        x0 += h
        #colocando valores numa lista
        r.append((x0, y0))
    
    return r


if __name__ == "__main__":
    def f(x,y):
        return y*(2-x) + x + 1
        
    x0 = 1.19498
    y0 = 2.13208
    
    r = euler_half(f, x0, y0, h=0.18598 , n=10)
    j = 1
    for i in r:
        print(f'{j}:\tx: {i[0]}\ty: {i[1]}')
        j += 1
    

    #print(r)