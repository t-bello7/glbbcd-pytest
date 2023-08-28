from unittest import TestCase
from calculator import Calculator

class CalculatorTest(TestCase):
    def test(self):
        self.assertTrue(True)
    def test_failing(self):
        self.assertTrue(False)

    def test_calculator_values_int(self):
        calculatorr = Calculator(4, 5) #arrange
        int_datatype = type(calculatorr.numA) #acted

        self.assertTrue(int_datatype == int)
        # if the value is going to the class
        # if the class exists
        # zeroDivisionError
        # value passed are integers
        # check if operations returns correct values
        # 