exception - These are events detected during excution that interept the flow of a program.


In Python, error handling is the process of detecting, handling, and recovering from runtime errors that occur during the execution of a program.
Python provides several mechanisms for error handling, including exceptions, try-except blocks, and finally blocks.

Exceptions are objects that represent an error that occurred during the execution of a program.
When an error occurs, Python raises an exception, which can then be caught and handled by the program.
Heres an example of how to catch and handle an exception:
  
  
  try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("y =", y)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

  
In this example, we use the try statement to enclose the code that might raise an exception. 
If an exception occurs in the try block, Python looks for an appropriate except block to handle the exception. 
In this case, we have two except blocks to handle ValueError and ZeroDivisionError exceptions.

If the code inside the try block executes without raising an exception,
Python skips the except blocks and moves on to the next statement after the try block.






Python also provides a finally block that can be used to specify code that should always be executed, whether or not an exception was raised.
Heres an example:

try:
    f = open("myfile.txt", "r")
    # Do some processing
finally:
    f.close()



In this example, we use the try block to open a file for reading, and then we do some processing with the file.
The finally block ensures that the file is always closed, whether or not an exception was raised.

In addition to using try-except and finally blocks, you can also raise your own exceptions using the raise statement. Here's an example:




def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)





In this example, we define a divide function that raises a ValueError if the second argument is zero.
We then use a try-except block to call the divide function and catch the ValueError if it occurs.
If the exception is caught, we print the error message that was passed to the raise statement.















































..
