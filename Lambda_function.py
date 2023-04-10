 lambda function = function written in 1 line using lambda keyword
                   accepts any number of arguments, but only has one expression.
                   (think of it as a shortcut)
                   (useful if needed for a short period of time, throw-away)
        
        
        
        This is their structure

        lambda parameters:expression


HERE IS AN EXAMPLE

This function can be written in one line using a  lambda function
def double (x):
  return x*2


This is the lambda function

double = lambda x: x * 2
print(double(1))




HERE IS MORE EXPLANTION
____________________________________________________________________________________________________________________


In Python, a lambda function is a small, anonymous function that can be defined without a name. 
Lambda functions are also known as anonymous functions or function literals.

Lambda functions are defined using the lambda keyword, followed by the functions arguments, a colon, and the function's body. Here's an example:



multiply = lambda x, y: x * y

result = multiply(3, 4)
print(result)  # prints 12




In this example, a lambda function is defined using the lambda keyword and assigned to the variable multiply. 
The lambda function takes two arguments (x and y) and returns their product (x * y). 
The lambda function is then called with the arguments 3 and 4, and the result (12) is printed to the console.

Lambda functions are often used when a function is needed for a short period of time and does not need to be defined with a specific name. 
They can be passed as arguments to other functions or used in list comprehensions and other functional programming techniques.

Heres an example of using a lambda function in a list comprehension:


numbers = [1, 2, 3, 4, 5]

squared_numbers = [lambda x: x ** 2 for x in numbers]

result = squared_numbers[2](3)
print(result)  # prints 9





In this example, a lambda function is defined inside a list comprehension that creates a list of lambda functions that square their input.
The squared_numbers list contains five lambda functions that square their input.

Finally, the third element of the squared_numbers list (which is the lambda function that squares 3) is called with the argument 3.
The result (9) is printed to the console.











































































































...
