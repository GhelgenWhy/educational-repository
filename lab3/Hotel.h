// Hotel.h
#ifndef HOTEL_H
#define HOTEL_H

#include <string>
#include <vector>

#include "Room.h"

class Hotel {
   public:
    Hotel(std::string name, int roomAmount);
    std::string info();
    void addRoom(Room room);
    std::vector<Room> getRooms();

   private:
    std::string name;
    int roomAmount;
    std::vector<Room> rooms;
};

#endif