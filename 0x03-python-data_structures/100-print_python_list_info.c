#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints python list info
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	long int size, j;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python Lis = %ld\n", size);

	list = (PyListPbject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (j = 0; j < size; j++)
	{
		item = PyList_GetItem(p, j);
		printf("Element %ld: %ls\n", j, Py_TYPE(item)->tp_name);
	}
}
