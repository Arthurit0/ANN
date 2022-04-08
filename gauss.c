#include <stdio.h>
#include <math.h>

#define ROWS 4
#define COLS 5

void print_matrix(double matrix[ROWS][COLS]){
    for (int i = 0; i < ROWS; i++){
        for (int j = 0; j < COLS; j++){
            printf("%f\t", matrix[i][j]);
        }
        printf("\n");
    }
    
}

void gauss(double E[ROWS][COLS]){
    for(int j=0; j<COLS-2;j++){
        for (int i = j; i < ROWS; i++){
            if (E[i][j] != 0){
                if(i != j){
                    for (int k = 0; k < COLS; k++){
                        double temp = E[i][k];
                        E[i][k] = E[j][k];
                        E[j][k] = temp;
                    }
                    
                }

                
                // Aplicar operações elementares em linha
                // num * Lj + Lm -> Lm
                for (int m = j+1; m < COLS; m++){
                    double a = -E[m][j] / E[j][j];
                    for(int n = j; n < COLS; n++){
                        E[m][n] = a* E[j][n] + E[m][n];
                    }
                }
                print_matrix(E);
                printf("\n");
                
            }
            break;
        }
        
    } 
}


int main(){
    // Matriz a ser escalonada
    double E[ROWS][COLS] = {
        {2,4,6,2,4},
        {1,2,-1,3,8},
        {-3,1,-2,1,-2},
        {1,3,-3,-2,6}
    };
    print_matrix(E);
    gauss(E);
    // reverse_sub(E);
}