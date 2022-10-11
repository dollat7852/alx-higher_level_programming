#include "lists.h"

/**
 * check_cycle - check if 2 consecutive elements of a list points to each other
 * @list: list to be checked
 * Return: 0 if no repetition, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	/* declare placeholders */
	listint_t *current, *tmp;

	current = list;
	tmp = list->next;
	if (!list)
		return (0);
	while(current && tmp)
	{
		if (current == tmp)
			return (1);
		current = current->next->next;
		tmp = tmp->next;
	}
	return (0);
}
