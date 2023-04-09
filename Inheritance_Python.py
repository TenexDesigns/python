Inheritance is a powerful feature in object-oriented programming that allows you to define a new class based on an existing class.
The new class inherits the attributes and methods of the existing class, and can also add new attributes and methods or override existing ones.

In Python, you can create a subclass by passing the name of the parent class in parentheses after the subclass name. Here's an example:



class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "woof")

dog = Dog("Fido")
dog.make_sound()  # Output: Fido says woof




In this example, we define a parent class Animal that has an __init__ method to initialize the name and sound attributes, 
as well as a make_sound method that prints out the animal's name and sound.

We then define a subclass Dog that inherits from Animal. 
In the Dog class, we define an __init__ method that calls the super function to initialize the name attribute with
the parent class __init__ method and sets the sound attribute to "woof".
We dont need to define the make_sound method again because it is inherited from the parent class.

We create a new Dog object called Fido and call the make_sound method to print out "Fido says woof".

Subclasses can also override methods of the parent class. For example:





class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")

    def make_sound(self):
        print(f"{self.name} purrs")

cat = Cat("Whiskers")
cat.make_sound()  # Output: Whiskers purrs






In this example, we define a Cat subclass that overrides the make_sound method of the parent class Animal. When we call make_sound on a Cat object, 
it prints out "Whiskers purrs" instead of "Whiskers says meow".

Inheritance allows you to reuse code and create a hierarchy of related classes that share attributes and methods. 
Its a powerful feature of object-oriented programming that can make your code more modular and easier to maintain.
















































































































..
