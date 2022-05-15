def areaTrapezio(B, b, h):
    return ((B+b)*h)/2

def modulo(x):
    if x < 0:
        return x*-1
    else:
        return x



x = [0.1, 0.286, 0.382, 0.41, 0.552, 1.863, 2.479, 2.683, 2.834, 3.033, 3.085, 3.223, 3.453, 3.581, 3.878, 3.899, 4.046, 4.126, 4.39, 4.692, 4.756]
y = [1.549, 2.202, 2.5, 2.576, 2.865, 2.019, 2.227, 2.45, 2.641, 2.876, 2.924, 2.997, 2.857, 2.599, 1.624, 1.552, 1.135, 1.018, 1.459, 2.821, 2.967]

somaAreas = 0
for i in range(len(x)-1):
    somaAreas += areaTrapezio(y[i], y[i+1], modulo(x[i] - x[i+1]))

print(somaAreas)