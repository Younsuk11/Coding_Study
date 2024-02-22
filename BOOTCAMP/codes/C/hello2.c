#include <stdio.h> // preprocessor
#define MY_CONSTANT 10 // preprocessor directive
// define X Y : X get substituted with Y : fixed values within a program



int main(void)
{
    printf("You define a fixed value %d\n", MY_CONSTANT);
    //with format string : %d : decimal number

    return 0;
}