//Prime factorization
//소인수 분해 문제

//36 = 2^2 X 3^2 
// (2,2) (3,2)


#include <stdio.h>

int main(void){
    int num;
    printf("Enter the number to be factorized: ");
    scanf("%d", &num);
    /* Your Code Here */
    
    for (int di = 2 ; di <= num ; di++)
    {
        int power = 0;
        while(num%di ==0)
        {
            num /= di; 
            // 이미 나눠주어서, 약수로 중복되게 나눠지지는 않는다. -> for문 test 부분에도 반영된다.

            
            power++;
        }

        if (power > 0)
        {
            printf("(%d %d)", di, power);
        }
    }


    return 0;
}



