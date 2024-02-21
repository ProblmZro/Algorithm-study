#include <stdio.h>
#include <stdlib.h>

int main(void) {
  char s[50], v;
  int cnt = 0;

  scanf("%[^\n]s", s);
  scanf("%s", &v);
  
  for(int i=0; i<50; i++) {
    if(s[i] == v) {
      cnt++;
    }
  }
  printf("%d\n", cnt);
}



// #include <stdio.h>
// #include <stdlib.h>  // malloc과 free 함수를 사용하기 위해 필요한 헤더 파일

// int main(void) {
//   char *s = NULL; // 문자열을 가리킬 포인터를 초기화

//   // 문자열을 동적으로 입력받음
//   int c;
//   int len = 0;
//   s = (char *)malloc(sizeof(char)); // 초기에 메모리를 할당하고
//   while ((c = getchar()) != '\n' && c != EOF) {
//     s[len++] = (char)c;
//     s = (char *)realloc(s, (len + 1) * sizeof(char)); // 문자 하나를 추가할 때마다 메모리 크기를 조정
//   }
//   s[len] = '\0'; // 문자열 끝에 null 문자 추가

//   // 이제 s는 동적으로 할당된 문자열을 가리킴

//   char v;
//   int cnt = 0;

//   printf("Enter a character to count: ");
//   scanf(" %c", &v);

//   for (int i = 0; s[i] != '\0'; i++) {
//     if (s[i] == v) {
//       cnt++;
//     }
//   }

//   printf("Character '%c' appears %d times.\n", v, cnt);

//   // 메모리 해제
//   free(s);

//   return 0;
// }
