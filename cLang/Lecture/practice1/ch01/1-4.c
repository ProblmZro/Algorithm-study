#include <stdio.h>
#define a 2
#define b 3
#define c 2

int main(void) {
  int mat1[a][b] = {{1, 2, 3}, {4, 5, 6}};
  int mat2[b][c] = { {7, 8}, {9, 10}, {11, 12}};
  int res[a][c] = {0, };
  
  for(int i = 0; i < a; i++) {
    for(int j = 0; j < c; j++) {
      for(int k = 0; k < b; k++) {
        res[i][j] += mat1[i][k] * mat2[k][j];
      }
    }
  }
 
  for(int i = 0; i < a; i++) {
    for(int j = 0; j < c; j++) {
      printf("%d ", res[i][j]);
    }
    printf("\n");
  }
}