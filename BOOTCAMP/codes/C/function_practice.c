// Greatest common divisior(GCD) : 최대 공약수

// recursively find its GCD

#include <stdio.h>

int GCD(int a, int b);

int main(void)
{
    int a;
    int b;
    int answer;

    printf("input first integer : " );
    scanf("%d", &a);

    printf("input second integer : " );
    scanf("%d", &b);

    answer = GCD(a,b);
    printf("GCD : %d\n" , answer);
    return 0;

}

int GCD(int a, int b)
{
    int low;
    int high;

    if (a >=b)
    {
        low = b;
        high = a;
    }
    else
    {
        low = a;
        high = b;
    }

    //base case
    if (low==0)
    {
        return high;
    }
    //condition case
    else if(low == 1)
    {
        return 1;
    }
    //recusive case
    else{
        return GCD(low, high%low); // 나머지를 처리하자.
    }


    
}