#include <iostream>

#include "FirewallSolverBuilder.hpp"

int main()
{
  FirewallSolverBuilder builder;
  FirewallSolver s = builder.build();

  std::cout << "severity = " << s.calculateSeverity() << std::endl;

  return 0;
}
