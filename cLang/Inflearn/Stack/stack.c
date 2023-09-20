#include <stdio.h>
#define MAX 5

int stack[MAX];
int top = -1;

void push(int i) {
  if (top >= MAX -1) {
    printf("stack이 다 찼습니다.\n");
    return;
  }
  stack[++top] = i;
}

int pop() {
  if (top == -1) {
    printf("stack이 비었습니다.\n");
    return;
  }
  return stack[top--];
}

int isEmpty() {
  return (top == -1);
  // if (top == -1) return 1;
  // else return 0;
}

int isFull() {
  return (top >= MAX -1);
  // if (top >= MAX -1) return 1;
  // else return 0;
}

int main(void) {

}