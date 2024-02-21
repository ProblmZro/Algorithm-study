#include <stdio.h>
#include "stackv1.h"

static int precedence( char op ) { 
  switch (op) {
    case '(' : case ')' : return 0; 
    case '+' : case '-' : return 1; 
    case '*' : case '/' : return 2;
  }
return -1;
}

void infix_to_postfix( char expr[] ) {
  int i = 0;
	char c;
	init_stack();

	while (expr[i] != '\0') {
		c = expr[i++];
    if (c>='0' && c<='9') {
      printf("%c ", c); 
    }
    else if (c == '(') {
      push(c); 
    }
    else if (c == ')') {
      while (!is_empty() && peek() != '(') {
        printf("%c ", pop());
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
        printf("%c ", pop());
      }
      push(c);
    }
  }

  while (!is_empty()) {
    printf("%c ", pop());
  }
  
}

void main()
{
  char expr[2][80] = { "8 / 2 - 3 + ( 3 * 2 )", "1 / 2 * 4 * ( 1 / 4 )" }; 
  printf("중위수식: %s ==> 후위수식: ", expr[0]); 
  infix_to_postfix(expr[0]);
  printf("\n중위수식: %s ==> 후위수식: ", expr[1]); 
  infix_to_postfix(expr[1]);
}