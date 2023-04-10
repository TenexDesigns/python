Method chaining - This is calling multiple methods sequentially.
                 Each call performs an action on the same object and returns self
  
  
  
  Note-> You have to return self on all methods that are to be method-chaine
This is because self refers to the wholle class i.e car and when the method chaining is occcuring e.g Car.tunon() then self will come here(car/self).drive
  
  
class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

 car.turn_on().drive()
 car.brake().turn_off()
 car.turn_on().drive().brake().turn_off()




HERE IS MORE EXPLANATION
___________________________________________________________________________________________

Method chaining in Python is a programming technique that involves calling multiple methods on the same object in a single statement.
It allows for concise and readable code by reducing the amount of boilerplate code required to perform a series of operations on an object.

Heres an example of how method chaining works in Python:

class Calculator:
    def __init__(self, number):
        self.number = number

    def add(self, value):
        self.number += value
        return self

    def subtract(self, value):
        self.number -= value
        return self

    def multiply(self, value):
        self.number *= value
        return self

    def divide(self, value):
        self.number /= value
        return self

calculator = Calculator(10)
result = calculator.add(5).subtract(3).multiply(2).divide(4).number
print(result)   # Output: 3.0



In the above code, we have defined a class Calculator with four methods: add(), subtract(), multiply(),
  and divide(). Each of these methods performs a mathematical operation on the number attribute of the Calculator object and returns the object itself. 
  This allows us to chain multiple method calls together in a single statement.

When we create an object of the Calculator class and chain together a series of method calls, the final value of the number attribute is returned as the result.
In the above example, the starting value is 10, and we add 5, subtract 3, multiply by 2, and divide by 4, resulting in a final value of 3.0.















































































































































































...
