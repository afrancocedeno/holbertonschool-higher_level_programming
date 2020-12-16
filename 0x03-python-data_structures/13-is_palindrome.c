#include "lists.h"

int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, buffer[1024];
	listint_t *aux_ptr = NULL;

	aux_ptr = *head;
	/* buffering */
	for (; i < 20; i++)
		buffer[i] = '\0';
	for (i = 0; aux_ptr; i++, aux_ptr = (*aux_ptr).next)
		buffer[i] = (*aux_ptr).n;
	for (; j <= i; j++, i--)
		if (buffer[j] != buffer[(i - 1)])
			return (0);
	return (1);
}