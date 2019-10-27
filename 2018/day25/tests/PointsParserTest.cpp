#include "gtest/gtest.h"
#include "../PointsParser.hpp"

TEST(PointsParserTest, oneLineIsParsedCorrectly)
{
    auto oneLine = std::vector<std::string>({"0,0,0,0"});
    PointsParser sut;
    auto result = sut.parse(oneLine);
    EXPECT_EQ(result[0], Point({0, 0, 0, 0}));
}

TEST(PointsParserTest, twoLinesAreParsedCorrectly)
{
    auto twoLines = std::vector<std::string>({"0,0,0,0",
                                              "3,0,0,0"});
    PointsParser sut;
    auto result = sut.parse(twoLines);
    EXPECT_EQ(result[0], Point({0, 0, 0, 0}));
    EXPECT_EQ(result[1], Point({3, 0, 0, 0}));
}

TEST(PointsParserTest, threeLinesAreParsedCorrectly)
{
    auto threeLines = std::vector<std::string>({"0,0,0,0",
                                                "3,0,0,0",
                                                "-1,1,0,10"});
    PointsParser sut;
    auto result = sut.parse(threeLines);
    EXPECT_EQ(result[0], Point({0, 0, 0, 0}));
    EXPECT_EQ(result[1], Point({3, 0, 0, 0}));
    EXPECT_EQ(result[2], Point({-1, 1, 0, 10}));
}