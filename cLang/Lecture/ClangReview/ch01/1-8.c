#include <stdio.h>
#include <string.h>

void compareInt(int n1, int n2) {
  if (n1 > n2) 
    printf("%d가 더 큽니다.\n", n1);
  else  
    printf("%d가 더 큽니다.\n", n2);
}

void compareChar(char c1, char c2) {
  if (c1 > c2) 
    printf("%c가 더 큽니다.\n", c1);
  else  
    printf("%c가 더 큽니다.\n", c2);
}

void compareStr(char *s1, char *s2) {
  if (strcmp(s1, s2) > 0) 
    printf("%s가 더 큽니다.\n", s1);
  else  
    printf("%s가 더 큽니다.\n", s2);
}

int main(void) {
  int (*compareType)() = NULL;
  
  char type;
  printf("어떤 타입을 비교할지 입력하시오(문자 : c, 숫자 : d, 문자열 : s) : ");
  scanf(" %c", &type);
  getchar();
  
  switch (type)
  {
  case 'c': {
    char c1, c2;
    printf("문자 두 개를 입력하시오 : ");
    scanf("%c %c", &c1, &c2);
    compareType=compareChar;
    compareType(c1, c2);
    break;
  }

  case 'd': {
    int n1, n2;
    printf("숫자 두 개를 입력하시오 : ");
    scanf("%d %d", &n1, &n2);
    // compareInt(n1, n2);
    compareType=compareInt;
    compareType(n1, n2);
    break;
  }

  case 's': {
    char s1[100], s2[100];
    printf("문자열 두 개를 입력하시오 : ");
    scanf("%s %s", s1, s2);
    compareType=compareStr;
    compareType(s1, s2);
    break;
  }

  default:
    printf("입력 값이 잘못됐습니다.\n");
    break;
  }
}