'''
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

'''

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        '''
        dp[i] : i번째 문자열까지 worddict의 단어로 나눌 수 있는지 여부
        for w in wordDict:
        각 하나씩 word를 검사해서, word를 뺀 부분이 true이고, len(word) ~ i까지의 부분이 word와 같다면 dp[i] = True

        '''
        dp = [False] * (len(s))


        for i in range(0, len(s)):
            for word in wordDict:
                if i-len(word) >=0:
                    if dp[i -len(word)] and s[i - len(word)+1 :i+1 ] == word:
                        dp[i] = True

                else:
                    if s[:i+1] == word:
                        dp[i] = True
        return dp[-1]
        







if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    print(Solution().wordBreak(s, wordDict)) # True

    s = "applepenapple"
    wordDict = ["apple","pen"]
    print(Solution().wordBreak(s, wordDict)) # True

    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(Solution().wordBreak(s, wordDict)) #