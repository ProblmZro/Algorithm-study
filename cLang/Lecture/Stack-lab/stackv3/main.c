#include <stdio.h>
#include "stackv3.h"

void main()
{
	int i;
	init_stack();
	for (i = 1; i < 10; i++)
		push(i);
	print_stack("스택 push 9회");
	printf("\tpop() --> %d\n", pop());
	printf("\tpop() --> %d\n", pop());
	printf("\tpop() --> %d\n", pop());
	print_stack("스택 pop 3회");
}

