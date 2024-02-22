#include <stdio.h>
#include <stdlib.h>
#include <math.h>



 // 3의 거듭제곱 혹은 그 조합의 합 순열에서 N 번째 수 찾기 : 3의 배수 아닌가? (아님, 같은 것끼리 합은 안되니)

 
int numofones(int n) {
// Write your code below
 

  //무한번 가능
  int k = 0;
  int ans = 0;
  while (n){
    if (n %2==1){
      ans +=pow(3, k);
    }
    n /=2;
    k++;
  }
  return ans;
}

// DO NOT MODIFY BELOW!
int main(int argc, char* argv[]) {
  int n = atoi(argv[1]);
  printf("%d", numofones(n));
  return 0;
}


