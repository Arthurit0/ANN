#include <stdio.h>
#include <math.h>

void bisection(double (*f)(double), double a, double b, int n) {
    if (f(a) * f(b) >= 0){
        printf("Nao eh possivel usar Bolzano para garantir a existencia de uma raiz em [%f, %f]", a, b);
    }else{
        for(int i=0; i<n; i++){
            double m=0.5*(a+b);
            printf("x_%d = %.16f\n",i+1,m);
            if(f(m) == 0){
                printf("Você encontrou uma raíz r = %.16f", m);
            }else{
                f(a)*f(m) < 0 ? (b = m) : (a = m);
            }
        }
    }
}

// Exemplo 1: f(x) = x³-2, [0,2]
double f(double x) {
    return pow(x,3)-2.0;
}

// Exemplo 2: Crescimento populacional
double P(double x){
    return 1000000 + exp(x) + (537142 / x) * (exp(x) - 1) - 1863961;
}

int main(){
    // Ponto inicial do Intervalo
    double a = 0;
    // Ponto final do Intervalo
    double b = 2;
    // Número de Iterações
    double n = 10;

    // Ponto inicial do Intervalo (ex2)
    // double a1 = 0.001;
    // Ponto final do Intervalo (ex2)
    // double b1 = 2;
    // Número de Iterações (ex2)
    // int n1 = 20;

    printf("\n1. Exemplo da função x³-2, [0,2]:\n\n");
    bisection(f, a, b, n);
    // printf ("\n2. Problema do crescimento populacional:\n\n");
    // bisection (P, a1, b1, n1);
}