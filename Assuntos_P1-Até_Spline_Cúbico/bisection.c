#include <stdio.h>
#include <math.h>

void bisection(double (*f)(double), double a, double b, int n)
{
    if (f(a) * f(b) >= 0)
    {
        printf("Nao eh possivel usar Bolzano para garantir a existencia de uma raiz em [%f, %f]", f(a), f(b));
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            double m = 0.5 * (a + b);
            printf("x_%d = %.7f\n", i + 1, m);
            if (f(m) == 0)
            {
                printf("Você encontrou uma raíz r = %.7f", m);
            }
            else
            {
                f(a) * f(m) < 0 ? (b = m) : (a = m);
            }
        }
    }
}

double f(double x)
{
    double g = 9.81, c = 15.31, v = 35.69, t = 7.16;

    return (g * x / c) * (1 - pow(M_E, (-(c / x) * t))) - v;
}

int main()
{
    // Ponto inicial do Intervalo
    double a = 30.57;
    // Ponto final do Intervalo
    double b = 195.41;
    // Número de Iterações
    double n = 12;

    bisection(f, a, b, n);
}