from typing import ClassVar


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25

    def __init__(self, fuel: float, horse_power: int) -> None:
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        if kilometers * self.fuel_consumption <= self.fuel:
            self.fuel -= self.fuel_consumption * kilometers


# if __name__ == "__main__":
#     from project.family_car import FamilyCar
#     vehicle = Vehicle(50, 150)
#     print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
#     print(vehicle.fuel)
#     print(vehicle.horse_power)
#     print(vehicle.fuel_consumption)
#     vehicle.drive(100)
#     print(vehicle.fuel)
#     family_car = FamilyCar(150, 150)
#     family_car.drive(50)
#     print(family_car.fuel)
#     family_car.drive(50)
#     print(family_car.fuel)
#     print(family_car.__class__.__bases__[0].__name__)
