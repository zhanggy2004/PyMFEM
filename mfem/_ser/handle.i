%module(package="mfem._ser") handle
%feature("autodoc", "1");
%{
#include <fstream>
#include <iostream>
#include "../common/io_stream.hpp"
#include "config/config.hpp"
#include "linalg/hypre.hpp"
#include "linalg/handle.hpp"
#include "fem/gridfunc.hpp"
#include "fem/linearform.hpp"
#include "numpy/arrayobject.h"
#include "../common/pyoperator.hpp"
#ifdef MFEM_USE_MPI
#include "fem/pfespace.hpp"
#endif
%}

%include "../common/mfem_config.i"

%include "exception.i"
%import "../common/exception.i"

 /*
#ifdef MFEM_USE_MPI
%include mpi4py/mpi4py.i
%mpi4py_typemap(Comm, MPI_Comm);
#endif
 */

%init %{
import_array();
%}

%import "operators.i"

 /*
#ifdef MFEM_USE_MPI
%import "hypre.i"
#endif
 */
#ifdef MFEM_USE_PETSC
%include "petsc.i"
#endif

%import "complex_operator.i"

%import "mem_manager.i"
%import "../common/handle_template.i"

// instantiate template methods (step 1: Rename Macro )
AS_RENAME(SparseMatrix)
IS_RENAME(SparseMatrix)
GET_RENAME(SparseMatrix)
RESET_RENAME(SparseMatrix)
CONVERT_FROM_RENAME(SparseMatrix)

AS_RENAME(ComplexSparseMatrix)
IS_RENAME(ComplexSparseMatrix)
GET_RENAME(ComplexSparseMatrix)
RESET_RENAME(ComplexSparseMatrix)
CONVERT_FROM_RENAME(ComplexSparseMatrix)

%include "linalg/handle.hpp"

%pythoncode %{
OperatorPtr=OperatorHandle
%}

// instantiate template methods (step 2: Instantiation)

AS_WRAP(SparseMatrix)
IS_WRAP(SparseMatrix)
GET_WRAP(SparseMatrix)
RESET_WRAP(SparseMatrix)
CONVERT_FROM_WRAP(SparseMatrix)

AS_WRAP(ComplexSparseMatrix)
IS_WRAP(ComplexSparseMatrix)
GET_WRAP(ComplexSparseMatrix)
RESET_WRAP(ComplexSparseMatrix)
CONVERT_FROM_WRAP(ComplexSparseMatrix)


