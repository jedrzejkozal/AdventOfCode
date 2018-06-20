#pragma once
#include <vector>

struct Layer
{
  Layer()
    : depth(0), range(0), scanerPosition(0), movingDown(false) {}
  Layer(int d, int r)
    : depth(d), range(r), scanerPosition(0), movingDown(false) {}

  void move() noexcept;

  const int depth;
  const int range;

  int scanerPosition;
  bool movingDown;
};

class FirewallSolver
{
public:
  void addLayer(Layer && l);
  void print();

  int calculateSeverity();
private:
  void addEmptyLayers(int newLayerDepth);
  bool checkIfEmptyLayerExists(Layer added);

  void movePacket();
  void moveAllScaners();
  int calcActualSeverity();

  int packetPostion;
  std::vector<Layer> layers;
};
