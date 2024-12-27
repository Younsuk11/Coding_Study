'''
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

2d dynamic programming
i : 앞에서 순회
j : 뒤에서 순회
d_ij = i ~ j 까지의 substring이 palindrome인지 여부
palindrome에서 앞 뒤, 한글자씩 추가 될 때, 맨 앞과 맨 뒤가 같으면 palindrome

길이가 3 이상인 길이에 대해:
dp[i+1][j-1] = True이고, s[i] == s[j]가 같으면 palindrome



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        ans = 0
        #초기화 : 길이가 1인 경우
        for i in range(n):
            dp[i][i] = True
            ans += 1

        #초기화 : 길이가 2인 경우 : 앞과 뒤가 같은 경우.
        for i in range(n-1):
            j = i+1
            if s[i] ==s[j]: 
                dp[i][j] = True
                ans +=1

        #길이가 3 이상인 경우
        for length in (3, n+1):
            for i in range(0, n-length + 1): # i가 될 수 있는 값의 조합이 length따라 다르다.
                j  = i+length -1  #j-i +1 = length
                if dp[i+1][j-1] and (s[i]== s[j]):
                    dp[i][j] = True
                    ans +=1

         


        return ans
    

def main():
    sol = Solution()
    print("Ans : ", sol.countSubstrings("abc"))
    print("Ans : ", sol.countSubstrings("aaa"))

if __name__ == "__main__":
    main()