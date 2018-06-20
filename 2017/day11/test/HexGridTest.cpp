#include <fstream>

#include "gtest/gtest.h"
#include "../HexGrid.hpp"

class HexGridTest : public ::testing::Test {};

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

TEST(HexGridTest, not_known_direction)
{
  fileSetUp("aa,aae");

  HexGrid h;
  ASSERT_EQ(h.calcDistance(), 0);

  fileTearDown();
}

TEST(HexGridTest, nenene_dicstance_is_3)
{
  fileSetUp("ne,ne,ne");

  HexGrid h;
  ASSERT_EQ(h.calcDistance(), 3);

  fileTearDown();
}

TEST(HexGridTest, neneswsw_dicstance_is_0)
{
  fileSetUp("ne,ne,sw,sw");

  HexGrid h;
  ASSERT_EQ(h.calcDistance(), 0);

  fileTearDown();
}

TEST(HexGridTest, neness_dicstance_is_2)
{
  fileSetUp("ne,ne,s,s");

  HexGrid h;
  ASSERT_EQ(h.calcDistance(), 2);

  fileTearDown();
}

TEST(HexGridTest, seswseswsw_dicstance_is_3)
{
  fileSetUp("se,sw,se,sw,sw");

  HexGrid h;
  ASSERT_EQ(h.calcDistance(), 3);

  fileTearDown();
}
