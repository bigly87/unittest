import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        #result = calc.add(10, 5)
        self.assertAlmostEqual(calc.add(10, 5), 15)
        self.assertAlmostEqual(calc.add(-1, 1), 0)
        self.assertAlmostEqual(calc.add(-1, -1), -2)
    
    def test_substract(self):
        self.assertAlmostEqual(calc.substract(10, 5), 5)
        self.assertAlmostEqual(calc.substract(-1, 1), -2)
        self.assertAlmostEqual(calc.substract(-1, -1), 0)

    def test_multiply(self):
        self.assertAlmostEqual(calc.multiply(10, 5), 50)
        self.assertAlmostEqual(calc.multiply(-1, 1), -1)
        self.assertAlmostEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertAlmostEqual(calc.devide(10, 5), 2)
        self.assertAlmostEqual(calc.devide(-1, 1), -1)
        self.assertAlmostEqual(calc.devide(-1, -1), 1)
        self.assertAlmostEqual(calc.devide(5, 2), 2.5)










if __name__ == "__main__":
    unittest.main()