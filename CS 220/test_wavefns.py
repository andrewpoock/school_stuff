# test_wavefns.py

import unittest
from math import pi, tau
from wavefns import trianglewave

class TestWaves(unittest.TestCase):

    def testTriangleWave(self):

        self.assertAlmostEqual(trianglewave(0.0), 0)
        self.assertAlmostEqual(trianglewave(pi/2), 1)
        self.assertAlmostEqual(trianglewave(pi/4), .5)
        self.assertAlmostEqual(trianglewave(pi), 0)
        self.assertAlmostEqual(trianglewave(3*pi/2), -1)
        self.assertAlmostEqual(trianglewave(0.0 + tau), 0)
        self.assertAlmostEqual(trianglewave(pi/2 + tau), 1)
        self.assertAlmostEqual(trianglewave(pi/4 + tau), .5)
        self.assertAlmostEqual(trianglewave(pi + tau), 0)
        self.assertAlmostEqual(trianglewave(3*pi/2 + tau), -1)

if __name__ == '__main__':
    unittest.main()
