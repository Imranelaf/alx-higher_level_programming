#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *obj)
{
    PyBytesObject *bytesObj;
    long int size;
    int i;
    char *byteData = NULL;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytesObj = (PyBytesObject *)obj;
    PyBytes_AsStringAndSize(obj, &byteData, &size);

    printf("  size: %li\n", size);
    printf("  byte data: %s\n", byteData);

    if (size < 10)
        printf("  first %li bytes:", size + 1);
    else
        printf("  first 10 bytes:");

    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", byteData[i]);

    printf("\n");
}

void print_python_list(PyObject *obj)
{
    long int size = PyList_Size(obj);
    int i;
    PyListObject *listObj = (PyListObject *)obj;
    const char *typeName;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", listObj->allocated);

    for (i = 0; i < size; i++)
    {
        typeName = (listObj->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, typeName);

        if (!strcmp(typeName, "bytes"))
            print_python_bytes(listObj->ob_item[i]);
    }
}
