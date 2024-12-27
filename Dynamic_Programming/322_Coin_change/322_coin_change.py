'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

총량을 만들기 위해 쓰인 동전의 최소 개수 반환.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0


1 <= coins.length <= 12 (동전 종류)
1 <= coins[i] <= 2^31 - 1 (각 동전의 금액)
0 <= amount <= 10^4 (총량)



'''


from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[i] : i원을 만들기 위해 필요한 최소 동전 개수

        dp = [float("inf")] * (amount + 1) # 최소로 계속 업데이트 할 예정
        #base 
        dp[0] = 0
        for i in range(1, amount +1):
            # 각 코인을 추가해서 최소 가지수를 얻을 수 있는지를 체크
            for coin in coins:
                if (i - coin)>=0:
                    dp[i] = min(dp[i] , dp[i-coin] +1)
    
        return dp[amount] if dp[amount] != float("inf") else -1 # 조합으로 만들 수 없는 경우는 계속 inf로 남아있음.
        




if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    print(Solution().coinChange(coins, amount)) # 3

    coins = [2]
    amount = 3
    print(Solution().coinChange(coins, amount)) # -1
    