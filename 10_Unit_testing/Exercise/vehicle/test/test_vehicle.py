from unittest import TestCase

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 350)

    def test_init_method(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(350, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        kilometers = 20
        self.vehicle.drive(kilometers)
        result = self.vehicle.fuel_consumption * kilometers
        self.assertEqual(result, self.vehicle.fuel)

    def test_drive_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_correct_amount_of_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)
        self.vehicle.refuel(10)
        self.assertEqual(47.5, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        result = str(self.vehicle)
        self.assertEqual(f"The vehicle has 350 horse power with 50 fuel left and 1.25 fuel consumption", result)