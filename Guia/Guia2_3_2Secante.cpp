#include <cstdio> //printf
#include <cmath> //cos, std::abs

// No termine

double f(double x) {
    int D=0.75; 
    int expo=-(x/(2*M_PI)) ;
    int euler_elevado=pow( M_E , expo);
    return (0.5 + ( (0.5*euler_elevado) * sin(x)) - D );

}

void secant(double p0, double p1, double TOL, int Nmax) {
    double p = 0; //aproximaciÃ³n actual
    for(int i = 0; i < Nmax; i++) {
        p = p1 - f(p1) * ( p1 - p0) / ( f(p1) - f(p0) );
        printf("%d\t%.10f\t%.10f\t%.16f\t%.20f\n", i, p0, p1, p, std::abs(p - p1));
        if(std::abs(p - p1) < TOL) break;
        p0 = p1;
        p1 = p;
    }
}

int main() {
    // printf(" Euler : %.20f  Pi : %.20f \n",M_E,M_PI);
    secant(0.65625 , 0.75625 , 10e-12, 10);
    return 0;
}