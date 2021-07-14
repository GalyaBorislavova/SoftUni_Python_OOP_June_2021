from Hotel_room_4.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.guests = 0
        self.rooms = []

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room_to_add: Room):
        self.rooms.append(room_to_add)
        return

    def take_room(self, room_number, people):
        searched_room: Room = [r for r in self.rooms if r.number == room_number][0]
        if not searched_room.is_taken and searched_room.capacity >= people:
            Room.take_room(searched_room, people)
            self.guests += people
        return

    def free_room(self, room_number):
        searched_room: Room = [r for r in self.rooms if r.number == room_number][0]
        if searched_room.is_taken:
            self.guests -= searched_room.guests
            Room.free_room(searched_room)
        return

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        output = [
            f"Hotel {self.name} has {self.guests} total guests",
            f"Free rooms: {', '.join(free_rooms)}",
            f"Taken rooms: {', '.join(taken_rooms)}"
        ]
        return '\n'.join(output)