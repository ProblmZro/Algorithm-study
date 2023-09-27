#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include "stackv2.h"


typedef struct node_t {
	int data;
	struct node_t* next;
} Node;

Node* top;

void init_stack() {
	top = NULL;
}

int is_empty() {
	return (top == NULL) ? 1 : 0;
}

int is_full() {
	return 0;
}

void push(int e)
{
	Node *p = (Node*)malloc(sizeof(Node));
	p->data = e;
	p->next = top;
	top = p;
}

int pop()
{
	Node *p;
	int e;
	if(is_empty()) perror("??");
	
	p = top;
	top = p->next;

	e = p->data;
	free(p);
	return e;
}


int size()
{

}

int peek() {
	if (is_empty())
		perror("¿¡·¯");

	return top->data;
}

void print_stack(char msg[]) {
	Node* p;

	printf("%s[%2d]= ", msg, size());
	for (p = top; p != NULL; p = p->next) {
		printf("%2d ", p->data);
	}
	printf("\n");
}
