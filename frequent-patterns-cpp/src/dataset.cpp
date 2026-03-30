#include "../include/dataset.hpp"
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;

unordered_map<string, vector<string>> 
load_raw_baskets(
  const string& filename
) 
{
  ifstream file(filename);
  string line;

  unordered_map<string, vector<string>> baskets;

  getline(file, line);

  while(getline(file, line))
  {
    stringstream ss(line);

    string invoice;
    string stock;
    string description;

    getline(ss, invoice, ',');
    getline(ss, stock, ',');
    getline(ss, description, ',');

    if(description.empty()) continue;

    baskets[invoice].push_back(description);
  }

  return baskets;
}

unordered_map<string, int> 
count_item_frequency(
  unordered_map<string, vector<string>>& baskets
) 
{  
  unordered_map<string, int> freq;

  for (const auto& kv: baskets)
    for (const auto& item: kv.second)
      freq[item]++;

  return freq;
}

vector<string> 
top_k_items(
  unordered_map<string, int>& freq, 
  int k
) 
{
  vector<pair<string, int>> v(freq.begin(), freq.end());

  sort(v.begin(), v.end(),
    [](auto& a, auto& b){ return a.second > b.second; });

  vector<string> result;

  for(int i=0; i<k && i<v.size(); i++)
    result.push_back(v[i].first);

  return result;
}

unordered_map<string, int>
build_item_mapping(
  const vector<string>& top_items
) 
{
  unordered_map<string, int> map;

  int id = 0;
  for(const auto& item: top_items)
    map[item] = id++;

  return map;
}

Dataset 
build_filtered_dataset(
  const unordered_map<string, vector<string>>& baskets,
  const unordered_map<string, int>& item_map
) 
{
  Dataset D;

  for (const auto& kv: baskets)
  {
    Transaction t;

    for (const auto& item: kv.second)
    {
      auto it = item_map.find(item);
      if(it != item_map.end())
        t.push_back(it->second);
    }

    if(!t.empty())
      D.push_back(t);
  }

  return D;
}