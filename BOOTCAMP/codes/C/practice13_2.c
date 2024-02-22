#include <stdio.h>

int num1 = 1;

int main(void)
{
    printf("%d\n", num1);
    {
        int num2 = 10 + num1 ; 

        printf("%d\n", num2); //11
        {
            int num1 = 100 + num2;
            printf("%d\n", num1); //111
        }
        printf("%d\n", num2); //11
    }
    printf("%d\n", num1); //1(global)
    return 0;
}

// local variable은 함수 안에서만. 함수는 {}로 구별 된다.
// 위에서부터 한줄씩
// 예상
/*
1
11
111
11
1
*/