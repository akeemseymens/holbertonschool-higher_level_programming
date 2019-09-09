#include "lists.h"
/**
 *int check_cycle - check if the singly linked list has a cycle in it.
 *@list: singly linked list.
 *
 **/
int check_cycle(listint_t *list)
{
  listint_t *slow_p = list;
  listint_t *fast_p = list;
  
  while (slow_p && fast_p && fast_p->next)
    {
      slow_p = slow_p->next; 
      fast_p = fast_p->next->next; 
      if (slow_p == fast_p)
	return 1; 
    } 
  return 0; 
}
