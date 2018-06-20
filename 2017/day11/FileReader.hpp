#include <fstream>
#include <string>
#include <vector>

#include "FileNotFoundException.hpp"

class FileReader
{
public:
  FileReader(char _separator)
    : separator(_separator) {}

  std::vector<std::string> read(std::string filename) throw(FileNotFoundException);

private:
  std::vector<std::string> readContent(std::fstream &s);
  char separator;
};
