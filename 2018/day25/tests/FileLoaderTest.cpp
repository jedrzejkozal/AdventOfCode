#include "gtest/gtest.h"
#include "../FileLoader.hpp"

TEST(FileLoader, testFileLoaded)
{
    FileLoader sut;
    auto result = sut.load("../tests/testFile.txt");
    ASSERT_EQ(result,
              std::vector<std::string>({"0,0,0,0",
                                        "3,0,0,0",
                                        "-1,1,0,10"}));
}