In Python, a class is a blueprint for creating objects.
It defines a set of attributes and methods that the objects of that class will have.
Heres an example of a simple class definition in Python:



    Note -> Class variables are defined outside the constructor and are normary given a default value that is applied to all instances of created of the class
         -> Instance variables are created inside the constructor and normary get their vaue from paramtrs received by the constructor.
    

class Person:
    
    race = "human"  ---> Classs variable 
    
    def __init__(self, name, age):
        self.name = name   ---> Instance variable
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")




In this example, we define a class called Person that has two attributes (name and age) and one method (say_hello). 
The __init__ method is a special method that is called when a new object is created.
It initializes the attributes of the object with the values passed to the constructor.

We create a new Person object called person1 by calling the class like a function and passing in the arguments for the __init__ method:



person1 = Person("Alice", 30)



We can access the attributes of the object using the dot notation:


print(person1.name)  # Output: Alice
print(person1.age)  # Output: 30



We can call the object's methods using the dot notation as well:



person1.say_hello()  # Output: Hello, my name is Alice and I am 30 years old.


Classes in Python can also inherit from other classes.
Inheritance allows a subclass to inherit attributes and methods from a parent class, and to add its own attributes and methods as well. 
Heres an example:


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def say_hello(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}.")




In this example, we define a subclass of Person called Student.
It has an additional attribute called student_id, and it overrides the say_hello method of the Person class to include the student ID in the output. 
The super() function is used to call the __init__ method of the parent class and initialize the name and age attributes.

We can create a new Student object in the same way we create a Person object, passing in the additional argument for the student_id attribute:


student1 = Student("Bob", 20, 12345)



We can access the attributes and methods of the parent class using the same dot notation as before:


print(student1.name)  # Output: Bob
print(student1.age)  # Output: 20
student1.say_hello()  # Output: Hello, my name is Bob, I am 20 years old, and my student ID is 12345.



And we can access the new attribute and method of the subclass using the dot notation as well:

print(student1.student_id)  # Output: 12345














































































































































































....
