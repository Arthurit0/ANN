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

    return sqrt(2*9.81*x)*tanh((sqrt(2*9.81*x)/(2*8.36))*4.3)-8.83;
}

int main(){
    // Ponto inicial do Intervalo
    double a = 0.38;
    // Ponto final do Intervalo
    double b = 18.82;
    // Número de Iterações
    double n = 12;

    bisection(f, a, b, n);

}