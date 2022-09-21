#include "lists.h"
/**
 *insert_node - A function that appropriately insert a node in a sorted list
 *@head: head address of the sorted list
 *@number: int value of the new node
 *Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *tmp;
	listint_t *new_l; 
		
	new_l = malloc(sizeof(listint_t));
	current = *head;
	tmp = current->next;
	new_l->n = number;

	if (new_l == NULL)
		return (NULL);
	if (current == NULL)
	{
		*head = new_l;
		return(new_l);
	}
	if (current->n > number)
	{
		new_l->next = current;
		current = new_l;
		return(new_l);
	}
	while(current != NULL && tmp)
	{
		if (current->n < number && tmp->n > number)
		{	
			new_l->next = tmp;
			current->next = new_l;
			return (new_l);
		}
		
		current = current->next;
		tmp = tmp->next;

	}
	current->next = new_l;
	return (new_l);
}
