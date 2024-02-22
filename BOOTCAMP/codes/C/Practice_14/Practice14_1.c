//find prime number : print all prime number less than 100
//소수 구하기

#include <stdio.h>

_Bool Primenumber(int n);

int main(void){
    /* Your Code Here */
    
    _Bool prime;
    for (int i = 2; i <=100; i++){

        prime = Primenumber(i);
        if (prime == 1)
        {
            printf("%d ", i);
        }
    }



    return 0; 
}

_Bool Primenumber(int n)
{
    
    for (int i = 2; i <n; i++)
    {
        if (n%i ==0)
        {
            return 0;
       }
        
    }
    return 1;
}






