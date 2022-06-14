#include <stdio.h>
#include <math.h>

void false_position(double (*f)(double), double a, double b, int n, double tol)
{
    if (f(a) * f(b) < 0)
    {

        for (int i = 0; i < n; i++)
        {
            double fa = f(a);
            double fb = f(b);
            double c;
            c = (a * fb - b * fa) / (fb - fa);
            if (f(c) == 0)
            {
                printf("Voce encontrou uma raiz para f. Ela é: %.16f\n", c);
                return;
            }

            printf("x_%d = %.15f \n", i + 1, c);
            if (fa * f(c) < 0)
            {
                b = c;
            }
            else
            {
                a = c;
            }
        }
    }
    else
    {
        printf("O intervalo [ %.16f, %.16f] nao serve\n", a, b);
    }
}

int main()
{
    /*double f(double x){
        return x - pow(2,-x);
    }
    double a = 0.0539;
    double b = 1.0293;
    int max_iter = 5;
    double tol = 0.00001;*/

    /*double f(double x){
        return pow(x, 2) - 3;
    }
    double a = -2.0251;
    double b = -0.6298;
    int max_iter = 5;
    double tol = 0.00001;*/

    /*double f(double x){
        return pow(x, 2) - 7;
    }
    double a = 2.3257;
    double b = 3.169;
    int max_iter = 5;
    double tol = 0.00001;*/

    /*double f(double x){
        return pow(x, 3) - 7*pow(x, 2) + 14*x - 7;
    }
    double a = 0.1187;
    double b = 4.4263;
    int max_iter = 5;
    double tol = 0.00001;*/

    /*double f(double x){
        return 2*(x+1)*(x-0.5)*(x-1);
    }
    double a = -1.8545;
    double b = 1.2668;
    int max_iter = 5;
    double tol = 0.00001;*/

    /* double f(double x){
        double e = 2.71828182845904523530287;
        return pow(e, 5*x) - 2;;
    }
    double a = -0.92732;
    double b = 1.91364;
    int max_iter = 6400;
    double tol = 0.00001; */

    //p1
    double f(double x){
        //double e = 2.71828182845904523530287;
        return 2*(x+1)*(x-0.5)*(x-1);
    }
    double a = 0.7036;
    double b = 1.2688;
    int max_iter = 5;
    double tol = 0.00001;

    false_position(f, a, b, max_iter, tol);
}