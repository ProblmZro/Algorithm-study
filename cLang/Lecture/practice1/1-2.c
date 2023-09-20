#include <stdio.h>

int main(void) {
  int num = 0;
  scanf("%d", &num);
  do {
    printf("%d", (num % 10));
    num /= 10;
  } while (num != 0);
}