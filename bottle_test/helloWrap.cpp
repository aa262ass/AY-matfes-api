// helloWrap.c
#include <python3.4/Python.h>
#define BUFSIZE 256

extern int add(int, int);
extern void out(const char*, const char*, char * const, const size_t);

static PyObject* hello_add(PyObject* self, PyObject* args){
	int x, y, g;

	if(!PyArg_ParseTuple(args, "ii", &x, &y)){
		return NULL;
	}else{
		g = add(x, y);
		return Py_BuildValue("i", g);
	}
}

static PyObject* hello_out(PyObject* self, PyObject* args, PyObject* kw){

	const char* adrs = NULL;
	const char* name = NULL;
	static char* argnames[] = {"adrs", "name", NULL};
	char str_out[BUFSIZE];

	if(!PyArg_ParseTupleAndKeywords(args, kw, "|ss", argnames, &adrs, &name)){
		return NULL;
	}else{
		out(adrs, name, str_out, sizeof(str_out));
		return Py_BuildValue("s", str_out);
	}
}


static PyMethodDef hellomethods[] = {
	{"add", (PyCFunction)hello_add, METH_VARARGS},
	{"out", (PyCFunction)hello_out, METH_VARARGS | METH_KEYWORDS},
	{NULL},
};

static struct PyModuleDef hellomodule = {
	PyModuleDef_HEAD_INIT,
	"hello",
	NULL,
	-1,
	hellomethods
};

#ifdef __cplusplus
extern "C" {
#endif
	PyMODINIT_FUNC PyInit_hello(void)
	{
		return PyModule_Create(&hellomodule);
	}
#ifdef __cplusplus
}
#endif
