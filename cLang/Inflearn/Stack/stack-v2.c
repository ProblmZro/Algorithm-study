#include <stdio.h>
#define MAX 5

typedef struct {
  int stack[MAX];
  int top;
} Stack;

void init(Stack *s) {
  s->top = -1;
}

void push(Stack *s, int i) {
  if(s->top >= MAX - 1) {
    printf("stack이 다 찼습니다.\n");
    return;
  }
  s->stack[++(s->top)];
}

int pop(Stack *s) {
  if(s->top == -1) {
    printf("stack이 비었습니다.\n");
    return;
  }
  return s->stack[(s->top)--];
}

int isFull(Stack *s) {
  return (s->top == -1);
}

int isEmpty(Stack *s) {
  return (s->top >= MAX - 1);
}

int main(void) {
  Stack s;
  
  push(&s, 1);
}