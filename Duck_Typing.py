 duck typing = concept where the class of an object is less important than the methods/attributes
               class type is not checked if minimum methods/attributes are present
              “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

      
      
      
      
class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

        
class Pigeon:


    def talk(self):
        print("This duck is qwuacking")
        
class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)  // Here we can pass the chicken and duck, because on the chicken class, it has walk and talk methods like a duck
                      // However we can not pass the pigeon class , because it does not have a wlak method, thus it does not wlak or talk like a duck






HERE IS MORE EXPLANATION
____________________________________________________________________________________________________________________________________________________________


Duck typing is a programming concept used in dynamic programming languages such as Python. 
In Python, duck typing refers to the practice of determining whether an object can be used for a particular purpose based on its behavior, 
rather than its class or type. The term "duck typing" comes from the saying, 
"If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

In other words, if an object has the necessary attributes and methods required by a particular piece of code, 
then it can be used in that context, regardless of its type or class. This allows for greater flexibility and code reusability.

For example, in Python, you can define a function that takes a parameter "animal" and checks if it has a "quack" method:

def make_sound(animal):
    animal.quack()



If you pass an object that has a "quack" method, such as a Duck object, it will work as expected.
However, you can also pass an object that is not a Duck object but has a "quack" method, such as a ToyDuck object:


class ToyDuck:
    def quack(self):
        print("Squeak")

toy_duck = ToyDuck()
make_sound(toy_duck)  # prints "Squeak"



In this case, the ToyDuck object is not a Duck object, but it can still be used in the context of the make_sound function because it has a "quack" method.

Overall, duck typing allows for more flexible and dynamic code in Python,
as long as you ensure that the objects you pass to your functions have the necessary attributes and methods.










































































































































































...
