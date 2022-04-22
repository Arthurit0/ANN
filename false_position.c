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


double f(double x){
    return ((9.81*x)/15.73)*(1-pow(M_E,(-15.73/x)*9.4))-30.2;
}

int main(){
    //Intervalo inicial
    double a = 25.22;
    double b = 195.97;
    // Número de iterações
    int n = 11;

    false_position(f, a, b, n); 
}