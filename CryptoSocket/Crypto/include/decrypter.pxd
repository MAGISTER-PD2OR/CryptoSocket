# distutils: language = c++
# cython: language_level=2

from libcpp.vector cimport vector
from libcpp.string cimport string

cdef extern from "Decrypter.h":

  cppclass Decrypter:

    Decrypter () except +
    Decrypter (unsigned long n, unsigned long d) except +

    # Attributes
    unsigned long n
    unsigned long d

    # Methods
    string decrypt (vector [unsigned long] enc)
