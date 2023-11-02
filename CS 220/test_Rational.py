# test_Rational.py
# unittest example

import unittest
from rational import Rational


class RationalTest(unittest.TestCase):
       
    def testConstructorOneInt(self):

        r = Rational(-3)
        self.assertEqual(str(r), '-3/1')
       
    def testConstructorTwoInt(self):

        r = Rational(3, 4)
        self.assertEqual(str(r), '3/4')

    def testMul(self):

        r1 = Rational(2, 3)
        r2 = Rational(3, 4)
        r3 = r1 * r2
        self.assertEqual(str(r3), '1/2')

    def testAdd(self):
        r1 = Rational(2, 3)
        r2 = Rational(3, 4)
        r3 = r1 + r2
        self.assertEqual(str(r3), '17/12')


if __name__ == '__main__':
    unittest.main()
