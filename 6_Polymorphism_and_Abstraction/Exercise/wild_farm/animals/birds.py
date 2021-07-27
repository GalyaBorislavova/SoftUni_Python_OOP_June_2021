from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    # def feed(self, food):
    #     if food in self.acceptable_foods:
    #         self.weight += food.quantity * self.weight_per_food
    #         self.food_eaten += food.quantity
    #     else:
    #         return f"{type(self).__name__} does not eat {type(food).__name__}!"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.acceptable_foods = [Fruit, Meat, Seed, Vegetable]
        self.weight_per_food = 0.35

    def make_sound(self):
        return "Cluck"

    # def feed(self, food):
    #     if food in self.acceptable_foods:
    #         self.weight += food.quantity * self.weight_per_food
    #         self.food_eaten += food.quantity
    #     else:
    #         return f"{type(self).__name__} does not eat {type(food).__name__}!"


if __name__ == "__main__":
    owl = Owl("Pip", 10, 10)
    print(owl)
    meat = Meat(4)
    print(owl.make_sound())
    owl.feed(meat)
    veg = Vegetable(1)
    print(owl.feed(veg))
    print(owl)

    print("*" * 88)

    hen = Hen("Harry", 10, 10)
    veg = Vegetable(3)
    fruit = Fruit(5)
    meat = Meat(1)
    print(hen)
    print(hen.make_sound())
    hen.feed(veg)
    hen.feed(fruit)
    hen.feed(meat)
    print(hen)