#include "lists.h"

/**
 *
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *head = list;

	if (list != NULL)
		return (0);
	for (; (*list).next; i++) /* is equal to (*list).next != NULL */
	{
		if ((*list).next == head)
			return (1);
		list = (*list).next;
	}
	return (0);
}
