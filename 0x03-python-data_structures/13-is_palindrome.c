#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - file description.
 * @head: input list.
 *
 * Return: value 0 or 1.
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, buffer[5 * 1024];
	listint_t *aux_ptr = NULL;

	aux_ptr = *head;
	if (!*head || !(*(*head)).next)
		return (1);
	/* buffering */
	for (; i < 20; i++)
		buffer[i] = '\0';
	for (i = 0; aux_ptr; i++)
	{
		buffer[i] = (*aux_ptr).n;
		aux_ptr = (*aux_ptr).next;
	}
	for (; j <= i; j++, i--)
		if (buffer[j] != buffer[(i - 1)])
			return (0);
	return (1);
}
