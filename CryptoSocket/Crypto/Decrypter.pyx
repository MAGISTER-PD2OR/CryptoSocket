#!/usr/bin/env python

cimport cython
from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.memory cimport unique_ptr
from cython.operator cimport dereference as deref

cdef extern from "Decrypter.h":
  cppclass Decrypter:
    Decrypter() except +
    Decrypter(unsigned long n, unsigned long d) except +

    # Attributes
    unsigned long n, d

    # Methods
    string decrypt(vector[unsigned long] enc)

cdef class PyDecrypter:
  cdef unique_ptr[Decrypter] thisptr

  def __cinit__(self, n, d):
    self.thisptr.reset(new Decrypter(n, d))

  def __init__(self, n, d):
    self.n = n
    self.d = d

  def encrypt(self, enc):
    decoded = deref(self.thisptr).decrypt(enc)
    return decoded

  def __repr__(self):
    return '<PyDecrypter (n: ' + str(self.n) + ', d: ' + str(self.d) + ')>'
