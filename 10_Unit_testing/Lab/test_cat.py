from cat import Cat
from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Daria")

    def test_uninitialized_correctly(self):
        self.assertEqual(self.cat.name, "Daria")
        self.assertEqual(self.cat.fed, False)
        self.assertEqual(self.cat.sleepy, False)
        self.assertEqual(self.cat.size, 0)

    def test_increase_size_after_eat(self):
        self.assertEqual(self.cat.size, 0)
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_is_fed_after_eat(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat_method_raises(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_togo_bed_hungry(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry',  str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()