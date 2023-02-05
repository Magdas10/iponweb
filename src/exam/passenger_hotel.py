class PassengerError(Exception):
    pass


class Passenger:
    def __init__(self, name, city, rooms):
        if isinstance(name, str):
            self.__name = name
        else:
            raise PassengerError("wrong input type for name")
        if isinstance(city, str):
            self.__city = city
        else:
            raise PassengerError("wrong input type for city")

        if isinstance(rooms, dict):
            self.__rooms = rooms
        else:
            raise PassengerError("wrong input type for rooms")

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city

    @property
    def rooms(self):
        return self.__rooms

    def __repr__(self):
        return f"name-{self.__name}, city-{self.__city}, rooms-{self.__rooms}"


class HotelError(Exception):
    pass


class Hotel:
    def __init__(self, city, rooms):
        if isinstance(city, str):
            self.__city = city
        else:
            raise PassengerError("wrong input type for city")

        if isinstance(rooms, dict):
            self.__rooms = rooms
        else:
            raise PassengerError("wrong input type for rooms")

    def __repr__(self):
        return f"city-{self.__city}, rooms-{self.__rooms}"

    def get_city(self):
        return self.__city

    def free_rooms_list(self, room_type):
        if isinstance(room_type, str):
            return self.__rooms[room_type]
        else:
            raise HotelError("wrong input type for room type")

    def reserve_rooms(self, room_type, count):
        if not isinstance(room_type, str):
            raise HotelError("wrong input type for room type")
        if not (isinstance(count, int) and count >= 0):
            raise HotelError("wrong input type for count")
        if count <= self.__rooms[room_type]:
            self.__rooms[room_type] -= count
        else:
            print("there is no so many free rooms")


def book(pass1, hotel1):
    print(pass1)
    print(pass1.rooms)
    print(hotel1.get_city())
    print(hotel1.free_rooms_list('single'))
    hotel1.reserve_rooms('vip', 4)
    hotel1.reserve_rooms('vip', 1)


book(Passenger("Anna", "Yerevan", {'single': 1}), Hotel("Yerevan", {'single': 10, 'vip': 4}))
