#include <stdio.h>
#include <math.h>

#define ROWS 4
#define COLS 4


void print_matrix(double matrix[ROWS][COLS]){
    for (int i = 0; i < ROWS; i++){
        for (int j = 0; j < COLS; j++){

            if(matrix[i][j]>=0) printf(" ");

            printf("%f   ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void gauss(double E[ROWS][COLS]){
    int steps = 1;
    for(int j=0; j<COLS-2;j++){
        for (int i = j; i < ROWS; i++){
            if (E[i][j] != 0){
                if(i != j){
                    // É preciso trocar linhas
                    for (int k = 0; k < COLS; k++){
                        double temp = E[i][k];
                        E[i][k] = E[j][k];
                        E[j][k] = temp;
                    }
                }
                
                // Aplicar operações elementares em linha
                // a * Lj + Lm -> Lm
                for (int m = j+1; m < ROWS; m++){
                    double a = -E[m][j] / E[j][j];
                    for(int n = j; n < COLS; n++){
                        E[m][n] += a* E[j][n];
                    }
                }

                printf("- Passo %d\n\n", steps);
                steps++;
                print_matrix(E);
                printf("------------------------------------------------------------\n\n");
                break;
            }
            
        }
    } 
}


int main(){
    // Matriz a ser escalonada
    double E[ROWS][COLS] = {
        {-5,4,-1},{-3,-3,6},{4,-7,-3}
    };
    printf("Matriz a ser escalonada: \n\n");
    print_matrix(E);
    printf("------------------------------------------------------------\n\n");
    printf("==> Passos do escalonamento: \n\n");
    gauss(E);
    // reverse_sub(E);
}