#include <stdio.h>
#include <math.h>

void false_position(double (*f)(double), double a, double b, int n){
    double fa = f(a);
    double fb = f(b); 

    if(fa * fb >= 0){
        printf("O Teorema de Bolzano não sabe dizer se existe raiz para f no intervalo [%.16f, %.16f]", a, b);
        return;
    }else{
        for(int i=0; i < n; i++){
            double x = (a * fb - b * fa) / (fb - fa);
            double fx = f(x);

            printf("x_%d = %.16f\n", i+1, x);

            if(fx == 0){
                printf("A raíz de f foi encontrada: ela é x = %.16f", x);
                return;
            }

            if(fa * fx <= 0){
                b = x;
                fb = fx;
            }else{
                a = x;
                fa = fx;
            }
            
        }
    }
}


// Função Exemplo: x²-2
double f(double x){
    return pow(x,2) - 2;
}


int main(){
    //Intervalo inicial
    double a = 1.0;
    double b = 2.0;
    // Número de iterações
    int n = 10;

    false_position(f, a, b, n); 
}