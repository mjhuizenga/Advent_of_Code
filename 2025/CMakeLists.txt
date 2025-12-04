cmake_minimum_required(VERSION 3.16)
project(advent_2025)
set(CMAKE_CXX_STANDARD 98)

add_subdirectory(my_libs)

set(ROOT_DIR ${CMAKE_CURRENT_SOURCE_DIR})

file(GLOB children RELATIVE ${ROOT_DIR} "*")

foreach(child ${children})
  if(IS_DIRECTORY "${ROOT_DIR}/${child}" AND child MATCHES "^[0-9]+$")
    set(SOLVE_FILE "${ROOT_DIR}/${child}/solve.cpp")
    if(EXISTS "${SOLVE_FILE}")
      set(target_name "solve_${child}")
      add_executable(${target_name} "${SOLVE_FILE}")
      target_link_libraries(${target_name} PRIVATE my_libs)
      target_include_directories(${target_name} PRIVATE my_libs)
      message(STATUS "Added target ${target_name} for ${child}/solve.cpp")
    endif()
  endif()
endforeach()
