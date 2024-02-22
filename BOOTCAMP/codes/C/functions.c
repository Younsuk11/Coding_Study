/*
Definition
Header : function name, parameter list with data type

callee must be declared
int answer;
answer = Factorial*/


//ex
#include <stdio.h>

int Factorial(int n);// declaration : return value type declaration


int main(void)
{
    int number;
    int answer;
    printf("input a number. ");
    scanf("%d" , &number);

    answer = Factorial(number); // call
    printf("The factorial of %d is %d\n", number, answer);
}

//definition
int Factorial(int n){
    int result = 1;
    for (int i = 1; i<=n; i++)
    {
        result *=i;
    }
    return result;
}