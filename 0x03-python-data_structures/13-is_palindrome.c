#include "lists.h"
/**
 *is_Palindrome_helper - checks to see if linked list is palindrome.
 *@left: left-ward end list
 *@right: righ-ward end of list
 *
 *Return: 0 on success
 **/

int is_Palindrome_helper(listint_t **left, listint_t *right)
{
	int result;

	if (right == NULL)
		return (1);
	result = is_Palindrome_helper(left, right->next);
	if (result == 0)
		return (0);
	if ((*left)->n == right->n)
	{
		*left = (*left)->next;
		return (1);
	}
	return (0);
}
/**
 * is_palindrome- recursively calls the function is_Palindrome_helper
 * @head: head of node
 *Return: 0 on success
 **/
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;

	return (is_Palindrome_helper(&temp, temp));
}
