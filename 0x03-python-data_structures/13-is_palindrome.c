#include "lists.h"
/**
 * reverse_listint - Reverses a linked list in place
 * @head: A pointer to the head of the linked list
 *
 * This function reverses a linked list in place, updating the head
 * pointer to point to the new first node of the reversed list.
 *
 * Return: A pointer to the new head of the reversed linked list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	for (; node; node = next)
	{
		next = node->next;
		node->next = prev;
		prev = node;
	}


	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: A pointer to the head of the linked list
 *
 * This function determines whether a linked list is a palindrome,
 * returning 1 if it is, and 0 otherwise.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *a, *b, *c;
	size_t s = 0, y;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	a = *head;
	for (; a; a = a->next)
	{
		s++;
	}


	a = *head;
	y = 0;
	while (y < (s / 2) - 1)
	{
		a = a->next;
		y++;
	}


	if ((s % 2) == 0 && a->n != a->next->n)
		return (0);

	a = a->next->next;
	b = reverse_listint(&a);
	c = b;

	a = *head;
	for (; b; a = a->next, b = b->next)
	{
		if (a->n != b->n)
			return (0);
	}

	reverse_listint(&c);

	return (1);
}
