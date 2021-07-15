class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, number_of_people):
        if self.capacity >= number_of_people and not self.is_taken:
            self.guests += number_of_people
            self.is_taken = True
            return
        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
            return
        return f"Room number {self.number} is not taken"