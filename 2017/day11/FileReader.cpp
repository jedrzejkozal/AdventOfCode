#include <iostream>
#include "FileReader.hpp"

std::vector<std::string> FileReader::readContent(std::fstream &s)
{
  std::string tmp;
  std::vector<std::string> v;
  while(!s.eof())
  {
    std::getline(s, tmp, separator);
    v.push_back(tmp);
  }
  return v;
}

std::vector<std::string> FileReader::read(std::string filename) throw(FileNotFoundException)
{
  std::vector<std::string> v;
  std::fstream file;
  file.open(filename.c_str(), std::ios::in);
  if(file.good())
  {
    v = readContent(file);
    file.close();
  }
  else
  {
    throw FileNotFoundException(filename, __FILE__, __LINE__);
  }
  return v;
}
