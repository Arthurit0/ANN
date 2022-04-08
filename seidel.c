#include <stdio.h>

#define ROWS 3

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
            printf("x_%d^(%d) = %.16f\t",i+1,k+1,bi);
            // next[i]=bi;
            est[i]=bi;
        }
        printf("\n");
        // Atualizar o valor chute não é necessário como no método de Jacobi
    }
    
}

int main(int argc, char const *argv[]){
    
    // Coeficientes do Sistema em que aplicaremos a técnica
    double A[ROWS][ROWS]={{4,1,-1},{-1,3,1},{1,-1,5}};
    // Termos independentes
    double B[ROWS] = {5,6,4};
    // Estimativa de soluções
    double est_ini[ROWS] = {-1,-1,-1};
    // Iterações
    int n = 10;

    seidel(A,B,est_ini, n);
}
