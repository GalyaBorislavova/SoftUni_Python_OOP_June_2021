from project.animal import Animal


class Mammal(Animal):
    pass


if __name__ == "__main__":
    mammal = Mammal("Stella")
    print(mammal.__class__.__bases__[0].__name__)
    print(mammal.name)
