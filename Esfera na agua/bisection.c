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
    double r = 1.24, ps = 131.31;

    double vs = (4*M_PI*pow(r,3))/3; // Volume da esfera
    double v = vs - ((ps*vs)/1000); // Volume acima da agua
    return ((M_PI*pow(x,2))/3)*(3*r-x)-v; // Formula
}

int main(){
    // Ponto inicial do Intervalo
    double a = 0;
    // Ponto final do Intervalo
    double b = 2.48;
    // Número de Iterações
    double n = 12;

    bisection(f, a, b, n);
}