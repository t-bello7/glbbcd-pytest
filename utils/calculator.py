## Creating the Blue Print of the calculator

## Attributes of the calculator
# -- The numeric numbers 

## Methods
# -- the arithmetic symbols 

class Calculator:
    def __init__(self, numA, numB):
        self.numA = numA
        self.numB = numB
        self.add = lambda numA, numB: numA + numB 
    
    def addition(self):
        return self.numA + self.numB

    def subtraction(self):
        return self.numA - self.numB

    def multiplication(self):
        return self.numA * self.numB

    def division(self):
        return self.numA / self.numB


# kazzimsCalc = Calculator(4,0)
# print(kazzimsCalc.division()) ## Same stuff
# print(Calculator.division(kazzimsCalc)) ## Same stuff
# print(kazzimsCalc.numA)
# print(kazzimsCalc.addition())
# print(kazzimsCalc.multiplication())
# print(kazzimsCalc.subtraction())
# print(kazzimsCalc.division())
