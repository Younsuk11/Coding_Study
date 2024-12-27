'''
tile 종류 2가지 : domino, tromino

Given an integer n, return the number of ways to tile an 2 x n board. 
Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. 
Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

둘 개의 tiling을 다르게 만드는 조건:
-인접한 두 셀이 있고, 두 셀이 둘 중 하나의 tiling에만 덮여 있을 때.
'''




class Solution:
    def numTilings(self, n: int) -> int:
        

        # dp table : dp[i] ; the number ways of tiling an 2 x i board
        # 어디서 왔는지에 따라 3가지 경우로 나눠어서 생각

        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 5

        if n>=4:
            dp = [0] *(n+1)
            dp[0] = 1
            dp[1] = 1
            dp[2] = 2
            dp[3] = 5 # 여기까지가 base case들

 
            for i in range(4, n+1):
            
                '''
                dp[n]=dp[n-1]+dp[n-2]+ 2*(dp[n-3]+...+d[0])
                    =dp[n-1]+dp[n-2]+dp[n-3]+dp[n-3]+2*(dp[n-4]+...+d[0])
                    =dp[n-1]+dp[n-3]+(dp[n-2]+dp[n-3]+2*(dp[n-4]+...+d[0]))
                    =dp[n-1]+dp[n-3]+dp[n-1]
                    =2*dp[n-1]+dp[n-3]
                '''
                dp[i] = (dp[i-1]*2+ dp[i-3]) %(10**9 +7) 
                #dp[i] = (dp[i-1] + dp[i-2]*2 + dp[i-3]*5)로 생각하면 안되는 이유:  dp[i-1], dp[i-2]에 대해 겹치는 계산들이 포함되어 있어서.
            return dp[n]
    
if __name__ == "__main__":
    n = 3
    print(Solution().numTilings(n)) # 5
    n = 4
    print(Solution().numTilings(n)) # 11
    n = 5
    print(Solution().numTilings(n)) # 24
    n = 6
    print(Solution().numTilings(n)) # 53
    n = 1
    print(Solution().numTilings(n)) # 1


    


