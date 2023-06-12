#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints information about a Python list.
 * @p: A pointer to a PyObject representing a list.
 *
 * Return: Void.
 */
void print_python_list_info(PyObject *p)
{
    long int size, allocated, i;
    PyObject *item;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List: %ld\n", size);
    printf("[*] Allocated: %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
