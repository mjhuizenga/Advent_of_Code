#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

class Node
{
public:
    Node(void *value, Node *next, Node *prev=NULL);
    void *value;
    Node *next;
    Node *prev;
};

class LinkedList
{
public:
    LinkedList();
    void push(void *value);
    void iterate_list(void (*func)(void *));
    void swap_with_next(Node *ptr);

    Node *head;
    Node *tail;
    int length;
};