WARNING_FLAGS = -pedantic -Wall -Wextra -Wsign-conversion
CC = g++ -std=c++11 -c $(WARNING_FLAGS)
CL = g++ -std=c++11 $(WARNING_FLAGS)
SOURCE_DIR = src
BUILD_DIR = build

all: dir SimpleAd.out

dir:
	mkdir -p $(BUILD_DIR)

SimpleAd.out: $(BUILD_DIR)/Main.o $(BUILD_DIR)/Advertiser.o $(BUILD_DIR)/Ad.o $(BUILD_DIR)/BaseAdvertising.o
	$(CL) $(BUILD_DIR)/Main.o $(BUILD_DIR)/Advertiser.o $(BUILD_DIR)/Ad.o $(BUILD_DIR)/BaseAdvertising.o -o SimpleAd.out 

$(BUILD_DIR)/Main.o: $(SOURCE_DIR)/Main.cpp $(SOURCE_DIR)/Advertiser.hpp $(SOURCE_DIR)/Ad.hpp ${SOURCE_DIR}/BaseAdvertising.hpp
	$(CC) $(SOURCE_DIR)/Main.cpp -o $(BUILD_DIR)/Main.o

$(BUILD_DIR)/Advertiser.o: $(SOURCE_DIR)/Advertiser.cpp $(SOURCE_DIR)/Advertiser.hpp 
	$(CC) $(SOURCE_DIR)/Advertiser.cpp -o $(BUILD_DIR)/Advertiser.o

$(BUILD_DIR)/Ad.o: $(SOURCE_DIR)/Ad.cpp $(SOURCE_DIR)/Ad.hpp 
	$(CC) $(SOURCE_DIR)/Ad.cpp -o $(BUILD_DIR)/Ad.o

$(BUILD_DIR)/BaseAdvertising.o: $(SOURCE_DIR)/BaseAdvertising.cpp $(SOURCE_DIR)/BaseAdvertising.hpp
	$(CC) $(SOURCE_DIR)/BaseAdvertising.cpp -o $(BUILD_DIR)/BaseAdvertising.o

	
.PHONY: clean
clean:
	rm -rf $(BUILD_DIR) 
	rm SimpleAd.out 