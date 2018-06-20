#include <vector>
#include <string>
#include <tuple>

class HexGrid
{
public:

  HexGrid()
    : northAxis(0), northEastAxis(0), northWestAxis(0),
      southAxis(0), southEastAxis(0), southWestAxis(0),
      furestDistance(0)
  {
    initlialize();
  }

  void initlialize();
  int calcDistance() noexcept;
  int getFurestDistance() noexcept;

private:
  void convertDirectoryToAxisAndAdd(std::string directory);
  void updateEachAxis();

  void optimiseAxis(int &resultAxis, int &firstOptimised, int &secendOptimised) noexcept;
  void optimiseRoute() noexcept;

  using sixPack = std::tuple<int, int, int, int, int, int>;
  bool checkIfStateIsTheSame(sixPack arg) const noexcept;

  void printAxis();

  int northAxis, northEastAxis, northWestAxis,
      southAxis, southEastAxis, southWestAxis;
  std::vector<std::string> steps;

  int furestDistance;
};
