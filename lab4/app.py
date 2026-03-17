Hotel = []


def addRoom(name, costPerDay):
    Hotel.append({"name": name, "value": costPerDay})


def calculateStayCost(room, days):
    return room["value"] * days


def bookRoom(name, days):
    for room in Hotel:
        if room["name"] == name:
            print(f"Room {room['name']} has been booked for {days} days.")
            print(f"Cost: {calculateStayCost(room, days)}")


addRoom("room 1", 100)
addRoom("room 2", 200)
addRoom("room 3", 300)

bookRoom("room 1", 5)
bookRoom("room 2", 3)
bookRoom("room 3", 2)
