#include "lists.h"

/**
 *
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *head = list, *speed_pointer = NULL;

	speed_pointer = list;
	if (!list) /* == NULL equals from unexistance */
		return (0);
	for (; speed_pointer != list; i++)
	{
		list = (*list).next;
		speed_pointer = (*(*speed_pointer).next).next;
		if ((*list).next == head)
			return (0);
		if (speed_pointer == list)
			return (1);
	}
	return (1);
}
