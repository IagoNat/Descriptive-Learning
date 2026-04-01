#include "../include/dataset.hpp"
#include "../include/naive.hpp"
#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]) 
{
  std::string filename = DATA_PATH;
  int n_items = 5;

  if(argc > 1) {
    filename = argv[1];
    n_items = std::stoi(argv[2]);
  }

  Dataset D = load_dataset(filename, n_items);

  std::cout << "Running Naive Itemset Mining Algorithm" << "\n";

  MiningResult res = naive_mine(D, 1000);

  std::ofstream out(RES_PATH);
    
  if(!out.is_open())
  {
    std::cerr << "Error opening JSON file\n";
    return 1;
  }

  write_json_result(out, "naive", n_items, res);  

  std::cout << "Results saved to JSON.\n";

  return 0;
}