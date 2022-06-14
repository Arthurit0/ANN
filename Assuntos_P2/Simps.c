#include <math.h>
#include <stdio.h>

void simps(double (*f)(double), double a, double b, int n) {
    if (n % 2 != 0) {
        printf("O número de subintervalos deve ser par!");
        return;
    }
    int numParabolas = n / 2;
    double soma = 0;
    double h = (double)(b - a) / (double)n;
    for (int i = 0; i < numParabolas; i++) {
        double x0 = a + (2 * i) * h;
        double x1 = a + (2 * i + 1) * h;
        double x2 = a + (2 * i + 2) * h;
        soma += (f(x0) + 4 * f(x1) + f(x2));
    }
    soma *= (h / 3.0);
    printf("Area aprox: %.16f\n", soma);
}

// Exemplo 1
double func1(double x) { return exp(-x * x); }

// Exemplo 2
double func2(double x) { return cos(x * x); }

// Exemplo 3
double func3(double x) { return x * x + 1; }

int main() {
    double a = 0, b = 1;
    int n = 100;  // Número de Intervalos

    simps(func1, a, b, n);
}