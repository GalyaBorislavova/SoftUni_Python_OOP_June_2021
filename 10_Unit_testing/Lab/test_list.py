from list import IntegerList
from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.list = IntegerList(5, 7, 16, 10, 12, 8)

    def test_constructor_with_correct_data(self):
        self.assertEqual(self.list._IntegerList__data, [5, 7, 16, 10, 12, 8])

    def test_constructor_with_incorrect_data(self):
        example_list = IntegerList(5, 7.2, 16, 10.1, 12, 8)
        self.assertEqual(example_list._IntegerList__data, [5, 16, 12, 8])

    def test_add_method_with_int_number(self):
        self.assertEqual(self.list._IntegerList__data, [5, 7, 16, 10, 12, 8])
        result = self.list.add(100)
        self.assertEqual(self.list._IntegerList__data, [5, 7, 16, 10, 12, 8, 100])
        self.assertEqual(result, [5, 7, 16, 10, 12, 8, 100])

    def test_add_method_with_incorrect_number_raises(self):
        self.assertEqual(self.list._IntegerList__data, [5, 7, 16, 10, 12, 8])
        with self.assertRaises(ValueError) as ex:
            self.list.add("100")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_method_with_correct_index(self):
        result = self.list.remove_index(0)
        self.assertEqual(5, result)
        self.assertEqual(self.list._IntegerList__data, [7, 16, 10, 12, 8])

    def test_remove_index_method_with_incorrect_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_method_with_correct_index(self):
        result = self.list.get(1)
        self.assertEqual(result, 7)
        self.assertEqual(self.list._IntegerList__data, [5, 7, 16, 10, 12, 8])

    def test_get_method_with_incorrect_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list.get(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_with_incorrect_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list.insert(10, "100")
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_with_string_number_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.list.insert(3, "100")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_method_with_correct_data(self):
        self.list.insert(0, 100)
        self.assertEqual(self.list.get_data(), [100, 5, 7, 16, 10, 12, 8])

    def test_get_biggest_method(self):
        result = self.list.get_biggest()
        self.assertEqual(result, 16)

    def test_get_index_method(self):
        result = self.list.get_index(5)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    main()