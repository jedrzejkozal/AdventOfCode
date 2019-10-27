#include "gtest/gtest.h"
#include "../PointsParser.hpp"
#include "../Clusters.hpp"

TEST(ModuleTest, firstConstelation)
{
    auto firstConstelation = std::vector<std::string>({"-1,2,2,0",
                                                       "0,0,2,-2",
                                                       "0,0,0,-2",
                                                       "-1,2,0,0",
                                                       "-2,-2,-2,2",
                                                       "3,0,2,-1",
                                                       "-1,3,2,2",
                                                       "-1,0,-1,0",
                                                       "0,2,1,-2",
                                                       "3,0,0,0"});
    PointsParser parser;
    auto points = parser.parse(firstConstelation);
    Clusters clusters(points);
    ASSERT_EQ(clusters.howManyClusters(), 4);
}

TEST(ModuleTest, secondConstelation)
{
    auto secondConstelation = std::vector<std::string>({"1,-1,0,1",
                                                        "2,0,-1,0",
                                                        "3,2,-1,0",
                                                        "0,0,3,1",
                                                        "0,0,-1,-1",
                                                        "2,3,-2,0",
                                                        "-2,2,0,0",
                                                        "2,-2,0,-1",
                                                        "1,-1,0,-1",
                                                        "3,2,0,2"});
    PointsParser parser;
    auto points = parser.parse(secondConstelation);
    Clusters clusters(points);
    ASSERT_EQ(clusters.howManyClusters(), 3);
}