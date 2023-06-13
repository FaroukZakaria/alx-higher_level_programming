#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - s
 * @head: s
 * Return: s
 */
int is_palindrome(listint_t **head)
{
	listint_t *cur = NULL, *next = NULL, *prev = NULL, *p = *head, *q = *head, *new;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		p = p->next->next;
		if (p == NULL)
		{
			new = q->next;
			break;
		}
		else if (p->next == NULL)
		{
			new = q->next->next;
			break;
		}
		q = q->next;
	}
	q->next = NULL;
	q = *head;
	cur = new;
	while (cur != NULL)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	new = prev;
	while (q != NULL && new != NULL)
	{
		if (q->n != new->n)
			return (0);
		q = q->next;
		new = new->next;
	}
	return (1);
}
