#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a Python list.
 * @list_obj: A pointer to a PyObject representing a list.
 *
 * Return: Void.
 */
void print_python_list_info(PyObject *list_obj)
{
    Py_ssize_t size, allocated, i;
    PyObject *item;

    if (list_obj == NULL)
    {
        printf("Invalid List Object\n");
        return;
    }

    size = PyList_Size(list_obj);
    allocated = ((PyListObject *)list_obj)->allocated;

    printf("[*] Size of the Python List: %ld\n", size);
    printf("[*] Allocated: %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %ld: ", i);

        item = PyList_GetItem(list_obj, i);
        printf("%s\n", Py_TYPE(item)->tp_name);
    }
}
