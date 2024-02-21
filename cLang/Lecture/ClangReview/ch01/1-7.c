#include <stdio.h>

int main(void) {
  int arr[4] = {1, 2, 3, 4};
  int* ptr = arr;

  for(int i = 0; i < 4; i++) {
    printf("%d\n", *(ptr+i));
  }
}