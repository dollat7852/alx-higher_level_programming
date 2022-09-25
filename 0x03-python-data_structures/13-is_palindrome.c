#include "lists.h"
/**
 * is_palindrome - check if the content of a singly linked list is a palindrome
 * @head: a pointer to the start of the link
 * Return: 0 for palindrome, 1 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *first, *last;
	int len = 0;

	if (!list)
		return (0);
	/* empty of a single element list is a palindrome*/
	if (!(*head) || !((*head)->next))
		return (1);
	current = *head;
	first = *head;
	while (current)
	{
		len += 1;
		last = current;
		current = current->next;
	}
	/* to be a palindrome, first and last value must be equal*/
	if (first->n != last->n)
		return (0);
	/* if it has 3 element and first and last are equal it is a palindrome*/
	else if (n == 3)
		return (1)
}
