#include "lists.h"

/**
 * check_cycle - checks if a singly linked list exist
 * @list: pointer to the list
 * Return: 0 if cycle exist,1 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *p;
	listint_t *pre;

	p = list;
	pre = list;
	while (list && p && p->next)
	{
		list = list->next;
		p = p->next->next;

		if (list == p)
		{
			list = pre;
			pre =  p;
			while (1)
			{
				p = pre;
				while (p->next != list && p->next != pre)
				{
					p = p->next;
				}
				if (p->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
