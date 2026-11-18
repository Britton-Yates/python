import unittest
from area import *

class testspace(unittest.TestCase):
    def tests(self):
        #circletests
        self.assertRaises(ValueError, circle, 'x')
        self.assertRaises(TypeError, circle, -1)
        self.assertRaises(TypeError, circle, 0)
        self.assertAlmostEqual(circle(1), 3.14, delta = 0.01)
        self.assertAlmostEqual(circle(1.0), 3.14, delta = 0.01)
        #squaretests
        self.assertRaises(ValueError, square, 'x')
        self.assertRaises(TypeError, square, -1)
        self.assertRaises(TypeError, square, 0)
        self.assertEqual(square(1), 1)
        self.assetAlmostEqual(square(1.5), 2.25)
        #rectangletests
        self.assertRaises(ValueError, rectangle, 'x', 1)
        self.assertRaises(TypeError, rectangle, -1, 1)
        self.assertRaises(TypeError, rectangle, 0, 1)
        self.assertEqual(rectangle(1, 2), 2)
        self.assetAlmostEqual(rectangle(1.5, 2), 3.0)
        #triangletests
        self.assertRaises(ValueError, triangle, 'x', 1)
        self.assertRaises(TypeError, triangle, -1, 1)
        self.assertRaises(TypeError, triangle, 0, 1)
        self.assertEqual(triangle(1, 2), 1)
        self.assetAlmostEqual(triangle(1.5, 2), 1.5)
