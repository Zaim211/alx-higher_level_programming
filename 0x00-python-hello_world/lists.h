#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct listint_s - singly linked list
 * @i: integer
 * @p: pointer to next node
 * Description: singly linked list node
 * For Holberton project
 */
typedef struct listint_s
{
	int i;
	struct listint_s *p;
} listint_t;
