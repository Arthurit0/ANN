#include<stdio.h>
#include<math.h>

void secant(double (*f)(double), double x0, double x1, int n){
    for (int i = 0; i < n; i++)
    {
        double fx0 = f(x0);
        double fx1 = f(x1);
        if (fx0 == fx1)
        {
            printf("Divisao por zero");
            return;
        }
        double x2;
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
        x0 = x1;
        x1 = x2;
        printf("x_%d = %.16f\n", i + 1, x2);
    }
}

int main(int argc, char *argv[]){
    /*double f(double x){
        return pow(x, 2) - 4*x + 2 - log(x);
    }

    double x0 = 1.02346;
    double x1 = 4.1604;
    int n = 5;*/

    /*double f(double x){
        return x - pow(2, -x);
    }

    double x0 = 0.35324;
    double x1 = 1.09999;
    int n = 5;*/

    /*double f(double x){
        return pow(x, 2) - 5;
    }

    double x0 = 1.53061;
    double x1 = 2.87249;
    int n = 5;*/

    /*double f(double x){
        return sqrt(x) - cos(x);
    }

    double x0 = 0.12389;
    double x1 = 1.24314;
    int n = 5;*/

    /*double f(double x){
        double e = 2.71828182845904523530287;
        double pi = 3.14159265358979323846;
        return pi*x - pow(e, x);
    }

    double x0 = 0.86031;
    double x1 = 1.89624;
    int n = 5;*/

    /*double f(double x){
        double e = 2.71828182845904523530287;
        double pi = 3.14159265358979323846;
        return pow(e, x) - 2 * pow(x, 2) + x - 1.5;
    }

    double x0 = -0.06897;
    double x1 = 2.70272;
    int n = 5;*/

    /*double f(double x){
        //double e = 2.71828182845904523530287;
        //double pi = 3.14159265358979323846;
        return pow(x, 2) - 3;
    }

    double x0 = -2.35176;
    double x1 = -0.93197;
    int n = 5;*/

    /* double f(double x){
        //double e = 2.71828182845904523530287;
        //double pi = 3.14159265358979323846;
        return pow(x, 2) - 3;
    }

    double x0 = -2.35176;
    double x1 = -0.93197;
    int n = 5; */
    
    double f(double x){
        //double e = 2.71828182845904523530287;
        //double pi = 3.14159265358979323846;
        return pow(x, 2) - 7;
    }

    double x0 = 2.10146;
    double x1 = 3.00242;
    int n = 6;

    secant(f , x0, x1, n);
}