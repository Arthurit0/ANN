#include <stdio.h>
#include <math.h>

void false_position(double (*f)(double), double a, double b, int n){
    double fa = f(a);
    double fb = f(b); 

    if(fa * fb >= 0){
        printf("O Teorema de Bolzano não sabe dizer se existe raiz para f no intervalo [%.7f, %.7f]", a, b);
        return;
    }else{
        for(int i=0; i < n; i++){
            double x = (a * fb - b * fa) / (fb - fa);
            double fx = f(x);

            printf("x_%d = %.7f\n", i+1, x);

            if(fx == 0){
                printf("A raíz de f foi encontrada: ela é x = %.7f", x);
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


double f(double t){
    double n = 116069052, lambda = 1.41*pow(10,-10);
                                                // 25%
    return (n+1)/(1+n*pow(M_E,-lambda*(n+1)*t))-(0.25*n);
}

int main(){
    //Intervalo inicial
    double a = 0;
    double b = 2270;
    // Número de iterações
    int n = 11;

    false_position(f, a, b, n); 
}