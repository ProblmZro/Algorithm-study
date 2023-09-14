#include <stdio.h>

int main(void) {
  int dwarf[9], r_dwarf[7];
  int sum = 0;
  int ans1, ans2 = 0;

  for(int i=0; i<9; i++) {
    scanf("%d", &dwarf[i]);
    sum += dwarf[i];
  }

  for(int i=0; i<9; i++) {
    for(int j=i+1; j<9; j++) {
      if((sum - dwarf[i] - dwarf[j]) == 100) {
        ans1 = i;
        ans2 = j;
        break;
      }
    }
  }

  int k = 0;
  for(int i=0; i<9; i++) {
    if((i != ans1) && (i != ans2)) {
      r_dwarf[k] = dwarf[i];
      k++;
    }
  }

  int tmp;
  for(int i=0; i<7; i++) {
    for(int j=i+1; j<7; j++) {
      if(r_dwarf[i] > r_dwarf[j]) {
        tmp = r_dwarf[i];
        r_dwarf[i] = r_dwarf[j];
        r_dwarf[j] = tmp;
      }
    }
  }

  for(int i=0; i<7; i++) {
    printf("%d\n", r_dwarf[i]);
  }

  return 0;
}