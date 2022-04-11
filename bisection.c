#include <stdio.h>
#include <math.h>

void bisection(double (*f)(double), double a, double b, int n) {
    if (f(a) * f(b) >= 0){
        printf("Nao eh possivel usar Bolzano para garantir a existencia de uma raiz em [%f, %f]", f(a), f(b));
    }else{
        for(int i=0; i<n; i++){
            double m=0.5*(a+b);
            printf("x_%d = %.7f\n",i+1,m);
            if(f(m) == 0){
                printf("Você encontrou uma raíz r = %.7f", m);
            }else{
                f(a)*f(m) < 0 ? (b = m) : (a = m);
            }
        }
    }
}

double f(double x) {
    return pow(2.7182818,x)-2*pow(x,2)+x-1.5;
}

// Exemplo 2: Crescimento populacional
// double P(double x){
//     return 1000000 + exp(x) + (537142 / x) * (exp(x) - 1) - 1863961;
// }

int main(){
    // Ponto inicial do Intervalo
    double a = -0.28075;
    // Ponto final do Intervalo
    double b = 0.95019;
    // Número de Iterações
    double n = 12;

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