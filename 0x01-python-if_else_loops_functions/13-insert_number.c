#include "lists.h"
#include <stddef.h>
/**
 * insert_node - s
 * @head: s
 * @number: s
 * Return: s
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	if (current == NULL or current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current != NULL || current->next != NULL || current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next
	current->next = new;
	return (new);
}
