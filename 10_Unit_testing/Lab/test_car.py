from car import Car
from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self) -> None:
        self.car = Car(make="Test", model="Test Model", fuel_consumption=10, fuel_capacity=100)

    def test_initialize_attributes_correctly(self):
        self.assertEqual("Test", self.car.make)
        self.assertEqual("Test Model", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_make_with_null_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_car_model_with_null_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -2
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_correct_data(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_with_negative_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.car.refuel(25)
        self.car.drive(10)
        self.assertEqual(24, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(250)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
