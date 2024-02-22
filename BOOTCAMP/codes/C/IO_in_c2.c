// Buffered I/O
//Enter를 누르기 까지 buffered
// 누르면 \n을 포함해서 전달된다.
//output from putchar 역시 \n을 만나기 전까지 buffered 
//putchar : print 한 글자(아스키 코드로도 가능)
//getchar : 한글짜 얻기 -> return its ASCII value



#include <stdio.h>

int main(void)
{
    char c1;
    char c2;

    printf("input char1 :\n");
    c1 = getchar();
    
    printf("input char2  :\n");
    c2 = getchar();

    printf("char1 is %c and char2 is %c\n", c1, c2);
    return 0;
}