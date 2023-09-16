#include <stdio.h>
#include <string.h>

int main(void) {
  char *words[100];
  char buffer[100];
  int n = 0;

  while (n < 5 && scanf("%s", buffer) != EOF) {
    words[n] = strdup(buffer);
    n++;
  }
  
  for (int i=0; i<5; i++) {
    printf("%s\n", words[i]);
  }
}