#include "lists.h"
/**
 * insert_node insers a number into a sorted singly linked list.
 * @head - location of node in list
 * @number - data in the node
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_int *new_node;
  listint_int *current = *head;
  
  if (!head)
    return (NULL);

  new_node = malloc(sizeof(list_int));
  if (!new_node)
    return (NULL);

  new_node->n = number;
  new_node->next = NULL;

  if (*head  == NULL)
    *head = new_node;
  else
    {
      while (ncurrent->next_node->n)
	{
	  if (number > current->next_node->n)
	    current = current->next;
	  else
	    break;
	}
      new_node->next = current->next;
      current->next = new_node;
    }
  return (new_node)
}
