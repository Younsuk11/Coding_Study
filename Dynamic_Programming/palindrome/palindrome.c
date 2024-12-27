/*
2023-09 programming 시험.
Given a string `s`, 
return the minimum number of characters that need to be deleted to obtain the longest palindromic subsequence 
and the resulting subsequence itself.  

가장 긴 palindrome을 만들기 위한 삭제하는 글자들의 최소 개수.
**Example 1**: Input -> s = "unique" 3 unu 
**Example 2**: Input -> s = "radar" 0 radar

input string은 scanf로 받을 것.
dp 문제임.
*/


/*
DP 배열 정의:
dp[i][j]를 문자열 s[i...j] (i에서 j까지의 부분 문자열)의 최장 팰린드롬 부분 수열의 길이로 정의합니다.

점화식:

만약 s[i] == s[j]라면, dp[i][j] = dp[i+1][j-1] + 2입니다.
그렇지 않다면, dp[i][j] = max(dp[i+1][j], dp[i][j-1])입니다.
기본 초기화:
모든 길이가 1인 부분 문자열은 팰린드롬이므로 dp[i][i] = 1입니다.

결과 추출:
최종적으로 dp[0][n-1]이 주어진 문자열 s의 최장 팰린드롬 부분 수열의 길이를 나타내며, 이를 통해 삭제해야 하는 문자 수는 n - dp[0][n-1]이 됩니다.

팰린드롬 부분 수열 복원:
dp 테이블을 사용하여 실제로 그 팰린드롬 수열을 복원할 수 있습니다.

*/

#include <stdio.h>
#include <string.h>

// 두 값 중 큰 값을 반환하는 함수
int max(int a, int b) {
    return (a > b) ? a : b;
}

// 가장 긴 팰린드롬 부분 수열을 구하는 함수
void longestPalindromeSubseq(char* s) {
    int n = strlen(s);
    int dp[n][n];

    // 초기화: 길이가 1인 경우 (모든 개별 문자는 팰린드롬)
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }

    // 길이가 2 이상인 부분 문자열에 대해 DP 테이블 채우기
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i <= n - length; i++) {
            int j = i + length - 1;

            if (s[i] == s[j]) {
                dp[i][j] = dp[i + 1][j - 1] + 2;
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }

    // 삭제해야 할 최소 문자 수
    int minDeletions = n - dp[0][n - 1];
    printf("Minimum deletions: %d\n", minDeletions);

    // 팰린드롬 부분 수열을 복원
    /*
    i와,j는 string에서 순회
    start와 end는 각각 양 옆에서 panlindrome 복원
    i,j는 최장길이를 계속 추적하기 위해서 backtrack
    */
    int i = 0, j = n - 1;
    int start = 0, end = dp[0][n - 1] - 1; // 가장 마지막은 null character이기에., dp[0][n-1]은 0~ n-1에 해당하는 index를 보았을 때 얻은 최장 길이 palindromic substring
    char palindrome[dp[0][n - 1] + 1];
    palindrome[dp[0][n - 1]] = '\0';

    while (i <= j) {
        if (s[i] == s[j]) {
            palindrome[start] = s[i];
            palindrome[end] = s[j];
            start++;
            end--;
            i++;
            j--;
        } else if (dp[i + 1][j] > dp[i][j - 1]) {
            i++;
        } else {
            j--;
        }
    }

    printf("Longest Palindromic Subsequence: %s\n", palindrome);
}

int main() {
    char s[100];
    printf("Enter the string: ");
    scanf("%s", s);
    longestPalindromeSubseq(s);
    return 0;
}

