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

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %ls\n", i, Py_TYPE(item)->tp_name);
	}
}
