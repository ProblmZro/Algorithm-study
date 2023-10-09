#include <stdio.h>

int main(void) {
  int n, ans=0;
  scanf("%d", &n);

  do {
    printf("%d", (n%10));
    n /= 10;
  } while (n != 0);
}