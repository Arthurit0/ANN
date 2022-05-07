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
    double m1 = 176,
           m2 = 80,
           m3 = 74,
           u1 = 0.16,
           u2 = 0.44,
           u3 = 0.47,
           g = 9.81,
           ang = 0.733038, // 42 graus em rad
        F1h = m1 * g * (sin(ang)),
           F2h = m2 * g * (sin(ang)),
           F3h = m3 * g * (sin(ang)),
           F1v = m1 * g * (cos(ang)),
           F2v = m2 * g * (cos(ang)),
           F3v = m3 * g * (cos(ang)),
           f1 = u1 * F1v,
           f2 = u2 * F2v,
           f3 = u3 * F3v;

    printf("sen %.7lf cos %.7lf", F1h, F1v);

    // Coeficientes do Sistema em que aplicaremos a técnica
    double A[ROWS][ROWS] = {{m3, 1, 0},
                            {m2, -1, 1},
                            {m3, 0, -1}};
    // Termos independentes
    double B[ROWS] = {F1h - f1, F2h - f2, F3h - f3};
    // Estimativa de soluções
    double est_ini[ROWS] = {50, 50, 50};
    // Iterações
    int n = 200;

    seidel(A, B, est_ini, n);
}
