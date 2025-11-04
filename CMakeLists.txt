cmake_minimum_required(VERSION 3.28)

project(geometry-central)


# Options
option(BUILD_SHARED_LIBS "Build the shared library" FALSE)
option(WITH_SUITESPARSE "Enable SuiteSparse." OFF)
option(GEOMETRY_CENTRAL_BUILD_TESTS "Build tests" OFF)


if(BUILD_SHARED_LIBS)
    message("-- Building SHARED libraries")
else()
    message("-- Building STATIC libraries")
endif()


if (WITH_SUITESPARSE)
  message(FATAL_ERROR "SuiteSparse currently not supported!")
endif()



find_package(Eigen3 REQUIRED)
find_package(nanoflann REQUIRED)
find_package(nanort REQUIRED)
find_package(happly REQUIRED)


add_library(
    geometry-central
)
add_library(geometry-central::geometry-central ALIAS geometry-central)

target_link_libraries(
  geometry-central PUBLIC
    Eigen3::Eigen
    nanoflann::nanoflann
    nanort::nanort
    happly::happly
)

# Set compiler properties for the library
target_compile_features(geometry-central PUBLIC cxx_std_11)
target_compile_definitions(geometry-central PUBLIC NOMINMAX _USE_MATH_DEFINES)

add_subdirectory(src)

if(GEOMETRY_CENTRAL_BUILD_TESTS)
    message(STATUS "Testing is enabled!")
    enable_testing()
    add_subdirectory(test)
endif()

install(
    TARGETS 
        geometry-central
    FILE_SET
        geometry_central_public_headers
)

# ### Handle windows-specific fixes
# if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
#   add_definitions (-DNOMINMAX)  # don't use weird windows built-in min/max
#   add_definitions (-D_USE_MATH_DEFINES)  # match unix behavior of constants in cmath
# endif()

# ### Do anything needed for dependencies and bring their stuff in to scope
# add_subdirectory(deps)

# # copy variables set by deps upward
# SET(GC_HAVE_SUITESPARSE ${GC_HAVE_SUITESPARSE} PARENT_SCOPE)

# ### Recurse to the source code
# add_subdirectory(src)

# # install
# install(
#   TARGETS geometry-central
#   ARCHIVE DESTINATION lib
#   RUNTIME DESTINATION bin
#   LIBRARY DESTINATION lib)

# install(
#   DIRECTORY ${CMAKE_SOURCE_DIR}/include/
#   DESTINATION include
#   FILES_MATCHING
#   PATTERN "*.h"
#   PATTERN "*.ipp")
