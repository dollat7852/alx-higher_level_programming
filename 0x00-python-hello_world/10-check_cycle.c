#include "lists.h"

/**
 * check_cycle - check if 2 consecutive elements of a list points to each other
 * @list: list to be checked
 * Return: 0 if no repetition, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	/* declare placeholders */
	listint_t *current = list;
	listint_t *tmp;

	if (current == NULL) /* an empty list cannot be cycle*/
		return (0);
	tmp = current->next;

	while (tmp != NULL && tmp->next != NULL)
	{
		if (current == tmp)
		{
			printf("1");
			return (1);
		}
		current = tmp;
		tmp = tmp->next;
	}
	return (0);
}
