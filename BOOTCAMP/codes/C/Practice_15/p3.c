#include <stdio.h>
#define SIZE 10   // Define constant

void selection_sort(int L[], int size);  // Remember declaration!

int main(void){
    int L[SIZE] = {9, 8, 1, 6, 23, 4, 3, 11, 85, 0};
    
    printf("Before selection sort: ");
    for (int i = 0; i < SIZE; i++){
        printf("%d ", L[i]);
    } 
    printf("\n");

    selection_sort(L, SIZE);

    printf("After selection sort: ");
    for (int i = 0; i < SIZE; i++){
        printf("%d ", L[i]);
    } 
    printf("\n");

    return 0;
}

void selection_sort(int L[], int size){
    int smallest;
    int temp;

    /* Your code here*/
    //여기서는 size가 정해져 있다.
    

    for(int i=0; i < size; i++)
    {
        smallest = i;

        //find smallest index
        for(int j=i+1; j< size; j++)
        {
            if(L[j] < L[smallest])
            {
                smallest = j;
            }
        }

        //swap by pointer
        temp = L[i];
        L[i] =  L[smallest];
        L[smallest] = temp;
    }


    ////////////////////
}

/*
<Test>
-> gcc p3.c -o p3
-> ./p3

<output>
Before selection sort: 9 8 1 6 23 4 3 11 85 0 
After selection sort: 0 1 3 4 6 8 9 11 23 85
*/

/*
selection sort란
find minimum value and swap it with the leftmost entry
*/


/*
insert sort란
iteration도는 값(leftmost)을 sorted 부분에 맞는 위치에 넣는다.
Insert the leftmost item of the unsorted list to the proper location of the sorted list
selection sort보다 조금 느리지만, 대부분 정렬되어 있다면, 더 빠름 kN
*/