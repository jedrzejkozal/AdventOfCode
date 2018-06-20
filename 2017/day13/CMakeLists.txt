project(test CXX C)
cmake_minimum_required(VERSION 3.0.2)

#include folder contains current project's header filed
include_directories("include")

set (PROJECT_SOURCE_DIR ..)
set (TEST_FILES_DIR ./test)

set(SOURCE_FILES
  ${PROJECT_SOURCE_DIR}/FileReader.cpp
  ${PROJECT_SOURCE_DIR}/FirewallSolver.cpp
  ${PROJECT_SOURCE_DIR}/FirewallSolverBuilder.cpp
)

set(TESTS_FILES
  ${PROJECT_SOURCE_DIR}/${TEST_FILES_DIR}/main_test.cpp
  ${PROJECT_SOURCE_DIR}/${TEST_FILES_DIR}/FirewallSolverTest.cpp
)

set(TEST_SOURCES
  ${SOURCE_FILES}
  ${TESTS_FILES}
)

set(PROGRAM_SOURCES
  ${SOURCE_FILES}
  ${PROJECT_SOURCE_DIR}/main.cpp
)

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --std=c++14")

add_executable(
  tests ${TEST_SOURCES}
)


add_executable(
  main ${PROGRAM_SOURCES}
)

# Link test executable against gtest nothing else required
target_link_libraries(tests gtest pthread)
target_link_libraries(main gtest pthread)

add_custom_target(run
  COMMAND tests
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
)
