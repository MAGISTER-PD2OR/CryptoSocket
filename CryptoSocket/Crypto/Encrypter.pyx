#!/usr/bin/env python
# distutils: language = c++
# distutils: sources = Encrypter.cpp
# cython: language_level=3

cimport cython
from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.memory cimport unique_ptr
from cython.operator cimport dereference as deref

cdef extern from "Encrypter.h":
  cppclass Encrypter:
    Encrypter() except +
    Encrypter(unsigned long n, unsigned long e) except +

    # Attributes
    unsigned long n, e

    # Methods
    vector[unsigned long] encrypt(string enc)

cdef class PyEncrypter:
  cdef unique_ptr[Encrypter] thisptr

  def __cinit__(self, n, e):
    self.thisptr.reset(new Encrypter(n, e))

  def __init__(self, n, e):
    self.n = n
    self.e = e

  def encrypt(self, enc):
    encoded = deref(self.thisptr).encrypt(enc)
    return encoded

  def __repr__(self):
    return '<PyEncrypter (n: ' + str(self.n) + ', e: ' + str(self.e) + ')>'
