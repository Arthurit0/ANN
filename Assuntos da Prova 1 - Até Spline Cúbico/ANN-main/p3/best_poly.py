import numpy as np

""" Dados de Entrada """
x = [0.1425, 0.4818, 0.7138, 0.895, 1.18, 1.4536, 1.6831, 2.0353, 2.284, 2.5504, 2.9629, 3.0325, 3.4133, 3.7465, 3.9438, 4.2358, 4.5195, 4.5999, 4.9833, 5.2608, 5.613, 5.8678, 6.0184, 6.4491, 6.6148, 6.8721, 7.228, 7.4097, 7.7193, 7.9644, 8.155, 8.5876, 8.6676, 9.1876, 9.3735, 9.4829, 9.9078]
y = [5.6321, 5.5216, 5.4253, 5.2324, 4.3343, 4.9322, 4.6417, 4.6649, 4.9067, 4.0934, 3.9593, 4.2934, 3.2964, 3.7787, 3.8571, 3.8392, 3.725, 3.981, 3.907, 4.1, 3.0552, 4.0185, 3.8085, 4.2097, 4.1687, 4.1598, 3.6024, 4.1032, 3.818, 4.6371, 4.4152, 5.0745, 6.919, 5.287, 5.4507, 5.4305, 5.8651]
x = np.array(x) 
y = np.array(y) 

""" Ajuste da curva a um polinômio """
#p1 = np.polyfit(x,y,1)  
p2 = np.polyfit(x,y,2)  
p3 = np.polyfit(x,y,3) 
p4 = np.polyfit(x, y, 4)
p5 = np.polyfit(x, y, 5)

""" Rotina para determinação do valor de R da equação da reta """
#from scipy import stats
#slope,intercept,r_value,p_value,std_err = stats.linregress(x,y)

""" Cálculo dos coeficientes de determinação dos polinômios de ordem 2 e 3 """
yfit2 = p2[0] * pow(x,2) + p2[1] * x + p2[2] 
yresid2 = y - yfit2 
SQresid = sum(pow(yresid2,2)) 
SQtotal = len(y) * np.var(y) 
R2_2 = 1 - SQresid/SQtotal 

yfit3 = p3[0] * pow(x,3) + p3[1] * pow(x,2) + p3[2] * x + p3[3] 
yresid3 = y - yfit3 
SQresid = sum(pow(yresid3,2))
SQtotal = len(y) * np.var(y) 
R2_3 = 1 - SQresid/SQtotal 

#yfit4 = p4[0] * pow(x,4) + p4[1] * pow(x,3) + p4[2] * pow(x,2) + p4[3] * x + p4[4]



""" Impressão dos Resultados """
#print('Equação da reta')
#print('Coeficientes',p1,'R2 =',pow(r_value,2))
#inverter a ordem do array
print('Polinomio de ordem 2')
print('Coeficientes',p2,'R2 =',R2_2) 
#a3 a2 a1 a0
print('Polinomio de ordem 3')
print('Coeficientes',p3,'R2 =',R2_3) 

print('Polinomio de ordem 4')
print('Coeficientes',p4) 

print('Polinomio de ordem 5')
print('Coeficientes',p5)