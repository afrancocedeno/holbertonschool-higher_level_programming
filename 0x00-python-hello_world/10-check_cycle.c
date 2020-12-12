#include "lists.h"

/**
 *
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *head = list, *speed_pointer = NULL;

	if (!list) /* == NULL equals from unexistance */
		return (0);
	for (; (*list).next; i++) /* is equal to (*list).next != NULL */
	{
		if ((*speed_pointer).next == list)
			return (1);
		if ((*list).next == head)
			return (1);
		list = (*list).next;
		speed_pointer = (*(*speed_pointer).next).next;
	}
	return (0);
}
