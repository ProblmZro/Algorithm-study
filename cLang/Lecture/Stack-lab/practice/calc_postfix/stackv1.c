#include <stdio.h>
#include <errno.h>
#include "stackv1.h"

double data[MAX_STACK_SIZE];
int top;

void init_stack() {
    top = -1; 
}

int size() { 
    return top + 1; 
}

int is_empty() {
    return (top == -1); 
}

int is_full() {
    return (top == MAX_STACK_SIZE - 1); 
}

void push(double e) {
    if (is_full())
        perror("스택 포화 에러");
    data[++top] = e;
}

double pop() {
    if(is_empty())
        perror("스택 공백 에러");
    return data[top--];
}

double peek() {
    if(is_empty())
        perror("스택 공백 에러");
    return data[top];
}

void print_stack(char msg[]) {
    int i;
    printf("%s[%2d]= ", msg, size());
    for (i = 0; i < size(); i++)
        printf("%2f ", data[i]);
    printf("\n");
}

