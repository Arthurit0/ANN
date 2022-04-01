#include <stdio.h>

void bisection(double *(f)(double), double a, double b, int n) {
    if (f(a) * f(b) >= 0){
        printf("Nao eh possivel usar Bolzano para garantir a existencia de uma raiz em [%f, %f]", a, b);
    }else{
        for(int i=0; i<n; i++){
            double m=0.5*(a+b);
            printf
        }
    }
}

int main(){
    // Exemplo 1: f(x) = x³-2, [0,2]
    double f(double x){
        return x*x*x-2.0;
    }

    // Exemplo 2: Crescimento populacional
    double P(double x){
        return 1000000 + exp(x) + (537142 / x) * (exp(x) - 1) - 1863961;
    }

    double a1 = 0.001;
    double b1 = 2;
    int n1 = 20;

    // bisection(f, a, b, n);

}