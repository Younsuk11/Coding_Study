#include <stdio.h>

int main() {
    int a, b;
    printf("Enter a number less than 1000: ");
    scanf("%d", &a);
    printf("Enter a number less than 1000: ");
    scanf("%d", &b);

    ////////////////////////////////
    // Write your code

    printf("%d\n", a * (b%10)); // 1의 자리
    printf("%d\n", a * ((b/10)%10)); // 10의 자리
    printf("%d\n", a * (b/100)); // 100의 자리
    // tip : 정수 끼리 나눈 것(/)은 몫과 같은 정수 값이 반환된다.

    printf("%d\n", a *b);
    ////////////////////////////////

    return 0;
}