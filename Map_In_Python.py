# ---------------------------------------------------------------------------------------------------------------
map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
The structure looks like this

 map(function,iterable)

  
  
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)  // We use this to access the price column in the stor and change the price
# to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)
# ---------------------------------------------------------------------------------------------------------------









HERE IS MORE EXPLANATION
____________________________________________________________________________________________________________________________________________________________

In Python, map() is a built-in higher-order function that applies a given function to each element of an iterable and returns an iterator of the results.
The syntax for using the map() function is as follows:


map(function, iterable)


where function is the function to be applied to each element of the iterable, and iterable is the collection of elements to be mapped.

Heres an example of using the map() function in Python:


# Defining a function to be applied to each element
def square(x):
    return x ** 2

# Using map() to apply the function to each element of a list
my_list = [1, 2, 3, 4, 5]
result = map(square, my_list)

# Converting the result iterator to a list
result_list = list(result)

# Printing the result
print(result_list)  # Output: [1, 4, 9, 16, 25]






In this example, we define a function square() that takes a number and returns its square.
We then use the map() function to apply the square() function to each element of the list my_list.
The result is an iterator, which we convert to a list using the list() function. Finally, we print the resulting list.

We can also use lambda functions with map() to avoid defining a separate function. Here's an example:


# Using lambda function with map()
my_list = [1, 2, 3, 4, 5]
result = map(lambda x: x ** 2, my_list)

# Converting the result iterator to a list
result_list = list(result)

# Printing the result
print(result_list)  # Output: [1, 4, 9, 16, 25]



In this example, we use a lambda function to define the function to be applied to each element of the list.
The lambda function takes a number x and returns its square. We then use the map() function as before, and the result is the same.

Another example of using the map() function is to apply a function to each element of multiple lists simultaneously:


 # Using map() with multiple iterables
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
result = map(lambda x, y: x + y, list1, list2)

# Converting the result iterator to a list
result_list = list(result)

# Printing the result
print(result_list)  # Output: [6, 8, 10, 12]



In this example, we use the map() function to apply a lambda function that adds the corresponding elements of two lists list1 and list2. 
The resulting iterator contains the sum of the elements at each index.











































































































...
