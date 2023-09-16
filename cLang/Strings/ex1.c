// 입력한 문자열을 그대로 출력하고 문자열의 길이를 출력
// (공백 포함, 버퍼 사이즈 초과시 사이즈에 해당하는 것까지만 출력)

#include <stdio.h>
#include <string.h>
#define BUFFER_SIZE 20

int read_line(char str[], int n) {
  int ch, i = 0;

  while ((ch = getchar()) != '\n')
  {
    if (i < n)
      str[i++] = ch;
  }
  str[i] = '\0';  // 마지막 줄바꿈 문자를 null로
  return i;
}

int main(void) {
  char buffer[BUFFER_SIZE];
  int k;

  while (1) {
    printf("$ ");
    // fgets(buffer, BUFFER_SIZE, stdin);
    k = read_line(buffer, BUFFER_SIZE);
    printf("%s: %d\n",buffer, k);
  }

  return 0;
}