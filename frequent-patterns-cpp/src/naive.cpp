#include "../include/naive.hpp"
#include <unordered_set>
#include <algorithm>
#include <chrono>

using namespace std;

static bool is_subset(
  const Itemset& X, 
  const Transaction& t
)
{
  for (int item: X)
    if(find(t.begin(), t.end(), item) == t.end())
      return false;
  return true;
}

static int 
support(
  const Itemset& X, 
  const Dataset& D
)
{
  int count = 0;
  for (const auto& t: D)
    if(is_subset(X, t))
      count++;
  return count;
}

static void dfs(
  const vector<int>& items,
  int idx,
  Itemset& current,
  const Dataset& D,
  int minsup,
  vector<pair<Itemset, int>>& patterns
)
{
  if(static_cast<size_t>(idx) == items.size())
  {
    if(!current.empty())
    {
      int sup = support(current, D);
      if(sup >= minsup)
        patterns.push_back({current, sup});
    }
    return;
  }

  dfs(items, idx+1, current, D, minsup, patterns);

  current.push_back(items[idx]);
  dfs(items, idx+1, current, D, minsup, patterns);
  current.pop_back();
}

MiningResult naive_mine(
  const Dataset& D,
  int minsup
)
{
  unordered_set<int> set_items;

  for (const auto& t: D)
    for(int x: t)
      set_items.insert(x);

  vector<int> items(set_items.begin(), set_items.end());

  vector<pair<Itemset, int>> patterns;
  Itemset current;

  auto start = chrono::high_resolution_clock::now();

  dfs(items, 0, current, D, minsup, patterns);

  auto end = chrono::high_resolution_clock::now();

  double runtime = chrono::duration<double>(end - start).count();

  return {patterns, runtime};
}