cmake_minimum_required(VERSION 3.12)

project(pybindCmake)
SET(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -fPIC")
add_subdirectory(thirdparty)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# set(PYBIND_INCLUDE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/pybind11/include)

pybind11_add_module(${PROJECT_NAME} ${CMAKE_CURRENT_SOURCE_DIR}/bindsrc/bind.cpp)
target_include_directories(${PROJECT_NAME} PUBLIC src/)

add_library(cAdd STATIC src/cAdd.cpp)

target_link_libraries(${PROJECT_NAME} PUBLIC cAdd)
#target_include_directories(cAdd PRIVATE ${PYBIND_INCLUDE} ${CMAKE_CURRENT_SOURCE_DIR}/lib)

#add_executable(test ./main.cpp)
#target_link_libraries(test PRIVATE ${PROJECT_NAME})
