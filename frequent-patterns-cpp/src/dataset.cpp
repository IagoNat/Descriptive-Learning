#include "../include/dataset.hpp"
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>

using namespace std;

unordered_map<string, vector<string>> load_raw_baskets(
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

unordered_map<string, int> count_item_frequency(
  unordered_map<string, vector<string>>& baskets
) 
{  
  unordered_map<string, int> freq;

  for (const auto& kv: baskets)
    for (const auto& item: kv.second)
      freq[item]++;

  return freq;
}

vector<string> top_k_items(
  unordered_map<string, int>& freq, 
  int k
) 
{
  vector<pair<string, int>> v(freq.begin(), freq.end());

  sort(v.begin(), v.end(),
    [](auto& a, auto& b){ return a.second > b.second; });

  vector<string> result;

  for(size_t i = 0; i < static_cast<size_t>(k) && i < v.size(); ++i)
    result.push_back(v[i].first);

  return result;
}

unordered_map<string, int> build_item_mapping(
  const vector<string>& top_items
) 
{
  unordered_map<string, int> map;

  int id = 0;
  for(const auto& item: top_items)
    map[item] = id++;

  return map;
}

Dataset build_filtered_dataset(
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

Dataset load_online_retail_subset(
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

void write_json_result(
    std::ofstream& out,
    const std::string& algorithm,
    int n_items,
    const MiningResult& res
)
{
    out << "{\n";
    out << "  \"" << algorithm << "\": {\n";
    out << "    \"" << n_items << "\": {\n";

    // runtime
    out << "      \"runtime\": " << res.runtime << ",\n";

    // results
    out << "      \"result\": [\n";

    for(size_t i = 0; i < res.patterns.size(); i++)
    {
        const auto& p = res.patterns[i];

        out << "        {\"items\": [";

        for(size_t j = 0; j < p.first.size(); j++)
        {
            out << p.first[j];
            if(j + 1 < p.first.size())
                out << ",";
        }

        out << "], \"support\": " << p.second << "}";

        if(i + 1 < res.patterns.size())
            out << ",";

        out << "\n";
    }

    out << "      ]\n";
    out << "    }\n";
    out << "  }\n";
    out << "}\n";
}