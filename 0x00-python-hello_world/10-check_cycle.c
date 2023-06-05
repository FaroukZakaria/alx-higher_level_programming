#include "lists.h"
/**
 * check_cycle - s
 * @list: s
 * Return: s
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	listint_t *step = fast->next;

	if (list == NULL)
		return (0);
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = step->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
