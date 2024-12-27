#include <stdio.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
    int mergedsize = nums1Size + nums1Size;
    int nums[mergedsize];
    
    int index = 0;
    int i = 0, j= 0;
    while(i < nums1Size && j < nums2Size){
        if (nums1[i] <= nums2[j]){
            nums[index++] = nums1[i++];
        }
        else{
            nums[index++] = nums2[j++];
        }
    }
    // handling remains
    while(i<nums1Size){
        nums[index++] = nums1[i++];
    }
    while(j<nums2Size){
        nums[index++] = nums2[j++];
    }

    int mid = mergedsize / 2;
    if(mergedsize % 2 ==1){
        return nums[mid];
    
    }
    else{
        return (double) (nums[mid-1] + nums[mid]) / 2.0;
    }


}


int main(void){

    int nums1[] = {1,2};
    int nums2[] = {3,4};
    int nums1Size = sizeof(nums1) / sizeof(nums1[0]);
    int nums2Size = sizeof(nums2) / sizeof(nums2[0]);
    // 각 메모리 크기로 나눠서 개수 구하기

    double ans  = findMedianSortedArrays(nums1, nums1Size, nums2, nums2Size);

    printf("%f", ans);



}