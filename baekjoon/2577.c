#include <stdio.h>

int main(void) {
  int n[3];
  int arr[10] = {0, };
  int res = 1;

  for(int i=0; i<3; i++) {
    scanf("%d", &n[i]);
    res *= n[i];
  }

  while (res > 0) {
    arr[(res % 10)]++;
    res /= 10;
  }

  for(int i=0; i<10; i++) {
    printf("%d\n", arr[i]);
  }  

  return 0;
}