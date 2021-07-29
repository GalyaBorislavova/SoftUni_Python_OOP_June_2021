class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = "AaEeOoUuIiYy"
        self.text_vowels = [char for char in self.text if char in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        while self.text_vowels:
            return self.text_vowels.pop(0)
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
