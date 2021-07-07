def print_rhombus_row(size, stars_count):
    for row in range(size - stars_count):
        print(" ", end="")
    for row in range(1, stars_count):
        print("*", end=" ")
    print("*")


n = int(input())
for stars in range(1, n):
    print_rhombus_row(n, stars)
for stars in range(n, 0, -1):
    print_rhombus_row(n, stars)
