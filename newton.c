#include <stdio.h>
#include <math.h>

void newton (double (*f)(double),double (*df)(double),double x0, int n) {
    for (int i = 0; i < n; i++){
        double dfx0 = df(x0);
        if (dfx0 == 0) {
            printf("Divisão por zero, não foi possível executar a iteração %d do método de Newton.", i+1);
            return;
        } else {
            x0 = x0 - f(x0) / dfx0;
            printf("x_%d = %.7f\n", i + 1, x0);
        }
    }
}


double f(double x){
    return 12*pow(x,2)-102.76*x+142.951;
}

// Derivada da função, que também precisamos para o método de Newton
double df(double x){
    return 24*x-102.76;
}

int main() {
    // Estimativa Inicial
    double x0 = 2.09;
    // Número de Iterações
    int n = 5;

    // Chamada do Método de Newton
    newton(f, df, x0, n);
}