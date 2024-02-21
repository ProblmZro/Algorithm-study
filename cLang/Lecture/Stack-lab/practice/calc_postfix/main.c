#include <stdio.h>
#include "stackv1.h"

double calc_postfix(char expr[]) {
	int i = 0;
  double val, val1, val2;
	char c;

	init_stack();
	while (expr[i] != '\0') {
		c = expr[i++];
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

void main()
{
	char expr[2][80] = { "8 2 / 3- 3 2 * +", "1 2 / 4 * 1 4 / *" }; 
  printf("수식: %s = %lf\n", expr[0], calc_postfix(expr[0])); 
  printf("수식: %s = %lf\n", expr[1], calc_postfix(expr[1]));
}

