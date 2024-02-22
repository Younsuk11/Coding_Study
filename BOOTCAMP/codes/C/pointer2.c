//swap again


#include <stdio.h>

void newSwap(int *firstVal, int *secondVal); // 이제는 pointer가 가리키는 메모리 공간을 직접 다룰 것임.

int main(void){
    int valA = 7;
    int valB = 5;

    printf("Before Swap : valA = %d, valB = %d\n", valA, valB);
    newSwap(&valA, &valB); 
    
    //값이 아닌 메모리 주소로 input-> 메모리 주소내 값에 직접 적용 가능

    printf(" After Swap : valA = %d, valB = %d\n", valA, valB);
    return 0;

}

void newSwap(int *firstVal, int *secondVal)
{
    int tempVal;

    tempVal = *firstVal; // pointer(firstVal)가 가리키는 메모리 공간의 값을 가져옴.
    *firstVal = *secondVal;

    *secondVal = tempVal;

    printf("In Swap : firstVal = %d, secondVal = %d\n", *firstVal, *secondVal);
}

//Null pointer
/*
points to nothing
*/
int *ptr;
ptr = NULL; //value 0 (points to nothing)

//Demystifying the syntax
// scanf("%d", &input);
// input의 값을 직접 바꾸면서 입력값을 받을려면 &input으로 해주면 값을 받아와서 주소 내 메모리에 넣어준다.