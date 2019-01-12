cmake_minimum_required (VERSION 3.8)
project (CryptoSocket LANGUAGES CXX VERSION 1.0.0 DESCRIPTION "TCP/IP Client Server with RSA cryptography")
set (CMAKE_CXX_STANDARD 11)
set (CMAKE_CXX_STANDARD_REQUIRED ON)

# Scorer version
set (MAJOR    1)
set (MINOR    0)
set (REVISION 0)
add_definitions (-DMAJOR=${MAJOR} -DMINOR=${MINOR} -DREVISION=${REVISION})

#################################################################
#                         SETTING VARIABLES                     #
#################################################################

set (CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake/Modules/" ${CMAKE_MODULE_PATH})

if ( NOT APPLE )
  set (CMAKE_SKIP_BUILD_RPATH             FALSE )
  set (CMAKE_BUILD_WITH_INSTALL_RPATH     FALSE )
  set (CMAKE_INSTALL_RPATH_USE_LINK_PATH  TRUE  )
endif()

if ( CMAKE_COMPILER_IS_GNUCC )
  add_compile_options (-Wall -Wextra -Wno-unused-result)
  string (REGEX REPLACE "-O3" "-Ofast" CMAKE_C_FLAGS_RELEASE ${CMAKE_C_FLAGS_RELEASE})
endif()
if ( MSVC )
  add_compile_options (/wd4028)
  add_compile_options (/wd4244)
  add_compile_options (/wd4267)
  add_compile_options (/wd4305)
  add_compile_options (/wd4477)
  add_compile_options (/wd4996)
  set (CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /NODEFAULTLIB:MSVCRTD")
  #set (CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /NODEFAULTLIB:MSVCRT")
  set (CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()

#################################################################
#                         SETTING DIRECTORIES                   #
#################################################################

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)

set(SRC_DIR    ${CMAKE_SOURCE_DIR}/cpp/src)
set(INC_DIR    ${CMAKE_SOURCE_DIR}/cpp/include)
set(EXAMPLE    ${CMAKE_SOURCE_DIR}/cpp/example)
set(OUT_DIR    ${CMAKE_SOURCE_DIR}/bin)
set(PYC_DIR    ${CMAKE_SOURCE_DIR}/CryptoSocket/Crypto) # cython directory


file(GLOB SRC    "${SRC_DIR}/*.cpp")
file(GLOB HEADER "${INC_DIR}/*.h"  )
file(GLOB EXE    "${EXAMPLE}/*.cpp")

include_directories(${INC_DIR})
include_directories(${PYC_DIR})

# Make the scripts available in the 'cmake' directory available for the
# 'include()' command, 'find_package()' command.
set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/cmake)

# Include the CMake script UseCython.cmake.  This defines add_cython_module().
# Instruction for use can be found at the top of cmake/UseCython.cmake.
include( UseCython )

# With CMake, a clean separation can be made between the source tree and the
# build tree.  When all source is compiled, as with pure C/C++, the source is
# no-longer needed in the build tree.  However, with pure *.py source, the
# source is processed directly.  To handle this, we reproduce the availability
# of the source files in the build tree.

#################################################################
#                         MAIN RULES                            #
#################################################################

add_subdirectory(${PYC_DIR})

add_executable(keygen    ${EXAMPLE}/generate_key.cpp  ${SRC_DIR}/RSA.cpp)
add_executable(encrypter ${EXAMPLE}/encrypt.cpp       ${SRC_DIR}/Encrypter.cpp)
add_executable(decrypter ${EXAMPLE}/decrypt.cpp       ${SRC_DIR}/Decrypter.cpp)

#################################################################
#                          INSTALLERS                           #
#################################################################

install(TARGETS keygen       DESTINATION ${CMAKE_SOURCE_DIR}/${OUT_DIR})
install(TARGETS encrypter    DESTINATION ${CMAKE_SOURCE_DIR}/${OUT_DIR})
install(TARGETS decrypter    DESTINATION ${CMAKE_SOURCE_DIR}/${OUT_DIR})
