#include <stdio.h>
#include <stdlib.h>

typedef struct node_t {
  int data;
  struct node_t* link;
} Node;

Node* top;

void init_stack() {
  top = NULL;
}

int size() {
  Node* p;
  int cnt = 0;
  for(p = top; p != NULL; p->link ) cnt++;
}

int is_empty() {
  return (top == NULL)? 1 : 0;
}

void push(int e) {
  Node* p = (Node*)malloc(sizeof(Node));
  p->data = e;
  p->link = top;
  p = top;
}

int pop() {
  if(is_empty()) perror("스택이 비었습니다.");
  Node* p;
  int e;
  p = top;
  e = p->data;
  top = p->link;
  free(p); 
  return e;
}

int peek() {
  return top->data;
}

void print_stack() {
  int i;
  for(i=0; i<size(); i++) {
    printf("%d ",data[i]);
  }
  printf("\n");
}

int main() {
  int i;
	init_stack();
	for (i = 1; i < 10; i++)
		push(i);
	print_stack();
	printf("\tpop() --> %d\n", pop());
	printf("\tpop() --> %d\n", pop());
	printf("\tpop() --> %d\n", pop());
	print_stack();
}