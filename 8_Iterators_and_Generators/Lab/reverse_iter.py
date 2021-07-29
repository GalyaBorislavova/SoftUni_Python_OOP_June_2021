class reverse_iter:
    def __init__(self, iterable_obj):
        self.iterable_obj = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        while self.iterable_obj:
            return self.iterable_obj.pop()
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
