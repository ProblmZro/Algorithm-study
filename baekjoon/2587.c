#include <stdio.h>

int main(void) {
  int num[5], temp;
  int sum = 0;
  
  for(int i=0; i<5; i++) {
    scanf("%d", &num[i]);
    sum += num[i];
  };

  for(int i=0; i<4; i++) {
    for(int j=i+1; j<5; j++) {
      if(num[i] > num[j]) {
        temp = num[i];
        num[i] = num[j];
        num[j] = temp;
       }
    }
  }

  printf("%d\n", (sum/5));
  printf("%d\n", num[2]);

  return 0;
}