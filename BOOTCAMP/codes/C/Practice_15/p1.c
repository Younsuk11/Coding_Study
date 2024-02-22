#include <stdio.h>
 
void swap(int *firstVal, int *secondVal);  // Remember declaration!
void reverse_dig(int *val);                // Remember declaration!

int main(){
    int a = 1234;
    int b = 67890;

    printf("Before Reverse: a = %d, b = %d\n", a, b);
    reverse_dig(&a);
    reverse_dig(&b);
    printf("After Reverse: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("After Swap: a = %d, b = %d\n", a, b);

    return 0;
}

void reverse_dig(int *val){
    int temp = *val;
    int ans = 0;
    int re = 0; // 나머지

    /* Your code here*/
    while(temp> 0)
    {
        re = temp %10;
        ans  = ans *10 + re; // 축적해서 더하기, 그리고 자리수 이동.
        temp /=10;// 나눈 몫반환
        
    }

    *val = ans;
    ///////////////////
}


void swap(int *firstVal, int *secondVal){
    int tempVal;

    /* Your code here*/
    tempVal = *firstVal;
    *firstVal = *secondVal;
    *secondVal = tempVal;

    ///////////////////
}

/*
<Test>
-> gcc p1.c -o p1
-> ./p1

<output>
Before Reverse: a = 1234, b = 67890
After Reverse: a = 4321, b = 9876
After Swap: a = 9876, b = 4321
*/