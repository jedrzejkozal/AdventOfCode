#include <iostream>
#include "FileLoader.hpp"
#include "PointsParser.hpp"
#include "Clusters.hpp"

int main()
{
    FileLoader fileLoader;
    PointsParser parser;
    auto rawPoints = fileLoader.load("../puzzle_input.txt");
    auto points = parser.parse(rawPoints);

    Clusters clusters(points);
    std::cout << clusters.howManyClusters() << std::endl;

    return 0;
}