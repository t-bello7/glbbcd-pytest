from utils.calculator import Calculator
# from calculator import *

# import utils.calculator.Calculator as thisdd
# import calculator 

# import calculator as myOwnCalculator
# Funcitonal programming
# print(thisdd)
kazzimsCalc = Calculator(4,0)
try:
    print(kazzimsCalc.division()) ## Same stuff
except ZeroDivisionError:
    print("We caught an error")
# print(Calculator.division(kazzimsCalc)) ## Same stuff
# print(kazzimsCalc.numA)
# print(kazzimsCalc.addition())
# print(kazzimsCalc.multiplication())
# print(kazzimsCalc.subtraction())
# print(kazzimsCalc.division())













def turnLeft():
    return 'We are moving left'

def turnRight():
    return 'We are moving right'

# Object Oriented Programming
#-->> The car

## --> Attributes/ Properties of the car
# color
# plate number
# brand
# number of wheels


## --> Methods of the car
## Turn left
## 
class Car:
    def __init__(self, color, plate_number, brand, no_of_wheels):
        self.color = color
        self.plate_number = plate_number
        self.brand = brand
        self.no_of_wheels = no_of_wheels
    def print_no_wheels(self):
        print(self.no_of_wheels)

    def drive(self):
        print('The car is moving forward')
    def play_music(self):
        print('The car is an mp3 player')

mrAdolfCar = Car('ash',3422, 'toyota', 4 )
# tomiCar = Car('red', **32, 'Lamboghini',6)

# list_of_cars = [mrAdolfCar, tomiCar]
print(mrAdolfCar.print_no_wheels())

# Importing the calculator in the car file
