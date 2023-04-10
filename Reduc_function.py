reduce ()  - Used to apply a function to an iterable and reduce it to a single cumulative value.
            performs function on the first two elemets and repeats the process to all other elemnts until 1 value remains
  
  
  
  The strunctire
  
  
  
  
  reduce (function, iterable)
  
  
  
  HERE IS AN EXAMPLE


mport functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y,:x * y,factorial)
print(result)



HERE IS MORE EXPLANATION
____________________________________________________________________________________________________________________________________________________


In Python, reduce() is a built-in higher-order function from the functools module that applies a binary function to the elements of an
iterable in a cumulative way.
The syntax for using the reduce() function is as follows:
  
  reduce(function, iterable[, initial])

where function is the function to be applied to the elements of the iterable, iterable is the collection of elements to be reduced,
and initial is an optional initial value to start the cumulative computation.

Heres an example of using the reduce() function in Python:

from functools import reduce

# Defining a function to be used with reduce
def add(x, y):
    return x + y

# Using reduce() to apply the function cumulatively to the elements of a list
my_list = [1, 2, 3, 4, 5]
result = reduce(add, my_list)

# Printing the result
print(result)  # Output: 15


In this example, we define a function add() that takes two numbers and returns their sum.
We then use the reduce() function to apply the add() function to the elements of the list my_list in a cumulative way. 
The result is the sum of all the elements in the list.

We can also use lambda functions with reduce() to avoid defining a separate function. Here's an example:


from functools import reduce

# Using lambda function with reduce()
my_list = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, my_list)

# Printing the result
print(result)  # Output: 15


In this example, we use a lambda function to define the binary function to be applied to the elements of the list.
The lambda function takes two numbers x and y and returns their sum. We then use the reduce() function as before, and the result is the same.

Another example of using the reduce() function is to find the maximum element in a list:



from functools import reduce

# Using reduce() to find the maximum element in a list
my_list = [1, 4, 2, 5, 3]
result = reduce(lambda x, y: x if x > y else y, my_list)

# Printing the result
print(result)  # Output: 5


In this example, we use a lambda function to define the binary function to be applied to the elements of the list.
The lambda function takes two numbers x and y and returns the larger of the two. We then use the reduce() function to
apply the lambda function to the elements of the list cumulatively and find the maximum element.

Note that the reduce() function is not built-in to Python 3.x, but is available in the functools module, so we need to import it before using it.







































































..
