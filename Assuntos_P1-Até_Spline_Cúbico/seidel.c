#include <stdio.h>
#include <math.h>

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

    // Coeficientes do Sistema em que aplicaremos a técnica
    double A[ROWS][ROWS] = {{-1.77, 0.07, -0.69},
                            {3.42, -9.16, 4.73},
                            {4.59, -4.24, 9.85}};
    // Termos independentes
    double B[ROWS] = {-3.18, -4.84, -2.12};
    // Estimativa de soluções
    double est_ini[ROWS] = {-4.88, 1.8, 1.28};
    // Iterações
    int n = 18;

    seidel(A, B, est_ini, n);
}
