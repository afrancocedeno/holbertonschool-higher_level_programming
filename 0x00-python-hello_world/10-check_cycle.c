#include "lists.h"

/**
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list, *speed_pointer = NULL;

	speed_pointer = list;
	if (!list) /* == NULL equals from unexistance */
		return (0);
	while (list && speed_pointer) /* while they exist */
	{
		list = (*list).next;
		speed_pointer = (*(*speed_pointer).next).next;
		if ((*list).next == head)
			return (1);
		if (speed_pointer == list)
			return (1);
	}
	return (0);
}
