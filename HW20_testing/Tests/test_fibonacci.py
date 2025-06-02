import unittest
from HW20_testing.utils import Fibonacci


# class TestFibonacci(unittest.TestCase):
#     fibonacci = Fibonacci()
#
#     def test_fibonacci_valid(self):
#         self.assertEqual(self.fibonacci(100), 354224848179261915075)
#
#     def test_fibonacci_0(self):
#         self.assertEqual(self.fibonacci(0), 0, 'Test value = 0')
#
#     def test_fibonacci_1(self):
#         self.assertEqual(self.fibonacci(1), 1, 'Test value = 1')
#
#     def test_fibonacci_negative(self):
#         with self.assertRaises(ValueError):
#             self.fibonacci(-1)
#
#     def test_fibonacci_wrong_value(self):
#         with self.assertRaises(ValueError):
#             self.fibonacci(str)


class TestFinabocciV1(unittest.TestCase):
    fibonacci = Fibonacci()

    def test_fibonacci_valid(self):
        valid_values = [
            (0, 0, 'value = 0'),
            (1, 1, 'value = 1'),
            (2, 1, 'value = 2'),
            (3, 2, 'value = 3'),
            (100, 354224848179261915075, 'value = 100')
        ]
        for value, expected_result, msg in valid_values:
            self.assertEqual(self.fibonacci(value), expected_result, msg=msg)

    def test_fibonacci_invalid_type(self):
        invalid_values = ['string', [], {}, None, 1.0, -1.5, 2.5]
        for value in invalid_values:
            with self.assertRaises(ValueError):
                self.fibonacci(value)


if __name__ == "__main__":
    unittest.main()
