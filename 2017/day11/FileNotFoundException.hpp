#include <exception>
#include <stdexcept>

class FileNotFoundException : public std::exception
{
public:

  FileNotFoundException(std::string _filename, std::string _codeSournceName,
      int _line)
    : filename(_filename), codeSournceName(_codeSournceName),
      line(_line)
    {}

  virtual ~FileNotFoundException() throw() {}

  const char* what() const throw()
  {
    std::string result(codeSournceName + " " + std::to_string(line) +
      " Cannot open file with name: " + filename);
    return result.c_str();
  }

private:
  std::string filename;
  std::string codeSournceName;
  int line;
};
