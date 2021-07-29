def reverse_text(text):
    reversed_text = list(text)
    while reversed_text:
        yield reversed_text.pop()


for char in reverse_text("step"):
    print(char, end='')