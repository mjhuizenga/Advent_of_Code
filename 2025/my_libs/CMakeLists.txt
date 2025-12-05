# Build a custom C library called "my_libs"
add_library(my_libs
    fileops.cpp
    mathops.cpp
    linkedlist.cpp
)

target_include_directories(my_libs PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
