#include <stdio.h>
#include "list.h"
#include <stdlib.h>
#include <string.h>

struct student_t
{
    int age;
    char name[20];
    struct LIST_HEAD_T list;
};
#define NUM_OF_ITEMS    10
struct student_t data_array[NUM_OF_ITEMS];
int index;
int alloc_data_st() {
    return (index < NUM_OF_ITEMS) ? index++ : 0;
}

int main() {

    LIST_HEAD(student_list);
    struct student_t* p1, * p2;
    struct LIST_HEAD_T* temp, *n;
    struct student_t* p;

    p1 = &data_array[alloc_data_st()];
    p2 = &data_array[alloc_data_st()];
    // p = malloc(sizeof(struct student_t));
    list_add(&p1->list, &student_list);
    list_add(&p2->list, &student_list);

    //for( temp = head.prev; temp != &head; temp = temp->prev ) 
    list_for_each_safe(temp, n, &student_list)
    {
        p = list_entry(temp, struct student_t, list);
        printf("name:%s, age:%d\n", p->name, p->age);
        free(p);
    }

	return 0;
}


// gcc test.c listlib.c -o test
// ./test