#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, sum = 0;
    int *array; // Pointer to a dynamically allocated memory area (heap)

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    /* Write your code here */
    if (n<0)
    {
        printf("Number of elements must be positive.\n");
        return 0;
    }

    //dynamic memory
    array = malloc(n*sizeof(int)); //n개 만큼  allocation
    // input 5 numbers
    
    printf("Enter %d integer : \n", n);
    for (int i=0; i < n; i++)
    {
        scanf("%d", &array[i]);
        sum += array[i];
    }

    printf("Element stored in the array : ");
    for (int i=0; i < n; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\nsum of all elements  = %d\n", sum);
    

    free(array); // 이거 반드시 해야함. deallocation
    /////////////////////////

    return 0;
}