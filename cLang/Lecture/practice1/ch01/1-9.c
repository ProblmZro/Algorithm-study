#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

int main(void){
  char *c1 = malloc(sizeof(char) * MAX);
  char *c2 = malloc(sizeof(char) * MAX);

  printf("첫 번째 문자열을 입력하세요 : ");
  scanf("%s", c1);

  printf("두 번째 문자열을 입력하세요 : ");
  scanf("%s", c2);

  char *res = malloc(sizeof(char) * (strlen(c1) + strlen(c2) + 1));

  strcpy(res, c1);
  strcat(res, c2);

  printf("%s\n", res);

  free(c1);
  free(c2);
  free(res);

  return 0;
}