#include <stdio.h>
#include <string.h>

int main(void) {
  char s1[100], s2[100];
  scanf("%s %s", s1, s2);
  strcat(s1, s2);
  printf("%s\n", s1);
}