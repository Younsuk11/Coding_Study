#include <stdio.h>
#include <stdlib.h>

// Implement model 
//pointer 활용문제.

void model(float *x){
// write your code below

    //*x : pointer(address) of x : 직접 반영
    float weight = 3.2;
    float bias = -1.1;
    
    *x = weight * (*x) +bias; // *x : get value of the address

    if (*x<0)
    {
        *x *=0.01;
    }


}


// DO NOT MODIFY BELOW!
int main(){
    float x = 32.4;
    // float x = 0;
    model(&x);
    
    // input not value of x, address of x
    // 그럼 같은 메모리의 값이 직접 변경된다.
    // 다른 값으로 하면 다른 메모리로 할당되므로...

    printf("%f",x);
    return 0;
}