#include <iostream>
#include <string>
#include <sstream>

#include "FirewallSolverBuilder.hpp"
#include "FileReader.hpp"

int FirewallSolverBuilder::getDepthFromString(std::string s)
{
  std::string depth;
  std::stringstream ss;
  ss << s;
  std::getline(ss, depth, ':');
  std::cout << "depth = " << depth << std::endl;
  return std::stoi(depth);
}

int FirewallSolverBuilder::getRangeFromString(std::string s)
{
  std::string range;
  std::stringstream ss;
  ss << s;
  std::getline(ss, range, ':');
  std::getline(ss, range, ':');
  std::cout << "range = " << range << std::endl;
  return std::stoi(range);
}

FirewallSolver FirewallSolverBuilder::parseVectorToLayers(std::vector<std::string> layers)
{
  FirewallSolver product;

  std::vector<std::string>::iterator it = layers.begin();
  for(; it != layers.end(); it++)
    if(*it != "")
    {
      std::cout << "it = " << *it << std::endl;
      product.addLayer(Layer(getDepthFromString(*it), getRangeFromString(*it)));
    }

  return product;
}

FirewallSolver FirewallSolverBuilder::build()
{
    FileReader r('\n');
    try
    {
      std::vector<std::string> layers = r.read("input.txt");
      return parseVectorToLayers(layers);
    }
    catch(const FileNotFoundException& e)
    {
      std::cerr << e.what() << std::endl;
    }
}
