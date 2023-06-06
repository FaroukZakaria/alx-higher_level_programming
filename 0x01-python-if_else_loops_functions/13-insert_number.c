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
	listint_t *current = *head;

	while (current->next != NULL)
	{
		current = current->next;
	}
	current->n = number;
	return (current);
}
