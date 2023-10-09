#include <stdio.h>
int mat1[100][100];
int mat2[100][100];
int res[100][100];

void mulMat(int a[][100], int b[][100], int row, int mid, int col) {
  for(int i = 0; i < row; i++) {
    for(int j = 0; j < col; j++) {
      for(int k = 0; k < mid; k++) {
        res[i][j] += a[i][k] * b[k][j];
      }
    }
  }
  printf("---두 행렬 곱 결과---\n");
  for(int i = 0; i < row; i++) {
    for(int j = 0; j < col; j++) {
      printf("%d ", res[i][j]);
    }
    printf("\n");
  }
}

int main(void) {
  int rowA, colA, rowB, colB;
  int num;
  printf("mat1의 row, col 입력 : ");
  scanf("%d %d", &rowA, &colA);
  if(rowA > 100 || colA > 100) {
    printf("row, col의 값이 100을 초과하면 안됩니다.\n");
    return -1;
  }
  for(int i=0; i < rowA; i++) {
    for(int j=0; j < colA; j++) {
      printf("---mat1의 %d행 %d열 입력 : ", i+1, j+1);
      scanf("%d", &num);
      mat1[i][j] = num;
    }
  }

  printf("mat2의 row, col 입력 : ");
  scanf("%d %d", &rowB, &colB);
  if(rowB > 100 || colB > 100) {
    printf("row, col의 값이 100을 초과하면 안됩니다.\n");
    return -1;
  }
  if(rowB != colA) {
    printf("A의 col 값과 B의 row값이 같아야 합니다.\n");
    return -1;
  }
  for(int i=0; i < rowB; i++) {
    for(int j=0; j < colB; j++) {
      printf("---mat2의 %d행 %d열 입력 : ", i+1, j+1);
      scanf("%d", &num);
      mat2[i][j] = num;
    }
  }

  mulMat(mat1, mat2, rowA, colA, colB);
}

