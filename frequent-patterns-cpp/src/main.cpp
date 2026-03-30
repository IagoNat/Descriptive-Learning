#include "../include/dataset.hpp"
#include "../include/naive.hpp"
#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

Dataset
load_online_retail_subset(
  const string& filename,
  int top_k
)
{
  auto baskets = load_raw_baskets(filename);

  auto freq = count_item_frequency(baskets);

  auto top_items = top_k_items(freq, top_k);

  auto item_map = build_item_mapping(top_items);
  
  return build_filtered_dataset(baskets, item_map);
}

Dataset load_dataset(
  const string& filename,
  int top_k
)
{
  std::cout << "Loading dataset...\n";

  Dataset D = load_online_retail_subset(filename, top_k);

  std::cout << "Transactions loaded: " << D.size() << "\n";

  if (D.empty())
  {
    std::cout << "Dataset is empty!\n";
    return D;
  }

  size_t total_items = 0;
  size_t max_size = 0;

  for (const auto& t: D)
  {
    total_items += t.size();
    if (t.size() > max_size)
      max_size = t.size();
  }

  double avg = (double) total_items / D.size();

  std::cout << "Average basket size: " << avg << "\n";
  std::cout << "Max basket size: " << max_size << "\n";

  std::cout << "\nSample transactions:\n";

  int sample_n = std::min((size_t)5, D.size());

  for (int i=0; i < sample_n; i++)
  {
    std::cout << "{ ";
    for (int item: D[i])
      std::cout << item << " ";
    std::cout << "}\n";
  }

  std::cout << "\n";

  return D;
}

int main() 
{
  Dataset D = load_dataset("../../data/online_retail.csv", 5);

  std::cout << "Running Naive Itemset Mining Algorithm" << "\n";

  MiningResult res = naive_mine(D, 1000);

  std::ofstream out("../../data/patterns_naive.csv");

  for (auto& p: res.patterns)
  {
    for (int item: p.first)
      out << item << " ";
    out << "," << p.second << "\n";
  }

  return 0;
}