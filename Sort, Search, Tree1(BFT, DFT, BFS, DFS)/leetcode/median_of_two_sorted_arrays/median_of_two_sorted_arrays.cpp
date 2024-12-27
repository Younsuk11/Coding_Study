#include<vector>
#include<iostream>
using namespace std;


/* 
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
*/
/* 
merge sort(sub array merge) -> find median 
*/
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        //sub array merge(sort)
        int i = 0;
        int j = 0;
        vector<double> nums;
        while((i < nums1.size()) && (j < nums2.size())){
            if(nums1[i] <= nums2[j]){
                nums.push_back(nums1[i]);
                i++;
            }
            

            else{
                nums.push_back(nums2[j]);
                j++;
            }
        }

        //handling remaining
        while(i< nums1.size()){
            nums.push_back(nums1[i]);
            i++;
        }
        while(j<nums2.size()){
            nums.push_back(nums2[j]);
            j++;
        }
        
        //get median
        int mid = nums.size()/2; // 3-> 1 , 4-> 2
        if (nums.size() % 2 ==1){
            return nums[mid];
        }
        else{
            return (nums[mid-1] + nums[mid]) / 2;
        }
        
    }
};

//test case
int main(){

    vector<int> num1 = {1,2};
    vector<int> num2 = {3,4};
    Solution sol;
    double ans = sol.findMedianSortedArrays(num1, num2);
    cout<< ans<<endl;

}