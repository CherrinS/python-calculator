import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add1(self):
        self.assertEqual(self.calc.add(3, 1), 4)
    
    def test_add2(self):
        self.assertEqual(self.calc.add(5, 6), 11)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(5, 6), -1)
    
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(7, 8), -1)

    def test_multipy1(self):
        self.assertEqual(self.calc.multiply(0, 4), 0)

    def test_multipy2(self):
        self.assertEqual(self.calc.multiply(3, -2), -6)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
    
    def test_divide2(self):
        self.assertEqual(self.calc.divide(20, 5), 4)
    
    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(11, 5), 1)
    
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(12, 5), 2)
    

if __name__ == '__main__':
    unittest.main()
