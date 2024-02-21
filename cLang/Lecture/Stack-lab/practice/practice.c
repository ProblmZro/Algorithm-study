#include <stdio.h>
#define MAX_STACK_SIZE 100

char data[100];
int top;

void init_stack() {
  top = -1;
}

int is_empty() {
    return (top == -1); 
}

int is_full() {
    return (top == MAX_STACK_SIZE - 1); 
}

char pop() {
  if(is_empty())
    perror("스택 공백 에러");
  return data[top--];
}

void push(int n) {
  if (is_full())
    perror("스택 포화 에러");
  data[++top] = n;
}

char peek() {
    if(is_empty())
        perror("스택 공백 에러");
    return data[top];
}

int check_matching(char expr[]) {
  int i = 0;
  char ch;
  init_stack();
  while (expr[i] != '\0') {
    ch = expr[i++];
    if (ch == '[' || ch == '(' || ch == '{') 
      push(ch);
    else if (ch == ']' || ch == ')' || ch == '}') 
      if(is_empty()) return 2;
      else {
        char a = pop();
        if(((ch == ']') && !(a == '[')) || ((ch == ')') && !(a == '(')) || ((ch == '}') && !(a == '{'))) 
          return 3;}
  }
  if(!is_empty()) return 1;25
  else return 0;
}

int main()
{
	char expr[4][80] = {"{A[(i+1)]=0;}", "if((i==0) && (j==0)", "A[(i+1])=0", "A[i] =f)(;"};
  int err, i;
  for(i=0; i<4; i++) {
    err = check_matching(expr[i]);
    if(err==0)
      printf("괄호정상: %s\n", expr[i]);
    else
      printf("괄호오류: %s (조건%d 위반)\n", expr[i], err);
  }
  
}

