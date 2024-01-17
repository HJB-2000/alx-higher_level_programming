#include "lists.h"
#include <stdlib.h>
#include <stddef.h>


/**
 * insert_node - Inserts a node into a sorted linked list
 * @head: A pointer to the head of the linked list
 * @number: The value to insert into the linked list
 *
 * This function inserts a new node with the given value into a sorted
 * linked list while maintaining the ascending order of the list.
 *
 * Return: A pointer to the newly inserted node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *n_node, *old = NULL;

	if (!head)
		return (NULL);

	n_node = malloc(sizeof(listint_t));
	if (!n_node)
		return (NULL);

	n_node->n = number;
	n_node->next = NULL;

	tmp = *head;
	for (; tmp && n_node->n > tmp->n; old = tmp, tmp = tmp->next)
	{
		old = tmp;
		tmp = tmp->next;
	}
	while (tmp && n_node->n == tmp->n)
	{
		n_node->next = tmp;
		old->next = n_node;
		if (!old)
		{
			n_node->next = *head;
			*head = n_node;
		}
		else
		{
			n_node->next = old->next;
			old->next = n_node;
		}
	}

	return (n_node);
}
