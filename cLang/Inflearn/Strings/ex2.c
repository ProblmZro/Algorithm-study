// 입력한 문자열의 연속 두 개 이상의 공백은 제거하고 출력
// 문자열의 길이를 출력

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define BUFFER_SIZE 20

int read_line(char compress[], int limit) {
  int ch, i = 0;
  while ((ch = getchar()) != '\n') {
    if ((i < BUFFER_SIZE - 1) && (!isspace(ch) || (i>0 && !isspace(compress[i-1]))))
      compress[i++] = ch;
  }
  if(i>0 && isspace(compress[i-1])) 
    i--;
  compress[i] = '\0';
  return i;
}
 
int main(void) {
  char buffer[BUFFER_SIZE];
  int len;

  while (1) {
    printf("$ ");
    len = read_line(buffer, BUFFER_SIZE);
    printf("%s: %d\n",buffer, len);
  }

  return 0;
}