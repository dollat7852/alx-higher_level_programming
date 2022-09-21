#include "lists.h"

/**
 * check_cycle - check if 2 consecutive elements of a list points to each other
 * @list: list to be checked
 * Return: 0 if no repetition, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	/* declare placeholders */
	listint_t *current;
	listint_t *tmp;

	current = list;

	if (current == NULL) /* an empty list cannot be cycle*/
		return (0);
	tmp = list->next;

	while (tmp != NULL && tmp->next != NULL)
	{
		printf("i am here\n");
		if (current == tmp)
		{
			printf("1ast name is \n");
			return (1);
		}
		tmp = tmp->next;
		current = current->next;
	}
	return (0);
}
