CXX = g++
CXXFLAGS = -Wall -std=c++17 -O3 -static-libgcc -static-libstdc++

TARGET = lab3
SOURCES = main.cpp Hotel.cpp Room.cpp
OBJECTS = $(SOURCES:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(TARGET)

main.o: main.cpp Hotel.h Room.h
	$(CXX) $(CXXFLAGS) -c main.cpp -o main.o

Room.o: Room.cpp Room.h
	$(CXX) $(CXXFLAGS) -c Room.cpp -o Room.o

Hotel.o: Hotel.cpp Hotel.h Room.h
	$(CXX) $(CXXFLAGS) -c Hotel.cpp -o Hotel.o

clean:
	rm -f $(OBJECTS) $(TARGET)

.PHONY: all clean

