#include <stdio.h>
#define SIZE 7                         // Define constant

void reverse(int array[], int size);   // Remember declaration!
void swap(int *a, int *b);             // Remember declaration!

int main(void){
    int arr[SIZE] = {3,1,4,6,5,9,2};

    printf("Before reverse: ");
    for (int i=0; i<SIZE; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");

    reverse(arr, SIZE);

    printf("After reverse: ");
    for (int i=0; i<7; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}

void reverse(int array[], int size){
    int *p1;         
    int *p2;

    /* Your code here*/
    for(int i=0; i<(size /2); i++)
    {
        p1 = array + i; // 앞에서 부터 이동 same as &array[i]
        p2 = array + size -1-i; // 뒤에서 부터 same as &array[size -1 -i]

        swap(p1, p2);

    }

    ///////////////////
}

void swap(int *a, int *b){
    int temp;

    /* Your code here*/
    temp = *a;
    *a = *b;
    *b = temp;
    ///////////////////
}

/*
<Test>
-> gcc p2.c -o p2
-> ./p2

<output>
Before reverse: 3 1 4 6 5 9 2 
After reverse: 2 9 5 6 4 1 3
*/