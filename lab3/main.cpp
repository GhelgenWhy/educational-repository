// main.cpp
#include <iostream>

#include "Hotel.h"
#include "Room.h"

using namespace std;

int main() {
    Hotel hotel("Clarion", 10);
    hotel.addRoom(Room("Single", 1));
    hotel.addRoom(Room("Double", 2));
    hotel.addRoom(Room("Suite", 3));
    cout << hotel.info() << endl;
    cout << hotel.getRooms()[0].info() << endl;
    return 0;
}