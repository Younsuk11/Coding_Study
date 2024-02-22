#include <stdio.h>

int main()
{
    int a = 4;
    int b = a++ + 9; // evaluation -> increment

    printf("a : %d, b: %d\n", a, b);// b = 4, a = 5, b = 13

    int c = ++b / a--; // increment -> evaluation -> 
    printf("a : %d, b: %d, c: %d\n", a, b, c); //  b = 14 , c = 2,  a = 4


    int d = c++ * 2.1;  // evaluation -> increment
    printf("c : %d, d: %d\n",c, d); // d= 2, c = 3 , d = 4
}