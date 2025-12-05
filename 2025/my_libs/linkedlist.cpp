#include "linkedlist.h"

Node::Node(void *value, Node *next, Node *prev) : value(value), next(next), prev(prev)
{
}

LinkedList::LinkedList() : head(NULL), tail(NULL), length(0)
{
}

void LinkedList::push(void *value)
{
    if (head == NULL)
    {
        head = new Node(value, NULL);
        tail = head;
    }
    else
    {
        tail->next = new Node(value, NULL, tail);
        tail = tail->next;
    }

    length++;
}

void LinkedList::iterate_list(void (*func)(void *))
{
    Node *ptr = head;
    while (ptr != NULL)
    {
        func(ptr->value);
        ptr = ptr->next;
    }
}

void LinkedList::swap_with_next(Node *ptr)
{
    if (ptr == NULL)
        return;

    Node *next = ptr->next;
    if (next == NULL)
        return;
    
    Node *back_one = ptr->prev;
    Node *forw_one = next->next;

    if (back_one != NULL)
    {
        back_one->next = next;
    }

    if (forw_one != NULL)
    {
        forw_one->prev = ptr;
    }

    ptr->prev = next;
    ptr->next = forw_one;

    next->prev = back_one;
    next->next = ptr;

    if (head == ptr)
        head = next;

    if (tail == next)
        tail = ptr;
}