// Room.cpp
#include "Room.h"

#include <string>

Room::Room(std::string name, int number) {
    this->name = name;
    this->number = number;
}

std::string Room::info() const {
    return name + " Room " + std::to_string(number);
}