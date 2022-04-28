#include <stdio.h>
#include <math.h>

void newton(double (*f)(double), double(*df)(double), double x0, int n){
    double der = df(x0);
    // Verifica se a derivada é 0, pois não podemos dividir por 0!
    if(der == 0){
        printf("Escolha outra estimativa inicial!");
    }else{
        for(int i = 0; i < n; i++){
            double x1 = x0 - f(x0) / der;
            der = df(x1);
            if(der == 0){
                printf("x_%d = %.7f\n\nDerivada igual a 0!", i+1, x1);
                return;
            }else{
                printf("x_%d = %.7f\n", i+1, x1);
            }
            x0 = x1;
        }
    }
}


double f(double x){
    double R = 9.42, V = 1219.0;

    return M_PI*pow(x,2)*((3*R-x)/3)-V;
}

// Derivada da função, que também precisamos para o método de Newton
double df(double x){
    return M_PI*pow(x,2);
}

int main() {
    // Estimativa Inicial
    double x0 = 4.73;
    // Número de Iterações
    int n = 5;

    // Chamada do Método de Newton
    newton(f, df, x0, n);
}