#include <stdio.h>

#define ROWS 3

void seidel(double A[ROWS][ROWS], double B[ROWS], double est[ROWS], int n)
{
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < ROWS; i++)
        {
            double bi = B[i];
            for (int j = 0; j < ROWS; j++)
            {
                if (j != i)
                {
                    bi -= A[i][j] * est[j];
                }
            }
            bi /= A[i][i];
            printf("x_%d^(%d) = %.7f\t", i + 1, k + 1, bi);
            // next[i]=bi;
            est[i] = bi;
        }
        printf("\n");
        // Atualizar o valor chute não é necessário como no método de Jacobi
    }
}

int main(int argc, char const *argv[])
{
    double k1 = 58.11,
           k2 = 65.57,
           k3 = 79.14,
           m1 = 3.12,
           m2 = 2.3,
           m3 = 2.48,
           g = 9.81;
    // Coeficientes do Sistema em que aplicaremos a técnica
    double A[ROWS][ROWS] = {{k1 + k2, -k2, 0}, {-k2, k2 + k3, -k3}, {0, -k3, k3}};
    // Termos independentes
    double B[ROWS] = {m1 * g, m2 * g, m3 * g};
    // Estimativa de soluções
    double est_ini[ROWS] = {50, 50, 50};
    // Iterações
    int n = 200;

    seidel(A, B, est_ini, n);
}
