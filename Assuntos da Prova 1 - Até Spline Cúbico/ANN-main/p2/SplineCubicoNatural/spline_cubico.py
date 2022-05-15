#algoritmo spline cubico
from math import*
import matplotlib.pyplot as plt 
import numpy as np

def splineSTR(x, y):
    n = len(x)
    a = {k: v for k,v in enumerate(y)}
    h = {k: x[k+1] - x[k] for k in range(n - 1)}
    A = [[1] + [0] *(n - 1)]
    for i in range(1, n-1):
        row = [0] * n
        row[i-1] = h[i-1]
        row[i] = 2*(h[i-1] + h[i])
        row[i+1] = h[i]
        A.append(row)
    A.append([0] * (n - 1) + [1])
    B = [0]
    for k in range (1, n-1):
        row = 3 * (a[k+1] - a[k]) / h[k] -3 * (a[k] - a[k-1])/ h[k-1]
        B.append(row)
    B.append(0)
    c = dict(zip(range(n), np.linalg.solve(A,B))) 
    b={}
    d={}
    for k in range(n-1):
        b[k] = (1/h[k]) * (a[k+1] - a[k]) - (h[k]/3) * (2*c[k]+c[k+1])
        d[k] = (c[k+1] - c[k])/(3*h[k])
    s = {}
    
    for k in range(n-1):
        print(f'ak: {a[k]} \t bk: {b[k]} \t ck:{c[k]} \t dk:{d[k]}')
        
        eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'        
        #s[k] = {'coefs': [a[k], b[k], c[k], d[k]], 'domain': [x[k], x[k+1]]} 
        s[k] = {'eq': eq, 'domain': [x[k], x[k+1]]} 
        
    return s

def splineListaCoef(x, y): #funcao criada para lista de coeficientes usar para quadnoa aplicar um x especifico
    n = len(x)
    a = {k: v for k,v in enumerate(y)}
    h = {k: x[k+1] - x[k] for k in range(n - 1)}
    A = [[1] + [0] *(n - 1)]
    for i in range(1, n-1):
        row = [0] * n
        row[i-1] = h[i-1]
        row[i] = 2*(h[i-1] + h[i])
        row[i+1] = h[i]
        A.append(row)
    A.append([0] * (n - 1) + [1])
    B = [0]
    for k in range (1, n-1):
        row = 3 * (a[k+1] - a[k]) / h[k] -3 * (a[k] - a[k-1])/ h[k-1]
        B.append(row)
    B.append(0)
    c = dict(zip(range(n), np.linalg.solve(A,B))) 
    b={}
    d={}
    for k in range(n-1):
        b[k] = (1/h[k]) * (a[k+1] - a[k]) - (h[k]/3) * (2*c[k]+c[k+1])
        d[k] = (c[k+1] - c[k])/(3*h[k])
    s = {}
    listaCoef =[]
    for k in range(n-1):       
        listaCoef.append([a[k], b[k], c[k], d[k]])
    return listaCoef

def f(x):
    e = 2.718281828459045235360287
    return e**(-x**2) + cos(x) +3
    #return e**(cos(x)**2) + e**(-x**2) + log(x)
    #return cos(x + log(x**2)**(1/2))

x = [0.503, 1.629, 2.473, 3.06, 4.14, 5.0, 6.014, 6.507]
y = [4.653, 3.012, 2.218, 2.003, 2.458, 3.284, 3.964, 3.975]
valores = [0.763, 6.198, 6.502]

#aplicando x para S(x)
listaCoef = splineListaCoef(x, y)
for i in range(len(valores)):
    for j in range(len(x)):
        if valores[i] > x[j] and valores[i] < x[j+1]:
            soma = listaCoef[j][0] + listaCoef[j][1]*(valores[i] - x[j]) + listaCoef[j][2]*(valores[i] - x[j])**2 + listaCoef[j][3]*(valores[i] - x[j])**3
            print(f'S({valores[i]} = {soma})')
            break


#eqs = splineSTR(x, y)
#print(eqs)