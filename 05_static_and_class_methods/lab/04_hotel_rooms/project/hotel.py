from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room: Room = next((r for r in self.rooms if r.number == room_number), None)
        return room.take_room(people)


    def free_room(self, room_number):
        room: Room = next((r for r in self.rooms if r.number == room_number), None)
        return room.free_room()


    def status(self):
        taken_rooms: list[Room] = [r.number for r in self.rooms if r.is_taken]
        free_rooms: list[Room] = [r.number for r in self.rooms if not r.is_taken]
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join([str(r) for r in free_rooms])}\n"
                f"Taken rooms: {', '.join([str(r) for r in taken_rooms])}")

