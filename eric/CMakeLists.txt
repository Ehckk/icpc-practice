cmake_minimum_required(VERSION 3.26)
project(eric)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin")

add_executable(forestforthetrees gnyr23/forestforthetrees.cpp)
add_executable(morsecodepalindrome gnyr23/morsecodepalindrome.cpp)
