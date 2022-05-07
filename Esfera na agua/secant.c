#include <stdio.h>
#include <math.h>

void secante(double (*f)(double), double x0, double x1, int n){
    double fx0 = f(x0);
    double fx1 = f(x1);

    // f(x0) = f(x1) -> f(x0) - f(x1) = 0, denominador zero!
    if(fx0 == fx1){
        printf("Escolha outras estimativas iniciais!\n\n");
    }else{
        for(int i = 0; i < n; i++){
            double x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
            // Atualiza valores para próxima iteração
            fx0 = fx1;
            fx1 = f(x2);
            x0 = x1;
            x1 = x2;
            if(fx0 == fx1){
                printf("x_%d = %.7f\n\nParei pois o denominador seria zero!", i+2, x2);
            }else{
                printf("x_%d = %.7f\n", i+2, x2);
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

int main() {
    // Estimativa inicial 1
    double x0 = 0;
    // Estimativa inicial 2
    double x1 = 2.4;
    // Número de iterações
    int n = 5;

    secante(f, x0, x1, n);
}