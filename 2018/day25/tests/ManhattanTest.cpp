#include "gtest/gtest.h"
#include "../Manhattan.hpp"

TEST(ManhattanTest, distanceForTheSamePointIsZero)
{
    Point a = {1, 1, 1, 1};
    auto distance = manhattanDistance(a, a);
    ASSERT_EQ(distance, distance);
}

TEST(ManhattanTest, distanceFor0and1Is4)
{
    Point a = {0, 0, 0, 0};
    Point b = {1, 1, 1, 1};

    auto distance = manhattanDistance(a, b);
    ASSERT_EQ(distance, 4);
}

TEST(ManhattanTest, distanceFor1100and2300Is3)
{
    Point a = {1, 1, 0, 0};
    Point b = {2, 3, 0, 0};

    auto distance = manhattanDistance(a, b);
    ASSERT_EQ(distance, 3);
}

TEST(ManhattanTest, distanceIs2)
{
    Point a = {0, 0, 2, -2};
    Point b = {0, 0, 0, -2};

    auto distance = manhattanDistance(a, b);
    ASSERT_EQ(distance, 2);
}