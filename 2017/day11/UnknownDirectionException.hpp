#include <exception>

class UnknownDirectionException : public std::exception
{
public:
	UnknownDirectionException(std::string _dircetion) : direction(_dircetion) {}

	const char* what() const throw()
  {
    std::string result("Cannot open file with name: " + direction);
    return result.c_str();
  }

	virtual ~UnknownDirectionException() throw() {}

private:
	std::string direction;
};
