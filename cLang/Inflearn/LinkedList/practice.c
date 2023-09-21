#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int data;
  struct node *link;
} Node;
Node *head = NULL;

void init_list() {head = NULL;}

int is_empty() {return head == NULL;}

int size() {
  Node *p;
  int cnt = 0;
  for(p = head; p!=NULL; p=p->link) cnt++;
  return cnt;
}

Node* get_entry(int pos) {
  Node *tmp = head;
  int i;
  for(i=0; i<pos; i++){
    if(tmp == NULL) return NULL;
    tmp = tmp->link;
  }
  return tmp;
}

void replace(int pos, int val) {
  Node *tmp = get_entry(pos);
  if(tmp != NULL)
    tmp->data = val;
}

Node* find(int val) {
  Node *p;
  for(p = head; p != NULL; p=p->link)
    if(p->data == val) return p;
  return NULL;
}

void insert(int pos, int val) {
  Node *tmp = (Node *)malloc(sizeof(Node));
  tmp->data = val;
  tmp->link = NULL;

  Node *prev;

  if(pos == 0) {
    tmp->link = head;
    head = tmp;
  }
  else {
    prev = get_entry(pos-1);
    if(prev != NULL) {
      tmp->link = prev->link;
      prev->link = tmp;
    }
    else free(tmp);
  }
}

void delete(int pos) {
  Node *tmp, *prev;

  if(pos == 0 && is_empty() == 0) {
    tmp = head;
    head = head->link;
    free(tmp);
  }
  else {
    prev = get_entry(pos-1);
    prev->link = prev->link->link;
  }
}

void clear_list() {
  while (is_empty() == 0)
  {
    delete(0);
  }
}

int sum() {
  int sum = 0;
  Node *p;
  for(p = head; p != NULL; p=p->link) {
    sum += p->data;
  }
  return sum;
}

void print_list() {
  Node* p;
  for(p=head; p!=NULL; p=p->link)
    printf("%2d ", p->data);
  printf("\n");
}

int main() {
  insert(0,10);
  insert(1,20);
  delete(0);
  print_list();
}