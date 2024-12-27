#include<iostream>
#include<vector>
#include<climits>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        
        int n = nums1.size();
        int m = nums2.size();

        if (n > m){
            return findMedianSortedArrays(nums2, nums1);
        }
        int start = 0;
        int end = nums1.size();


        while(start <= end){
            
            int i = (start + end)/2;
            int j= (n + m + 1)/2 -i;


            int A_left = (i>0) ? nums1[i-1] : INT_MIN;
            int A_right = (i<n) ? nums1[i] : INT_MAX;
            int B_left = (j>0) ? nums2[j-1] : INT_MIN;
            int B_right = (j<m) ? nums2[j] : INT_MAX;

            if (A_right >= B_left && A_left <= B_right){
                if ((n+m) % 2 == 1){
                    return (double)max(A_left, B_left);
                }
                else{
                    return (double)(max(A_left , B_left) + min(A_right, B_right))/2.0;
                }

            
            }
            else if (A_right < B_left){
                start = i +1;

            }
            else{
                end = i-1;
            }

        }
        return -1.0;
    }
};



int main(){
    vector<int> nums1 = {1,2};
    vector<int> nums2 = {3};
    Solution sol;
    double ans = sol.findMedianSortedArrays(nums1, nums2);
    std::cout<<ans<<std::endl;

    return 0;
}