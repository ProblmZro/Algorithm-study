// #include <stdio.h>
// #include <stdlib.h>

// int main(void) {
//   int n, x, cnt = 0;
//   int *arr;
//   scanf("%d", &n);
//   arr = (int *)malloc(sizeof(int) * n);

//   for(int i=0; i<n; i++) {
//     scanf("%d", &arr[i]);
//   }

//   scanf("%d", &x);
//   for(int i=0; i<n; i++) {
//     for(int j=i+1; j<n; j++) {
//       if(x == arr[i] + arr[j])
//         cnt++;
//     }
//   }

//   printf("%d\n", cnt++);

//   free(arr);
// }