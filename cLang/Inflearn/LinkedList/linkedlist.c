#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  char *data;
  struct node *next;
}Node;

Node *head = NULL;

int main() {
  // Mon -> Tues -> Thurs
  head = (Node *)malloc(sizeof(Node));
  head->data = "Tuesday";
  head->next = NULL;

  Node *q = (Node *)malloc(sizeof(Node));
  q->data = "Thursday";
  q->next = NULL;
  head->next = q;

  q = (Node *)malloc(sizeof(Node));
  q->data = "Monday";
  q->next = head;
  head = q;

  Node *p = head;
  while (p != NULL)
  {
    printf("%s\n", p->data);
    p = p->next;
  }
}