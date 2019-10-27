cmake_minimum_required(VERSION 3.10.2)
project(day25)
SET(CMAKE_CXX_STANDARD 14)


SET(TEST_FILES_DIR tests)

find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIR})

SET(PROJECT_FILES
    Manhattan.cpp
)

SET(TEST_FILES
    ${TEST_FILES_DIR}/main_test.cpp
    ${TEST_FILES_DIR}/ManhattanTest.cpp
    ${TEST_FILES_DIR}/PointsParserTest.cpp
    ${TEST_FILES_DIR}/FileLoaderTest.cpp
    ${TEST_FILES_DIR}/ModuleTest.cpp
)

SET(TEST_SOURCE
    ${PROJECT_FILES}
    ${TEST_FILES}
)

add_executable(${PROJECT_NAME} ${PROJECT_FILES} main.cpp)
add_executable(${PROJECT_NAME}_tests ${TEST_SOURCE})


target_link_libraries(${PROJECT_NAME}_tests gtest pthread)


add_custom_target(run
    COMMAND ${PROJECT_NAME}_tests
    DEPENDS ${PROJECT_NAME}_tests)