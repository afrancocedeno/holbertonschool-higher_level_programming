#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: input variable.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list, *speed_pointer = NULL;

	speed_pointer = list;
	if (!list || (*list).next == NULL) /* == NULL equals from unexistance */
		return (0);
	while ((*list).next != NULL && (*speed_pointer).next != NULL) /* while they exist */
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
