#include <stdio.h>

void swap(int firstVal, int secondVal); // function declaration

int main(void)
{
    int valA = 7;
    int valB = 5;

    printf("Before Swap : valA = %d, valB = %d\n", valA, valB);
    swap(valA, valB); 
    
    // 안에서는 swap이 가능하지만, local varable상에서 이루어진 것이므로 main 에서는 바뀌지 않음.
    // main stack 상 바뀐 부분이 없음 -> pointer를 사용해야함.

    printf(" After Swap : valA = %d, valB = %d\n", valA, valB);
    return 0;

}

void swap(int firstVal, int secondVal)
{
    int tempVal;
    tempVal = firstVal;
    firstVal = secondVal;
    secondVal = tempVal;

    printf("In Swap : firstVal = %d, secondVal = %d\n", firstVal, secondVal);
}



/// Pointer Declaration
int *ptr; // contains an address of an integer variable
char *ptr; // address of a character variable (주소가 문자형이라는게 아니라, 문자형 변수를 가리키는 pointer라는 것.)

int intVariable = 10;
int *intptr; ///이런식으로 초기화를 하기보다는 Null로 초기화하는 것이 좋음(어떤 것을 가리키고 있는지 모르므로)
intptr = &intVariable;
/*
Then, *intptr++ is same as intVariable++*/