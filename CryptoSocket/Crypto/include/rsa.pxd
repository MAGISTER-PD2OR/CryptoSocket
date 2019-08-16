# distutils: language = c++
# cython: language_level=2

cdef extern from "RSA.h":

  cppclass RSA:

    RSA () except +
    RSA (unsigned long p, unsigned long q) except +

    # Attributes
    unsigned long n
    unsigned long e
    unsigned long d
    unsigned long phi

    # Methods
    void compute_public_key (const unsigned int & phi)
    void compute_private_key (const unsigned int & phi, const unsigned int & e)
