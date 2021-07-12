from vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3


# if __name__ == "__main__":
#     red_car = Car(80, 150)
#     print(Car.DEFAULT_FUEL_CONSUMPTION)
#     print(red_car.fuel)
#     print(red_car.horse_power)
#     print(red_car.fuel_consumption)
#     red_car.drive(20)
#     print(red_car.fuel)
