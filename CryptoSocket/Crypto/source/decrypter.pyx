# distutils: language = c++
# cython: language_level=2

from cython.operator cimport dereference as deref
from libcpp.memory cimport unique_ptr
from libcpp.vector cimport vector

from decrypter cimport Decrypter

cdef class _decrypter:

  cdef unique_ptr[Decrypter] thisptr

  cdef public:
    long int n
    long int d

  def __init__ (self, n, d):
    self.thisptr.reset(new Decrypter(n, d))

    self.n, self.d = n, d

  def decrypt (self, enc):
    cdef vector[unsigned long] cpp_enc = enc
    decoded = deref(self.thisptr).decrypt(cpp_enc)
    return decoded.decode('utf-8')

  def __repr__ (self):
    return '<Decrypter (n: {}, d {})>'.format(self.n, self.d)

