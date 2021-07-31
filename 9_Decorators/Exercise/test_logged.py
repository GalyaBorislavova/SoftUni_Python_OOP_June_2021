from logged import logged

import unittest


class LoggedTests(unittest.TestCase):
    def test_zero(self):
        @logged
        def func(*args):
            return 3 + len(args)
        result = func(4, 4, 4)
        self.assertEqual(result, 'you called func(4, 4, 4)\nit returned 6')


if __name__ == '__main__':
    unittest.main()