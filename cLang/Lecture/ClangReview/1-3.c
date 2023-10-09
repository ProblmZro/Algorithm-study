#include <stdio.h>

int main(void) {
  int a, b, num, j;
  scanf("%d %d", &a, &b);

  if (a > b) {
    num = a;
    a = b;
    b = num;
  }

  for(int i = a+1; i < b; i++) {
    for(j=2; j <= i; j++) {
      if (i % j == 0)
        break;
    }
    if (j == i) 
      printf("%d ", i);
  }
}