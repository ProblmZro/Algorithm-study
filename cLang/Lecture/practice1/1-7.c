#include <stdio.h>
#define NUM 5

int main(void) {
  int arr[NUM] = {1, 2, 3, 4, 5};
  int* prt = arr;

  for(int i = 0; i < NUM; i++){
  printf("%d ", *prt+i);
  }
  printf("\n");

  // while(*prt) {printf(); prt++;}

  // for (prt = str; *prt != NULL; prt++)

  return 0;
}