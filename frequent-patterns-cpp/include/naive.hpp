#pragma once
#include "dataset.hpp"
#include <vector>

using Itemset = std::vector<int>;

struct MiningResult {
  std::vector<std::pair<Itemset, int>> patterns;
  double runtime;
};

MiningResult 
naive_mine(
  const Dataset& D,
  int minsup
);