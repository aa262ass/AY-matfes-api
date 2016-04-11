// helloWrap.c
#include <python3.4/Python.h>
#define BUFSIZE 2048

extern int add(int, int);
extern void out(const char*, const char*, char* const, const size_t);
extern int mycat(const char*, char* const, const size_t);

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

	const char* fname = NULL;
	const char* lname = NULL;
	static char* argnames[] = {(char*)"fname", (char*)"lname", NULL};
	char strout[BUFSIZE];

	if(!PyArg_ParseTupleAndKeywords(args, kw, "|ss", argnames, &fname, &lname)){
		return NULL;
	}else{
		out(fname, lname, strout, sizeof(strout));
		return Py_BuildValue("s", strout);
	}
}

static PyObject* hello_mycat(PyObject* self, PyObject* args, PyObject* kw){

	const char* filename = NULL;
	static char* argnames[] = { (char*)"filename", NULL};
	char strout[BUFSIZE];

	if(!PyArg_ParseTupleAndKeywords(args, kw, "|s", argnames, &filename)){
		return NULL;
	}else{
		if(mycat(filename, strout, sizeof(strout)) < 0) {
			return Py_BuildValue("s", "Error");
		}
		return Py_BuildValue("s", strout);
	}
}

static PyMethodDef hellomethods[] = {
	{"add", (PyCFunction)hello_add, METH_VARARGS},
	{"out", (PyCFunction)hello_out, METH_VARARGS | METH_KEYWORDS},
	{"mycat", (PyCFunction)hello_mycat, METH_VARARGS | METH_KEYWORDS},
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
