# solution with generator
def squares(n):
    num = 1
    while num <= n:
        yield num ** 2
        num += 1


# solution with iterator
class squares_iter:
    def __init__(self, end_number):
        self.end_number = end_number
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end_number:
            raise StopIteration
        square = self.start ** 2
        self.start += 1
        return square


print(list(squares(5)))
