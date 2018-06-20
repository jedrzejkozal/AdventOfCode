#pragma once

#include "FirewallSolver.hpp"

class FirewallSolverBuilder
{
public:
  FirewallSolver build();

private:
  int getDepthFromString(std::string s);
  int getRangeFromString(std::string s);
  FirewallSolver parseVectorToLayers(std::vector<std::string> layers);
};
