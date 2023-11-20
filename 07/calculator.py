import unittest

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Can not divide by zero!")
    return x / y

def data_provider_add():
    return [
        (10, 5, 15),
        (-1, 1, 0),
        (-1, -1, -2),
    ]

def data_provider_subtract():
    return [
        (10, 5, 5),
        (-1, 1, -2),
        (-1, -1, 0),
    ]

def data_provider_multiply():
    return [
        (10, 5, 50),
        (-1, 1, -1),
        (-1, -1, 1),
    ]

def data_provider_divide():
    return [
        (10, 5, 2),
        (-1, 1, -1),
        (-1, -1, 1),
        (5, 2, 2.5),
        (5, 0, 0)
    ]


class TestCalculator(unittest.TestCase):

    def test_add(self):
        for x, y, expected in data_provider_add():
            self.assertEqual(add(x, y), expected)

    def test_subtract(self):
        for x, y, expected in data_provider_subtract():
            self.assertEqual(subtract(x, y), expected)

    def test_multiply(self):
        for x, y, expected in data_provider_multiply():
            self.assertEqual(multiply(x, y), expected)

    def test_divide(self):
        for x, y, expected in data_provider_divide():
            if y == 0:
                with self.assertRaises(ValueError):
                    divide(x, y)
            else:
                self.assertEqual(divide(x, y), expected)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            multiply('a', 'b')
        with self.assertRaises(TypeError):
            divide('a', 'b')

if __name__ == '__main__':
    unittest.main()