#include <stdio.h>
#define MAX 100

int main(void) {
  char s[MAX], ans;
  int cnt = 0;
  scanf("%[^\n]s", s);
  scanf("%s", &ans);

  for(int i = 0; i < MAX; i++){
    if(s[i] == ans)
      cnt++;
  }

  printf("%d\n", cnt);
}