class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.start_number = self.count
        self.end_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_number < self.end_number:
            raise StopIteration
        number = self.start_number
        self.start_number -= 1
        return number


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")