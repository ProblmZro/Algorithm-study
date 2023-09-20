#include <stdio.h>
#include <string.h>

int compareInt(int a, int b) {
  if (a > b) return 1;
  else if (a < b) return -1;
  else return 0;
}

int compareChar(char a, char b) {
  if (a > b) return 1;
  else if (a < b) return -1;
  else return 0;
}

int compareStr(char *a, char *b) {
  return strcmp(a, b);
}

int main(void) {
  int (*comparePtr)() = NULL;
  char type;
  int res;

  printf("어떤 타입을 비교할지 입력하시오(문자 : c, 숫자 : n, 문자열 : s) : ");
  scanf(" %c", &type);
  getchar();

  switch (type)
  {
  case 'c': {
    char c1, c2;
    printf("문자 두 개를 입력하시오 : ");
    scanf("%c %c", &c1, &c2);
    comparePtr = compareChar;
    res = comparePtr(c1, c2);
    break;
  }
  case 'n': {
    char n1, n2;
    printf("숫자 두 개를 입력하시오 : ");
    scanf("%d %d", &n1, &n2);
    comparePtr = compareInt;
    res = comparePtr(n1, n2);
    break;
  }
  case 's': {
    char s1[100], s2[100];
    printf("문자열 두 개를 입력하시오 : ");
    scanf("%s %s", s1, s2);
    comparePtr = compareStr;
    res = comparePtr(s1, s2);
    break;
  }
  default: {
    printf("입력 값이 잘못됐습니다.\n");
    return -1;
    break;
  }
  }

  if (res == 1) printf("첫 번째 값이 더 큽니다.\n");
  // else if (/* condition */)
  else if (res == -1) printf("두 번째 값이 더 큽니다.\n");
  else printf("두 값이 동일합니다.\n");

  return 0;
}