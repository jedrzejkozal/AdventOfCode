#include <iostream>

#include "HexGrid.hpp"


int main()
{
  HexGrid h;
  std::cout << h.calcDistance() << std::endl;
  std::cout << h.getFurestDistance() << std::endl;

  return 0;
}
