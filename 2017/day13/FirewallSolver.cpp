#include <algorithm>
#include <iostream>

#include "FirewallSolver.hpp"

void Layer::move() noexcept
{
  if(scanerPosition == 0 || scanerPosition == range-1)
    movingDown = !movingDown;

  if(movingDown)
    scanerPosition++;
  else
    scanerPosition--;
}


bool FirewallSolver::checkIfEmptyLayerExists(Layer added)
{
  std::vector<Layer>::iterator it = find_if(layers.begin(), layers.end(),
    [added](Layer l)
    {
      return l.depth == added.depth;
    });

  return it != layers.end();
}

void FirewallSolver::addEmptyLayers(int newLayerDepth)
{
  int diffrence = newLayerDepth - layers.back().depth;

  while(--diffrence)
    layers.push_back(Layer(layers.back().depth+1, 0));
}

void FirewallSolver::addLayer(Layer && l)
{
  if(layers.empty())
    layers.push_back(l);

  if(!checkIfEmptyLayerExists(l))
  {
    addEmptyLayers(l.depth);
    layers.push_back(l);
  }
}

void FirewallSolver::print()
{
  std::vector<Layer>::iterator it = layers.begin();
  for(; it != layers.end(); it++)
    std::cout << it->depth << ": " << it->range << std::endl;
}

void FirewallSolver::movePacket()
{
  packetPostion++;
}

void FirewallSolver::moveAllScaners()
{
  for(std::vector<Layer>::iterator it = layers.begin(); it != layers.end(); it++)
    it->move();
}

int FirewallSolver::calcActualSeverity()
{
  if(layers[packetPostion].scanerPosition == 0)
  {
    std::cout << "packetPostion = "   << packetPostion  <<
                 "scanerPosition = "  << layers[packetPostion].scanerPosition <<
                 "depth = "           << layers[packetPostion].depth <<
                 "range = "           << layers[packetPostion].range << std::endl;
    return layers[packetPostion].depth * layers[packetPostion].range;
  }
  else
    return 0;
}

int FirewallSolver::calculateSeverity()
{
  int severity = 0;
  packetPostion = -1;

  for(std::vector<Layer>::iterator it = layers.begin(); it != layers.end(); it++)
  {
    movePacket();
    severity += calcActualSeverity();
    moveAllScaners();
  }

  return severity;
}
