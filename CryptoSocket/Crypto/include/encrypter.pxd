# distutils: language = c++
# cython: language_level=2

from libcpp.vector cimport vector
from libcpp.string cimport string

cdef extern from "Encrypter.h":

  cppclass Encrypter:

    Encrypter () except +
    Encrypter (unsigned long n, unsigned long e) except +

    # Attributes
    unsigned long n
    unsigned long e

    # Methods
    vector[unsigned long] encrypt(string enc)
