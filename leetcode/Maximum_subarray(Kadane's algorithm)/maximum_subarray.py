from typing import List

class Solution:
    def max_sumSubArray(self, nums: List[int]) -> int:
        sum = 0
        max_sum = -float("inf")

        for i in range(len(nums)):
            sum +=nums[i]

            if (sum > max_sum): max_sum = sum
            if (sum <0): sum = 0



        return max_sum


    def Kadane(self, nums):
        sum = nums[0]
        max_sum = nums[0]


        for num in nums[1:]:
            sum = max(num, sum + num)

            max_sum = max(max_sum, sum)
        return max_sum
    
if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5,4]
    print("ans : ",sol.max_sumSubArray(nums))
    print("kadane: ", sol.Kadane(nums))