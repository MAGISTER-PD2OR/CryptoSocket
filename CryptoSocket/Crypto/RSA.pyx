#!/usr/bin/env python

cimport cython
from libcpp.memory cimport unique_ptr
from cython.operator cimport dereference as deref

cdef extern from "RSA.h":
  cppclass RSA:
    RSA() except +
    RSA(unsigned long p, unsigned long q) except +

    # Attributes
    unsigned long n, e, d, phi

    # Methods

cdef class PyRSA:
  cdef unique_ptr[RSA] thisptr

  def __cinit__(self, p, q):
    self.thisptr.reset(new RSA(p, q))

  def __init__(self, p, q):
    self.p = p
    self.q = q

  def get_public_key(self):
    return (self.n, self.e)

  def get_private_key(self):
    return (self.n, self.d)

  def __repr__(self):
    return '<PyRSA (p: ' + str(self.p) + ', q: ' + str(self.q) + ')>'
