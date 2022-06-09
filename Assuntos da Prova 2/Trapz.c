#include <math.h>
#include <stdio.h>

void trapz(double (*f)(double), double a, double b, int n) {
    double soma = 0;
    double h = (double)(b - a) / (double)n;
    for (int k = 0; k < n; k++) {
        soma += f(a + k * h);
    }
    soma *= 2;
    soma += f(a);
    soma += f(b);
    soma *= (h / 2.0);

    printf("\nArea aprox: %.16lf\n", soma);
}

// Exemplo 1
double func1(double x) { return exp(-x * x); }

// Exemplo 2
double func2(double x) { return cos(x * x); }

// Exemplo 3
double func3(double x) { return x * x + 1; }

int main() {
    double a = -1, b = 1;
    int n = 1000000000;  // Número de Intervalos / Trapézios

    trapz(func2, a, b, n);
}