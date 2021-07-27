from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Vegetable, Fruit]
        self.weight_per_food = 0.10

    def make_sound(self):
        return "Squeak"

    # def feed(self, food):
    #     if food in self.acceptable_foods:
    #         self.weight += food.quantity * self.weight_per_food
    #         self.food_eaten += food.quantity
    #     else:
    #         return f"{type(self).__name__} does not eat {type(food).__name__}!"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 0.40

    def make_sound(self):
        return "Woof!"

    # def feed(self, food):
    #     if food in self.acceptable_foods:
    #         self.weight += food.quantity * self.weight_per_food
    #         self.food_eaten += food.quantity
    #     else:
    #         return f"{type(self).__name__} does not eat {type(food).__name__}!"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat, Vegetable]
        self.weight_per_food = 0.30

    def make_sound(self):
        return "Meow"

    # def feed(self, food):
    #     if food in self:
    #         self.weight += food.quantity * self.weight_per_food
    #         self.food_eaten += food.quantity
    #     else:
    #         return f"{type(self).__name__} does not eat {type(food).__name__}!"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 1

    def make_sound(self):
        return "ROAR!!!"

    # def feed(self, food):
    #     if food in self.acceptable_foods:
    #         self.weight += food.quantity * self.weight_per_food
    #         self.food_eaten += food.quantity
    #     else:
    #         return f"{type(self).__name__} does not eat {type(food).__name__}!"