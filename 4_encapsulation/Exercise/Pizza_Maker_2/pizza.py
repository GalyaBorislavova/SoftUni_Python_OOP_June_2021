from Pizza_Maker_2.dough import Dough
from Pizza_Maker_2.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, new_topping: Topping):
        if self.toppings_capacity > len(self.toppings):
            if new_topping.topping_type not in self.toppings:
                self.toppings[new_topping.topping_type] = new_topping.weight
            else:
                self.toppings[new_topping.topping_type] += new_topping.weight
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        toppings_weight = sum(map(lambda topping: topping, self.toppings.values()))
        return self.dough.weight + toppings_weight


if __name__ == "__main__":
    from Hotel_room_4.dough import Dough
    # from Hotel_room_4.pizza import Pizza
    from Hotel_room_4.topping import Topping

    tomato_topping = Topping("Tomato", 60)
    print(tomato_topping.topping_type)
    print(tomato_topping.weight)

    mushrooms_topping = Topping("Mushroom", 75)
    print(mushrooms_topping.topping_type)
    print(mushrooms_topping.weight)

    mozzarella_topping = Topping("Mozzarella", 80)
    print(mozzarella_topping.topping_type)
    print(mozzarella_topping.weight)

    cheddar_topping = Topping("Cheddar", 150)

    pepperoni_topping = Topping("Pepperoni", 120)

    white_flour_dough = Dough("White Flour", "Mixing", 200)
    print(white_flour_dough.flour_type)
    print(white_flour_dough.weight)
    print(white_flour_dough.baking_technique)
    whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
    print(whole_wheat_dough.weight)
    print(whole_wheat_dough.flour_type)
    print(whole_wheat_dough.baking_technique)

    p = Pizza("Margherita", whole_wheat_dough, 2)

    p.add_topping(tomato_topping)
    print(p.calculate_total_weight())

    p.add_topping(mozzarella_topping)
    print(p.calculate_total_weight())

    p.add_topping(mozzarella_topping)
