#pragma once
#include <vector>
#include <string>
#include <unordered_map>

using Item = int;
using Transaction = std::vector<int>;
using Dataset = std::vector<Transaction>;

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