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
    double g = 9.81, L = 8.36, t = 4.3;

    return sqrt(2*g*x)*tanh((sqrt(2*g*x)/(2*L))*t)-8.83;
}

// Derivada da função, que também precisamos para o método de Newton
double df(double x){
    double g = 9.81, L = 8.36, t = 4.3;
    double x1 = (sqrt(x)*t*sqrt(g))/sqrt(2)*L;

    return ((sqrt(x)*tanh(x1))/(sqrt(2)*sqrt(g)))+(x*t*pow(sinh(x1),2))/2*L;
}

int main() {
    // Estimativa Inicial
    double x0 = 0.51;
    // Número de Iterações
    int n = 5;

    // Chamada do Método de Newton
    newton(f, df, x0, n);
}