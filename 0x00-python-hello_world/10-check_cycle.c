#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: A pointer to the head of the linked list
 *
 * This function checks if a linked list has a cycle using
 * Floyd's cycle-finding algorithm (tortoise and hare).
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *heade;

	if (!(list && list->next))
	{
		return (0);
	}

	turtle = list->next;
	heade = list->next->next;

	for (; turtle && heade && heade->next;
			turtle = turtle->next, heade = heade->next->next)
	{
		if (turtle == heade)
		{
			return (1);
		}
	}

	return (0);
}
