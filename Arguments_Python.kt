positional, default,keyword and *arg and **kwargs arguments in python


In Python, functions can have different types of arguments. Here are some of the most common ones:



Positional arguments: These are the most basic type of argument and are specified by their position in the function call.
When you call a function with positional arguments, the first argument corresponds to the first parameter, the second argument to the second parameter, and so on.



def greet(name, message):
    print(f"{message}, {name}!")

greet("John", "Hello") # Output: Hello, John!




Default arguments: These are arguments that have a default value specified in the function definition.
If a value is not provided for a default argument in the function call, the default value is used instead.


def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("John") # Output: Hello, John!
greet("John", "Hi") # Output: Hi, John!





Keyword arguments: These are arguments that are specified by their name in the function call.
Keyword arguments allow you to specify arguments in any order, and to provide default values for some arguments while specifying others explicitly.


def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet(message="Hi", name="John") # Output: Hi, John!





*args arguments: These are used to pass a variable number of positional arguments to a function. 
The *args syntax allows you to pass any number of arguments to the function, which are collected into a tuple.
You have to include the unpacking operator(*) to make an args , Then you can give the args any name , as long as there is an unpacking oprarrotr.
args means arguments.

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

result = add(1, 2, 3, 4)
print(result) # Output: 10



**kwargs arguments: These are used to pass a variable number of keyword arguments to a function.
The **kwargs syntax allows you to pass any number of keyword arguments to the function, which are collected into a dictionary.
You have to include the unpacking operator(*) to make an kwargs , Then you can give the kwargs any name , as long as there is an unpacking oprarrotr.
Kwargs meas key word argumends 

def greet(**kwargs):
    name = kwargs.get("name", "World")
    message = kwargs.get("message", "Hello")
    print(f"{message}, {name}!")

greet() # Output: Hello, World!
greet(name="John", message="Hi") # Output: Hi, John!




Note that *args and **kwargs should always be the
last arguments in the function definition, as they collect any remaining arguments after all other positional and keyword arguments have been processed.


























































































..
