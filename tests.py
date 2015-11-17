from unittest import TestCase
from mandelbrot import scaled


class Tests(TestCase):
    def testScaling(self):
        self.assertEqual(0, scaled(0, 0, 10, 0, 255))
        self.assertEqual(255, scaled(10, 0, 10, 0, 255))

