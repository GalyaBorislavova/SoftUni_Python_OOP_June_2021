from wild_farm.animals.animal import Mammal
from wild_farm.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Vegetable, Fruit]
        self.weight_per_food = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat, Vegetable]
        self.weight_per_food = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 1

    def make_sound(self):
        return "ROAR!!!"