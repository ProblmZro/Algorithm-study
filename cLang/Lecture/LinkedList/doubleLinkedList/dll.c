#include <stdio.h> 
#include <stdlib.h> 

typedef struct node_t {
	int data;
	struct node_t* prev;
	struct node_t* next;
} Node;

Node head;	

void init_list() { head.next = NULL; }
Node* get_head() { return head.next; }
int is_empty() { return get_head() == NULL; }

Node* get_entry(int pos)
{
	Node* n = &head;
	int i = -1;
	for (i = -1; i < pos; i++, n = n->next)
		if (n == NULL) break;
	return n;
}

void replace(int pos, int val)
{
	Node* node = get_entry(pos);
	if (node != NULL)
		node->data = val;
}

int size()
{
	Node* p;
	int count = 0;
	for (p = get_head(); p != NULL; p = p->next)
		count++;
	return count;
}

Node* find(int val)
{
	Node* p;
	for (p = get_head(); p != NULL; p = p->next)
		if (p->data == val) return p;
	return NULL;
}

void print_list(char* msg)
{
	Node* p;
	printf("%s[%2d]: ", msg, size());
	for (p = get_head(); p != NULL; p = p->next)
		printf("%2d ", p->data);
	printf("\n");
}

void insert_next(Node* before, Node* n)
{
	if(n != NULL) {
		n->prev = before;
		n->next = before->next;
		if(before->next != NULL)
			before->next->prev = n;
		before->next = n;
	}
}

void insert(int pos, int val)
{
	Node* new_node, * prev;

	prev = get_entry(pos - 1);
	if (prev != NULL) {
		new_node = (Node*)malloc(sizeof(Node));
		new_node->data = val;
		new_node->prev = NULL;
		new_node->next = NULL;

		insert_next(prev, new_node);
	}
}

void remove_curr(Node* n)
{
	if(n->prev != NULL)
		n->prev->next = n->next;
	if(n->next != NULL)
		n->next->prev = n->prev;
}

void delete(int pos)
{
	Node* n = get_entry(pos);
	if (n != NULL)
		remove_curr(n);
}

void clear_list()
{
	while (is_empty() == 0)
		delete(0);
}

int sum_forward() {
  int sum = 0;
  Node* p = NULL;
  for(p = get_head(); p != NULL; p = p->next) {
    sum += p->data;
  }
  return sum;
}

int sum_backward() {
  int sum = 0;
  Node* p = NULL;
  for(p = get_entry(size() - 1); p != NULL; p = p->prev) {
    sum += p->data;
  }
  return sum;
}

int main()
{
	init_list();
	insert(0, 10);
	insert(0, 20);
	insert(1, 30);
	insert(size(), 40);
	insert(2, 50);
	print_list("���߿��Ḯ��Ʈ�� ������ List(����x5)");
	printf("sum : %d\n", sum_backward());
	printf("sum : %d\n", sum_forward());

	replace(2, 90);
	print_list("���߿��Ḯ��Ʈ�� ������ List(��üx1)");

	delete(2);
	delete(size() - 1);
	delete(0);
	print_list("���߿��Ḯ��Ʈ�� ������ List(����x3)");

	clear_list();
	print_list("���߿��Ḯ��Ʈ�� ������ List(������)");
}

