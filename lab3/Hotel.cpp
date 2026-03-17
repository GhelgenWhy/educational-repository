// Hotel.cpp
#include "Hotel.h"

Hotel::Hotel(std::string name, int roomAmount) {
    this->name = name;
    this->roomAmount = roomAmount;
}

std::string Hotel::info() {
    return name + " has " + std::to_string(roomAmount) + " rooms.";
}

void Hotel::addRoom(Room room) { rooms.push_back(room); }

std::vector<Room> Hotel::getRooms() { return rooms; }