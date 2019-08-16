# If the pyx file is a C++ file, we should specify that here.

set(PYC_SRC_DIR    ${PYC_DIR}/Crypto/source       CACHE PATH "Path where find pyx files" )
set(PYC_INC_DIR    ${PYC_DIR}/Crypto/include      CACHE PATH "Path where find pxd files" )

set_source_files_properties( ${PYC_SRC_DIR}/encrypter.pyx  PROPERTIES CYTHON_IS_CXX TRUE )
set_source_files_properties( ${PYC_SRC_DIR}/decrypter.pyx  PROPERTIES CYTHON_IS_CXX TRUE )
set_source_files_properties( ${PYC_SRC_DIR}/rsa.pyx        PROPERTIES CYTHON_IS_CXX TRUE )

include_directories(${PYC_INC_DIR})

# Multi-file cython modules do not appear to be working at the moment.
cython_add_module( Encrypter encrypter.pyx ${INC_DIR}/Encrypter.h  ${SRC_DIR}/Encrypter.cpp)
cython_add_module( Decrypter decrypter.pyx ${INC_DIR}/Decrypter.h  ${SRC_DIR}/Decrypter.cpp)
cython_add_module( rsa       rsa.pyx       ${INC_DIR}/RSA.h        ${SRC_DIR}/RSA.cpp)
