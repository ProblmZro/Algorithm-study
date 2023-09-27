#include "list.h"


void __list_add(struct LIST_HEAD_T* new,
    struct LIST_HEAD_T* prev,
    struct LIST_HEAD_T* next) {
    next->prev = new;
    new->next = next;
    new->prev = prev;
    prev->next = new;
}

void list_add(struct LIST_HEAD_T* new, struct LIST_HEAD_T* head) {
    __list_add(new, head, head->next);
}

void list_add_tail(struct LIST_HEAD_T* new, struct LIST_HEAD_T* head) {
    __list_add(new, head->prev, head);
}

void __list_del(struct LIST_HEAD_T* prev, struct LIST_HEAD_T* next) {
    next->prev = prev;
    prev->next = next;
}

void list_del(struct LIST_HEAD_T* entry) {
    __list_del(entry->prev, entry->next);
    entry->next = (void*)0;
    entry->prev = (void*)0;
}

int list_empty(struct LIST_HEAD_T* head) {
    return head->next == head;
}

