# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_hash')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_hash')
    _hash = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_hash', [dirname(__file__)])
        except ImportError:
            import _hash
            return _hash
        try:
            _mod = imp.load_module('_hash', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _hash = swig_import_helper()
    del swig_import_helper
else:
    import _hash
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

import mfem._par.array
import mfem._par.ostream_typemap
import mfem._par.mem_manager
import mfem._par.vector
class Hashed2(_object):
    """Proxy of C++ mfem::Hashed2 class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Hashed2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Hashed2, name)
    __repr__ = _swig_repr
    __swig_setmethods__["p1"] = _hash.Hashed2_p1_set
    __swig_getmethods__["p1"] = _hash.Hashed2_p1_get
    if _newclass:
        p1 = _swig_property(_hash.Hashed2_p1_get, _hash.Hashed2_p1_set)
    __swig_setmethods__["p2"] = _hash.Hashed2_p2_set
    __swig_getmethods__["p2"] = _hash.Hashed2_p2_get
    if _newclass:
        p2 = _swig_property(_hash.Hashed2_p2_get, _hash.Hashed2_p2_set)
    __swig_setmethods__["next"] = _hash.Hashed2_next_set
    __swig_getmethods__["next"] = _hash.Hashed2_next_get
    if _newclass:
        next = _swig_property(_hash.Hashed2_next_get, _hash.Hashed2_next_set)

    def __init__(self):
        """__init__(mfem::Hashed2 self) -> Hashed2"""
        this = _hash.new_Hashed2()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _hash.delete_Hashed2
    __del__ = lambda self: None
Hashed2_swigregister = _hash.Hashed2_swigregister
Hashed2_swigregister(Hashed2)

class Hashed4(_object):
    """Proxy of C++ mfem::Hashed4 class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Hashed4, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Hashed4, name)
    __repr__ = _swig_repr
    __swig_setmethods__["p1"] = _hash.Hashed4_p1_set
    __swig_getmethods__["p1"] = _hash.Hashed4_p1_get
    if _newclass:
        p1 = _swig_property(_hash.Hashed4_p1_get, _hash.Hashed4_p1_set)
    __swig_setmethods__["p2"] = _hash.Hashed4_p2_set
    __swig_getmethods__["p2"] = _hash.Hashed4_p2_get
    if _newclass:
        p2 = _swig_property(_hash.Hashed4_p2_get, _hash.Hashed4_p2_set)
    __swig_setmethods__["p3"] = _hash.Hashed4_p3_set
    __swig_getmethods__["p3"] = _hash.Hashed4_p3_get
    if _newclass:
        p3 = _swig_property(_hash.Hashed4_p3_get, _hash.Hashed4_p3_set)
    __swig_setmethods__["next"] = _hash.Hashed4_next_set
    __swig_getmethods__["next"] = _hash.Hashed4_next_get
    if _newclass:
        next = _swig_property(_hash.Hashed4_next_get, _hash.Hashed4_next_set)

    def __init__(self):
        """__init__(mfem::Hashed4 self) -> Hashed4"""
        this = _hash.new_Hashed4()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _hash.delete_Hashed4
    __del__ = lambda self: None
Hashed4_swigregister = _hash.Hashed4_swigregister
Hashed4_swigregister(Hashed4)


def sort3(a, b, c):
    """sort3(int & a, int & b, int & c)"""
    return _hash.sort3(a, b, c)

def sort4(a, b, c, d):
    """sort4(int & a, int & b, int & c, int & d)"""
    return _hash.sort4(a, b, c, d)
# This file is compatible with both classic and new-style classes.


