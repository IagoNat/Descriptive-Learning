#pragma once
#include "dataset.hpp"
#include <vector>

MiningResult 
naive_mine(
  const Dataset& D,
  int minsup
);