super() = Function is used to give access to the methods of a parent class.
          It returns a temporay object of a parent class when used
  
  
  
  In Python, super() is a built-in function that provides a way to call methods of a superclass from a subclass.
  It is commonly used in method overriding scenarios to call the overridden method of the superclass.

Heres an example of how super() works in Python:



class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

dog = Dog()
dog.speak()   # Output: Animal speaks \n Dog barks


In the above code, we have defined two classes Animal and Dog. The Animal class has a method called speak() which prints "Animal speaks".
The Dog class inherits from the Animal class and overrides the speak() method with its own implementation that calls the speak() method of
the superclass using the super() function and then prints "Dog barks".

When we create an object of the Dog class and call the speak() method, 
it will print "Animal speaks" first, which is the output of the speak() method of the Animal class called by the super() function, 
followed by "Dog barks", which is the output of the speak() method of the Dog class.

Note that the super() function is used to call the method of the superclass, and it takes no arguments.
By using super(), we can avoid hardcoding the name of the superclass in the code, which makes it easier to maintain and modify the class hierarchy.






HERE WE CAN ALSO USE THE RECEIVED METHOD PROM THE CLASS AND ITS PARAMETERS
___________________________________________________________________


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height
      
      
      
Here we receive the      
      


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())




In the given code, the super() function is used to call the constructor of the superclass (Rectangle) in the subclasses (Square and Cube).

Heres how it works:


class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)



In the Square class, we define an __init__() method that takes two arguments, length and width.
Instead of defining the length and width attributes directly in the Square class,
we inherit them from the Rectangle class by calling the __init__() method of the superclass using the super() function.
This initializes the length and width attributes of the Square object with the values passed to the Square constructor.

Similarly, in the Cube class, the __init__() method calls the __init__() method of the Rectangle class using the super() function to initialize the length 
and width attributes, and also initializes the height attribute:



class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height



The super() function takes no arguments in this case because it automatically refers to the superclass that the current class inherits from (Rectangle in this case).

By calling the constructor of the superclass using super(), we can reuse the code of the superclass,
and also make sure that the superclass is initialized properly before the subclass.
This is important because the superclass may define some attributes or methods that are used by the subclass.

In summary, the super() function is used to call the constructor or method of the superclass in the subclass, 
and it allows us to reuse and extend the code of the superclass.








































































































...
