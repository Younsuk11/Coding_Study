#include<iostream>
#include<vector>
#include<climits>
using namespace std;


/* 
Given an integer array nums, find the subarray with the largest sum, and return its sum
subarray : 연속적인 부분 array -> 순서대로 array를 바라봐도 좋다.

dp[i] = i개의 subarray 중 가장 최대 값?
어디가 max인지를 찾는게 아니라, "최대"에 집중하자


최대 부분합 : kadane's algorithm
각 index에서 가질 수 있는 최대 부분합 = 이전 index에서 구한 최대 부분합에서 연장  or 자기 값으로 초기화
1. 현재 index값을 더한게 더 큰 경우
2. 부분합이 0으로 떨어졌을 때, 초기화 -> 하나를 더해서 음수 : 다시 양수로 복구 하는 것보다 다시 시작하는 편이 최대합을 구하는데 더 가능성이 높다.

*/



class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int sum = 0; // 현재까지 고려한 부분합
        int max = INT_MIN; // 지금까지 발견된 부분 배열의 최대 합

        for (int i =0; i<nums.size(); i++){
            sum += nums[i];

            if (sum > max){ // update
                max = sum;
            }
            if (sum < 0){ //초기화
                sum = 0;
            }
        } 
        return max;   
    }
};

int main()
{
    vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5,4};
    Solution sol;
    int output = sol.maxSubArray(nums);
    cout<< output <<endl;
}