#include <stdio.h>

int main(void) {
  int n1, n2, a;
  int j;
  scanf("%d %d", &n1, &n2);
  if (n1 > n2) {
    a = n1;
    n1 = n2;
    n2 = a;
  }
  for(int i=n1+1; i<n2; i++){
    for(j=2; j<=i; j++){
      if (i % j == 0)
        break;
    }
    if (j == i)
      printf("%d ", i);
  }
}