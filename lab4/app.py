"""
Author: Firstname Lastname
Date: 2023-08-17
"""

HOTEL_ROOMS = []


def add_room(name, cost_per_day):
    """
    Add a room to the hotel.

    :param name: The name of the room.
    :param cost_per_day: The cost of the room per day.
    """
    HOTEL_ROOMS.append({"name": name, "value": cost_per_day})


def calculate_stay_cost(room, days):
    """
    Calculate the total cost of a stay in a room.

    :param room: The room to calculate the cost for.
    :param days: The number of days to stay in the room.
    :return: The total cost of the stay.
    """
    return room["value"] * days


def book_room(name, days):
    """
    Book a room for a specific number of days.

    :param name: The name of the room to book.
    :param days: The number of days to book the room for.
    """
    for room in HOTEL_ROOMS:
        if room["name"] == name:
            print(f"Room {room['name']} has been booked for {days} days.")
            print(f"Cost: {calculate_stay_cost(room, days)}")


add_room("room 1", 100)
add_room("room 2", 200)
add_room("room 3", 300)

book_room("room 1", 5)
book_room("room 2", 3)
book_room("room 3", 2)
