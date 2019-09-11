#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted linked list.
 * @head: Pointer to the pointer of the first node of listint_t list.
 * @number: Integer to be included into the new node.
 * Return: Upon sucess the address of the new node. Otherwise NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *current;
  listint_t *new_node;

  if (head == NULL)
    return (NULL);

  current = *head;
  new_node = malloc(sizeof(listint_t));

  if (new_node == NULL)
    return (NULL);

  new_node->n = number;
  new_node->next = NULL;

  if (*head == NULL)
  {
      *head = new_node;
      return (new_node);
  }

  if (current->n > number)
  {
      *head = new_node;
      new_node->next = tmp;
      return (new_node);
   }

  while (tmp->next != NULL)
  {
      if (tmp->next->n > number)
	{
	  new_node->next = tmp->next;
	  tmp->next = new_node;
	  return (new_node);
	}
      tmp = tmp->next;
  }

  tmp->next = new_node;
  return (new_node);
}
