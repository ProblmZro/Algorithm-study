#pragma once

/* Stack implementation using array */

#define MAX_STACK_SIZE		256

void init_stack();
int size();
int is_empty();
int is_full();
void push(double e);
double pop();
double peek();
void print_stack(char msg[]);
