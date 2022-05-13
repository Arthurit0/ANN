#include <stdio.h>
#include <math.h>

void newton(double (*f)(double), double (*df)(double), double x0, double n)
{
    for (int i = 0; i < n; i++)
    {
        double xn;
        xn = x0 - f(x0) / df(x0);
        x0 = xn;
        printf("x_%d = %.16f\n", i + 1, xn);
    }
}

double f(double x)
{
    double g = 9.81, c = 15.31, v = 35.69, t = 7.16;

    return (g * x / c) * (1 - pow(M_E, (-(c / x) * t))) - v;
}

// Derivada da função, que também precisamos para o método de Newton
double df(double x)
{
    double g = 9.81, c = 15.31, v = 35.69, t = 7.16;

    return ((x * (1 - pow(M_E, -(c / x) * t))) / c);
}

int main(int argc, char *argv[])
{

    double x0 = 29.99;
    int n = 5;

    newton(f, df, x0, n);
}