#include <stdio.h>

int fibonacci(int n) {
  if (n==0) return 0;
  else if (n==1) return 1;
  else {
    return fibonacci(n-1) + fibonacci(n-2);
  }
}

int main(void) {
  int n = 0;
  scanf("%d", &n);
  printf("%d\n", fibonacci(n));
}