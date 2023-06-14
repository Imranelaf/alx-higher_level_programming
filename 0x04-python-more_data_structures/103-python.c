#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about a bytes object
 *
 * @p: Python bytes object
 * Return: No return value
 */
void print_python_bytes(PyObject *p)
{
	char *data;
	long int size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	data = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  data: %s\n", data);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		if (data[i] >= 0)
			printf(" %02x", data[i]);
		else
			printf(" %02x", 256 + data[i]);
	}

	printf("\n");
}

/**
 * print_python_list - Prints information about a Python list object
 *
 * @p: Python list object
 * Return: No return value
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
