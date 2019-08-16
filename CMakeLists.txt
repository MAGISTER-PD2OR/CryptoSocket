cmake_minimum_required (VERSION 3.8)

# CryptoSocket Version
# Scorer version
set (CRYPTO_MAJOR    1)
set (CRYPTO_MINOR    0)
set (CRYPTO_REVISION 0)
set (CRYPTO_VERSION ${CRYPTO_MAJOR}.${CRYPTO_MINOR}.${CRYPTO_REVISION})

project (CryptoSocket LANGUAGES CXX VERSION ${CRYPTO_VERSION} DESCRIPTION "TCP/IP Client Server with RSA cryptography")
set (CMAKE_CXX_STANDARD 11)
set (CMAKE_CXX_STANDARD_REQUIRED ON)

add_definitions (-DMAJOR=${CRYPTO_MAJOR} -DMINOR=${CRYPTO_MINOR} -DREVISION=${CRYPTO_REVISION})

#################################################################
#                         SETTING VARIABLES                     #
#################################################################

set (CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake/Modules/" ${CMAKE_MODULE_PATH})

if ( NOT APPLE )
  set (CMAKE_SKIP_BUILD_RPATH             FALSE )
  set (CMAKE_BUILD_WITH_INSTALL_RPATH     FALSE )
  set (CMAKE_INSTALL_RPATH_USE_LINK_PATH  TRUE  )
endif()

# make sure that the default is a RELEASE
set (default_build_type "Release")
if (NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  message (STATUS "Setting build type to '${default_build_type}' as none was specified.")
  set (CMAKE_BUILD_TYPE "${default_build_type}" CACHE STRING "Choose the type of build." FORCE)
  # Set the possible values of build type for cmake-gui
  set_property (CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif ()

if ( CMAKE_COMPILER_IS_GNUCXX )
  add_compile_options (-Wall -Wextra -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -Wno-narrowing -Wpedantic)
  if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    string (REGEX REPLACE "-O[0123]" "-Og" CMAKE_CXX_FLAGS_DEBUG ${CMAKE_CXX_FLAGS_DEBUG})
    set (CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG" )
    set (CMAKE_CXX_FLAGS_RELEASE "")
  elseif (CMAKE_BUILD_TYPE STREQUAL "Release")
    string (REGEX REPLACE "-O3" "-Ofast" CMAKE_CXX_FLAGS_RELEASE ${CMAKE_CXX_FLAGS_RELEASE})
    set (CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -DNDEBUG" )
    set (CMAKE_CXX_FLAGS_DEBUG "")
  endif ()
  list (APPEND linked_libs stdc++fs)
endif ()

if ("${CMAKE_CXX_COMPILER_ID}" MATCHES "Clang")
  add_compile_options (-Wno-deprecated -Wno-writable-strings -stdlib=libstdc++ -std=c++1z)
  if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    string (REGEX REPLACE "-O0" "-Og" CMAKE_CXX_FLAGS_DEBUG ${CMAKE_CXX_FLAGS_DEBUG})
    set (CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG" )
  elseif (CMAKE_BUILD_TYPE STREQUAL "Release")
    string (REGEX REPLACE "-O3" "-Ofast" CMAKE_CXX_FLAGS_RELEASE ${CMAKE_CXX_FLAGS_RELEASE})
    set (CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -DNDEBUG" )
  endif ()
  list (APPEND linked_libs stdc++fs)
endif ()

if (MSVC)
  set (CMAKE_CXX_FLAGS "/wd4013 /wd4018 /wd4028 /wd4047 /wd4068 /wd4090 /wd4101 /wd4113 /wd4133 /wd4190 /wd4244 /wd4267 /wd4305 /wd4477 /wd4996 /wd4819 /fp:fast ${CMAKE_CXX_FLAGS}")
  string (REGEX REPLACE "/O2" "/Ox" CMAKE_CXX_FLAGS_RELEASE ${CMAKE_CXX_FLAGS_RELEASE})
  add_definitions (-D_CRT_RAND_S)
  add_definitions (-DNOMINMAX)
  add_definitions (-D_USE_MATH_DEFINES)
  add_definitions (-D_CRT_SECURE_NO_DEPRECATE -D_SCL_SECURE_NO_WARNINGS)
  set (CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif ()


include (CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG ("-march=native" COMPILER_SUPPORTS_MARCH_NATIVE)
if (COMPILER_SUPPORTS_MARCH_NATIVE AND NOT MSVC)
  set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS_RELEASE} -march=native -mtune=native")
endif ()

#################################################################
#                         SETTING DIRECTORIES                   #
#################################################################

set (SRC_DIR      ${CMAKE_SOURCE_DIR}/cpp/src         CACHE PATH "Path where find cpp files"                        )
set (INC_DIR      ${CMAKE_SOURCE_DIR}/cpp/include     CACHE PATH "Path where find header files"                     )
set (EXAMPLE      ${CMAKE_SOURCE_DIR}/cpp/example     CACHE PATH "Path where find examples files"                   )
set (OUT_DIR      ${CMAKE_SOURCE_DIR}/bin             CACHE PATH "Path where outputs will be installed"        FORCE)
set (PYC_DIR      ${CMAKE_SOURCE_DIR}/CryptoSocket    CACHE PATH "Path where find pythonize version of DNetPRO"     )

file(GLOB SRC    "${SRC_DIR}/*.cpp")
file(GLOB HEADER "${INC_DIR}/*.h"  )
file(GLOB EXE    "${EXAMPLE}/*.cpp")

include_directories(${INC_DIR})
include_directories(${PYC_DIR})

set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/cmake)
include( UseCython )

add_subdirectory (${PYC_DIR}/Crypto/source)

string (REPLACE " " ";" CMAKE_CXX_FLAGS_LIST ${CMAKE_CXX_FLAGS})


#################################################################
#                          SUMMARY                              #
#################################################################

message(STATUS ""                                                                            )
message(STATUS "=================== CryptoSocket configuration Summary =================="   )
message(STATUS "   CryptoSocket version: ${CRYPTO_MAJOR}.${CRYPTO_MINOR}.${CRYPTO_REVISION}" )
message(STATUS ""                                                                            )
message(STATUS "   Build type : ${CMAKE_BUILD_TYPE}"                                         )
message(STATUS "   C++ :"                                                                    )
message(STATUS "      C++ Compiler : ${CMAKE_CXX_COMPILER}"                                  )
message(STATUS "      C++ flags    :"                                                        )
foreach(FLAG ${CMAKE_CXX_FLAGS_LIST})
  message(STATUS "                    * ${FLAG}"                                             )
endforeach(FLAG)
if (CMAKE_BUILD_TYPE STREQUAL "Debug")
  message(STATUS "      C++ Debug flags:"                                                    )
  foreach(FLAG ${CMAKE_CXX_FLAGS_DEBUG})
    message(STATUS "                    * ${FLAG}"                                           )
  endforeach(FLAG)
elseif (CMAKE_BUILD_TYPE STREQUAL "Release")
  message(STATUS "      C++ Release flags  :"                                                )
  foreach(FLAG ${CMAKE_CXX_FLAGS_RELEASE})
    message(STATUS "                    * ${FLAG}"                                           )
  endforeach(FLAG)
endif()
message(STATUS "      Linker flags : "                                                       )
foreach(FLAG ${linked_libs})
  message(STATUS "                    * ${FLAG}"                                             )
endforeach(FLAG)
message(STATUS ""                                                                            )


#################################################################
#                         MAIN RULES                            #
#################################################################

add_executable(keygen    ${EXAMPLE}/generate_key.cpp  ${SRC_DIR}/RSA.cpp)
add_executable(encrypter ${EXAMPLE}/encrypt.cpp       ${SRC_DIR}/Encrypter.cpp)
add_executable(decrypter ${EXAMPLE}/decrypt.cpp       ${SRC_DIR}/Decrypter.cpp)

#################################################################
#                          INSTALLERS                           #
#################################################################

install(TARGETS keygen       DESTINATION ${OUT_DIR})
install(TARGETS encrypter    DESTINATION ${OUT_DIR})
install(TARGETS decrypter    DESTINATION ${OUT_DIR})
