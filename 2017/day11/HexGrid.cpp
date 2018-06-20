#include <iostream>

#include "HexGrid.hpp"
#include "FileReader.hpp"
#include "UnknownDirectionException.hpp"

void HexGrid::initlialize()
{
  FileReader r(',');
  try
  {
    steps = r.read("input.txt");
  }
  catch(const FileNotFoundException& e)
  {
    std::cerr << e.what() << std::endl;
  }
  updateEachAxis();
}

void HexGrid::convertDirectoryToAxisAndAdd(std::string direction)
{
  if(direction == "n")
    northAxis += 1;
  else if (direction == "s")
    southAxis += 1;
  else if (direction == "ne")
    northEastAxis += 1;
  else if (direction == "se")
    southEastAxis += 1;
  else if (direction == "nw")
    northWestAxis += 1;
  else if (direction == "sw")
    southWestAxis += 1;
  else
    throw UnknownDirectionException(direction);
}

void HexGrid::updateEachAxis()
{
  int currentDistance;
  for( auto s : steps)
  {
    try
    {
      convertDirectoryToAxisAndAdd(s);
      currentDistance = calcDistance();
      if(currentDistance > furestDistance)
        furestDistance = currentDistance;
    }
    catch(UnknownDirectionException)
    {
      continue;
    }
  }
}

void HexGrid::optimiseAxis(int &resultAxis, int &firstOptimised, int &secendOptimised) noexcept
{
  int commonMoves = std::min(firstOptimised, secendOptimised);
  resultAxis += commonMoves;
  firstOptimised -= commonMoves;
  secendOptimised -= commonMoves;
}

bool HexGrid::checkIfStateIsTheSame(sixPack arg) const noexcept
{
  return (std::get<0>(arg) == northAxis) &&
        (std::get<1>(arg) == northEastAxis) &&
        std::get<2>(arg) == northWestAxis &&
        std::get<3>(arg) == southAxis &&
        std::get<4>(arg) == southEastAxis &&
        std::get<5>(arg) == southWestAxis;
}

void HexGrid::optimiseRoute() noexcept
{
  sixPack state;
  do
  {
    state = std::make_tuple(northAxis, northEastAxis, northWestAxis,
        southAxis, southEastAxis, southWestAxis);

    optimiseAxis(northAxis, northWestAxis, northEastAxis);
    optimiseAxis(northEastAxis, northAxis, southEastAxis);
    optimiseAxis(northWestAxis, northAxis, southEastAxis);
    optimiseAxis(southAxis, southWestAxis, southEastAxis);
    optimiseAxis(southEastAxis, northEastAxis, southAxis);
    optimiseAxis(southWestAxis, northWestAxis, southAxis);

  } while(!checkIfStateIsTheSame(state));
}

void HexGrid::printAxis()
{
  std::cout << northAxis << std::endl
            << northEastAxis << std::endl
            << northWestAxis << std::endl
            << southAxis << std::endl
            << southEastAxis << std::endl
            << southWestAxis << std::endl;
}

int HexGrid::calcDistance() noexcept
{
  optimiseRoute();
  // printAxis();
  return abs( northAxis + northEastAxis + northWestAxis
            - southAxis - southEastAxis - southWestAxis);
}

int HexGrid::getFurestDistance() noexcept
{
  return furestDistance;
}
