def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for n in range(n):
            result.append(next(seq))
        return result

    return take, halves, integers


take_function = solution()[0]
halves_function = solution()[1]
integers_function = solution()[2]
print(take_function(5, halves_function()))
print(take_function(10, integers_function()))
