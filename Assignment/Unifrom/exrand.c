#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
    //Uniform random numbers
    //uniform("uni.dat", 1000000);

    //Gaussian random numbers
    gaussian("gau.dat", 100000000);

    //Mean of uniform
    //printf("%lf\n",mean("uni.dat"));

    //Mean of uniform_sqr
    //printf("%lf\n",mean_sqr("uni.dat"));

    //Var of uniform
    //printf("%lf\n",var("uni.dat"));

    //Mean of gau
    //printf("%lf\n",mean("gau.dat"));

    //Var of gau
    //printf("%lf\n",var("gau.dat"));
    
return 0;
}

