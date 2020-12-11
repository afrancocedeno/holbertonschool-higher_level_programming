#include "lists.h"

/**
 * dlistint_len - number of element in a linked list.
 * @h: input variable with header.
 *
 * Return: value with
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t i = 0;

	for (; h; i++)
		h = h->next;
	return (i);
}
