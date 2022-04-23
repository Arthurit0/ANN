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
<<<<<<< Updated upstream
    return ((9.81*x)/15.73)*(1-pow(M_E,(-15.73/x)*9.4))-30.2;
=======
    return 2*(x+1)*(x-0.5)*(x-1);
>>>>>>> Stashed changes
}

// Derivada da função, que também precisamos para o método de Newton
double df(double x){
    return (9.81/15.73)*(-pow(M_E,-147.862/x)-((147.862*pow(M_E,-147.862/x))/x)+1);
}

int main() {
    // Estimativa Inicial
<<<<<<< Updated upstream
    double x0 = 27.97;
=======
    double x0 = -0.03173;
>>>>>>> Stashed changes
    // Número de Iterações
    int n = 5;

    // Chamada do Método de Newton
    newton(f, df, x0, n);
}