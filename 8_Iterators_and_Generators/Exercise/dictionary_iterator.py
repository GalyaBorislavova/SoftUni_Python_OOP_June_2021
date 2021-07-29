class dictionary_iter:
    def __init__(self, dictionary_obj):
        self.dictionary_obj = dictionary_obj

    def __iter__(self):
        return self

    def __next__(self):
        if not self.dictionary_obj:
            raise StopIteration
        for key, value in self.dictionary_obj.items():
            return key, self.dictionary_obj.pop(key)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
