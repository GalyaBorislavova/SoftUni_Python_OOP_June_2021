from car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10


# if __name__ == "__main__":
#     sport_car = SportCar(200, 450)
#     sport_car.drive(50)
#     print(sport_car.fuel)
#     sport_car.drive(5)
#     print(sport_car.fuel)
#     print(sport_car.__class__.__bases__[0].__name__)