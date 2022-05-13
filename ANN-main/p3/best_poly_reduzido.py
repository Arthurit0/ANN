import numpy as np

""" Dados de Entrada """
x = [-1.39017, 1.41543]
y = [43.459833463052185, 56.93989843406345]

x = np.array(x) 
y = np.array(y) 

""" Ajuste da curva a um polinômio """
p = np.polyfit(x,y,5)#(x,y, grau do polinomio)
#printar de tras pra frente

print(p)