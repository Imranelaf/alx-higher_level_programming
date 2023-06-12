#include <Python.h>

/**
 * print_python_list_info - Prints information about a Python list.
 * @list_obj: A pointer to a PyObject representing a list.
 *
 * Return: Void.
 */
void print_python_list_info(PyObject *list_obj)
{
	int size, allocated, i;
	PyObject *item;

	size = Py_SIZE(list_obj);
	allocated = ((PyListObject *)list_obj)->allocated;

	printf("[*] Size of the Python List: %d\n", size);
	printf("[*] Allocated: %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		item = PyList_GetItem(list_obj, i);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
