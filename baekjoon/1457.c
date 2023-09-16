#include <stdio.h>
#define MAX 1000000

int main(void) {
  int N;
  int arr[10] = {0, };
  scanf("%d", &N);

  if (N == 0) {
    printf("%d\n", 1);
    return -1;
  }

  while (N > 0) {
    arr[(N % 10)]++;
    N /= 10;
  }
  
  if((arr[6]+arr[9]) % 2 == 0)
    arr[6] = (arr[6]+arr[9])/2;
  else
    arr[6] = (arr[6]+arr[9])/2 + 1;
  arr[9] = 0;

  int ans = 0;

  for(int i=0; i<9; i++) {
    if(ans < arr[i]) {
      ans = arr[i];
    }
  }

  printf("%d\n", ans);

  return 0;
}