// Room.h
#ifndef ROOM_H
#define ROOM_H

#include <string>

class Room {
   public:
    Room(std::string name, int number);
    std::string info() const;

   private:
    std::string name;
    int number;
};

#endif