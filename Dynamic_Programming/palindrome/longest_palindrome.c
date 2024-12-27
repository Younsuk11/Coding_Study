#include<stdio.h>
#include<string.h>


int countSubstring(char* s){
    int n = 0;
    while(s[n] != '\0'){
        n++;
    }
    int dp[n][n];
    int ans = 0;

    for (int i =0 ; i< n ; ++i){
        dp[i][i] = 1;
        ans ++;
    }
    for(int i =0; i< n-1; ++i){
        int j = i +1;
        if (s[i] == s[j]){
            dp[i][j] = 1;
            ans ++;
        }
        else{
            dp[i][j] = 0;
        }
    }

    //길이가 3이상
    for (int length = 3; length<n+1; ++length){
        for (int i =0; i <n-length+1; ++i){
            int j = i+length -1;
            if (dp[i+1][j-1]==1 && s[i] == s[j]){
                dp[i][j] = 1;
                ans++;
            }
            else{
                dp[i][j] =0;
            }
        }
    }
    return ans;

}


int main(){

    char s[] = "aaa";
    char s2[] = "abc";
    printf("%d\n", countSubstring(s));
    printf("%d\n", countSubstring(s2));
    return 0;
}