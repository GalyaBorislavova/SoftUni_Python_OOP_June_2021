class ImageArea:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def get_area(self):
        return self.width * self.height

    # Override magic methods for comparison of two image areas

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()


if __name__ == "__main__":
    a1 = ImageArea(7, 10)
    a2 = ImageArea(35, 2)
    a3 = ImageArea(8, 9)
    print(a1 == a2)
    print(a1 != a3)

    a1 = ImageArea(7, 10)
    a2 = ImageArea(35, 2)
    a3 = ImageArea(8, 9)
    print(a1 != a2)
    print(a1 >= a3)

    a1 = ImageArea(7, 10)
    a2 = ImageArea(35, 2)
    a3 = ImageArea(8, 9)
    print(a1 <= a2)
    print(a1 < a3)
