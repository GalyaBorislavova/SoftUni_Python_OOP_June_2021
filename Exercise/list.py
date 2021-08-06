numbers = [i for i in range(1, 21)]

odds = [i for i in numbers if i % 2 != 0]
odds_with_filter = list(filter(lambda x: x % 2 != 0, numbers))

print(odds)
print(odds_with_filter)