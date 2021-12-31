# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _gridfunc
else:
    import _gridfunc

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _gridfunc.SWIG_PyInstanceMethod_New
_swig_new_static_method = _gridfunc.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.vector
import mfem._ser.coefficient
import mfem._ser.globals
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.symmat
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.fe_base
import mfem._ser.fe_fixed_order
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.fe_h1
import mfem._ser.fe_nd
import mfem._ser.fe_rt
import mfem._ser.fe_l2
import mfem._ser.fe_nurbs
import mfem._ser.fe_pos
import mfem._ser.fe_ser
import mfem._ser.mesh
import mfem._ser.sort_pairs
import mfem._ser.ncmesh
import mfem._ser.vertex
import mfem._ser.vtk
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.doftrans
import mfem._ser.handle
import mfem._ser.restriction
import mfem._ser.bilininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
class GridFunction(mfem._ser.vector.Vector):
    r"""Proxy of C++ mfem::GridFunction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def MakeOwner(self, fec_):
        r"""MakeOwner(GridFunction self, FiniteElementCollection fec_)"""
        return _gridfunc.GridFunction_MakeOwner(self, fec_)
    MakeOwner = _swig_new_instance_method(_gridfunc.GridFunction_MakeOwner)

    def OwnFEC(self):
        r"""OwnFEC(GridFunction self) -> FiniteElementCollection"""
        return _gridfunc.GridFunction_OwnFEC(self)
    OwnFEC = _swig_new_instance_method(_gridfunc.GridFunction_OwnFEC)

    def VectorDim(self):
        r"""VectorDim(GridFunction self) -> int"""
        return _gridfunc.GridFunction_VectorDim(self)
    VectorDim = _swig_new_instance_method(_gridfunc.GridFunction_VectorDim)

    def GetTrueVector(self, *args):
        r"""
        GetTrueVector(GridFunction self) -> Vector
        GetTrueVector(GridFunction self) -> Vector
        """
        return _gridfunc.GridFunction_GetTrueVector(self, *args)
    GetTrueVector = _swig_new_instance_method(_gridfunc.GridFunction_GetTrueVector)

    def GetTrueDofs(self, tv):
        r"""GetTrueDofs(GridFunction self, Vector tv)"""
        return _gridfunc.GridFunction_GetTrueDofs(self, tv)
    GetTrueDofs = _swig_new_instance_method(_gridfunc.GridFunction_GetTrueDofs)

    def SetTrueVector(self):
        r"""SetTrueVector(GridFunction self)"""
        return _gridfunc.GridFunction_SetTrueVector(self)
    SetTrueVector = _swig_new_instance_method(_gridfunc.GridFunction_SetTrueVector)

    def SetFromTrueDofs(self, tv):
        r"""SetFromTrueDofs(GridFunction self, Vector tv)"""
        return _gridfunc.GridFunction_SetFromTrueDofs(self, tv)
    SetFromTrueDofs = _swig_new_instance_method(_gridfunc.GridFunction_SetFromTrueDofs)

    def SetFromTrueVector(self):
        r"""SetFromTrueVector(GridFunction self)"""
        return _gridfunc.GridFunction_SetFromTrueVector(self)
    SetFromTrueVector = _swig_new_instance_method(_gridfunc.GridFunction_SetFromTrueVector)

    def GetValue(self, *args):
        r"""
        GetValue(GridFunction self, int i, IntegrationPoint ip, int vdim=1) -> double
        GetValue(GridFunction self, ElementTransformation T, IntegrationPoint ip, int comp=0, Vector tr=None) -> double
        """
        return _gridfunc.GridFunction_GetValue(self, *args)
    GetValue = _swig_new_instance_method(_gridfunc.GridFunction_GetValue)

    def GetVectorValue(self, *args):
        r"""
        GetVectorValue(GridFunction self, int i, IntegrationPoint ip, Vector val)
        GetVectorValue(GridFunction self, ElementTransformation T, IntegrationPoint ip, Vector val, Vector tr=None)
        """
        return _gridfunc.GridFunction_GetVectorValue(self, *args)
    GetVectorValue = _swig_new_instance_method(_gridfunc.GridFunction_GetVectorValue)

    def GetValues(self, *args):
        r"""
        GetValues(GridFunction self, int i, IntegrationRule ir, Vector vals, int vdim=1)
        GetValues(GridFunction self, int i, IntegrationRule ir, Vector vals, DenseMatrix tr, int vdim=1)
        GetValues(GridFunction self, ElementTransformation T, IntegrationRule ir, Vector vals, int comp=0, DenseMatrix tr=None)
        """
        return _gridfunc.GridFunction_GetValues(self, *args)
    GetValues = _swig_new_instance_method(_gridfunc.GridFunction_GetValues)

    def GetVectorValues(self, *args):
        r"""
        GetVectorValues(GridFunction self, int i, IntegrationRule ir, DenseMatrix vals, DenseMatrix tr)
        GetVectorValues(GridFunction self, ElementTransformation T, IntegrationRule ir, DenseMatrix vals, DenseMatrix tr=None)
        """
        return _gridfunc.GridFunction_GetVectorValues(self, *args)
    GetVectorValues = _swig_new_instance_method(_gridfunc.GridFunction_GetVectorValues)

    def GetFaceValues(self, i, side, ir, vals, tr, vdim=1):
        r"""GetFaceValues(GridFunction self, int i, int side, IntegrationRule ir, Vector vals, DenseMatrix tr, int vdim=1) -> int"""
        return _gridfunc.GridFunction_GetFaceValues(self, i, side, ir, vals, tr, vdim)
    GetFaceValues = _swig_new_instance_method(_gridfunc.GridFunction_GetFaceValues)

    def GetFaceVectorValues(self, i, side, ir, vals, tr):
        r"""GetFaceVectorValues(GridFunction self, int i, int side, IntegrationRule ir, DenseMatrix vals, DenseMatrix tr) -> int"""
        return _gridfunc.GridFunction_GetFaceVectorValues(self, i, side, ir, vals, tr)
    GetFaceVectorValues = _swig_new_instance_method(_gridfunc.GridFunction_GetFaceVectorValues)

    def GetLaplacians(self, *args):
        r"""
        GetLaplacians(GridFunction self, int i, IntegrationRule ir, Vector laps, int vdim=1)
        GetLaplacians(GridFunction self, int i, IntegrationRule ir, Vector laps, DenseMatrix tr, int vdim=1)
        """
        return _gridfunc.GridFunction_GetLaplacians(self, *args)
    GetLaplacians = _swig_new_instance_method(_gridfunc.GridFunction_GetLaplacians)

    def GetHessians(self, *args):
        r"""
        GetHessians(GridFunction self, int i, IntegrationRule ir, DenseMatrix hess, int vdim=1)
        GetHessians(GridFunction self, int i, IntegrationRule ir, DenseMatrix hess, DenseMatrix tr, int vdim=1)
        """
        return _gridfunc.GridFunction_GetHessians(self, *args)
    GetHessians = _swig_new_instance_method(_gridfunc.GridFunction_GetHessians)

    def GetValuesFrom(self, orig_func):
        r"""GetValuesFrom(GridFunction self, GridFunction orig_func)"""
        return _gridfunc.GridFunction_GetValuesFrom(self, orig_func)
    GetValuesFrom = _swig_new_instance_method(_gridfunc.GridFunction_GetValuesFrom)

    def GetBdrValuesFrom(self, orig_func):
        r"""GetBdrValuesFrom(GridFunction self, GridFunction orig_func)"""
        return _gridfunc.GridFunction_GetBdrValuesFrom(self, orig_func)
    GetBdrValuesFrom = _swig_new_instance_method(_gridfunc.GridFunction_GetBdrValuesFrom)

    def GetVectorFieldValues(self, i, ir, vals, tr, comp=0):
        r"""GetVectorFieldValues(GridFunction self, int i, IntegrationRule ir, DenseMatrix vals, DenseMatrix tr, int comp=0)"""
        return _gridfunc.GridFunction_GetVectorFieldValues(self, i, ir, vals, tr, comp)
    GetVectorFieldValues = _swig_new_instance_method(_gridfunc.GridFunction_GetVectorFieldValues)

    def ReorderByNodes(self):
        r"""ReorderByNodes(GridFunction self)"""
        return _gridfunc.GridFunction_ReorderByNodes(self)
    ReorderByNodes = _swig_new_instance_method(_gridfunc.GridFunction_ReorderByNodes)

    def GetNodalValues(self, *args):
        '''
        GetNodalValues(i)   ->   GetNodalValues(vector, vdim)
        GetNodalValues(i, array<dobule>, vdim)
        '''
        from .vector import Vector
        if len(args) == 1:
            vec = Vector()
            _gridfunc.GridFunction_GetNodalValues(self, vec, args[0])
            vec.thisown = 0
            return vec.GetDataArray()
        else:
            return _gridfunc.GridFunction_GetNodalValues(self, *args)



    def GetVectorFieldNodalValues(self, val, comp):
        r"""GetVectorFieldNodalValues(GridFunction self, Vector val, int comp)"""
        return _gridfunc.GridFunction_GetVectorFieldNodalValues(self, val, comp)
    GetVectorFieldNodalValues = _swig_new_instance_method(_gridfunc.GridFunction_GetVectorFieldNodalValues)

    def ProjectVectorFieldOn(self, vec_field, comp=0):
        r"""ProjectVectorFieldOn(GridFunction self, GridFunction vec_field, int comp=0)"""
        return _gridfunc.GridFunction_ProjectVectorFieldOn(self, vec_field, comp)
    ProjectVectorFieldOn = _swig_new_instance_method(_gridfunc.GridFunction_ProjectVectorFieldOn)

    def GetDerivative(self, comp, der_comp, der):
        r"""GetDerivative(GridFunction self, int comp, int der_comp, GridFunction der)"""
        return _gridfunc.GridFunction_GetDerivative(self, comp, der_comp, der)
    GetDerivative = _swig_new_instance_method(_gridfunc.GridFunction_GetDerivative)

    def GetDivergence(self, tr):
        r"""GetDivergence(GridFunction self, ElementTransformation tr) -> double"""
        return _gridfunc.GridFunction_GetDivergence(self, tr)
    GetDivergence = _swig_new_instance_method(_gridfunc.GridFunction_GetDivergence)

    def GetCurl(self, tr, curl):
        r"""GetCurl(GridFunction self, ElementTransformation tr, Vector curl)"""
        return _gridfunc.GridFunction_GetCurl(self, tr, curl)
    GetCurl = _swig_new_instance_method(_gridfunc.GridFunction_GetCurl)

    def GetGradient(self, tr, grad):
        r"""GetGradient(GridFunction self, ElementTransformation tr, Vector grad)"""
        return _gridfunc.GridFunction_GetGradient(self, tr, grad)
    GetGradient = _swig_new_instance_method(_gridfunc.GridFunction_GetGradient)

    def GetGradients(self, *args):
        r"""
        GetGradients(GridFunction self, ElementTransformation tr, IntegrationRule ir, DenseMatrix grad)
        GetGradients(GridFunction self, int const elem, IntegrationRule ir, DenseMatrix grad)
        """
        return _gridfunc.GridFunction_GetGradients(self, *args)
    GetGradients = _swig_new_instance_method(_gridfunc.GridFunction_GetGradients)

    def GetVectorGradient(self, tr, grad):
        r"""GetVectorGradient(GridFunction self, ElementTransformation tr, DenseMatrix grad)"""
        return _gridfunc.GridFunction_GetVectorGradient(self, tr, grad)
    GetVectorGradient = _swig_new_instance_method(_gridfunc.GridFunction_GetVectorGradient)

    def GetElementAverages(self, avgs):
        r"""GetElementAverages(GridFunction self, GridFunction avgs)"""
        return _gridfunc.GridFunction_GetElementAverages(self, avgs)
    GetElementAverages = _swig_new_instance_method(_gridfunc.GridFunction_GetElementAverages)

    def GetElementDofValues(self, el, dof_vals):
        r"""GetElementDofValues(GridFunction self, int el, Vector dof_vals)"""
        return _gridfunc.GridFunction_GetElementDofValues(self, el, dof_vals)
    GetElementDofValues = _swig_new_instance_method(_gridfunc.GridFunction_GetElementDofValues)

    def ImposeBounds(self, *args):
        r"""
        ImposeBounds(GridFunction self, int i, Vector weights, Vector lo_, Vector hi_)
        ImposeBounds(GridFunction self, int i, Vector weights, double min_=0.0, double max_=mfem::infinity())
        """
        return _gridfunc.GridFunction_ImposeBounds(self, *args)
    ImposeBounds = _swig_new_instance_method(_gridfunc.GridFunction_ImposeBounds)

    def RestrictConforming(self):
        r"""RestrictConforming(GridFunction self)"""
        return _gridfunc.GridFunction_RestrictConforming(self)
    RestrictConforming = _swig_new_instance_method(_gridfunc.GridFunction_RestrictConforming)

    def ProjectGridFunction(self, src):
        r"""ProjectGridFunction(GridFunction self, GridFunction src)"""
        return _gridfunc.GridFunction_ProjectGridFunction(self, src)
    ProjectGridFunction = _swig_new_instance_method(_gridfunc.GridFunction_ProjectGridFunction)

    def ProjectCoefficient(self, *args):
        r"""
        ProjectCoefficient(GridFunction self, Coefficient coeff)
        ProjectCoefficient(GridFunction self, Coefficient coeff, intArray dofs, int vd=0)
        ProjectCoefficient(GridFunction self, VectorCoefficient vcoeff)
        ProjectCoefficient(GridFunction self, VectorCoefficient vcoeff, intArray dofs)
        ProjectCoefficient(GridFunction self, VectorCoefficient vcoeff, int attribute)
        ProjectCoefficient(GridFunction self, mfem::Coefficient *[] coeff)
        """
        return _gridfunc.GridFunction_ProjectCoefficient(self, *args)
    ProjectCoefficient = _swig_new_instance_method(_gridfunc.GridFunction_ProjectCoefficient)
    ARITHMETIC = _gridfunc.GridFunction_ARITHMETIC
    
    HARMONIC = _gridfunc.GridFunction_HARMONIC
    

    def ProjectDiscCoefficient(self, *args):
        r"""
        ProjectDiscCoefficient(GridFunction self, VectorCoefficient coeff)
        ProjectDiscCoefficient(GridFunction self, Coefficient coeff, mfem::GridFunction::AvgType type)
        ProjectDiscCoefficient(GridFunction self, VectorCoefficient coeff, mfem::GridFunction::AvgType type)
        """
        return _gridfunc.GridFunction_ProjectDiscCoefficient(self, *args)
    ProjectDiscCoefficient = _swig_new_instance_method(_gridfunc.GridFunction_ProjectDiscCoefficient)

    def ProjectBdrCoefficient(self, *args):
        r"""
        ProjectBdrCoefficient(GridFunction self, Coefficient coeff, intArray attr)
        ProjectBdrCoefficient(GridFunction self, VectorCoefficient vcoeff, intArray attr)
        ProjectBdrCoefficient(GridFunction self, mfem::Coefficient *[] coeff, intArray attr)
        """
        return _gridfunc.GridFunction_ProjectBdrCoefficient(self, *args)
    ProjectBdrCoefficient = _swig_new_instance_method(_gridfunc.GridFunction_ProjectBdrCoefficient)

    def ProjectBdrCoefficientNormal(self, vcoeff, bdr_attr):
        r"""ProjectBdrCoefficientNormal(GridFunction self, VectorCoefficient vcoeff, intArray bdr_attr)"""
        return _gridfunc.GridFunction_ProjectBdrCoefficientNormal(self, vcoeff, bdr_attr)
    ProjectBdrCoefficientNormal = _swig_new_instance_method(_gridfunc.GridFunction_ProjectBdrCoefficientNormal)

    def ProjectBdrCoefficientTangent(self, vcoeff, bdr_attr):
        r"""ProjectBdrCoefficientTangent(GridFunction self, VectorCoefficient vcoeff, intArray bdr_attr)"""
        return _gridfunc.GridFunction_ProjectBdrCoefficientTangent(self, vcoeff, bdr_attr)
    ProjectBdrCoefficientTangent = _swig_new_instance_method(_gridfunc.GridFunction_ProjectBdrCoefficientTangent)

    def ComputeL2Error(self, *args):
        r"""
        ComputeL2Error(GridFunction self, Coefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL2Error(GridFunction self, mfem::Coefficient *[] exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL2Error(GridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0, intArray elems=None) -> double
        """
        return _gridfunc.GridFunction_ComputeL2Error(self, *args)
    ComputeL2Error = _swig_new_instance_method(_gridfunc.GridFunction_ComputeL2Error)

    def ComputeGradError(self, exgrad, irs=0):
        r"""ComputeGradError(GridFunction self, VectorCoefficient exgrad, mfem::IntegrationRule const *[] irs=0) -> double"""
        return _gridfunc.GridFunction_ComputeGradError(self, exgrad, irs)
    ComputeGradError = _swig_new_instance_method(_gridfunc.GridFunction_ComputeGradError)

    def ComputeCurlError(self, excurl, irs=0):
        r"""ComputeCurlError(GridFunction self, VectorCoefficient excurl, mfem::IntegrationRule const *[] irs=0) -> double"""
        return _gridfunc.GridFunction_ComputeCurlError(self, excurl, irs)
    ComputeCurlError = _swig_new_instance_method(_gridfunc.GridFunction_ComputeCurlError)

    def ComputeDivError(self, exdiv, irs=0):
        r"""ComputeDivError(GridFunction self, Coefficient exdiv, mfem::IntegrationRule const *[] irs=0) -> double"""
        return _gridfunc.GridFunction_ComputeDivError(self, exdiv, irs)
    ComputeDivError = _swig_new_instance_method(_gridfunc.GridFunction_ComputeDivError)

    def ComputeDGFaceJumpError(self, *args):
        r"""
        ComputeDGFaceJumpError(GridFunction self, Coefficient exsol, Coefficient ell_coeff, JumpScaling jump_scaling, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeDGFaceJumpError(GridFunction self, Coefficient exsol, Coefficient ell_coeff, double Nu, mfem::IntegrationRule const *[] irs=0) -> double
        """
        return _gridfunc.GridFunction_ComputeDGFaceJumpError(self, *args)
    ComputeDGFaceJumpError = _swig_new_instance_method(_gridfunc.GridFunction_ComputeDGFaceJumpError)

    def ComputeH1Error(self, *args):
        r"""
        ComputeH1Error(GridFunction self, Coefficient exsol, VectorCoefficient exgrad, Coefficient ell_coef, double Nu, int norm_type) -> double
        ComputeH1Error(GridFunction self, Coefficient exsol, VectorCoefficient exgrad, mfem::IntegrationRule const *[] irs=0) -> double
        """
        return _gridfunc.GridFunction_ComputeH1Error(self, *args)
    ComputeH1Error = _swig_new_instance_method(_gridfunc.GridFunction_ComputeH1Error)

    def ComputeHDivError(self, exsol, exdiv, irs=0):
        r"""ComputeHDivError(GridFunction self, VectorCoefficient exsol, Coefficient exdiv, mfem::IntegrationRule const *[] irs=0) -> double"""
        return _gridfunc.GridFunction_ComputeHDivError(self, exsol, exdiv, irs)
    ComputeHDivError = _swig_new_instance_method(_gridfunc.GridFunction_ComputeHDivError)

    def ComputeHCurlError(self, exsol, excurl, irs=0):
        r"""ComputeHCurlError(GridFunction self, VectorCoefficient exsol, VectorCoefficient excurl, mfem::IntegrationRule const *[] irs=0) -> double"""
        return _gridfunc.GridFunction_ComputeHCurlError(self, exsol, excurl, irs)
    ComputeHCurlError = _swig_new_instance_method(_gridfunc.GridFunction_ComputeHCurlError)

    def ComputeMaxError(self, *args):
        r"""
        ComputeMaxError(GridFunction self, Coefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeMaxError(GridFunction self, mfem::Coefficient *[] exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeMaxError(GridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        """
        return _gridfunc.GridFunction_ComputeMaxError(self, *args)
    ComputeMaxError = _swig_new_instance_method(_gridfunc.GridFunction_ComputeMaxError)

    def ComputeW11Error(self, exsol, exgrad, norm_type, elems=None, irs=0):
        r"""ComputeW11Error(GridFunction self, Coefficient exsol, VectorCoefficient exgrad, int norm_type, intArray elems=None, mfem::IntegrationRule const *[] irs=0) -> double"""
        return _gridfunc.GridFunction_ComputeW11Error(self, exsol, exgrad, norm_type, elems, irs)
    ComputeW11Error = _swig_new_instance_method(_gridfunc.GridFunction_ComputeW11Error)

    def ComputeL1Error(self, *args):
        r"""
        ComputeL1Error(GridFunction self, Coefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeL1Error(GridFunction self, VectorCoefficient exsol, mfem::IntegrationRule const *[] irs=0) -> double
        """
        return _gridfunc.GridFunction_ComputeL1Error(self, *args)
    ComputeL1Error = _swig_new_instance_method(_gridfunc.GridFunction_ComputeL1Error)

    def ComputeLpError(self, *args):
        r"""
        ComputeLpError(GridFunction self, double const p, Coefficient exsol, Coefficient weight=None, mfem::IntegrationRule const *[] irs=0) -> double
        ComputeLpError(GridFunction self, double const p, VectorCoefficient exsol, Coefficient weight=None, VectorCoefficient v_weight=None, mfem::IntegrationRule const *[] irs=0) -> double
        """
        return _gridfunc.GridFunction_ComputeLpError(self, *args)
    ComputeLpError = _swig_new_instance_method(_gridfunc.GridFunction_ComputeLpError)

    def ComputeElementLpErrors(self, *args):
        r"""
        ComputeElementLpErrors(GridFunction self, double const p, Coefficient exsol, Vector error, Coefficient weight=None, mfem::IntegrationRule const *[] irs=0)
        ComputeElementLpErrors(GridFunction self, double const p, VectorCoefficient exsol, Vector error, Coefficient weight=None, VectorCoefficient v_weight=None, mfem::IntegrationRule const *[] irs=0)
        """
        return _gridfunc.GridFunction_ComputeElementLpErrors(self, *args)
    ComputeElementLpErrors = _swig_new_instance_method(_gridfunc.GridFunction_ComputeElementLpErrors)

    def ComputeElementL1Errors(self, *args):
        r"""
        ComputeElementL1Errors(GridFunction self, Coefficient exsol, Vector error, mfem::IntegrationRule const *[] irs=0)
        ComputeElementL1Errors(GridFunction self, VectorCoefficient exsol, Vector error, mfem::IntegrationRule const *[] irs=0)
        """
        return _gridfunc.GridFunction_ComputeElementL1Errors(self, *args)
    ComputeElementL1Errors = _swig_new_instance_method(_gridfunc.GridFunction_ComputeElementL1Errors)

    def ComputeElementL2Errors(self, *args):
        r"""
        ComputeElementL2Errors(GridFunction self, Coefficient exsol, Vector error, mfem::IntegrationRule const *[] irs=0)
        ComputeElementL2Errors(GridFunction self, VectorCoefficient exsol, Vector error, mfem::IntegrationRule const *[] irs=0)
        """
        return _gridfunc.GridFunction_ComputeElementL2Errors(self, *args)
    ComputeElementL2Errors = _swig_new_instance_method(_gridfunc.GridFunction_ComputeElementL2Errors)

    def ComputeElementMaxErrors(self, *args):
        r"""
        ComputeElementMaxErrors(GridFunction self, Coefficient exsol, Vector error, mfem::IntegrationRule const *[] irs=0)
        ComputeElementMaxErrors(GridFunction self, VectorCoefficient exsol, Vector error, mfem::IntegrationRule const *[] irs=0)
        """
        return _gridfunc.GridFunction_ComputeElementMaxErrors(self, *args)
    ComputeElementMaxErrors = _swig_new_instance_method(_gridfunc.GridFunction_ComputeElementMaxErrors)

    def ComputeFlux(self, blfi, flux, wcoef=True, subdomain=-1):
        r"""ComputeFlux(GridFunction self, BilinearFormIntegrator blfi, GridFunction flux, bool wcoef=True, int subdomain=-1)"""
        return _gridfunc.GridFunction_ComputeFlux(self, blfi, flux, wcoef, subdomain)
    ComputeFlux = _swig_new_instance_method(_gridfunc.GridFunction_ComputeFlux)

    def Update(self):
        r"""Update(GridFunction self)"""
        return _gridfunc.GridFunction_Update(self)
    Update = _swig_new_instance_method(_gridfunc.GridFunction_Update)

    def FESpace(self, *args):
        r"""
        FESpace(GridFunction self) -> FiniteElementSpace
        FESpace(GridFunction self) -> FiniteElementSpace
        """
        return _gridfunc.GridFunction_FESpace(self, *args)
    FESpace = _swig_new_instance_method(_gridfunc.GridFunction_FESpace)

    def SetSpace(self, f):
        r"""SetSpace(GridFunction self, FiniteElementSpace f)"""
        return _gridfunc.GridFunction_SetSpace(self, f)
    SetSpace = _swig_new_instance_method(_gridfunc.GridFunction_SetSpace)

    def MakeRef(self, *args):
        r"""
        MakeRef(GridFunction self, Vector base, int offset, int size)
        MakeRef(GridFunction self, Vector base, int offset)
        MakeRef(GridFunction self, FiniteElementSpace f, double * v)
        MakeRef(GridFunction self, FiniteElementSpace f, Vector v, int v_offset)
        """
        return _gridfunc.GridFunction_MakeRef(self, *args)
    MakeRef = _swig_new_instance_method(_gridfunc.GridFunction_MakeRef)

    def MakeTRef(self, *args):
        r"""
        MakeTRef(GridFunction self, FiniteElementSpace f, double * tv)
        MakeTRef(GridFunction self, FiniteElementSpace f, Vector tv, int tv_offset)
        """
        return _gridfunc.GridFunction_MakeTRef(self, *args)
    MakeTRef = _swig_new_instance_method(_gridfunc.GridFunction_MakeTRef)

    def SaveVTK(self, out, field_name, ref):
        r"""SaveVTK(GridFunction self, std::ostream & out, std::string const & field_name, int ref)"""
        return _gridfunc.GridFunction_SaveVTK(self, out, field_name, ref)
    SaveVTK = _swig_new_instance_method(_gridfunc.GridFunction_SaveVTK)

    def SaveSTL(self, out, TimesToRefine=1):
        r"""SaveSTL(GridFunction self, std::ostream & out, int TimesToRefine=1)"""
        return _gridfunc.GridFunction_SaveSTL(self, out, TimesToRefine)
    SaveSTL = _swig_new_instance_method(_gridfunc.GridFunction_SaveSTL)
    __swig_destroy__ = _gridfunc.delete_GridFunction

    def __init__(self, *args):
        r"""
        __init__(GridFunction self) -> GridFunction
        __init__(GridFunction self, GridFunction orig) -> GridFunction
        __init__(GridFunction self, FiniteElementSpace f) -> GridFunction
        __init__(GridFunction self, FiniteElementSpace f, double * data) -> GridFunction
        __init__(GridFunction self, FiniteElementSpace f, Vector base, int base_offset=0) -> GridFunction
        __init__(GridFunction self, Mesh m, std::istream & input) -> GridFunction
        __init__(GridFunction self, Mesh m, mfem::GridFunction *[] gf_array, int num_pieces) -> GridFunction
        __init__(GridFunction self, FiniteElementSpace fes, Vector v, int offset) -> GridFunction
        """
        _gridfunc.GridFunction_swiginit(self, _gridfunc.new_GridFunction(*args))

    def Assign(self, *args):
        r"""
        Assign(GridFunction self, double const v)
        Assign(GridFunction self, Vector v)
        Assign(GridFunction self, GridFunction v)
        Assign(GridFunction self, PyObject * param)
        """

        from numpy import ndarray, ascontiguousarray, array
        keep_link = False
        if len(args) == 1:
            if isinstance(args[0], ndarray):
                if args[0].dtype != 'float64':
                    raise ValueError('Must be float64 array ' + str(args[0].dtype) +
        		   ' is given')
                elif args[0].ndim != 1:
                    raise ValueError('Ndim must be one') 
                elif args[0].shape[0] != self.Size():
                    raise ValueError('Length does not match')
                else:
                    args = (ascontiguousarray(args[0]),)
            elif isinstance(args[0], tuple):
                args = (array(args[0], dtype = float),)      
            elif isinstance(args[0], list):	      
                args = (array(args[0], dtype = float),)      
            else:
                pass


        val = _gridfunc.GridFunction_Assign(self, *args)

        return self


        return val


    def SaveToFile(self, gf_file, precision):
        r"""SaveToFile(GridFunction self, char const * gf_file, int const precision)"""
        return _gridfunc.GridFunction_SaveToFile(self, gf_file, precision)
    SaveToFile = _swig_new_instance_method(_gridfunc.GridFunction_SaveToFile)

    def WriteToStream(self, StringIO):
        r"""WriteToStream(GridFunction self, PyObject * StringIO) -> PyObject *"""
        return _gridfunc.GridFunction_WriteToStream(self, StringIO)
    WriteToStream = _swig_new_instance_method(_gridfunc.GridFunction_WriteToStream)

    def iadd(self, c):
        r"""iadd(GridFunction self, GridFunction c) -> GridFunction"""
        return _gridfunc.GridFunction_iadd(self, c)
    iadd = _swig_new_instance_method(_gridfunc.GridFunction_iadd)

    def isub(self, *args):
        r"""
        isub(GridFunction self, GridFunction c) -> GridFunction
        isub(GridFunction self, double c) -> GridFunction
        """
        return _gridfunc.GridFunction_isub(self, *args)
    isub = _swig_new_instance_method(_gridfunc.GridFunction_isub)

    def imul(self, c):
        r"""imul(GridFunction self, double c) -> GridFunction"""
        return _gridfunc.GridFunction_imul(self, c)
    imul = _swig_new_instance_method(_gridfunc.GridFunction_imul)

    def idiv(self, c):
        r"""idiv(GridFunction self, double c) -> GridFunction"""
        return _gridfunc.GridFunction_idiv(self, c)
    idiv = _swig_new_instance_method(_gridfunc.GridFunction_idiv)

    def Save(self, *args):
        r"""
        Save(GridFunction self, std::ostream & out)
        Save(GridFunction self, char const * fname, int precision=16)
        Save(GridFunction self, char const * file, int precision=16)
        """
        return _gridfunc.GridFunction_Save(self, *args)
    Save = _swig_new_instance_method(_gridfunc.GridFunction_Save)

    def SaveGZ(self, file, precision=16):
        r"""SaveGZ(GridFunction self, char const * file, int precision=16)"""
        return _gridfunc.GridFunction_SaveGZ(self, file, precision)
    SaveGZ = _swig_new_instance_method(_gridfunc.GridFunction_SaveGZ)

# Register GridFunction in _gridfunc:
_gridfunc.GridFunction_swigregister(GridFunction)

class JumpScaling(object):
    r"""Proxy of C++ mfem::JumpScaling class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CONSTANT = _gridfunc.JumpScaling_CONSTANT
    
    ONE_OVER_H = _gridfunc.JumpScaling_ONE_OVER_H
    
    P_SQUARED_OVER_H = _gridfunc.JumpScaling_P_SQUARED_OVER_H
    

    def __init__(self, *args, **kwargs):
        r"""__init__(JumpScaling self, double nu_=1.0, mfem::JumpScaling::JumpScalingType type_=CONSTANT) -> JumpScaling"""
        _gridfunc.JumpScaling_swiginit(self, _gridfunc.new_JumpScaling(*args, **kwargs))

    def Eval(self, h, p):
        r"""Eval(JumpScaling self, double h, int p) -> double"""
        return _gridfunc.JumpScaling_Eval(self, h, p)
    Eval = _swig_new_instance_method(_gridfunc.JumpScaling_Eval)
    __swig_destroy__ = _gridfunc.delete_JumpScaling

# Register JumpScaling in _gridfunc:
_gridfunc.JumpScaling_swigregister(JumpScaling)

class QuadratureFunction(mfem._ser.vector.Vector):
    r"""Proxy of C++ mfem::QuadratureFunction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(QuadratureFunction self) -> QuadratureFunction
        __init__(QuadratureFunction self, QuadratureFunction orig) -> QuadratureFunction
        __init__(QuadratureFunction self, QuadratureSpace qspace_, int vdim_=1) -> QuadratureFunction
        __init__(QuadratureFunction self, QuadratureSpace qspace_, double * qf_data, int vdim_=1) -> QuadratureFunction
        __init__(QuadratureFunction self, Mesh mesh, std::istream & _in) -> QuadratureFunction
        """
        _gridfunc.QuadratureFunction_swiginit(self, _gridfunc.new_QuadratureFunction(*args))
    __swig_destroy__ = _gridfunc.delete_QuadratureFunction

    def GetSpace(self):
        r"""GetSpace(QuadratureFunction self) -> QuadratureSpace"""
        return _gridfunc.QuadratureFunction_GetSpace(self)
    GetSpace = _swig_new_instance_method(_gridfunc.QuadratureFunction_GetSpace)

    def SetSpace(self, *args):
        r"""
        SetSpace(QuadratureFunction self, QuadratureSpace qspace_, int vdim_=-1)
        SetSpace(QuadratureFunction self, QuadratureSpace qspace_, double * qf_data, int vdim_=-1)
        """
        return _gridfunc.QuadratureFunction_SetSpace(self, *args)
    SetSpace = _swig_new_instance_method(_gridfunc.QuadratureFunction_SetSpace)

    def GetVDim(self):
        r"""GetVDim(QuadratureFunction self) -> int"""
        return _gridfunc.QuadratureFunction_GetVDim(self)
    GetVDim = _swig_new_instance_method(_gridfunc.QuadratureFunction_GetVDim)

    def SetVDim(self, vdim_):
        r"""SetVDim(QuadratureFunction self, int vdim_)"""
        return _gridfunc.QuadratureFunction_SetVDim(self, vdim_)
    SetVDim = _swig_new_instance_method(_gridfunc.QuadratureFunction_SetVDim)

    def OwnsSpace(self):
        r"""OwnsSpace(QuadratureFunction self) -> bool"""
        return _gridfunc.QuadratureFunction_OwnsSpace(self)
    OwnsSpace = _swig_new_instance_method(_gridfunc.QuadratureFunction_OwnsSpace)

    def SetOwnsSpace(self, own):
        r"""SetOwnsSpace(QuadratureFunction self, bool own)"""
        return _gridfunc.QuadratureFunction_SetOwnsSpace(self, own)
    SetOwnsSpace = _swig_new_instance_method(_gridfunc.QuadratureFunction_SetOwnsSpace)

    def GetElementIntRule(self, idx):
        r"""GetElementIntRule(QuadratureFunction self, int idx) -> IntegrationRule"""
        return _gridfunc.QuadratureFunction_GetElementIntRule(self, idx)
    GetElementIntRule = _swig_new_instance_method(_gridfunc.QuadratureFunction_GetElementIntRule)

    def GetElementValues(self, *args):
        r"""
        GetElementValues(QuadratureFunction self, int idx, Vector values)
        GetElementValues(QuadratureFunction self, int idx, Vector values)
        GetElementValues(QuadratureFunction self, int idx, int const ip_num, Vector values)
        GetElementValues(QuadratureFunction self, int idx, int const ip_num, Vector values)
        GetElementValues(QuadratureFunction self, int idx, DenseMatrix values)
        GetElementValues(QuadratureFunction self, int idx, DenseMatrix values)
        """
        return _gridfunc.QuadratureFunction_GetElementValues(self, *args)
    GetElementValues = _swig_new_instance_method(_gridfunc.QuadratureFunction_GetElementValues)

    def Save(self, *args):
        r"""
        Save(QuadratureFunction self, std::ostream & out)
        Save(QuadratureFunction self, char const * file, int precision=16)
        """
        return _gridfunc.QuadratureFunction_Save(self, *args)
    Save = _swig_new_instance_method(_gridfunc.QuadratureFunction_Save)

    def SaveGZ(self, file, precision=16):
        r"""SaveGZ(QuadratureFunction self, char const * file, int precision=16)"""
        return _gridfunc.QuadratureFunction_SaveGZ(self, file, precision)
    SaveGZ = _swig_new_instance_method(_gridfunc.QuadratureFunction_SaveGZ)

# Register QuadratureFunction in _gridfunc:
_gridfunc.QuadratureFunction_swigregister(QuadratureFunction)


def __lshift__(*args):
    r"""
    __lshift__(std::ostream & os, SparseMatrix mat) -> std::ostream
    __lshift__(std::ostream & out, Mesh mesh) -> std::ostream
    __lshift__(std::ostream & out, GridFunction sol) -> std::ostream
    __lshift__(std::ostream & out, QuadratureFunction qf) -> std::ostream &
    """
    return _gridfunc.__lshift__(*args)
__lshift__ = _gridfunc.__lshift__

def ZZErrorEstimator(blfi, u, flux, error_estimates, aniso_flags=None, with_subdomains=1, with_coeff=False):
    r"""ZZErrorEstimator(BilinearFormIntegrator blfi, GridFunction u, GridFunction flux, Vector error_estimates, intArray aniso_flags=None, int with_subdomains=1, bool with_coeff=False) -> double"""
    return _gridfunc.ZZErrorEstimator(blfi, u, flux, error_estimates, aniso_flags, with_subdomains, with_coeff)
ZZErrorEstimator = _gridfunc.ZZErrorEstimator

def ComputeElementLpDistance(p, i, gf1, gf2):
    r"""ComputeElementLpDistance(double p, int i, GridFunction gf1, GridFunction gf2) -> double"""
    return _gridfunc.ComputeElementLpDistance(p, i, gf1, gf2)
ComputeElementLpDistance = _gridfunc.ComputeElementLpDistance
class ExtrudeCoefficient(mfem._ser.coefficient.Coefficient):
    r"""Proxy of C++ mfem::ExtrudeCoefficient class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, m, s, n_):
        r"""__init__(ExtrudeCoefficient self, Mesh m, Coefficient s, int n_) -> ExtrudeCoefficient"""
        _gridfunc.ExtrudeCoefficient_swiginit(self, _gridfunc.new_ExtrudeCoefficient(m, s, n_))

    def Eval(self, T, ip):
        r"""Eval(ExtrudeCoefficient self, ElementTransformation T, IntegrationPoint ip) -> double"""
        return _gridfunc.ExtrudeCoefficient_Eval(self, T, ip)
    Eval = _swig_new_instance_method(_gridfunc.ExtrudeCoefficient_Eval)
    __swig_destroy__ = _gridfunc.delete_ExtrudeCoefficient

# Register ExtrudeCoefficient in _gridfunc:
_gridfunc.ExtrudeCoefficient_swigregister(ExtrudeCoefficient)


def Extrude1DGridFunction(mesh, mesh2d, sol, ny):
    r"""Extrude1DGridFunction(Mesh mesh, Mesh mesh2d, GridFunction sol, int const ny) -> GridFunction"""
    return _gridfunc.Extrude1DGridFunction(mesh, mesh2d, sol, ny)
Extrude1DGridFunction = _gridfunc.Extrude1DGridFunction

def __iadd__(self, v):
    ret = _gridfunc.GridFunction_iadd(self, v)
    ret.thisown = 0
    return self
def __isub__(self, v):
    ret = _gridfunc.GridFunction_isub(self, v)
    ret.thisown = 0
    return self
def __idiv__(self, v):
    ret = _gridfunc.GridFunction_idiv(self, v)
    ret.thisown = 0
    return self
def __imul__(self, v):
    ret = _gridfunc.GridFunction_imul(self, v)
    ret.thisown = 0
    return self

GridFunction.__iadd__  = __iadd__
GridFunction.__idiv__  = __idiv__
GridFunction.__isub__  = __isub__
GridFunction.__imul__  = __imul__      



