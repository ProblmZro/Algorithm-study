#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int data;
  struct node *next;
  struct node *prev;
} Node;
Node head;

void init_list() {head.next = NULL;}
Node* get_head() {return head.next;}
int is_empty() {return get_head() == NULL;}

int size() {
  Node *p;
  int cnt = 0;
  for(p = get_head(); p!=NULL; p=p->next) cnt++;
  return cnt;
}

Node* get_entry(int pos) {
  Node *tmp = &head;
  int i;
  for(i=-1; i<pos; i++){
    if(tmp == NULL) break;
    tmp = tmp->next;
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
  for(p = get_head(); p != NULL; p=p->next)
    if(p->data == val) return p;
  return NULL;
}

void insert_next(Node *before, Node *n) {
  if(n != NULL) {
    n->prev = before;
    n->next = before->next;
    if(before->next != NULL)
      before->next->prev = n;
    before->next = n;
  }
}

void insert(int pos, int val) {
  Node *tmp, *prev;

  prev = get_entry(pos-1);
  if(prev != NULL) {
    tmp = (Node *)malloc(sizeof(Node));
    tmp->data = val;
    tmp->prev = NULL;
    tmp->next = NULL;
    
    insert_next(prev, tmp);
  }
}

void remove_curr(Node *n) {
  if(n->prev != NULL)
    n->prev->next = n->next;
  if(n->next != NULL)
    n->next->prev = n->prev;
}

void delete(int pos) {
  Node *n;

  n = get_entry(pos);
  if(n != NULL) {
    remove_curr(n);
  }
}

void clear_list() {
  while (is_empty() == 0)
    delete(0);
}

void print_list() {
  Node* p;
  for(p=get_head(); p!=NULL; p=p->next)
    printf("%2d ", p->data);
  printf("\n");
}

int main() {
  insert(0,10);
  insert(1,20);
  // delete(0);
  print_list();
}