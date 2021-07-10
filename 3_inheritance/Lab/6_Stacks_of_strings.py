class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        return True

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


custom_s = Stack()
custom_s.push("5")
custom_s.push("7")
custom_s.push("8")
custom_s.push("2")
print(custom_s.pop())
print(custom_s.is_empty())
print(custom_s)

