#include <fstream>

#include "gtest/gtest.h"
#include "../FirewallSolverBuilder.hpp"

class FirewallSolverTest : public ::testing::Test {};

void fileSetUp(std::string input)
{
  std::fstream file;
  file.open("input.txt", std::ios::out | std::ios::trunc);
  file << input;
  file.close();
}

void fileTearDown()
{
  remove("input.txt");
}

TEST(FirewallSolverTest, layers_are_added)
{
  FirewallSolver f;
  f.addLayer(Layer(1, 2));
  f.addLayer(Layer(3, 4));
  f.addLayer(Layer(6, 7));
  f.print();
}

TEST(FirewallSolverTest, builder_add_all_layers)
{
  fileSetUp("0: 3\n1: 2\n4: 4\n6: 4");

  FirewallSolverBuilder builder;
  FirewallSolver s = builder.build();
  s.print();
}

TEST(FirewallSolverTest, solver_calculate_severity_from_example)
{
  fileSetUp("0: 3\n1: 2\n4: 4\n6: 4");

  FirewallSolverBuilder builder;
  FirewallSolver s = builder.build();

  ASSERT_EQ(s.calculateSeverity(), 24);
}
