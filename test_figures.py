import unittest
import math

from circle import area as circle_area
from circle import perimeter as circle_perimeter

from rectangle import area as rectangle_area
from rectangle import perimeter as rectangle_perimeter

from square import area as square_area
from square import perimeter as square_perimeter

from triangle import area as triangle_area
from triangle import perimeter as triangle_perimeter


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(circle_area(4), math.pi * 16)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(4), 2 * math.pi * 4)

    def test_zero_radius(self):
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_perimeter(0), 0)


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(rectangle_area(4, 9), 36)

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(4, 9), 26)

    def test_zero_side(self):
        self.assertEqual(rectangle_area(10, 0), 0)
        self.assertEqual(rectangle_perimeter(10, 0), 20)


class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(square_area(8), 64)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(8), 32)

    def test_zero_side(self):
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_perimeter(0), 0)


class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(triangle_area(5, 2), 5)

    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 3, 5), 11)

    def test_zero_base(self):
        self.assertEqual(triangle_area(0, 5), 0)

    def test_zero_sides(self):
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)


if __name__ == "__main__":
    unittest.main()
