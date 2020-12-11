#include "lists.h"

/**
 *
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *head = list, *speed_pointer = NULL;

	if (!list)
		return (0);
	for (; (*list).next; i++) /* is equal to (*list).next != NULL */
	{
		if ((*list).next == head)
			return (1);
		list = (*list).next;
		speed_pointer = (*(*speed_pointer).next).next; /* equals to speed_pointer->next->next */
		if (speed_pointer != head)
			return (1);
	}
	return (0);
}
