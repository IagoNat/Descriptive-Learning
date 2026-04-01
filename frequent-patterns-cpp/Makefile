CXX = g++
CXXFLAGS = -O3 -Wall -Wextra -Iinclude

SRC_DIR = src
OBJ_DIR = obj
BIN = program

SRC = $(wildcard $(SRC_DIR)/*.cpp)
OBJ = $(SRC:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

all: $(BIN)

$(BIN): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $^

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	mkdir -p $(OBJ_DIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

run: $(BIN)
	./$(BIN) ../data/online_retail.csv 15

clean: 
	rm -rf $(OBJ_DIR) $(BIN)