def testePontos(x, y):
    for i in range(len(x)):
        try:
            print(f'i: {i}')
            print(f'x1-x0  = {x[1+i]} - {x[0+i]} = {x[1+i] - x[0+i]}')
            print(f'x2-x1 = {x[2+i]} - {x[1+i]} = {x[2+i] - x[1+i]}')
            if(x[1+i] - x[0+i]) == (x[2+i] - x[1+i]):
                return([[x[0+i], x[1+i], x[2+i]], [y[0+i], y[1+i], y[2+i]]])
        except:
            return 'erro nao existem 3 pontos que satisfação x1−x0=x2−x1'


x = [0.905, 1.051, 1.197, 2.8735, 4.55]
y = [2.932, 2.784, 2.601, 2.691, 2.218]
print(testePontos(x, y))