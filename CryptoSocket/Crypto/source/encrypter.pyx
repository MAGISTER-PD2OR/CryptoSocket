# distutils: language = c++
# cython: language_level=2

from cython.operator cimport dereference as deref
from libcpp.memory cimport unique_ptr

from encrypter cimport Encrypter

cdef class _encrypter:

  cdef unique_ptr[Encrypter] thisptr

  cdef public:
    long int n
    long int e

  def __init__ (self, n, e):
    self.thisptr.reset(new Encrypter(n, e))

    self.n, self.e = n, e

  def encrypt (self, dec):

    dec = dec.encode('utf-8')

    encrypted = deref(self.thisptr).encrypt(dec)

    return encrypted

  def __repr__ (self):
    return '<Encrypter (n: {}, e {})>'.format(self.n, self.e)

