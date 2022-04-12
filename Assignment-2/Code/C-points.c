#include <stdio.h>
#include <stdlib.h>

/*
 To store the point of intersection of lines in a file as uning them for annotating points in 
                                      PY-ploy.py file.
*/


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
	return 0;
}
