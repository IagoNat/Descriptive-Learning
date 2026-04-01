#pragma once
#include <vector>
#include <string>
#include <unordered_map>

#define DATA_PATH "../data/online_retail.csv"
#define RES_PATH "../data/results.json"

using Item = int;
using Transaction = std::vector<int>;
using Dataset = std::vector<Transaction>;
using Itemset = std::vector<int>;
struct MiningResult {
  std::vector<std::pair<Itemset, int>> patterns;
  double runtime;
};

std::unordered_map<std::string, std::vector<std::string>>
load_raw_baskets(const std::string& filename);

std::unordered_map<std::string,int>
count_item_frequency(
    std::unordered_map<std::string,
    std::vector<std::string>>& baskets);

std::vector<std::string>
top_k_items(
    std::unordered_map<std::string,int>& freq,
    int k);

std::unordered_map<std::string,int>
build_item_mapping(
    const std::vector<std::string>& top_items);

Dataset build_filtered_dataset(
    const std::unordered_map<std::string,
    std::vector<std::string>>& baskets,
    const std::unordered_map<std::string,int>& item_map);

Dataset load_online_retail_subset(
  const std::string& filename,
  int top_k
);

Dataset load_dataset(
  const std::string& filename,
  int top_k
);

void write_json_result(
    std::ofstream& out,
    const std::string& algorithm,
    int n_items,
    const MiningResult& res
);