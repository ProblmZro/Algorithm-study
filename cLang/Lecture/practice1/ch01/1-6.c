#include <stdio.h>

int main(void) {
  FILE* fp = fopen(__FILE__, "r");
  char c;

  while ((c = fgetc(fp)) != EOF) {
    putchar(c);
  }

  fclose(fp);
}