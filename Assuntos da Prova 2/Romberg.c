#include <math.h>
#include <stdio.h>

#define error_order 32
// numElemsFirstCol deve ser error_order / 2
#define numElemsFirstCol error_order / 2

// Método da regra dos trapézios
double trapz(double (*f)(double), double a, double b, int n) {
    double soma = 0;
    double h = (double)(b - a) / (double)n;
    for (int k = 1; k < n; k++) {
        soma += f(a + k * h);
    }
    soma *= 2;
    soma += f(a);
    soma += f(b);
    soma *= (h / 2.0);
    return soma;
}

void romberg(double array[]) {
    // i=0 está calculando a coluna f2
    int numCols = numElemsFirstCol - 1;
    for (int i = 0; i < numCols; i++) {
        for (int j = 0; j < numCols; j++) {
            double numer = pow(2, (i + 1) * 2) * array[j + 1] - array[j];
            double denom = pow(2, (i + 1) * 2) - 1;
            array[i] = numer / denom;
        }
    }

    printf("Aprox O(h^%d) = %.16f\n", error_order, array[0]);
}

double f(double x) {
    return exp(-x * x);
}

int main(int argc, char const *argv[]) {
    // Exemplo:
    // Aproximar int exp(-x*x), de 0 a 1
    double a = 0, b = 1, h = 0.5;

    int n = (int)((b - a) / h);

    printf("n = %.16f\n\n", (double)n);
    printf("Error_order: %d \nnumElemensFirstCol: %d\n\n", error_order, numElemsFirstCol);

    double coluna_F1[numElemsFirstCol];
    for (int i = 0; i < numElemsFirstCol; i++) {
        coluna_F1[i] = trapz(f, a, b, (i + 1) * n);
    }
    romberg(coluna_F1);

    return 0;
}
