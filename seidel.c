#include <stdio.h>

#define ROWS 4

void seidel(double A[ROWS][ROWS], double B[ROWS], double est[ROWS], int n){
    for (int k = 0; k < n; k++){
        for (int i = 0; i < ROWS; i++){
            double bi=B[i];
            for (int j = 0; j < ROWS; j++){
                if(j != i){
                    bi -= A[i][j]* est[j];

                }
            }
            bi /= A[i][i];
            printf("x_%d^(%d) = %.7f\t",i+1,k+1,bi);
            // next[i]=bi;
            est[i]=bi;
        }
        printf("\n");
        // Atualizar o valor chute não é necessário como no método de Jacobi
    }
    
}

int main(int argc, char const *argv[]){
    
    // Coeficientes do Sistema em que aplicaremos a técnica
    double A[ROWS][ROWS]={{-9.73, 0.31, -4.36, 3.26},
                          {2.83, -6.63, 1.83, 0.18},
                          {1.16, -0.82, 7.73, -3.95},
                          {-2.17, -0.93, 3.22, 8.12}};
    // Termos independentes
    double B[ROWS] = {-1.84, -2.41, 0.46, -4.29};
    // Estimativa de soluções
    double est_ini[ROWS] = {3.25, -1.94, 3.84, -3.47};
    // Iterações
    int n = 16;

    seidel(A,B,est_ini, n);
}
