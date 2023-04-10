
list comprehension =  a way to create a new list with less syntax
                       can mimic certain lambda functions, easier to read
                       list = [expression for item in iterable]
                       list = [expression for item in iterable if conditional]
                       list = [expression if/else for item in iterable]
 --------------------------------------------------------------
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)    # define what each loop iteration should do
print(squares)

# create a list AND defines what each loop iteration should do
1. list = [expression for item in iterable]
           Here is an example.
           
           
squares = [i * i for i in range(1,11)]
print(squares)







HERE IS MORE EXPLANATION
_________________________________________________________________________________________________________________________________________

In Python, list comprehension is a concise and elegant way to create a new list by iterating over an existing iterable (e.g., list, tuple, set, dictionary, etc.)
and applying a condition on its elements.

The basic syntax for list comprehension in Python is as follows:

new_list = [expression for item in iterable if condition]

where expression is an expression to be applied to each item in the iterable, item is the current item in the iterable,
iterable is the existing iterable, and condition is an optional condition that filters the items in the iterable.

Heres an example of using list comprehension to create a new list of even numbers:
  
  # Creating a new list of even numbers using list comprehension
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [x for x in my_list if x % 2 == 0]

# Printing the new list
print(new_list)  # Output: [2, 4, 6, 8, 10]



In this example, we create a new list of even numbers by iterating over the original list my_list and applying the condition x % 2 == 0, 
which filters out the odd numbers.

List comprehension can also be used with nested loops to create a new list of tuples or lists. 
Heres an example of creating a new list of tuples by combining two lists:



# Creating a new list of tuples using list comprehension with nested loops
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
new_list = [(x, y) for x in list1 for y in list2]

# Printing the new list
print(new_list)  # Output: [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]



In this example, we create a new list of tuples by iterating over two lists list1 and list2 using nested loops,
and applying the expression (x, y) to each pair of items.

List comprehension can also be used to create a new list of dictionaries by using dictionary comprehension. Here's an example:



# Creating a new list of dictionaries using dictionary comprehension with conditional expression
students = [{'name': 'Alice', 'score': 85},            {'name': 'Bob', 'score': 75},  
            {'name': 'Charlie', 'score': 90},            {'name': 'Dave', 'score': 80}]
passed_students = [{x['name']: x['score']} for x in students if x['score'] >= 80]

# Printing the new list of dictionaries
print(passed_students)  # Output: [{'Alice': 85}, {'Charlie': 90}, {'Dave': 80}]





In this example, we create a new list of dictionaries passed_students by iterating over the list students and applying a 
conditional expression that filters out students with a score less than 80.
The expression {x['name']: x['score']} creates a dictionary with each students name as the key and score as the value.

































