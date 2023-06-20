import unittest
from fields import rectangle, triangle, trapezoid

class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 5
        self.h = 5

    def test_rectangle_with_correct_values(self):
        result = rectangle(self.a, self.b)
        self.assertEqual(result, 50)

    def test_rectangle_with_incorrect_values(self):
        # self.assertRaises(ValueError, rectangle, True, "sting")
        with self.assertRaises(ValueError):
            rectangle(self.a, "incorrect value")

    def test_triangle_with_correct_values(self):
        result = triangle(self.a, self.b)
        self.assertEqual(result, 25)

    def test_triagle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            triangle(self.a, "incorrect value")

    def test_trapezoid_with_correct_values(self):
        result = trapezoid(self.a, self.b, self.h)
        expected_result = 37.5
        self.assertEqual(result, expected_result)

    def test_trpezoid_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            trapezoid(self.a, self.b, "incorrect value")

    def tearDown(self):
        del self.a
        del self.b


if __name__ == '__main__':
    unittest.main()