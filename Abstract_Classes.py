abstract class = a class which contains one or more abstract methods.
abstract method = a method that has a declaration but does not have an implementation.

 prevents a user from creating an object of that class
 compels a user to override abstract methods in a child class





from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()  -Not allowd as you can not instanciate a abstract class
car = Car()
motorcycle = Motorcycle()

#vehicle.go()  // Not allowed as you can not instance an abstract method as it has not been implemented
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()







Here is more Explanation
_____________________________________________________________________________________________

Python abstract classes are classes that cannot be instantiated directly. 
Instead, they are designed to be inherited by other classes that provide concrete implementations for their abstract methods. 
Abstract classes are typically used to define a common interface for a group of related classes, without implementing any specific behavior.

In Python, we can create an abstract class by importing the abc module and using the ABC (Abstract Base Class) class as a base class for our abstract class.
Heres an example:


import abc

class MyAbstractClass(abc.ABC):

    @abc.abstractmethod
    def my_abstract_method(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def my_static_abstract_method():
        pass





In this example, we define an abstract class called MyAbstractClass that inherits from abc.ABC.
We also define two abstract methods using the @abc.abstractmethod decorator: my_abstract_method() and my_static_abstract_method().
  These methods have no implementation and raise a TypeError if called.

To implement an abstract class, we create a subclass that provides concrete implementations for all the abstract methods. Here's an example:


class MyClass(MyAbstractClass):

    def my_abstract_method(self):
        print("Hello, abstract method!")

    @staticmethod
    def my_static_abstract_method():
        print("Hello, static abstract method!")




In this example, we define a subclass called MyClass that inherits from MyAbstractClass and provides implementations
for the abstract methods my_abstract_method() and my_static_abstract_method().

Note that if we try to instantiate MyAbstractClass, Python will raise a TypeError:


>>> my_abstract_class = MyAbstractClass()
TypeError: Cant instantiate abstract class MyAbstractClass with abstract methods my_abstract_method, my_static_abstract_method




This is because MyAbstractClass is an abstract class and cannot be instantiated directly. 
We need to create a concrete subclass that provides implementations for its abstract methods in order to create an instance of the class.

In summary, Python abstract classes are used to define a common interface for a group of related classes, without implementing any specific behavior.
They are defined using the abc.ABC class and the @abc.abstractmethod decorator,
and can only be instantiated through a concrete subclass that provides implementations for all their abstract methods.




in the above context , what does   @staticmethod mean and how is it used
_______________________________________________________________________________________________________________

In the given context, @staticmethod is a decorator applied to a method to indicate that it is a static method.
A static method is a method that belongs to the class and not to the instance of the class.
It can be called on the class itself without the need for an instance of the class.

Heres an example:

class MyAbstractClass(abc.ABC):

    @abc.abstractmethod
    def my_abstract_method(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def my_static_abstract_method():
        pass



In this example, we define a static method called my_static_abstract_method() using the @staticmethod decorator. 
This method does not take a self parameter, which means it does not operate on the instance of the class.
Instead, it operates on the class itself, and can be called on the class directly without creating an instance.

Heres an example of how to call a static method:

  MyAbstractClass.my_static_abstract_method()


In this example, we call the static method my_static_abstract_method() on the MyAbstractClass class itself, without creating an instance of the class.

In summary, @staticmethod is a decorator that indicates that a method is a static method. Static methods belong to the class and not to the instance of the class,
and can be called on the class directly without the need for an instance.
They are useful for defining methods that operate on the class as a whole, rather than on individual instances.















































..
