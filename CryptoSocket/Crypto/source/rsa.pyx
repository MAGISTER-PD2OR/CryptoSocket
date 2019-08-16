# distutils: language = c++
# cython: language_level=2

from cython.operator cimport dereference as deref
from libcpp.memory cimport unique_ptr

from rsa cimport RSA

cdef class _rsa:

  cdef unique_ptr[RSA] thisptr

  cdef public:
    long int p
    long int q

  def __init__ (self, p, q):
    self.thisptr.reset(new RSA(p, q))

    self.p, self.q = p, q

  @property
  def public_key(self):
    return (deref(self.thisptr).n, deref(self.thisptr).e)

  @property
  def private_key(self):
    return (deref(self.thisptr).n, deref(self.thisptr).d)

  def __repr__(self):
    return '<RSA (p: {}, q: {})>'.format(self.p, self.q)
