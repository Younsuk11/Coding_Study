'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence


Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.


A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
'''




from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        '''
        dp[i] : i번째 원소를 마지막으로 하는 LIS의 길이
        '''

        N = len(nums)

        dp = [1] * (N)


        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                #else 넘어가도 되는 이유는 이미 모두 1로 초기화 했기 때문(자기 자신)


        # find max
        ans=  0
        for i in range(N):
            ans = max(ans, dp[i])
        return ans



if __name__  == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums)) # 4
    nums = [0,1,0,3,2,3]
    print(Solution().lengthOfLIS(nums)) # 4

    nums = [1,3,6,7,9,4,10,5,6]
    print(Solution().lengthOfLIS(nums)) # 6
    