#include<stdio.h>
#include<math.h>

void newton(double (*f)(double), double (*df)(double), double x0, int n){
    for(int i; i< n; i++){
        double dfx0 = df(x0);
        if(dfx0 == 0){
            printf("Divisão por zero, Não foi possivel a interação %d do método de Newton.", i+1);
            return;
        }else{
            x0 = x0 - f(x0)/dfx0;
            printf("x_%d = %.16f\n", i + 1, x0);
        }
    }
}
int main(int argc, char *argv[]){
    /*double f(double x){
        return x*x*x-2;
    }
    double df(double x){
        return 3 * x * x;
    }
    double x0 = 1;
    int n = 12;*/

    /*double f(double x){
        double e = 2.71828182845904523530287;
        return pow(e, x) - 2*pow(x, 2) + x - 1.5;
    }
    double df(double x){
        double e = 2.71828182845904523530287;
        return pow(e, x) - 4*x + 1;
    }
    double x0 = 0.45873;
    int n = 12;*/

    /*double f(double x){
        //double e = 2.71828182845904523530287;
        //double pi = 3.14159265358979323846;
        return 2*(x+1)*(x-1/2)*(x-1);
    }
    double df(double x){
        //double e = 2.71828182845904523530287;
        //double pi = 3.14159265358979323846;
        return 3*pow(x,2) -2*x -2;
    }
    double x0 = 0.10161;
    int n = 5;*/

    /*double f(double x){
        return 2 * (x + 1) * (x - 0.5) * (x - 1);
    }
    double df(double x){
        return 6*pow(x,2) -2*x -2;
    }
    double x0 = 0.01274;
    int n = 5;*/

    /*double f(double x){
        return pow(x,3) - 7*pow(x,2) + 14*x - 7;
    }
    double df(double x){
        return 3*pow(x,2) - 14*x + 14;
    }
    double x0 = 0.29698;
    int n = 5;*/

    /*double f(double x){
        return (double) sqrt(x) - cos(x);
    }
    double df(double x){
        return (double) 1/(sqrt(x)*2) + sin(x);
    }
    double x0 = 0.04722;
    int n = 5;*/

    /*double f(double x){
        return pow(x, 4) - 2*pow(x,3) - 3*pow(x, 2) + 3*x + 2;
    }
    double df(double x){
        return 4*pow(x,3) - 6*pow(x,2) - 6*x + 3;
    }
    double x0 = -1.92173;
    int n = 5;*/

    /*double f(double x){
        return x + 1 -3 * sin(x);
    }
    double df(double x){
        return 1 - 3 * cos(x);
    }
    double x0 = -1.03;
    int n = 5;*/

    /* double f(double x){
        double e = 2.71828182845904523530287;
        //double pi = 3.14159265358979323846;
        return pow(e, 5*x) - 2;
    }
    double df(double x){
        double e = 2.71828182845904523530287;
        //double pi = 3.14159265358979323846;
        return 5*pow(e, 5*x);
    }
    double x0 = -1.16076274;
    int n = 700; */

    //p1
    double f(double x){
        // /double e = 2.71828182845904523530287;
        //double pi = 3.14159265358979323846;
        return 4*pow(x, 2) - ;
    }
    double df(double x){
        //double e = 2.71828182845904523530287;
        //double pi = 3.14159265358979323846;
        return 2*x;
    }
    double x0 = -2.4257 ;
    int n = 5;

    newton(f, df, x0, n);
}