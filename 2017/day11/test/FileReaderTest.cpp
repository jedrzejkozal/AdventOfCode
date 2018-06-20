#include <fstream>
#include <stdio.h>

#include "gtest/gtest.h"
#include "../FileReader.hpp"

namespace tests {

  class FileReaderTest : public ::testing::Test
  {
  public:
    FileReaderTest() {}
  };

  void fileSetUp(std::string input)
  {
    std::fstream file;
    file.open("file.txt", std::ios::out | std::ios::trunc);
    file << input;
    file.close();
  }

  void fileTearDown()
  {
    remove("file.txt");
  }

  TEST(FileReaderTest, file_not_found)
  {
    FileReader r(' ');
    try
    {
      r.read("s.txt");
    }
    catch(FileNotFoundException e)
    {
      ASSERT_EQ(std::string(e.what()),
      std::string(
        "/home/jkozal/Dokumenty/AdventOfCode/day11/FileReader.cpp 28 Cannot open file with name: s.txt"));
      return;
    }
    FAIL();
  }

  TEST(FileReaderTest, file_read_single_word)
  {
    fileSetUp("aaa");

    FileReader r(' ');
    try
    {
      auto v = r.read("file.txt");
      ASSERT_GT(v.size(), 0);
      if(v.size())
        ASSERT_EQ(v[0], "aaa");
    }
    catch(FileNotFoundException)
    {
      FAIL();
    }
    fileTearDown();
  }

  TEST(FileReaderTest, file_read_two_words)
  {
    fileSetUp("aaa,bbb");

    FileReader r(',');
    try
    {
      auto v = r.read("file.txt");
      ASSERT_GT(v.size(), 0);
      ASSERT_EQ(v[0], "aaa");
      ASSERT_EQ(v[1], "bbb");
    }
    catch(FileNotFoundException)
    {
      FAIL();
    }
    fileTearDown();
  }

} // tests
