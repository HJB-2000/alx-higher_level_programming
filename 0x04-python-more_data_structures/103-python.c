#include <stdio.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A pointer to the Python bytes object
 *
 * This function prints information about a Python bytes object, including
 * its size, a portion of its content as a string, and the first few bytes
 * represented in hexadecimal.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t s = 0, a = 0;
	char *string = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &string, &s) != -1)
	{
		printf("  size: %zd\n", s);
		printf("  trying string: %s\n", string);
		printf("  first %zd bytes:", s < 10 ? s + 1 : 10);
		for (; a < s + 1 && a < 10; a++)
		{
			printf(" %02hhx", string[a]);
		}

		printf("\n");
	}
}

/**
 * print_python_list - Prints information about a Python list
 * @p: A pointer to the Python list object
 *
 * This function prints information about a Python list, including its size,
 * allocation, and information about each element's data type. If an element
 * is a bytes object, additional information is printed using
 *  print_python_bytes.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t s = 0;
	PyObject *item;
	int a = 0;

	if (PyList_CheckExact(p))
	{
		s = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		for (; a < s; a++)
		{
			item = PyList_GET_ITEM(p, a);
			printf("Element %d: %s\n", a, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
		}

	}
}
