#include<stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int size = argc-2; // Size of array
    int arr[size];
    for(int i=0;i<size;i++){
        arr[i] = atoi(argv[i+1]);
    }
    int result[size]; // array you have to fill it
    int rotate = atoi(argv[size+1]); // number of rotation  

    /* Write your code here */ 

    for(int r= 0; r<rotate; r++)
    {
        for (int j =0; j< size ; j++)
        {
            if(j== size-1)
            {
                result[0] = arr[j];
            }
            else{
                result[j+1] = arr[j];
            }
            
        }


        for (int k = 0; k <size ; k++)
        {
            arr[k] = result[k];
        }

        
    }





    // DO NOT MODIFY BELOW!!!
    for (int i=0; i<size; i++) {
        printf("%d ", result[i]);
    }

    return 0;
}