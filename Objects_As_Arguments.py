class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle,color):

    vehicle.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1,"red")
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(bike_1,"black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)




Here is more explanation
______________________________________________________________________________________________________________________________________________________________

In Python, objects can be passed as arguments to functions just like any other data type such as integers, strings, or lists.
When an object is passed as an argument, the function receives a reference to the object, not a copy of the object itself.
This means that any changes made to the object within the function will affect the original object outside the function.

Heres an example:

  
  def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]


In this example, the modify_list() function takes a list as an argument, appends the value 4 to the list, and returns nothing.
The original list passed as an argument is modified because it is a mutable object.

Its important to note that when passing immutable objects like strings or integers, the original object cannot be modified within the function.
Instead, a new object with the modified value can be returned from the function.



def increment(num):
    return num + 1

x = 5
y = increment(x)
print(x)  # Output: 5
print(y)  # Output: 6


In this example, the increment() function takes an integer as an argument, adds 1 to it, and returns the new value.
The original integer x is not modified because integers are immutable objects.


















































































































..
