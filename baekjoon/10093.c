#include <stdio.h>

int main(void) {
  long long n1, n2, temp, cnt;
  scanf("%lld %lld", &n1, &n2);

  if (n1 > n2) {
    temp = n1;
    n1 = n2;
    n2 = temp;
  }
  cnt = n2-n1-1;

  if (n1 == n2) {
    cnt = 0;
  }

  printf("%lld\n", cnt);
  for(long long i=0; i < cnt; i++){
    printf("%lld", n1+i+1);
    if (i < cnt - 1) {
      printf(" ");
    }
  }
}