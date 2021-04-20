#include <cstdio> //printf
#include <cmath> //sin, cos
//OJO ESTE Y EL PYTHON SON LO MISMO SOLO ESTABA COMPROBANDO

double f(double x) { 
    return pow(x,4)-16*pow(x,3)+78*pow(x,2)-412*x+624; 

}
double df(double x) { 
    double h=10e-4;
    double xh=x+h;
    return ((f(xh)-f(x))/h);    
}
void Newton(double p0, double TOL, int Nmax){
    double p = 0; //p will hold the current approximation
    for(int i=0; i<Nmax; i++){
        p = p0 - f(p0)/df(p0);
        printf("%d\t%.10f\t%.10f\t%.10f\n", i, p0, p, std::abs(p - p0));
        if(std::abs(p - p0) < TOL) break;
        p0 = p;
    }
}
int main() {		
    Newton(-6, 1e-6, 100);
    return 0;
}