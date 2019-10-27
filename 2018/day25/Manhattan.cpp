#include "Manhattan.hpp"

unsigned manhattanDistance(Point a, Point b)
{
    unsigned distance = 0;
    for (unsigned i = 0; i < nDims; i++)
        distance += abs(b[i] - a[i]);
    return distance;
}