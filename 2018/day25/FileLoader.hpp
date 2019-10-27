#pragma once
#include <string>
#include <fstream>
#include <iostream>
#include <vector>

class FileLoader
{
public:
    std::vector<std::string> load(const std::string &filename) const
    {
        std::vector<std::string> result;
        std::fstream file;
        file.open(filename);
        if (file.is_open())
        {
            std::string tmp;
            while (getline(file, tmp, '\n'))
            {
                result.push_back(tmp);
            }
            file.close();
            return result;
        }
        else
            throw FileNotOpenedException();
    }

private:
    class FileNotOpenedException : public std::exception
    {
    public:
        FileNotOpenedException()
            : what("Unable to open file") {}

        const char *what;
    };
};