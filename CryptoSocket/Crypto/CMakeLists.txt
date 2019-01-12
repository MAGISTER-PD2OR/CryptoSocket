# If the pyx file is a C++ file, we should specify that here.

set_source_files_properties( ${PYC_DIR}/Encrypter.pyx  PROPERTIES CYTHON_IS_CXX TRUE )
set_source_files_properties( ${PYC_DIR}/Decrypter.pyx  PROPERTIES CYTHON_IS_CXX TRUE )
set_source_files_properties( ${PYC_DIR}/RSA.pyx        PROPERTIES CYTHON_IS_CXX TRUE )

# Multi-file cython modules do not appear to be working at the moment.
cython_add_module( Encrypter Encrypter.pyx ${INC_DIR}/Encrypter.h  ${SRC_DIR}/Encrypter.cpp)
cython_add_module( Decrypter Decrypter.pyx ${INC_DIR}/Decrypter.h  ${SRC_DIR}/Decrypter.cpp)
cython_add_module( rsa       RSA.pyx       ${INC_DIR}/RSA.h        ${SRC_DIR}/RSA.cpp)
