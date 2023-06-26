#include <Python.h>

void print_python_list(PyObject *list_object);
void print_python_bytes(PyObject *bytes_object);
void print_python_float(PyObject *float_object);

/**
 * print_python_list - Prints basic information about Python list objects.
 * @list_object: A PyObject list object.
 */
void print_python_list(PyObject *list_object)
{
	Py_ssize_t size, allocated, i;
	const char *type;
	PyListObject *list = (PyListObject *)list_object;
	PyVarObject *var = (PyVarObject *)list_object;

	size = var->ob_size;
	allocated = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(list_object->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic information about Python bytes objects.
 * @bytes_object: A PyObject bytes object.
 */
void print_python_bytes(PyObject *bytes_object)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)bytes_object;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(bytes_object->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)bytes_object)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)bytes_object)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)bytes_object)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic information about Python float objects.
 * @float_object: A PyObject float object.
 */
void print_python_float(PyObject *float_object)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)float_object;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(float_object->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
