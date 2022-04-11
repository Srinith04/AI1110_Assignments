#include <stdio.h>
#include <stdlib.h>

float xcoordi(int *arr,int *brr)
{
    float x = (float)((arr[1]*brr[2] - brr[1]*arr[2]))/(arr[0]*brr[1] - brr[0]*arr[1]);
    if(x==0) return 0;   //To make sure that we dont get -0.00 as value.
    else return x; 
}

float ycoordi(int *arr,int *brr)
{
    float y = (float)((arr[2]*brr[0] - brr[2]*arr[0]))/(arr[0]*brr[1] - brr[0]*arr[1]);
    if(y==0) return 0;   //To make sure that we dont get -0.00 as value.
    else return y; 
}

void GrossIncome(float a,float b,float *arr,int i)
{
    if( 2*a+b-90<=0 && a+2*b-80<=0 && a+b-50<=0 && a>=0 && b>=0) //Required conditions.
    {
        arr[i] = 48*a + 40*b ;
    }
    else
    {
        arr[i]=0;  //else zero.
    }
    return ;
}

int main()
{
    // If every line is of form ax+by+c = 0 ; then for our given lines
    // let us store those values in a 2D array.

    int arr[5][3] = { 2,1,-90 , 1,2,-80 , 1,1,-50 , 1,0,0 , 0,1,0 };

    float points[10][2]; //2D array for storing point of intersections of lines.
    
    int a=0;
    for(int i=0;i<4;i++)
    {
        for(int j=i+1;j<5;j++)
        {
            points[a][0] = xcoordi(arr[i],arr[j]);  //x-coordinate
            points[a][1] = ycoordi(arr[i],arr[j]);  //y-coordinate
            a++;
        }
    }
    

    // Storing the point of intersections in a file so that can be used
    // to annotate in the python code for plotting.

    FILE *pointer;
    pointer = fopen("Points.txt","w");
    fprintf(pointer,"\tx\t\t\t\ty\n");
    for(a=0;a<10;a++)
    {
        fprintf(pointer,"%f\t\t%f\n",points[a][0],points[a][1]); 
    }

    //Places income for each case in each block of array
    float *income;
    income = (float *)calloc(10,sizeof(int));
    int p=0;
    for(p=0;p<10;p++)
    {
        GrossIncome(points[p][0],points[p][1],income,p);  
    }
    
    //checks for maximum in array and replaces if it is new maximum.1`
    float max = 0;
    int answer=0;     
	for(int i=0;i<10;i++)
	{
	    if(max<=income[i])    
	    {
	        max = income[i];
	        answer = i;
	    }
	}

	printf("The carpenter should produce %0.1f units of Product A and %0.1f units of Product B for maximum gross income.",points[answer][0],points[answer][1]);
	
	free(income);
	return 0;
}
