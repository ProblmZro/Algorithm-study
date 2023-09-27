#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include "list.h"
#include "stackv3.h"

typedef struct node_t {
	int data;
	struct LIST_HEAD_T list;
} Node;

struct LIST_HEAD_T stack;

void init_stack() {
	stack.next = stack.prev = &stack;
}

int is_empty() {
	return list_empty(&stack);
}

void push(int e)
{
	Node* p = (Node*)malloc(sizeof(Node));
	if (p != NULL) {
		p->data = e;
		list_add(&p->list, &stack);
	} 
	else
		perror("memory error");
}

int pop()
{
	Node* p;
	struct LIST_HEAD_T* temp = NULL;
	int e;

	if (is_empty())
		perror("에러");

	temp = stack.next;
	p = list_entry(temp, Node, list);

	e = p ? p->data : -1;
	list_del(temp);

	free(p);

	return e;
}


int peek() {
	Node* p;
	struct LIST_HEAD_T* temp = NULL;
	int e;

	if (is_empty())
		perror("에러");

	temp = stack.next;
	p = list_entry(temp, Node, list);
	e = p ? p->data : -1;

	return e;
}

void print_stack(char msg[]) {
	Node* p;
	struct LIST_HEAD_T* temp;

	printf("%s= ", msg);
	list_for_each(temp, &stack) {
		p = list_entry(temp, Node, list);
		printf("%2d ", p->data);
	}
	printf("\n");
}
