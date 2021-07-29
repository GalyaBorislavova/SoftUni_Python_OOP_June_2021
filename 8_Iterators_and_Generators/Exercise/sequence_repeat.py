class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence  # string
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    #  way 1
    # def __next__(self):
    #     if self.number == 0:
    #         raise StopIteration
    #     self.number -= 1
    #     if self.index >= len(self.sequence):
    #         self.index = 0
    #     item = self.sequence[self.index]
    #     self.index += 1
    #     return item

    # way 2
    def __next__(self):
        if self.index < self.number:
            ind = self.index
            self.index += 1
            return self.sequence[ind % len(self.sequence)]
        else:
            raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

