#include <stdio.h> 
//preprocessor macros : contains contents from file stdio.h(head file)
// like import in python, but it literally copies the content of the file
// stdio.h(head file) : declarations of I/O functions(like printf)


// 주석 처리
/* 다중 줄 주석 처리*/
int main(){  
    printf("Hello World\n"); //should end with semicolone
    return 0;//returns integer
}
//gcc hello.c -o hello 
// hello.c compile and make .exe
// ./hello 실행