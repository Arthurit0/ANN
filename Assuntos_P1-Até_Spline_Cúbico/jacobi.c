#include <stdio.h>

#define ROWS 3

void jacobi(double A[ROWS][ROWS], double B[ROWS], double est[ROWS], int n){
    double next[ROWS];
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
            next[i]=bi;
        }
        printf("\n");
        // Atualizar chute
        for (int i = 0; i < ROWS; i++)
        {
            est[i] = next[i];
        }
    }
}

int main(int argc, char const *argv[]){
    
    // Coeficientes do Sistema em que aplicaremos a técnica
    double A[ROWS][ROWS]={{3.5, -0.66, -1.25},
                          {1.39, 7.39, -4.4},
                          {0.52, 0.4, 2.52}
};
    // Termos independentes
    double B[ROWS] = {-4.27, -1.38, -0.32};
    // Estimativa de soluções
    double est_ini[ROWS] = {3.48, 1.0, 3.46};
    // Iterações
    int n = 18;

    jacobi(A,B,est_ini, n);
}
