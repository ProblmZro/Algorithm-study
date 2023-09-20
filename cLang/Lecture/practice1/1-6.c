#include <stdio.h>

int main(void) {
  FILE* fs;
  fs = fopen(__FILE__, "r");
  char c;

  while ((c = fgetc(fs)) != EOF)
  {
    putchar(c);
  };
  
  fclose(fs);  
}