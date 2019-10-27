#pragma once
#include "Point.hpp"
#include <vector>
#include <sstream>

class PointsParser
{
public:
    std::vector<Point> parse(std::vector<std::string> pointsRaw) const
    {
        std::vector<Point> points;
        for (auto pointString : pointsRaw)
        {
            auto tokens = split(pointString, ',');
            points.push_back(tokens2Point(tokens));
        }
        return points;
    }

private:
    std::vector<std::string> split(const std::string &s, char delimeter) const
    {
        std::vector<std::string> tokens;
        std::string token;
        std::istringstream tokenStream(s);
        while (std::getline(tokenStream, token, delimeter))
        {
            tokens.push_back(token);
        }
        return tokens;
    }

    Point tokens2Point(const std::vector<std::string> &tokens) const
    {
        return Point({std::stoi(tokens[0]),
                      std::stoi(tokens[1]),
                      std::stoi(tokens[2]),
                      std::stoi(tokens[3])});
    }
};