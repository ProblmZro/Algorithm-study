#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stackv1.h"

static int precedence(char op) { 
  switch (op) {
    case '(' : case ')' : return 0; 
    case '+' : case '-' : return 1; 
    case '*' : case '/' : return 2;
  }
  return -1;
}

void infix_to_postfix(char expr[], char postfix[]) {
  int i = 0;
	char c;
	init_stack();
  int idx = 0;

	while (expr[i] != '\0') {
		c = expr[i++];
    if (c>='0' && c<='9') {
      postfix[idx++] = c;
      postfix[idx++] = ' ';
    }
    else if (c == '(') {
      push(c); 
    }
    else if (c == ')') {
      while (!is_empty() && peek() != '(') {
        postfix[idx++] = pop();
        postfix[idx++] = ' ';
      }
      if (!is_empty() && peek() == '(') {
        pop();
      }
      else {
        printf("소괄호 에러"); 
      }
    }
    else if (c == '+' || c == '-' || c == '*' || c == '/') {
      while (!is_empty() && precedence(peek()) >= precedence(c)) {
        postfix[idx++] = pop();
        postfix[idx++] = ' ';
      }
      push(c);
    }
  }

  while (!is_empty()) {
    postfix[idx++] = pop();
    postfix[idx++] = ' ';
  }
  postfix[idx] = '\0';
}

double calc_postfix(char postfix[]) {
	int i = 0;
  double val, val1, val2;
	char c;

	init_stack();
	while (postfix[i] != '\0') {
		c = postfix[i++];
		if (c>='0' && c<='9') {
      val = c - '0';
      push(val);
    }
    else if (c=='+' || c=='-' || c=='*' ||  c=='/') {
      val1 = pop();
      val2 = pop();
      switch (c) {
      case '+': push(val2 + val1); break;
      case '-': push(val2 - val1); break;
      case '*': push(val2 * val1); break;
      case '/': push(val2 / val1); break;
      }
    }
  }
  return peek();
}

int main() {
  char expr[80];
  char postfix[80];

  while (1) {
    printf("수식을 입력하세요: ");
    if(fgets(expr, sizeof(expr), stdin) == NULL) {
      break;
    }
    expr[strlen(expr) - 1] = '\0';

    infix_to_postfix(expr, postfix);
    printf("중위수식: %s ==> 후위수식: %s\n", expr, postfix); 
    printf("계산: %s = %lf\n", postfix, calc_postfix(postfix)); 
    printf("\n");
  }

  return 0;
}