#include <stdio.h>
#include <math.h>


float f(float a)
{
    return a*a + 7*a -7;
}

int main ()
{
    // To find the roots of x^2 +7x -7 =0 
    // We know that for any equation ax^2 +bx +c =0 ,
    // if b^2-4ac >=0 ; then the real roots of equation are
    // (-b-sqrt{b^2-4ac})/2a and (-b+sqrt{b^2-4ac})/2a

    float root1,root2;
    root1 = (-7-sqrt(49-4*1*(-7)))/2*1 ;
    root2 = (-7+sqrt(49-4*1*(-7)))/2*1 ;
    //Here we can also say that root1 is smaller than root2 as
    // for root1 we used '-' and '+' for the latter.

    printf("The roots are %0.2f,%0.2f",root1,root2);  //prints the roots rounded off to 2 decimals.

    FILE *pointer;
    pointer = fopen("Data.txt","w");
    fprintf(pointer,"\tx\t\t\t\ty\n");
    float a=0;
    for(a=root1-2;a<root2+2;a=a+0.02)
    {
        fprintf(pointer,"%f\t\t%f\n",a,f(a));
    }
}
