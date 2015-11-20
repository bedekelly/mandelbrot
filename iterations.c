#include "complex.h"
#include "Python.h"


/* Calculate the number of iterations a point takes to leave a bound. */
int iterations(int cr, int ci, int max_it) {
  int i;
  double complex z = 0 + 0*I;
  double complex c = cr + ci*I;
  for (i=0; i<max_it; i++) {
    z = z*z + c;
    if (cabs(z) > 4)
      break;
  }
  return i;
}


/* Wrap the C function with a Python callable. */
static PyObject *py_iterations (PyObject *self, PyObject *args) {
  double x, y;
  int its, max_iterations;
  
  if (!PyArg_ParseTuple(args, "dd|i:iterations", &x, &y, &max_iterations))
    return NULL;
  
  its = iterations(x, y, max_iterations);
  return PyLong_FromLong((long) its);
}


/* List all methods defined by this module. */
static PyMethodDef its_methods[] = {
  {"iterations", py_iterations, METH_VARARGS, NULL},  // TODO: docstrings.
  {NULL, NULL}  // TODO: what? why?
};


static struct PyModuleDef its_module = {
  PyModuleDef_HEAD_INIT,
  "iterations",
  NULL,
  -1,
  its_methods
};


PyMODINIT_FUNC PyInit_iterations(void) {
  return PyModule_Create(&its_module);
}
