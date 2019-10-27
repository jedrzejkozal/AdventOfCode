#pragma once
#include "Point.hpp"
#include "Manhattan.hpp"
#include <vector>
#include <algorithm>
#include <iostream>

void printPoint(const Point &p)
{
    std::cout << "[" << p[0] << ", " << p[1] << ", " << p[2] << ", " << p[3] << "] ";
}

class Clusters
{
public:
    Clusters(std::vector<Point> points)
    {
        for (auto &p : points)
        {
            bool isInCluster = false;
            unsigned assignedCluster = 0;
            for (unsigned i = 0; i < clusters.size(); i++)
                if (clusters[i].shouldContainPoint(p))
                {
                    if (not isInCluster)
                    {
                        clusters[i].add(p);
                        isInCluster = true;
                        assignedCluster = i;
                    }
                    else
                    {
                        mergeClusters(i, assignedCluster);
                    }
                }
            if (not isInCluster)
                createNewCluster(p);
        }
    }

    unsigned howManyClusters() const
    {
        return clusters.size();
    }

private:
    class Cluster
    {
    public:
        bool shouldContainPoint(const Point &point) const noexcept
        {
            for (const auto &p : points)
            {
                std::cout << "manhDIstance for ";
                printPoint(point);
                std::cout << " ";
                printPoint(p);
                std::cout << " is " << manhattanDistance(p, point) << std::endl;
                if (manhattanDistance(p, point) <= 3)
                    return true;
            }
            return false;
        }

        void add(const Point &point)
        {
            points.push_back(point);
        }

        void expand(const Cluster &m)
        {
            for (auto &p : m.points)
                points.push_back(p);
        }

        bool operator==(const Cluster &lhs) const
        {
            return points == lhs.points;
        }

    private:
        std::vector<Point> points;
    };

    void mergeClusters(unsigned newCluster, unsigned clusterToMergeTo)
    {
        clusters[clusterToMergeTo].expand(clusters[newCluster]);
        clusters.erase(std::find(clusters.cbegin(), clusters.cend(), clusters[newCluster]));
    }

    void createNewCluster(const Point &p)
    {
        Cluster c;
        c.add(p);
        clusters.push_back(c);
    }

    std::vector<Cluster> clusters;
};