 y tho?
 1. Module can be run as a standalone program
    or
 2. Module can be imported and used by other modules

  Python interpreter sets "special variables", one of which is _name_
  Python will assign the _name_ variable a value of '__main__' if it's
  the initial module being run





if __name__ == '__main__' is a common line of code you may see at the bottom of a Python script.
It is used to separate the code that should be executed when the script is run directly from the code that should be executed when the script is 
imported as a module into another script.

When a Python script is run directly, the special variable __name__ is set to the string '__main__'. 
However, when a script is imported as a module into another script, __name__ is set to the name of the module.

By using if __name__ == '__main__', you can ensure that the code within that block will only be executed if the script is run directly. 
This is useful for writing code that can be used as a standalone script or as a module in another script.

Heres an example to illustrate how it works:

  
  # my_script.py

def my_function():
    print("Hello, world!")

if __name__ == '__main__':
    my_function()




In this example, the my_function() function is defined at the top of the script. The if __name__ == '__main__' block at 
the bottom ensures that my_function() is only called if my_script.py is run directly.
If my_script.py is imported as a module into another script, my_function() will not be called automatically.
























































































































...
