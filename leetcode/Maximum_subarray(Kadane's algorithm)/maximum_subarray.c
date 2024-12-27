#include <stdio.h>
#include<limits.h>


int maxSubArray(int* nums, int numsSize) {

    int sum = 0;
    int max_sum= INT_MIN;
    for (int i = 0; i<numsSize; i++){
        sum += nums[i];
        if (sum >max_sum){
            max_sum = sum;
        }
        if (sum <0){
            sum = 0;
        }
        
    }
    return max_sum;

    
}

int main(void)
{
    int nums[] = {-2, 1, -3, 4, -1, 2, 1, -5,4};
    int ans = maxSubArray(nums, 9);
    printf("%d", ans);
}