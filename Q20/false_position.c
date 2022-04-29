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
    double r = 1.24, ps = 131.31;

    double vs = (4*M_PI*pow(r,3))/3; // Volume da esfera
    double v = vs - ((ps*vs)/1000); // Volume acima da agua
    return ((M_PI*pow(x,2))/3)*(3*r-x)-v; // Formula
}

int main(){
    //Intervalo inicial
    double a = 0;
    double b = 2.48;
    // Número de iterações
    int n = 11;

    false_position(f, a, b, n); 
}