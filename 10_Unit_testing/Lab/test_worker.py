from unittest import TestCase, main
from worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker(name="Test", salary=1700, energy=10)

    def test_uninitialized_correctly(self):
        self.assertEqual(self.worker.name, "Test")
        self.assertEqual(self.worker.salary, 1700)
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)

    def test_increase_energy_after_rest_method(self):
        self.assertEqual(self.worker.energy, 10)
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_word_method_raises(self):
        worker = Worker("Test", 1000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_increase_money_after_work(self):
        self.assertEqual(self.worker.money, 0)
        self.worker.work()
        self.assertEqual(self.worker.money, 1700)

    def test_decrease_energy_after_work_method(self):
        self.assertEqual(self.worker.energy, 10)
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_get_info(self):
        result = self.worker.get_info()
        self.assertEqual(result, f'{self.worker.name} has saved {self.worker.money} money.')


if __name__ == "__main__":
    main()